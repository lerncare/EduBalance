from flask import Blueprint, render_template
from flask_login import login_required, current_user
from utils.ai_coach import get_daily_tips
from utils.gamification import award_points
from models import ForumPost

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
@login_required
def dashboard():
    daily_tip = get_daily_tips(current_user)
    award_points(current_user.id, 1)  # Award points for visiting dashboard
    recent_posts = ForumPost.query.order_by(ForumPost.created_at.desc()).limit(5).all()
    return render_template('dashboard.html', user=current_user, daily_tip=daily_tip, recent_posts=recent_posts)
