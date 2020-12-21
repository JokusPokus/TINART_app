from flask import Blueprint

lm = Blueprint("lm", __name__)

from . import views