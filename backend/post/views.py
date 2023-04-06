from .serializers import *
from .models import *
from .pdf_generation.pdf_generator import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from database_tools.tools import get_database_data
from ML_components.encoder import encode_data
from ML_components.price_prediction import calc_predicted_price
from CompDatabase import CompExtraction

# The views file in Django is responsible for handling incoming requests and returning responses. 
# It defines functions or classes that encapsulate the business logic of the application and interact with models, serializers, and other components to generate a response.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # display everything in database on REST fraemwork webpage
    def get(self, request, *args, **kwargs):
        posts = Listing.objects.all()
        serializer = ListingSerializer(posts, many=True)
        return Response(serializer.data)


    # Post data to database
    def post(self, request, *args, **kwargs):
        listing_serializer = ListingSerializer(data=request.data, context={'request': request})
        if listing_serializer.is_valid():
            listing_serializer.save()

            price_prediction, comps = get_predicted_price()

            # Calling the PDF generator
            generate_pdf(price_prediction, comps)

            # Deleting user data because it is now obselete
            Listing.objects.all().delete()

            return Response(listing_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', listing_serializer.errors)
            return Response(listing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This is called when the user clicks the appraise button in the frontend after saving the entry into the database
def get_predicted_price():
    user_input_data = get_database_data()
    if user_input_data != 0:
        encoded_input_data = encode_data(user_input_data)
        predicted_price = calc_predicted_price(encoded_input_data)
        

        # comps is currently returned in a list. Waiting to change until we are ready to print it in the PDF
        
        #comps = CompExtraction.FindComps(user_input_data)
        
        print('------------------------------------')
        print('it works! Heres the price:', predicted_price)
        print('------------------------------------')
        
        return predicted_price, comps