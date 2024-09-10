import unittest
from datetime import datetime
from app import create_app, db
from models import User, ForumPost

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='test', email='test@example.com')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_user_creation(self):
        u = User(username='john', email='john@example.com')
        u.set_password('password')
        db.session.add(u)
        db.session.commit()
        self.assertIsNotNone(User.query.filter_by(username='john').first())

    def test_forum_post_creation(self):
        u = User(username='jane', email='jane@example.com')
        u.set_password('password')
        db.session.add(u)
        db.session.commit()

        post = ForumPost(title='Test Post', content='This is a test post', user_id=u.id)
        db.session.add(post)
        db.session.commit()

        retrieved_post = ForumPost.query.filter_by(title='Test Post').first()
        self.assertIsNotNone(retrieved_post)
        self.assertEqual(retrieved_post.content, 'This is a test post')
        self.assertEqual(retrieved_post.user_id, u.id)
        self.assertIsInstance(retrieved_post.created_at, datetime)

if __name__ == '__main__':
    unittest.main()
