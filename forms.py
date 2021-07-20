from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

states = [("AL", "Alabama"),
          ("AK", "Alaska"),
          ("AZ", "Arizona"),
          ("AR", "Arkansas"),
          ("CA", "California"),
          ("CO", "Colorado"),
          ("CT", "Connecticut"),
          ("DE", "Delaware"),
          ("DC", "District Of Columbia"),
          ("FL", "Florida"),
          ("GA", "Georgia"),
          ("HI", "Hawaii"),
          ("ID", "Idaho"),
          ("IL", "Illinois"),
          ("IN", "Indiana"),
          ("IA", "Iowa"),
          ("KS", "Kansas"),
          ("KY", "Kentucky"),
          ("LA", "Louisiana"),
          ("ME", "Maine"),
          ("MD", "Maryland"),
          ("MA", "Massachusetts"),
          ("MI", "Michigan"),
          ("MN", "Minnesota"),
          ("MS", "Mississippi"),
          ("MO", "Missouri"),
          ("MT", "Montana"),
          ("NE", "Nebraska"),
          ("NV", "Nevada"),
          ("NH", "New Hampshire"),
          ("NJ", "New Jersey"),
          ("NM", "New Mexico"),
          ("NY", "New York"),
          ("NC", "North Carolina"),
          ("ND", "North Dakota"),
          ("OH", "Ohio"),
          ("OK", "Oklahoma"),
          ("OR", "Oregon"),
          ("PA", "Pennsylvania"),
          ("RI", "Rhode Island"),
          ("SC", "South Carolina"),
          ("SD", "South Dakota"),
          ("TN", "Tennessee"),
          ("TX", "Texas"),
          ("UT", "Utah"),
          ("VT", "Vermont"),
          ("VA", "Virginia"),
          ("WA", "Washington"),
          ("WV", "West Virginia"),
          ("WI", "Wisconsin"),
          ("WY", "Wyoming")
          ]

animalType = [("dog", "Dog"),
              ("cat", "Cat"),
              ("bird", "Bird"),
              ("reptile", "Reptile"),
              ("smallfurry", "Small Furry"),
              ("horse", "Horse"),
              ("barnyard", "Barnyard")
              ]



class AnimalsForm(FlaskForm):
    animalType = SelectField('Animal Type', choices=animalType,
                             validators=[DataRequired()])
    # breed = StringField('Email',
    #                    validators=[DataRequired(), Email()])
    state = SelectField('State', choices=states, validators=[DataRequired()])
    kids = BooleanField('Good with Kids', default=False)
    dogs = BooleanField('Good with Dogs', default=False)
    cats = BooleanField('Good with Cats', default=False)
    submit = SubmitField('Search')


class OrganizationForm(FlaskForm):
    zip_code = StringField('Zip Code')
    state = SelectField('State', choices=states, validators=[DataRequired()])
    submit = SubmitField('Search')
