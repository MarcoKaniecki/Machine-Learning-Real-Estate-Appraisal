from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = "adb3838b97db400f9c5326e36e2d7037"
endpoint = "https://marcoscomputervision.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
Quickstart variables
These variables are shared by several examples
'''
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
'''
END - Quickstart variables
'''

file_path = "/Users/marcokaniecki/Desktop/ECED4900-SYP/Sample-Data/286454219_5412071062164274_1507514144798269009_n.jpg"

with open(file_path, mode='rb') as image_stream:
    # Call API with remote image
    results = computervision_client.describe_image_in_stream(image_stream)
    # tags_result_remote = computervision_client.tag_image(remote_image_url )

    # Print results with confidence score
    print("Tags in the remote image: ")
    if (len(results.tags) == 0):
        print("No tags detected.")
    else:
        for tag in results.tags:
            print(tag)
        #for tag in results.tags:
            #print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
    print()
