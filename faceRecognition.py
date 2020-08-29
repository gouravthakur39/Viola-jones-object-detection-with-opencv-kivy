

# Import the libraries
import cv2 as cv
import numpy as np
import json
from helper.preprocess import preprocess_image, face_detector
font = cv.FONT_HERSHEY_COMPLEX

with open('labels_to_name.json') as json_file:
    labels_to_name = json.load(json_file)


# Load the model
model = cv.face.LBPHFaceRecognizer_create()
model.read("trainer/model.xml")

# Initialize the webcam
video_capture = cv.VideoCapture(0)

while True:
        _, img = video_capture.read()
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face, coord = face_detector(gray_img)
        x,y,w,h = coord
        if face is not None:
            face = preprocess_image(face)
            # Pass the face to model
            # "results" comprises of a tuple
            # containing label and confidence value

            results = model.predict(face)


            if results[1] < 500:
                confidence = int(100 * (1-(results[1]/300)))
                matched_id = str(results[0])
                person_name = labels_to_name[matched_id]["full_name"]
                person_id = labels_to_name[matched_id]["person_id"]
                display_string  = "Name: {}  Confidence: {}  ID: {}".format(person_name, confidence ,person_id)


            if confidence > 70:
                            
                            cv.putText(img, display_string, (x+10, y-30), font, 0.5, (32, 245, 73), 2)
                            

                            cv.imshow("Face Cropper", img)
            else:
                cv.putText(img, "Unknown", (x+10, y-30), font, 0.5, (255, 120, 150), 2)
                cv.imshow("Face Cropper", img)
    
        else:
            cv.imshow("Face Cropper", img)

        if (cv.waitKey(1) & 0xFF == ord("q")):
            break

video_capture.release()
cv.destroyAllWindows()