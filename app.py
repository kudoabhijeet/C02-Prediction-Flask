from flask import Flask , render_template,redirect,request
import requests

app = Flask(__name__)   
fruits = ['Apple', 'Banana', 'Mango']
@app.route('/')
def home():
    return render_template('index.html', fruits = fruits)
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/home')
def redirect_home():
    return redirect('/')
@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['user']
    f = request.files['userfile']
    f.save(f.filename)
    return "<h2>Hello {}".format(name)

    
if __name__ == '__main__':
    app.run(debug = True)