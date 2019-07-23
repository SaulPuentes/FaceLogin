from services import sighthound

def fr_api(path, img):
    # opencv.request(img)
    # sighthound.request_recognition(img)
    sighthound.request_detection(img)