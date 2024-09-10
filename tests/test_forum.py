import unittest
from flask import url_for
from flask_login import current_user
from app import create_app, db
from models import User, ForumPost

class TestForumRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Create a test user
        user = User(username='testuser', email='testuser@example.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self, username, password):
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_new_post(self):
        self.login('testuser', 'testpassword')
        response = self.client.post('/forum/new', data=dict(
            title='Test Post',
            content='This is a test post content'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        post = ForumPost.query.filter_by(title='Test Post').first()
        self.assertIsNotNone(post)
        self.assertEqual(post.content, 'This is a test post content')

    def test_view_post(self):
        self.login('testuser', 'testpassword')
        # Create a test post
        post = ForumPost(title='Test Post', content='Test Content', user_id=1)
        db.session.add(post)
        db.session.commit()

        response = self.client.get(f'/forum/post/{post.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Post', response.data)
        self.assertIn(b'Test Content', response.data)

if __name__ == '__main__':
    unittest.main()
