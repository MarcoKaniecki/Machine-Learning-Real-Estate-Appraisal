from fpdf import Align, FPDF
import os
from datetime import date
from django.forms import model_to_dict
from post.models import *
from globals import DECODE_DATABASE_NAMES

# Decoding features to make them more readable
def dict_decode(in_dict):
    out_dict = in_dict
    for feature in DECODE_DATABASE_NAMES.values():
      for coded_name,decoded_name in feature.items():
          for key,value in out_dict.items():
              if value == coded_name:
                out_dict[key] = decoded_name
    return out_dict

def generate_pdf():

    # Path of this python file
    current_file_path = os.path.abspath(__file__)

    # Directory this python file is in, used to retrieve boiler plate images
    current_directory_path = os.path.dirname(current_file_path)

    # Retrieving listing created by user
    listing = Listing.objects.first()
    listing_dict = dict_decode(model_to_dict(listing))

    # Comps for testing
    comp_1_dict = listing_dict.copy()
    comp_2_dict = listing_dict.copy()
    comp_3_dict = listing_dict.copy()
    comp_4_dict = listing_dict.copy()
    comp_5_dict = listing_dict.copy()
    
    

    # Retrieving list of images and getting path to first one
    title_image = Image.objects.filter(listing = listing.id).first()
    image_path = title_image.image.path


    # Date of appraisal
    today = date.today()
    today_pretty = today.strftime("%B %d, %Y")

    # Header and footer
    class PDF(FPDF):
        def header(self):
            # House
            self.image(current_directory_path + '/house_icon.png', 0, 0, 50)
            # Printing REALM        
            self.set_font('helvetica', 'B', 16)
            self.set_text_color(0, 0, 0)
            self.cell(29,65,'REALM.',align='C')
            # Line break
            self.ln()
        
        def footer(self):
            # Position cursor at 1.5 cm from bottom
            self.set_y(-15)
            # Setting font
            self.set_font("helvetica", "I", 8)
            self.set_text_color(0, 0, 0)
            # Printing page number
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="R")

    # Creating pdf object
    pdf = PDF('P', 'mm', 'A4')

    # Setting auto page break
    pdf.set_auto_page_break(auto=True, margin=15)
    

    # Title page creation
    pdf.add_page()

    # Setting font
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_text_color(0, 0, 0)

    # Offsetting additions to start lower on the page
    pdf.set_y(60)

    # Title page
    pdf.cell(0,0,'APPRAISAL OF', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.ln()
    pdf.ln()
    pdf.image(image_path, x = Align.C, h = pdf.epw/3)
    pdf.set_y(160)
    pdf.write_html("""
        <br>
        <center><h3><font color="black"><b>Client:</b></font></h3></center>
        <center><h3><font color="black">_____________________</font></h3></center>
        <br>
        <center><h3><font color="black"><b>Date of appraisal:</b></font></h3></center>
        <center><h3><font color="black">""" + today_pretty + """</font></h3></center>
    """)


    # Page for price reveal and other property info
    pdf.add_page()
    pdf.cell(0,0,'Results of Appraisal', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(120)
    pdf.cell(0,0,'Price and other info about appraised propery goes here', align='C', new_x="LMARGIN", new_y="NEXT")


    # Comps comparison table page
    pdf.add_page()
    pdf.cell(0,0,'Feature Comparison with Similar Properties', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(80)

    # Constructing the string that will populate the html table
    table_string = ""
    for key, value in listing_dict.items():
        if key != 'id':
            # Row with features
            table_string += "<tr><font size=9><td>" + str(key) + "</td>"
            table_string += "<td>" + str(value) + "</td>"
            table_string += "<td>" + str(comp_1_dict[str(key)]) + "</td>"
            table_string += "<td>" + str(comp_2_dict[str(key)]) + "</td>"
            table_string += "<td>" + str(comp_3_dict[str(key)]) + "</td>"
            table_string += "<td>" + str(comp_4_dict[str(key)]) + "</td>"
            table_string += "<td>" + str(comp_5_dict[str(key)]) + "</td></font>"
            # Row for line separation
            seperator_cell = '<td align="left">____________</td>'
            table_string += "<tr><font size=7>" + 7*seperator_cell + "</font></tr>"


    # Table creation
    pdf.write_html("""
    <font size=9>
    <table width="100%" border=1>
      <thead>
        <tr>
          <th width="14%">Feature</th>
          <th width="14%">Client property</th>
          <th width="14%">Comp 1</th>
          <th width="14%">Comp 2</th>
          <th width="14%">Comp 3</th>
          <th width="14%">Comp 4</th>
          <th width="14%">Comp 5</th>
        </tr>
      </thead>
      <tbody>
        """+ table_string +"""
      </tbody>
    </table></font>
    
""")



    # Page with more photos of appraised property
    pdf.add_page()
    pdf.cell(0,0,'More Photos of Appraised Property', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(90)

    # Adding images
    for image in Image.objects.filter(listing = listing.id):
        pdf.image(image.image.path, x = Align.C, h = pdf.epw/3)


    # Saving PDF
    pdf.output('./Report.pdf')