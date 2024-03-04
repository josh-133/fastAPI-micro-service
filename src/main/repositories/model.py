import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from typing import List

import database as _database

class Recipe(_database.Base):
    __tablename__ = "recipes"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    ingredients = _sql.Column(_sql.String)
    method = _sql.Column(_sql.String)  