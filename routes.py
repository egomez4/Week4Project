#sudo pip3 install petpy
import petpy
from flask import Flask, render_template, url_for, flash, redirect
from forms import AnimalsForm, OrganizationForm
from flask_behind_proxy import FlaskBehindProxy


app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '9964c5b701ffc08bb7832c6c9d603d04'

api_key = 'JNGvI97bit2E3e4Vawh0diK8VQyRwXvIoaK8sGAm91DevlHJwU'
api_secret = 'IijpJC2ivqOzvZrJItbXxBNp7KUHZefKsP5YlNtY'

pf = petpy.Petfinder(api_key, secret=api_secret)

#print(pf.animal_types())

@app.route('/')
def home():
    return render_template('home.html', subtitle = 'Home')

@app.route('/animals', methods=['GET', 'POST'])
def animals():
    form = AnimalsForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('animals.html', subtitle='Animals', form=form)

@app.route('/organizations', methods=['GET', 'POST'])
def organizations():
    form = OrganizationForm()
    zip_code = form.zip_code.data
    print(zip_code)
    return render_template('organizations.html', subtitle='Organizations', form=form)

if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")