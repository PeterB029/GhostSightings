from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.non_believer import Non_believer

@app.route('/create/non_believer', methods=['POST'])
def create_non_believer():
    data = {
        "user_id": request.form['user_id'],
        "sighting_id": request.form['sighting_id']
    }
    Non_believer.add_non_believer(data)
    return redirect(f'/sighting/{request.form["sighting_id"]}')

@app.route('/delete/non_believer/<int:user_id>/<int:sighting_id>')
def delete_non_believer(user_id, sighting_id):
    data = {
        "user_id":user_id,
        "sighting_id": sighting_id
    }
    Non_believer.remove_non_believer(data)
    return redirect(f'/sighting/{sighting_id}')