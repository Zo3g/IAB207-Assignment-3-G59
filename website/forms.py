from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, IntegerField, FloatField, DateField, TimeField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed


ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

# Create new event

class EventForm(FlaskForm):
  name = StringField('Your Event Name', validators=[InputRequired()])
  venuename = StringField('Venue', 
            validators=[InputRequired()])
  image = FileField('Destination Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])
  organiser = SelectField('Select', choices=['Faculty of Business', 'Faculty of Creative Industries', 'Faculty of Engineering', 'Faculty of Information Technology', 'Faculty of Sciences', 'QUT Bookclub', 'CODE Network', 'Debating Society', 'QUT Cheer and Dance', 'QUT Cliffhangers'])
  numticket = IntegerField('Number of available tickets', validators=[InputRequired()])
  ticketcost = FloatField('Cost of a single ticket', validators=[InputRequired()])
  eventdate = DateField('Event date', format='%Y-%m-%d', validators=[InputRequired()])
  eventtime = TimeField('Event time', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  submit = SubmitField("Create")

class EventEditForm(FlaskForm):
  name = StringField('Your Event Name')
  venuename = StringField('Venue')
  image = FileField('Destination Image', validators=[
      FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])
  organiser = SelectField('Select', choices=['Faculty of Business', 'Faculty of Creative Industries', 'Faculty of Engineering', 'Faculty of Information Technology', 'Faculty of Sciences', 'QUT Bookclub', 'CODE Network', 'Debating Society', 'QUT Cheer and Dance', 'QUT Cliffhangers'])
  numticket = IntegerField('Number of available tickets')
  ticketcost = FloatField('Cost of a single ticket')
  eventdate = DateField('Event date', format='%Y-%m-%d')
  eventtime = TimeField('Event time')
  description = TextAreaField('Description')
  submit = SubmitField("Submit")
  

# creates the login information


class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[
                            InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form


class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])
    address = StringField("Address", validators=[InputRequired()])
    contactNumber = StringField("Mobile Number", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    # submit button
    submit = SubmitField("Register")

    # User comment


class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Submit')

class BookingForm(FlaskForm):
  tickets = IntegerField('Number of tickets purchased', validators=[InputRequired()])
  submit = SubmitField("Tickets selected")