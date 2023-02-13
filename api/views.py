from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RawAppraisalDataSerializer
from .models import RawAppraisalData


# from . import DescriptionForm

@api_view(['POST'])
def post_data(request):
    return HttpResponse('processed successfully')

@api_view(['GET'])
def get_data(request):
    appr_data = RawAppraisalData.objects.all()
    serializer = RawAppraisalDataSerializer(appr_data, many=True) # serialize multiple objects
    return Response(serializer.data)
        
'''
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