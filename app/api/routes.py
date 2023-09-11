from flask import Blueprint, request, jsonify, render_template
from app.helpers import token_required
from app.models import db, User, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix = '/api')