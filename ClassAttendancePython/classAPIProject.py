import base64
from PIL import Image
import io
import cv2
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from PIL import Image
import imagehash
import base64
import face_recognition
img=[]
pho=[]
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def solve(img1):
    image = base64.b64decode(str(img1)) 
    imagePath = ("test.jpeg")      
    img3 = Image.open(io.BytesIO(image))
    img3.save(imagePath, 'jpeg')
    co=0

    picture_of_me = face_recognition.load_image_file("test.jpeg")
    for i in img:
        image = base64.b64decode(str(i)) 
        imagePath = ("test1.jpeg")      
        img3 = Image.open(io.BytesIO(image))
        img3.save(imagePath, 'jpeg')
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

        unknown_picture = face_recognition.load_image_file("test1.jpeg")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0] == True:
            co=co+1
    return co

from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/attendance")
def attend():
    img1=str(request.args['image'])
    co=solve(img1)
    if co>0:
        return jsonify({'success':'attended'})
    return jsonify({'success':'not attended'})

@app.route("/register")
def reg():
    img1=str(request.args['image'])
    phone=str(request.args['phone'])
    if not(phone in pho):
        img.append(img1)
        pho.append(phone)
        return jsonify({'success':'added'})

    return jsonify({'success':'rejected'})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)