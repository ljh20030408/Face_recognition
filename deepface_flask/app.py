import base64
from flask import Flask, request, jsonify
from deepface.commons import distance as dst
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import time
import imghdr
import io,os
import tempfile
from PIL import Image
from base64 import b64decode
from deepface import DeepFace
from datetime import datetime

from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources=r'/*')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:clz1515@101.43.93.152:3306/face_info?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=True)
    name = db.Column(db.String(255), nullable=True)
    ip = db.Column(db.String(255), nullable=True)


@app.route('/write', methods=['POST'])
def write():
    # Get the image file from the request
    img_file = request.files['img_file']
    img = Image.open(img_file)
    max_dimension = 512
    width, height = img.size
    if width > height:
        new_width = max_dimension
        new_height = int(height * max_dimension / width)
    else:
        new_width = int(width * max_dimension / height)
        new_height = max_dimension
    img = img.resize((new_width, new_height))

    # Save the uploaded file to the 'templates/img/' directory with the given name
    name = request.form.get('name')
    img_path = os.path.join('templates', 'img', f'{name}.jpg')
    img.save(img_path)

    # Get the image binary data from the file
    with open(img_path, 'rb') as f:
        img_binary = f.read()

    # Get the embedding for the image
    representation = DeepFace.represent(img_path=img_path, model_name="VGG-Face", enforce_detection=False)[0]["embedding"]

    # Save the image binary to a file in templates/img folder only if the image name is not a timestamp
    if not name.isdigit():
        img_filename = name
        with open(f"templates/img/{img_filename}.jpg", "wb") as f:
            f.write(img_binary)
    else:
        img_filename = ""

    # Add filename and representation to instance
    instance = [img_filename, representation]

    # Load existing representations
    try:
        with open('representations.pkl', 'rb') as f:
            representations = pickle.load(f)
    except:
        representations = []

    # Append new representation and save to file
    representations.append(instance)
    with open('representations.pkl', 'wb') as f:
        pickle.dump(representations, f)

    # Add data to database
    data = Data(name=name)
    db.session.add(data)
    db.session.commit()

    return jsonify({'message': 'Face written to database'}), 200




@app.route('/verify', methods=['POST'])
def verify():
    result = 'false'
    try:
        # get the image data from the request
        img = Image.open(request.files['image'])

        max_dimension = 512
        width, height = img.size
        if width > height:
            new_width = max_dimension
            new_height = int(height * max_dimension / width)
        else:
            new_width = int(width * max_dimension / height)
            new_height = max_dimension
        target_img = img.resize((new_width, new_height))

        # save the PIL image to a temporary file
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as f:
            target_img.save(f.name)
            target_path = f.name

        # extract the face representation
        target_representation = DeepFace.represent(img_path=target_path, model_name="VGG-Face", enforce_detection=False)[0]["embedding"]

        # check if a face was detected in the input image
        if not target_representation:
            return jsonify({'message': 'No face detected in input image'}, {'result': result})

        # load representations of faces in database
        try:
            f = open('representations.pkl', 'rb')
            representations = pickle.load(f)
            f.close()
        except FileNotFoundError:
            return jsonify({'message': 'No face representations found'}, {'result': result})

        distances = []

        start_time = time.time()
        print(len(representations))
        print()

        for i in range(0, len(representations)):
            source_name = representations[i][0]
            source_representation = representations[i][1]
            distance = dst.findCosineDistance(source_representation, target_representation)
            distances.append(distance)

        # find the minimum distance index
        idx = np.argmin(distances)
        similarity = 1 - distances[idx]

        if similarity < 0.8:
            return jsonify({'message': 'Not Found'}, {'result': result})

        matched_name = representations[idx][0]

        end_time = time.time()
        matched_name = matched_name.split('/')[-1].split('.')[0]
        current_time = (end_time - start_time) * 1000
        ip = request.form.get('ip')
        now = datetime.now()
        data = info(name=matched_name, time=now, ip=ip)
        db.session.add(data)
        db.session.commit()
        print(current_time)
        result = 'true'

        return jsonify({'matched_name': matched_name}, {'result': result})

    except Exception as e:
        return jsonify({'message': str(e)})




@app.route('/delete', methods=['POST'])
def delete():

    try:
        name= request.form.get('name')
        # load existing representations
        with open('representations.pkl', 'rb') as f:
            representations = pickle.load(f)

        # find the index of the instance with the matching name
        idx = None
        for i in range(len(representations)):
            if representations[i][0] == name:
                idx = i
                break

        # delete the image file if it exists
        if os.path.exists(f"templates/img/{name}.jpg"):
            os.remove(f"templates/img/{name}.jpg")

        # remove the instance from the representations list if found
        if idx is not None:
            del representations[idx]
            with open('representations.pkl', 'wb') as f:
                pickle.dump(representations, f)

                name = request.form.get('name')
                data = Data.query.filter_by(name=name).first_or_404()
                db.session.delete(data)
                db.session.commit()
            return jsonify({'message': f"{name} deleted successfully"})
        else:
            return jsonify({'message': f"No matching name found in database"})
    except Exception as e:
        return jsonify({'message': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port='5000',
            debug=True,
            threaded=True)
