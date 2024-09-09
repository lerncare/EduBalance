from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required
from urllib.parse import urlparse
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from utils.gamification import award_points

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        award_points(user.id, 10)  # Award points for registration
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@bp.route('/check_db_and_create_test_user')
def check_db_and_create_test_user():
    try:
        # Check database connection
        users = User.query.all()
        
        # Create test user
        test_user = User.query.filter_by(username='testuser').first()
        if not test_user:
            test_user = User(username='testuser', email='testuser@example.com')
            test_user.set_password('testpassword123')
            db.session.add(test_user)
            db.session.commit()
        
        # Verify test user creation
        created_user = User.query.filter_by(username='testuser').first()
        if created_user:
            return jsonify({'status': 'success', 'message': 'Database connection successful and test user created/verified.'})
        else:
            return jsonify({'status': 'error', 'message': 'Test user creation failed.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Database operation failed: {str(e)}'})
