from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import Resource, db, User
from utils.gamification import award_points, check_badges

bp = Blueprint('resources', __name__)

@bp.route('/resources')
def resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)

@bp.route('/interactive-resources')
@login_required
def interactive_resources():
    resources = Resource.query.all()
    return render_template('interactive_resources.html', resources=resources)

@bp.route('/complete-resource', methods=['POST'])
@login_required
def complete_resource():
    resource_id = request.form.get('resource_id')
    resource = Resource.query.get(resource_id)
    if resource:
        initial_points = current_user.points
        award_points(current_user.id, resource.points)
        check_badges(current_user)
        db.session.refresh(current_user)
        earned_points = current_user.points - initial_points
        return jsonify({
            "success": True,
            "points": current_user.points,
            "badges": current_user.badges,
            "earned_points": earned_points
        })
    return jsonify({"success": False}), 400

@bp.route('/leaderboard')
@login_required
def leaderboard():
    top_users = User.query.order_by(User.points.desc()).limit(10).all()
    leaderboard_data = [{"username": user.username, "points": user.points} for user in top_users]
    return jsonify(leaderboard_data)
