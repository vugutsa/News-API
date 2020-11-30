from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,errors
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()