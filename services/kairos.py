
#!/usr/bin/env python

import cv2
import json
import base64
import requests

# put your keys in the header
headers = {
    "Content-Type": "application/json",
    "app_id": "f41de7f3",
    "app_key": "49ad2ac88ed5631b24ffaee50873cb33"
}


def request(img):
    url = 'https://api.kairos.com/recognize'

    _, img_encoded = cv2.imencode('.jpg', img)

    base64_image = base64.b64encode(img_encoded.tostring())

    params = json.dumps({
        "image": base64_image,
        "gallery_name": "helicon"
    })

    r = requests.post(url, data=params, headers=headers)

    print json.loads(r.text)


def enroll():
    img = open('../images/Saul/IMG_20190531_145345__1559576890_45.235.172.162.jpg','r')
    base64_image = base64.b64encode(img.read())
   

    params = json.dumps({
        "image": base64_image,
        "subject_id":"Saul",
        "gallery_name":"helicon"
        })

    url = "http://api.kairos.com/enroll"

    # make request
    r = requests.post(url, data=params, headers=headers)

    print json.loads(r.text)