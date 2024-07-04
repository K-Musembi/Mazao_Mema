from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.county import County
from models.consultant import Consultant
from models.input_dealer import InputDealer
from models.buyer import Buyer
