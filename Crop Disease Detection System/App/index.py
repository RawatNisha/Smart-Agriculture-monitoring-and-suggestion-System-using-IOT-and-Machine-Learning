from flask import Flask,render_template,redirect,request,send_from_directory,jsonify

file_name=""


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


@app.route('/upload',methods=['POST','GET'])
def upload():
    global file_name;
    if request.method=="POST":
        print(request.files['file']);








if __name__=='__main__':
    app.run(debug=True)