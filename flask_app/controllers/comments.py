from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.comment import Comment

@app.route('/comment/create/<int:sighting_id>/<int:user_id>', methods=['POST'])
def create_comment(sighting_id, user_id):
    if not Comment.validate_comment(request.form):
        return redirect(f'/sighting/{sighting_id}')
    data = {
        "content": request.form['content'],
        "sighting_id": sighting_id,
        "user_id": user_id
    }
    Comment.add_comment(data)
    return redirect(f'/sighting/{sighting_id}')

@app.route('/comment/update/<int:comment_id>/<int:sighting_id>', methods=['POST'])
def update_comment(comment_id, sighting_id):
    if not Comment.validate_comment(request.form):
        return redirect(f'/sighting/{sighting_id}')
    data = {
        "id": comment_id,
        "content": request.form['content']
    }
    Comment.update_comment(data)
    return redirect(f'/sighting/{sighting_id}')

@app.route('/comment/delete/<int:comment_id>/<int:sighting_id>')
def delete_comment(comment_id, sighting_id):
    data = {
        "id": comment_id
    }
    Comment.delete_comment(data)
    return redirect(f'/sighting/{sighting_id}')