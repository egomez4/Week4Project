# sudo pip3 install petpy
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


@app.route('/')
def home():
    return render_template('home.html', subtitle='Home')


@app.route('/animals', methods=['GET', 'POST'])
def animals():
    form = AnimalsForm()
    if form.validate_on_submit():
        animalType = form.animalType.data
        print(animalType)
        state = form.state.data
        kids = form.kids.data
        dogs = form.dogs.data
        cats = form.cats.data
        try:
            data = findAnimal(animalType, state, kids, dogs, cats)
        except KeyError:
            return redirect(url_for('animals'))
        dictionary = createDictionary(data)
        return render_template('animalsResults.html',
                                subtitle='Results',
                                data=dictionary
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

        # get all organizations
        orgs_list = []

        for org in data['organizations']:
            # dictionary for organization
            orgs = {}

            # fill in organization information
            orgs.update({'id': org['id']})
            orgs.update({'name': org['name']})
            orgs.update({'email': org['email']})
            orgs.update({'phone': org['phone']})
            orgs.update({'address': org['address']})
            orgs.update({'website': org['website']})
            # some orgs may not have an image
            if org['photos']:
                orgs.update({'photo': org['photos'][0]['medium']})

            orgs.update({'social_media': org['social_media']})

            # add this organization to the list of all organizations
            orgs_list.append(orgs)

        return render_template('organizationResults.html', subtitle='Organizations', data=data, orgs=orgs_list)
    
    return render_template('organizations.html', subtitle='Organizations', form=form)


def findAnimal(animalType, state, kids, dogs, cats):
    return pf.animals(animal_type=animalType, location=state,
                      good_with_children=kids,
                      good_with_dogs=dogs,
                      good_with_cats=cats,
                      return_df = True
                    )


def find_organization(state, zip_code):
    return pf.organizations(state=state, location=zip_code)


def createDictionary(data):
    animalsDict = {}
    for ind in data.index:
        animalsDict[data['id'][ind]] = {'Name': data['name'][ind],
                                        'Species': data['species'][ind],
                                        'Age': data['age'][ind], 
                                        'Size': data['size'][ind], 
                                        'Link': data['url'][ind],
                                        'Photo': data['primary_photo_cropped.small'][ind],
                                       }
    return animalsDict


if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")