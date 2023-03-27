#python version 3.6.5(64bit)
#pip install easyfacenet
#pip uninstall numpy
#pip install numpy==1.16.2

import os
import cv2
from easyfacenet.simple import facenet
test1=0
path = 'db/'

images = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            images.append(os.path.join(r, file))

print(images)
#camera = cv2.VideoCapture(0)
camera = cv2.VideoCapture('http://192.168.2.3:8080/video')# For IP Camera

i=input("look at webcam properly and press enter")
return_value, image = camera.read()
cv2.imwrite('db/testim.jpg', image)
del(camera)
images.insert(0,'db/testim.jpg')

aligned = facenet.align_face(images)
comparisons = facenet.compare(aligned)
l=len(images)
for cnt in range(1,l):
    if(bool(comparisons[0][cnt])):
        print('Matched With',images[cnt])
        test1=1


if(test1==0):
    print("Unknwon Face")
os.remove("db/testim.jpg")
