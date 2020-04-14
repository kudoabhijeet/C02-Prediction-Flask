from flask import Flask , render_template,redirect
import requests

app = Flask(__name__)   

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/home')
def redirect_home():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)