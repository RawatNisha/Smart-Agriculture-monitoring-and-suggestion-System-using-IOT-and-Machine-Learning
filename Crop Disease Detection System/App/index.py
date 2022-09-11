from flask import Flask,render_template,redirect,request,send_from_directory,jsonify
import numpy
import tensorflow
import time
import os
import cv2
file_name=""
class_list=[
    "Cotton",
    "Maize",
    "Rice",
    "Sugarcane",
    "Wheat"
]

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/visualization')
def visualization():
    return render_template('visualization.html')
@app.route('/analytics')
def analytics():
    return render_template('analytics.html')
@app.route('/detection')
def detection():
    return render_template('crop_disease_prediction.html')
@app.route('/prediction')
def prediction():
    return render_template('crop_prediction.html')

@app.route('/getdiseaseresult',methods=['POST','GET'])
def getdiseaseresult():
    global file_name
    print("getdiseaseresult is requested")
    if request.method=='POST':
        print("Post Method")
        if file_name!="":
            print("File Found")
            return jsonify({"data":"We are Working on it, Please Try After some week"})
        else:
            return "ERROR"
    else:
        return "ERROR"






@app.route('/getresult',methods=['POST','GET'])
def getresult():
    global file_name
    print("getresult is requested")
    if request.method=='POST':
        print("Post Method")
        if file_name!="":
            print("File Found")
            trained_model=tensorflow.keras.models.load_model('../Models/Simple_Model_4_colored_For_Crop_Detection.h5')
            print(trained_model.summary())
            image_array=cv2.imread(os.path.dirname(__file__)+f"\\static\\images\\data\\{file_name}")
            print(image_array)
            image_array=cv2.resize(image_array,(160,160))
            image_array=image_array/255
            print(image_array)
            image_array=numpy.array([image_array])
            print(image_array.shape)
            # image_array=numpy.expand_dims(image_array,axis=-1)
            predictions=trained_model.predict([image_array]).round(5)*100
            prediction_=predictions[0]
            print(prediction_)
            temp=list(prediction_)
            sorted_classes={}
            for i in prediction_:
                sorted_classes.update({class_list[temp.index(max(temp))]:max(temp)})
                temp[temp.index(max(temp))]=-1
            print(sorted_classes)
            index_=0
            max_=max(prediction_)
            for i in range(len(prediction_)):
                if prediction_[i]==max_:
                    index_=i
            
            print(class_list[index_])
            response_value="""
             <h2>Crop and their prediction values</h2>
            <ul>
            """
            for key,value in sorted_classes.items():
                response_value=response_value+f"""
                <li><span class="red">{key}</span> -- >  <b>{value:.3f}%</b></li>
                """
            response_value=response_value+"""
             </ul>            
            """
            print(response_value)
            return jsonify({
                "data":response_value
            })
        else:
            return "ERROR"
    else:
        return "ERROR"






@app.route('/upload',methods=['POST','GET'])
def upload():
    global file_name
    if request.method=='POST':
        print(request.files['file'])
        # print(request.files)
        file=request.files['file']
        file_name=file.filename
        extension=file_name.split(".")[-1]
        print(extension)
        miliseconds_value=round(time.time()*1000)
        file_name=f"{miliseconds_value}.{extension}"
        print(file_name)
        file_path=f"/static/images/data/{file_name}"
        file.filename=file_name
        print(file)
        file.save(os.path.dirname(__file__)+f"\\static\\images\\data\\{file_name}")
        return jsonify({'image_path':file_path})
    else:
        return "error"







if __name__=='__main__':
    app.run(debug=True)