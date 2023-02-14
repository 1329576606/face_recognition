import face_recognition
import requests
from io import BytesIO

def face_encodings_from_url(url):
    response = requests.get(url)
    image=face_recognition.load_image_file(BytesIO(response.content))
    return face_recognition.face_encodings(image)
def face_encodings(file):
    image=face_recognition.load_image_file(file)
    return face_recognition.face_encodings(image)
    