import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendance-system-b362d-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "23SCSE1180232":
        {
            "name": "Mayank",
            "course": "BTech - CSE",
            "starting_year": "2023",
            "total_attendance": 12,
            "section": "Sec-26",
            "year": "1st",
            "last_attendance_time": "2024-01-17 00:54:34"
        },
    
    "23SCSE1180237":
        {
            "name": "Sarthak Vanshaj",
            "course": "BTech - CSE",
            "starting_year": "2923",
            "total_attendance": 12,
            "section": "Sec-26",
            "year": "1st",
            "last_attendance_time": "2024-01-17 00:54:34"
        },
    
}

for key, value in data.items():
    ref.child(key).set(value)