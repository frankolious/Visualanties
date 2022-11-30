# Import Modules
import os
import numpy as np
from PIL import Image
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

# CONSTANTS
UPLOAD_FOLDER = 'static/uploads/'  # Specify a variable for the upload folder
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])  # Specify the allowed extensions to be uploaded

# Initiate the flask app
app = Flask(__name__)
app.secret_key = "secret key"  # Set a secrete key for the app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Configure the app's variable for the upload folder
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Configure the app for a maximum upload for the string

# Specify that Bootstrap shall be utilized with app object
Bootstrap(app)


# Function to determine whether the uploaded file meets the criteria and is accepted
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Function to return list of the top 10 most common colors in the picture (R, G, B)
def color_palette(image):
    # Import a random image
    file_name = image
    # Use Image to open the image file
    my_img = Image.open(file_name)
    # Convert the image to an array to manipulate
    img_array = np.array(my_img)
    # Reshape the image array to more easily determine most used colors
    img_reshape = np.reshape(a=img_array, newshape=(-1, 3))
    # Determine the amount of unique 1-D arrays and return their counts
    unique, counts = np.unique(img_reshape, axis=0, return_counts=True)
    # Sorts the "counts" list and grabs the last 10 which are the most used.
    b = np.sort(counts)[-10:]
    # Takes the numbers from the list "b" and returns a list with the index numbers for each item
    index_list = [int(np.where(counts == x)[0]) for x in b]
    index_list.reverse()  # Reverses the list so the first one in the list is the highest and descends
    # Creates new list by using the "index list" and grabbing each one of the values from the "unique" list
    rgb_list = [unique[x] for x in index_list]
    y = [{"R": int(n[0]), "G": int(n[1]), "B": int(n[2])} for n in rgb_list]
    return y


# Set home page routing
@app.route("/")
def upload_form():
    return render_template("index.html")  # Returns index.html page from templates folder


# Redirect back to index page once upload has occurred
@app.route('/', methods=['POST'])
def upload_image():
    # If statement to determine whether a file was uploaded
    if 'file' not in request.files:
        flash('No file part')  # Flash notice on screen specifying that no file was uploaded
        return redirect(request.url)  # Return back to index page
    file = request.files['file']  # Specify a variable for the file uploaded
    if file.filename == '':
        flash('No image selected for uploading')  # Flash notice on screen specifying that no file was uploaded
        return redirect(request.url)  # Return back to index page
    # Once both arguments are true execute the following
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Ensure filename is appropriate
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save the file the uploads folder specified
        flash('Image successfully uploaded and displayed')  # Flash notice specifying it was a success
        # Return back to index page with the uploaded image and the colors in the image
        return render_template('index.html', filename=filename, colors=color_palette(image=file))
    else:
        # Else statement specifying that the file type was incorrect and what is allowed
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)  # Return back to index page


# Route for displaying image to index page
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


# Initiate the script and start a development server
if __name__ == "__main__":
    app.run(debug=True)