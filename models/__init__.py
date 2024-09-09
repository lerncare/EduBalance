from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models after db is defined
from .user import User
from .resource import Resource
from .forum import ForumPost

# Make db and models available at the package level
__all__ = ['db', 'User', 'Resource', 'ForumPost']
