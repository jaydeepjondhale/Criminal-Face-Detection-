#python version 3.6.5(64bit)
#pip install easyfacenet
#pip uninstall numpy
#pip install numpy==1.16.2
from datetime import datetime
import openpyxl
from openpyxl import Workbook
from openpyxl import Workbook
from openpyxl import load_workbook

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
while True:
      
      #camera = cv2.VideoCapture(0) #For Default Web Camera
      camera = cv2.VideoCapture('http://192.168.2.3:8080/video')# For IP Camera

      i=input("look at webcam properly and press enter")
      return_value, image = camera.read()
      cv2.imwrite('db/testim.jpg', image)
      del(camera)
      images.insert(0,'db/testim.jpg')

      aligned = facenet.align_face(images)
      comparisons = facenet.compare(aligned)
      l=len(images)
      print(images)
      for cnt in range(1,l):
          if(bool(comparisons[0][cnt])):
              print('Matched With',images[cnt])
              name=str(images[cnt])
              name=name[3:-4]
              test1=1


      if(test1==0):
          print("sarthak")
          name="sarthak"
      d=datetime.now()
      d2=str(d);
      d2=d2.replace(" ","_")
      d2=d2[0:16]
      d4=d2
      d2=name+"_"+d2+".jpg";
      d2=d2.replace("-","_")
      d2=d2.replace(":","_")
      print(d2)
      cv2.imwrite("daily_data/"+d2,image)
      rows=((name,d4),
          (name,d4)
          )
      wb = load_workbook('appending.xlsx')
      ws = wb.active
      images.remove('db/testim.jpg')
      os.remove("db/testim.jpg")

      for row in rows:
            
            
            
            ws.append(row)
      wb.save('appending.xlsx')
      
      
