from datetime import datetime
import base64
<<<<<<< Updated upstream
import http.client
import json
import os
import sys
=======
import json
import os
import sys
try:
    import httplib # Python 2
except:
    import http.client as httplib # Python 3
    
import cv2
>>>>>>> Stashed changes

from save_result import save_result

# Set this variable to True to print all server responses.
_print_responses = False

# Your Sighthound Cloud token. More information at
# https://www.sighthound.com/support/creating-api-token
_cloud_token = "pslS5Wzcc6x8Efr62fvftn8oet548bACppMW"

# The cloud server to use, here we set the development server.
_cloud_host = "dev.sighthoundapi.com"

# A set in which to gather object names during step 1.
_object_ids = set()

# The name of the group to which we will add objects (step 2), train (step 3),
# and test with (step 4).
_group_name = "helicon"

# The directory where annotated test images will be written.
_output_folder = "out"

# The name of the person detected by the face recognition request
_person_id = None


def send_request(request_method, request_path, params):
    """A utility function to send API requests to the Sighthound Cloud server.

    This function will abort the script with sys.exit(1) on API errors.
    
    @param  request_method  The request method, "PUT" or "POST".
    @param  request_path    The URL path for the API request.
    @param  params          The parameters of the API request, if any.
    @return response_body   The body of the response.
    """
    # Send the request.
    headers = {"Content-type": "application/json",
               "X-Access-Token": _cloud_token}
    conn = http.client.HTTPSConnection(_cloud_host)
    conn.request(request_method, request_path, params, headers)

    # Process the response.
    response = conn.getresponse()
    body = response.read()
    error = response.status not in [200, 204]

    if _print_responses or error:
        print(response.status, body)

    if error:
        sys.exit(1)

    return body


def request_recognition(img):
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpg', img)

    base64_image = base64.b64encode(img_encoded.tostring())
    
    params = json.dumps({"image": base64_image.decode('ascii')})
    url_path = "/v1/recognition?groupId=" + _group_name
    response = json.loads(send_request("POST", url_path, params))
    
    save_result(response)
    save_image(response, img)
    # print_message(response)


def print_message(response):
    confidence = None
    # Show a message in console
    for face in response['objects']:

        # Retrieve and draw the id and confidence of the recongition.
        _person_id = face['objectId']
        confidence = face['faceAnnotation']['recognitionConfidence']
    print('[SIGHTHOUND] Hola ' + str(_person_id) + '.La confianza es :' + str(confidence))


def save_image(response, img):
    # Retrieve and draw the id and confidence of the recongition.
    for face in response['objects']:
        _person_id = face['objectId']
        confidence = face['faceAnnotation']['recognitionConfidence']
    
    # Classify in folders
    if confidence >= .5:
        path = 'images/out/' + _person_id + '/'
    else:
        path = 'images/out/unknown/'
    
    # If folders doesn't exist
    if not os.path.exists(path):
        os.makedirs(path)

    path = path + str(datetime.now()) +'.jpg'
    cv2.imwrite(path, img)
    

def request_detection(img):
    # encode image as jpeg
    _, img_encoded = cv2.imencode('.jpg', img)

    base64_image = base64.b64encode(img_encoded.tostring())
    
    params = json.dumps({"image": base64_image.decode('ascii')})
    url_path = "/v1/detections?type=face&faceOption=gender,landmark,age,pose,emotion"
    response = json.loads(send_request("POST", url_path, params))
    
    save_result(response)


# Group Management
def list_all_groups():
    params = None
    url_path = '/v1/group'
    response = json.loads(send_request("GET", url_path, params))
    

def delete_group():
    params = json.dumps({'groupId': 'family'})
    url_path = '/v1/group/{groupId}/all'
    response = json.loads(send_request("DELETE", url_path, params))


# Images Management
def list_all_images():
    params = None
    url_path = '/v1/image'
    response = json.loads(send_request("GET", url_path, params))


def delete_image():
    params = None
    imageId = 'IMG_9257.jpg'
    url_path = '/v1/image/' + imageId
    response = json.loads(send_request("DELETE", url_path, params))
    

# Object Management
def delete_object():
    params = None
    objectId = 'Daniel_Carrizales'
    url_path = '/v1/object/' + objectId
    response = json.loads(send_request("DELETE", url_path, params))
