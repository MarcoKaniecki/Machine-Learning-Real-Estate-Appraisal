from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# The views file in Django is responsible for handling incoming requests and returning responses. 
# It defines functions or classes that encapsulate the business logic of the application and interact with models, serializers, and other components to generate a response.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # get all info in database, will be displayed in REST framework page
    # def get(self, request, *args, **kwargs):
    #     posts = Post.objects.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)

    # post data to database
    def post(self, request, *args, **kwargs):
        # posts_serializer = ListingSerializer(data=request.data, files=request.FILES)
        posts_serializer = ListingSerializer(data=request.data, context={'request': request})
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     # get all info in database, will be displayed in REST fraemwork page
#     def get(self, request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     # post data to database
#     def post(self, request, *args, **kwargs):
#         posts_serializer = PostSerializer(data=request.data)
#         if posts_serializer.is_valid():
#             posts_serializer.save()
#             return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
