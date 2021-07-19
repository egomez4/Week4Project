#sudo pip3 install petpy
import petpy
from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

api_key = 'JNGvI97bit2E3e4Vawh0diK8VQyRwXvIoaK8sGAm91DevlHJwU'
api_secret = 'IijpJC2ivqOzvZrJItbXxBNp7KUHZefKsP5YlNtY'

pf = petpy.Petfinder(api_key, secret=api_secret)

#print(pf.breeds())

@app.route('/')
def home():
    return render_template('home.html', subtitle = 'Home')

@app.route('/animals')
def animals():
    return render_template('animals.html', subtitle='Animals')

@app.route('/organizations')
def organizations():
    return render_template('organizations.html', subtitle='Organizations')

if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")