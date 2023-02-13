from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView
from .serializers import ApprDataSerializer
from .models import ApprData


# from . import DescriptionForm

class PostApprData(APIView):
    parser_classes = (FormParser, FileUploadParser)
    
    def get(self, request, *args, **kwargs):
        data = ApprData.objects.all()
        serializer = ApprDataSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data_serializer = ApprDataSerializer(data=request.data)
        if data_serializer.is_valid():
            data_serializer.save()
            return Response(data_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', data_serializer.errors)
            return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
'''    
def postDescription(APIview):
    appr_data = ApprData.objects.all()
    serializer = ApprDataSerializer
    return Response(serializer.data)

def post_data(request):
    return HttpResponse('processed successfully')


def get_data(request):
    appr_data = RawAppraisalData.objects.all()
    serializer = RawAppraisalDataSerializer(appr_data, many=True) # serialize multiple objects
    return Response(serializer.data)
        

def post_description_and_images(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        HouseDescription = DescriptionForm(request.POST)
        # check whether it's valid
        if HouseDescription.is_valid():
            # process the data in form.cleaned_data as required
            HouseDescription.save()
            # redirect to a new URL:
            return HttpResponse('House description processed successfully')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DescriptionForm()

    return render(request, 'name.html', {'form': form})
'''