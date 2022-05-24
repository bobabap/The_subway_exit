import cv2
import os 
import numpy  as np

path = "C:/Users/pc/Desktop/image_file" #원본 사진이 있는 폴더 위치

file_list = os.listdir(path)
    
for k in file_list:
    img = cv2.imread(path + '\\' + k)
    width, height = img.shape[:2]
    resize_img = cv2.resize(img, (416 , 416), interpolation=cv2.INTER_CUBIC) #사진크기
    cv2.imwrite('C:/Users/pc/Desktop\\' + k, resize_img)  #리사이즈된 후 사진이 저장될 폴더 위치