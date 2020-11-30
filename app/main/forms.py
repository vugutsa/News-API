from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Articles title',validators=[Required()])
    review = TextAreaField('News review', validators=[Required()])
    submit = SubmitField('Submit')