from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

# island reffering to kitchen island
important_features = [
    "wood", "furniture", "table", "kitchen", "island", "bedroom", "bed", "porch", "stone",
    "Driveway", "sidewalk", "basement"
]

# Authenticates credentials and creates a client
subscription_key = "adb3838b97db400f9c5326e36e2d7037"
endpoint = "https://marcoscomputervision.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


# images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")

# file_path = str(input("Enter path of image: "))
folder = "Sample-Data/sample house 1"
files = os.listdir(folder)

# loop through each image in folder
for file in files:
    # ignore hidden files
    if file.startswith("."):
        continue

    file_path = os.path.join(folder, file)
    
    with open(file_path, mode='rb') as image_stream:
        # Call API with image
        results = computervision_client.describe_image_in_stream( image_stream )
        # tags_result_remote = computervision_client.tag_image(remote_image_url)

        # Print results with extracted tags
        print(f"## Tags in the {file} image ##")
        if (len(results.tags) == 0):
            print("No tags detected.")
        else:
            for tag in results.tags:
                print(tag)
        print()
