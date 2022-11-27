print("""
Crop Disease Detection System  🚀🚀🚀⚡⚡⚡
Further Updaes is Coming Soon.......
""")


import time
import urllib.request
import cv2
import numpy
import PIL.Image
imageURL="http://192.168.43.1:8080/shot.jpg"

while True:
    response=urllib.request.urlopen(url=imageURL)
    imageBytes=bytearray(response.read())
    imageArray=numpy.array(imageBytes,dtype=numpy.uint8)
    print(imageArray)
    imageFrame=cv2.imdecode(imageArray,1)
    cv2.imshow("Scanner Frame",imageFrame)
    savingImage=PIL.Image.fromarray(imageFrame)
    savingImage.save("./App/static/Files/image.jpg")
    # time.sleep(1)
    print(cv2.waitKey(1))