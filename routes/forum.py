from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, ForumPost

bp = Blueprint('forum', __name__)

@bp.route('/forum')
def forum():
    posts = ForumPost.query.order_by(ForumPost.created_at.desc()).all()
    return render_template('forum.html', posts=posts)

@bp.route('/forum/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = ForumPost(title=title, content=content, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('forum.forum'))
    return render_template('new_post.html')

@bp.route('/forum/post/<int:post_id>')
def view_post(post_id):
    post = ForumPost.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)
