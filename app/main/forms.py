from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class RequirementForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    name = StringField('Name', validators=[DataRequired(), Length(1, 64),
                                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                  'Usernames must have only letters, numbers, dots or '
                                                  'underscores')])
    contact_no = StringField('Contact No', validators=[DataRequired()])
    project_type = SelectField('Project Type', choices=[('desktop Application', 'Desktop Application'),
                                                        ('website', 'Website'), ('web', 'Web Application'),
                                                        ('android', 'Android Application')],
                               validators=[DataRequired])
    project_db = SelectField('Database', choices=[('oracle', 'Oracle'), ('postgre', 'Postgre'), ('mysql', 'MySQL')],
                             validators=[DataRequired])
    project_lang = SelectField('Programming Language', choices=[('java', 'Java'), ('py', 'Python'), ('php', 'PHP')])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Register')


class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired])
    email = StringField("Email", validators=[DataRequired])
    subject = StringField("Subject", validators=[DataRequired])
    message = TextAreaField("Message", validators=[DataRequired])
    submit = SubmitField("Send")