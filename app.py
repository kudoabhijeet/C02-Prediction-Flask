from flask import Flask , render_template,redirect,request
import requests
import joblib

app = Flask(__name__)   
m = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def model():
    if request.method == 'POST':
        engine_size = float(request.form['engine_size'])

        emission = str(m.predict([[engine_size]]))
        emission = emission[:-2]
        emission = emission[2:]
        print(emission)
    return render_template('index.html', emission = emission)

# @app.route('/login')
# def login():
#     return render_template('login.html')
# @app.route('/home')
# def redirect_home():
#     return redirect('/')
# #@app.route('/submit', methods = ['POST'])
# # def submit():
# #     name = request.form['user']
# #     f = request.files['userfile']
# #     f.save(f.filename)
# #     return "<h2>Hello {}".format(name)
# @app.route('/', method='POST')
# def load():

    
if __name__ == '__main__':
    app.run(debug = True)