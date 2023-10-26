from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, IntegerField, FloatField, DateTimeField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed


ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

#Create new event
class EventForm(FlaskForm):
  name = StringField('Your Event Name', validators=[InputRequired()])
  venue = StringField('Venue', 
            validators=[InputRequired()])
  image = FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])
  organiser = SelectField('Select', choices=['Faculty of Business', 'Faculty of Creative Industries', 'Faculty of Engineering', 'Faculty of Information Technology', 'Faculty of Sciences', 'QUT Bookclub', 'CODE Network', 'Debating Society', 'QUT Cheer and Dance', 'QUT Cliffhangers'])
  numticket = IntegerField('Number of available tickets', validators=[InputRequired()])
  ticketcost = FloatField('Cost of a single ticket', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  submit = SubmitField("Create")

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")