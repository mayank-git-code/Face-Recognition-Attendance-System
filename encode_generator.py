import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials,storage
from firebase_admin import db

# add images to the database

# database link credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendance-system-b362d-default-rtdb.firebaseio.com/",
    'storageBucket' : "attendance-system-b362d.appspot.com"
})

# importing student images

folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])     # remove .png from file name

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
  
print(studentIds)

# find encoding of the images

def findEncodings(imagesList):
    encodeList = []                      # list to strore encodings
    for img in imagesList:               # loop through images
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)            # opencv library uses bgr and face recogition lib uses rgb
        encode = face_recognition.face_encodings(img)[0]     # find encodings of face image
        encodeList.append(encode)        # add the encodings to the list

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)    # call the defined function
encodeListKnownWithIds = [encodeListKnown,studentIds]
print("Encoding Complete")

# save the encodings with Ids in a file using picke library

file = open("EncodeFile.p", 'wb')  # create a flie & wb is permission to write data
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")

