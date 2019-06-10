# -*- coding: utf-8 -*-
import urllib2
import urllib
import time


key = "d2brUJKKfTEmEiR7T9-CYyBgnMZ8sRy0"
<<<<<<< Updated upstream
secret = "DD3wQF__5aqMHhZDOHewTXSKONLAPnBq"    
=======
<<<<<<< HEAD
secret = "DD3wQF__5aqMHhZDOHewTXSKONLAPnBq"

=======
secret = "DD3wQF__5aqMHhZDOHewTXSKONLAPnBq"    
>>>>>>> master
>>>>>>> Stashed changes

def request():
    http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    filepath = "../images/Saul/IMG_20190531_145345__1559576890_45.235.172.162.jpg"
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr=open(filepath,'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)
    http_body='\r\n'.join(data)
    #buld http request
    req=urllib2.Request(http_url)
    #header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        #post data to server
        resp = urllib2.urlopen(req, timeout=5)
        #get response
        qrcont=resp.read()
        print qrcont

    except urllib2.HTTPError as e:
        print e.read()

def faceset_create():
    http_url = 'https://api-us.faceplusplus.com/facepp/v3/faceset/create'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
<<<<<<< Updated upstream
    
=======
    fr=open(filepath,'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)
    http_body='\r\n'.join(data)
    #buld http request
    req=urllib2.Request(http_url)
    #header
    req.add_header('Content-Type', 'multipart/form-data; =%s' % boundary)
    req.add_data(http_body)
    try:
        #post data to server
        resp = urllib2.urlopen(req, timeout=5)
        #get response
        qrcont=resp.read()
        print qrcont

    except urllib2.HTTPError as e:
        print e.read()
<<<<<<< HEAD
=======

def faceset_create():
    http_url = 'https://api-us.faceplusplus.com/facepp/v3/faceset/create'
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    
>>>>>>> master
>>>>>>> Stashed changes
