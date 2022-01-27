# importing the required libraries
import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import numpy as np
import json
import datetime

from eventHandlers.courseAssignments import courseAssignments
from eventHandlers.courseCirriculum import courseCirriculum
from eventHandlers.courseDescriptor import courseDescriptor
from eventHandlers.courseVideoResources import courseVideoResources


# initialising the flask app
app = Flask(__name__)

# Creating the upload folder
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

# The path for uploading the file
@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':  # check if the method is post
        f = request.files['file']  # get the file from the files object
        # Saving the file in the required destination
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        filename = f.filename # this will secure the file
        filenamesplitter = filename.split(".")
        filenamewithoutextension = filenamesplitter[0]
        filepath = "uploads/" + filename
        coursedesc = courseDescriptor(filename=filepath, sheetname="Course Basic Information")
        coursecirr = courseCirriculum(filename=filepath, sheetname="Course Landing Page Info")
        coursevids = courseVideoResources(filename=filepath, sheetname="Course Videos")
        courseassi = courseAssignments(filename=filepath, sheetname="Course Assignments")
        course_json = {
            "Course Basic Information": coursedesc,
            "Course Landing Page Info": coursecirr,
            "Course Videos": coursevids,
            "Course Assignments": courseassi,
        }
        currentDatetime = datetime.datetime.now().strftime("%d%B%I%M%p")
        global json_filename
        json_filename = filenamewithoutextension + currentDatetime + ".json"
        reader = json.dumps(course_json, cls=NpEncoder)
        with open(json_filename, "w") as outfile:
            outfile.write(reader)
        return 'File uploaded & JSON created successfully'  # Display this message after uploading


# displaying the HTML template at the home url
@app.route('/downloader')
def index():
   return render_template('download.html')

# Sending the file to the user
@app.route('/download')
def download():
   return send_file(json_filename, as_attachment=True)


if __name__ == '__main__':
    app.run()  # running the flask app


# git config --global user.email "paulbindass@gmail.com"
# 			git config --global user.name "Sourangshu Pal"
