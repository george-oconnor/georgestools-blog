from sharepoint_stuff import getCTX, downloadFile
from flaskblog.config import Config
from flaskblog.models import Class
from flaskblog import db
from flask import current_app
import pandas as pd
import os

def getTimetableFile():
    username = Config.MAIL_USERNAME
    pswd = Config.MAIL_PASSWORD
    ctx = getCTX("https://ioedub.sharepoint.com/sites/Timetablesystemproject/", username, pswd)
    downloadFile(ctx, "/sites/Timetablesystemproject/Shared Documents/General/2023-24/Timetable_Drafting.xlsx", "timetable.xlsx", os.path.join(current_app.root_path, 'static/'), False)

    df = pd.read_excel(os.path.join(current_app.root_path, 'static/timetable.xlsx'), 'Classes List')

    Class.query.delete()

    for index, row in df.iterrows():

        if str(row['Pace']) == "nan":
            type = ""
        elif row['Pace'] == "Fast Pace":
            type = "FP"
        elif row['Pace'] == "Normal Pace":
            type = "NP"
        elif row['Pace'] == "Continuation":
            type = "Cont."
        elif row['Pace'] == "New":
            type = "New"
        elif row['Pace'] == "FP Continuation":
            type = "FP"
        else:
            type = str(row['Pace'])

        type = row['Pace']

        new_class = Class(
            goc_id = row["GOC_Class_ID"],
            subject = row["Subject"],
            level = row['Level'],
            pace = type,
            group = row["Group"],
            teacher = row["Teacher"],
            acronym = row["Acronym"],
            day = row["Day"],
            starttime = str(row["Start Time"]),
            duration = str(row["Duration"]),
            endtime = str(row["End Time"]),
            stream = row["Stream"],
            room = row["Room"])
        db.session.add(new_class)
        
    db.session.commit()

    return df

def countScheduledClasses(classes,times, days):
    scheduled_classes = 0
    for item in classes:
        if item.day in days and item.starttime in times:
            scheduled_classes += 1

    return scheduled_classes