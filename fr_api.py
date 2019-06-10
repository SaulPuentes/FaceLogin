from services import faceplusplus, kairos, lmbdalabs, opencv, sighthound

def fr_api(path, img):
    opencv.request(img)
    sighthound.request(img)
    # kairos.request(img)