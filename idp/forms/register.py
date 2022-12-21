from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.file import FileField, FileAllowed

class frm_register(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    mail = StringField('E-mail', validators=[Email()])
    img = FileField('Profile image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Registrarse')