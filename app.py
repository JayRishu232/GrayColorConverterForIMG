# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# import additional libraries below
import cv2
import numpy as np



app = Flask(__name__)

# Open and redirect to default upload webpage
@app.route('/')
def load_form():
    return render_template('upload.html')

# Function to upload image and redirect to new webpage
@app.route('/gray', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    # write the read and write function on image below 
    
    file_data = convert_gray(file.read())
    with open(os.path.join("static/", filename), "wb") as f:
        f.write(file_data)


        # ends here

    display_message = 'Image successfully uploaded and displayed below'
    return render_template('upload.html', filename=filename, message = display_message)


# Write the make_grayscale() function below
def convert_gray(input_image):
    intconvertedimg = np.fromstring(input_image, dtype="uint8")
    print("Converted image into array successfully:", intconvertedimg)

    decodedimg = cv2.imdecode(intconvertedimg, cv2.IMREAD_UNCHANGED)
    print("Image decoded successfully: ", decodedimg)
    convertedto_grayscale = cv2.cvtColor(decodedimg, cv2.COLOR_RGB2GRAY)
    status, encoded_output = cv2.imencode(".JPG", convertedto_grayscale)
    print("Status: ", status)
    return encoded_output

# make_grayscale() function ends above
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))



if __name__ == "__main__":
    app.run()


