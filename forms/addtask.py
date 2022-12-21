from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp

class frm_addtask(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(max=255)])
    text = TextAreaField('Description:', validators=[DataRequired(), Length(max=2000)])
    estimatedTime = StringField('Estimated time:', validators=[Length(max=5), Regexp('^(1[0-2]|0?[1-9]):([0-5]?[0-9])$')])
    deadline = StringField('Deadline:', validators=[Length(max=10), Regexp('^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|(([1][26]|[2468][048]|[3579][26])00))))$')])
    submit = SubmitField('Send')