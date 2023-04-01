import globals
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from ML_price_prediction import get_database_data, calc_predicted_price, encode_data


# The views file in Django is responsible for handling incoming requests and returning responses. 
# It defines functions or classes that encapsulate the business logic of the application and interact with models, serializers, and other components to generate a response.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # get all info in database, will be displayed in REST fraemwork page
    def get(self, request, *args, **kwargs):
        posts = Listing.objects.all()
        serializer = ListingSerializer(posts, many=True)

        # if there is data in the database, call the get_database_data() function
        if Listing.objects.exists():
            user_input_data = get_database_data()
            encoded_input_data = encode_data(user_input_data)
            predicted_price = calc_predicted_price(encoded_input_data)
            print('it works! Heres the price:', predicted_price)
        else:
            print('No data in database')
        
        return Response(serializer.data)


    # Post data to database
    def post(self, request, *args, **kwargs):
        posts_serializer = ListingSerializer(data=request.data, context={'request': request})
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
