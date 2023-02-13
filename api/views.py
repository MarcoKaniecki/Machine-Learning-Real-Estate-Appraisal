from django.shortcuts import render
from django.http import HttpResponse

from . import DescriptionForm

# Create your views here.

def post_images(request):
    if request.method == 'POST':
        pass
        # form = ImageForm
        
def post_description(request):
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

    # return render(request, 'name.html', {'form': form})