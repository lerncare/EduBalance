from extensions import db

# Import models
from .user import User
from .resource import Resource
from .forum import ForumPost

__all__ = ['db', 'User', 'Resource', 'ForumPost']
