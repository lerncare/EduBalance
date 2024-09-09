from models import User, db

def award_points(user_id, points):
    user = User.query.get(user_id)
    if user:
        user.points += points
        db.session.commit()
        check_badges(user)

def check_badges(user):
    if user.points >= 100 and "Novice" not in user.badges:
        user.badges.append("Novice")
    if user.points >= 500 and "Intermediate" not in user.badges:
        user.badges.append("Intermediate")
    if user.points >= 1000 and "Expert" not in user.badges:
        user.badges.append("Expert")
    db.session.commit()
