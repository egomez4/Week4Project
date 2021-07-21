# sudo pip3 install petpy
import petpy
import pandas as pd
from flask import Flask, render_template, url_for, flash, redirect
from forms import AnimalsForm, OrganizationForm
from flask_behind_proxy import FlaskBehindProxy


app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '9964c5b701ffc08bb7832c6c9d603d04'

api_key = 'JNGvI97bit2E3e4Vawh0diK8VQyRwXvIoaK8sGAm91DevlHJwU'
api_secret = 'IijpJC2ivqOzvZrJItbXxBNp7KUHZefKsP5YlNtY'

pf = petpy.Petfinder(api_key, secret=api_secret)


@app.route('/')
def home():
    return render_template('home.html', subtitle='Home')


@app.route('/animals', methods=['GET', 'POST'])
def animals():
    form = AnimalsForm()
    if form.validate_on_submit():
        animalType = form.animalType.data
        state = form.state.data
        kids = form.kids.data
        dogs = form.dogs.data
        cats = form.cats.data
        data = findAnimal(animalType, state, kids, dogs, cats)
        dictionary = createDictionary(data)
        df = dict_to_dataframes(dictionary)
        return render_template(
            'animalsResults.html',
            subtitle='results',
            data = df
            )
    return render_template('animals.html', subtitle='Animals', form=form)


@app.route('/organizations', methods=['GET', 'POST'])
def organizations():
    form = OrganizationForm()

    if form.validate_on_submit():
        # zip_code = form.zip_code.data
        state = form.state.data
        zip_code = form.zip_code.data
        data = find_organization(state=state, zip_code=zip_code)
        img_url = data['organizations'][0]['photos'][0]['medium']
        print(img_url)
        #dictionary = createDictionary(data)
        #df = dict_to_dataframes(dictionary)
        return render_template(
            'organizationResults.html',
            subtitle='Organizations',
            data=data, img_url=img_url)
    return render_template('organizations.html', subtitle='Organizations', form=form)



def findAnimal(animalType, state, kids, dogs, cats):
    return pf.animals(animal_type=animalType, location=state,
                      good_with_children=kids,
                      good_with_dogs=dogs,
                      good_with_cats=cats)

def find_organization(state, zip_code):
    return pf.organizations(state=state, location=zip_code)

def createDictionary(data):
    animalsDict = {}
    for animals in data['animals']:
        animalsDict[animals['id']] = [animals['name'], animals['age'], animals['size'], animals['url']]
    
    return animalsDict

def dict_to_dataframes(animalsDict):
    df = pd.DataFrame.from_dict(animalsDict,
                                  orient='index', columns=['Name','Age','Size', 'Link'])
    return df



if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")
