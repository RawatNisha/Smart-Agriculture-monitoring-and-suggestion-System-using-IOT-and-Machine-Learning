from flask import Flask,render_template,redirect,request,send_from_directory,jsonify




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




if __name__=='__main__':
    app.run(debug=True)