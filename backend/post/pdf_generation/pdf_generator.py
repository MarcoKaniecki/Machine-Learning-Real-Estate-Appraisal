from fpdf import Align, FPDF
import os
from datetime import date
from django.forms import model_to_dict
import sys

# Setting the python environment
from post.models import *

def generate_pdf():

    # Path of this python file
    current_file_path = os.path.abspath(__file__)

    # Directory this python file is in, used to retrieve boiler plate images
    current_directory_path = os.path.dirname(current_file_path)

    # Retrieving listing created by user
    listing = Listing.objects.first()
    listing_dict = model_to_dict(listing)

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

    

    # # Example listing
    # listing = {
    #     "Owner":"Owen Houseguy",
    #     "Address":"123 Road St",
    #     "Price":400,
    #     "Image path":b_dir + '/PDF generator/house1.webp',
    # }

    # #example comp
    # comp = {
    #     "Owner":"Owen Otherhouseguy",
    #     "Address":"124 Road St",
    #     "Price":401,
    #     "Image path":b_dir + '/PDF generator/house2.webp',
    # }

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

    # Page 1
    pdf.add_page()

    # Setting font
    pdf.set_font('helvetica', 'B', 20)
    pdf.set_text_color(0, 0, 0)

    # Text
    #pdf.cell(0,30)

    # Creating space from top
    # num_lines = 10
    # for i  in range(0,num_lines):
    #     pdf.cell(txt=' ', new_x="LMARGIN", new_y="NEXT")


    pdf.set_y(60)

    pdf.cell(0,0,'APPRAISAL OF', align='C', new_x="LMARGIN", new_y="NEXT")
    # pdf.cell(0,0,'This is a test ' + listing['Address'])
    pdf.ln()
    pdf.ln()
    pdf.image(image_path, x = Align.C, h = pdf.epw/3)
    # pdf.image(listing['Image path'],w=pdf.epw/1.5,x=pdf.epw/4-6)


    features_string = ""
    for key, value in listing_dict.items():
        features_string += "<center><h5>" + str(key) + ": " + str(value) + "</h5></center>"

    pdf.set_y(160)
    pdf.write_html("""
        <br>
        <center><h3><font color="black"><b>Client:</b></font></h3></center>
        <center><h3><font color="black">_____________________</font></h3></center>
        <br>
        <center><h3><font color="black"><b>Date of appraisal:</b></font></h3></center>
        <center><h3><font color="black">""" + today_pretty + """</font></h3></center>
    """)


    # Price reveal and other info

    pdf.add_page()
    pdf.cell(0,0,'Feature Comparison with Similar Properties', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(160)
    pdf.cell(0,0,'Price and other info about appraised propery goes here', align='C', new_x="LMARGIN", new_y="NEXT")



    # Comps table

    pdf.add_page()
    pdf.cell(0,0,'Feature Comparison with Similar Properties', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(80)

    # Constructing the string that will be the html table
    table_string = ""
    for key, value in listing_dict.items():
        if key != 'id':
            table_string += "<tr><td>" + str(key) + "</td>"
            table_string += "<td>" + str(value) + "</td>"
            table_string += "<td>" + str(comp_1_dict[str(key)]) + "</td>"
            table_string += "<td>" + str(comp_2_dict[str(key)]) + "</td>"
            table_string += "<td>" + str(comp_3_dict[str(key)]) + "</td>"
            table_string += "<td>" + str(comp_4_dict[str(key)]) + "</td>"
            table_string += "<td>" + str(comp_5_dict[str(key)]) + "</td>"


    # Font size for the feature table and its elements
    table_font_size = str(9)

    pdf.write_html("""
    <font size="""+ table_font_size +""">
    <table width="90%">
      <thead>
        <tr>
          <th width="20%">Feature</th>
          <th width="20%">Appraised property</th>
          <th width="12%">Comp 1</th>
          <th width="12%">Comp 2</th>
          <th width="12%">Comp 3</th>
          <th width="12%">Comp 4</th>
          <th width="12%">Comp 5</th>
        </tr>
      </thead>
      <tbody>
        """+ table_string +"""
      </tbody>
    </table></font>
    
""")



    # More photos of appraised property

    pdf.add_page()
    pdf.cell(0,0,'More Photos of Appraised Property', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(90)

    for image in Image.objects.filter(listing = listing.id):
        pdf.image(image.image.path, x = Align.C, h = pdf.epw/3)


    # # Title page

    # pdf.write_html("""
    #     <br>
    #     <br>
    #     <center><h3>Owner's name:   """ + listing["Owner"] + """</h3></center>
    #     <center><h3>Address:   """ + listing["Address"] + """</h3></center>
    #     <center><b><h3><u>Estimated price:   $""" + str(listing["Price"]) + """</u></h3></b></center>
    #     <center><h3>Date of appraisal:</h3></center>
    #     <center><h3>""" + today_pretty + """</h3></center>
    # """)



    # Next page code

    # # Example comp
    # comp = {
    #     "Owner":"Owen Otherhouseguy",
    #     "Address":"124 Road St",
    #     "Price":401,
    #     "Image path":b_dir + '/PDF generator/house2.webp',
    # }

    # pdf.add_page()
    # pdf.set_font('arial', 'B', 16)
    # pdf.set_y(60)

    # pdf.cell(0,0,'Example comparable property 1', align='C', new_x="LMARGIN", new_y="NEXT")

    # pdf.ln()
    # pdf.ln()
    # pdf.image(comp['Image path'],w=pdf.epw/1.5,x=pdf.epw/4-6)

    # pdf.write_html("""
    #     <br>
    #     <br>
    #     <center><h3>Address:   """ + comp["Address"] + """</h3>
    #     <center><h3>Proximity to Subject:   0.12 km</h3>
    #     <center><h3>Price:   $""" + str(comp["Price"]) + """</h3>
    #     <center><h3>Age, features, etc...</h3>
    # """)

    pdf.output('./Report.pdf')