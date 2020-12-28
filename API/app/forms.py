from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext as _l

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SearchForm(FlaskForm):
    q = StringField(_l('Search for...'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)

class ClassifierForm(FlaskForm):
    index = StringField('Enter your text here', validators=[DataRequired()])
    submit = SubmitField('Categorize')