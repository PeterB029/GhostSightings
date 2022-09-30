from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.sighting import Sighting

@app.route('/sighting/add')
def add_sighting_page():
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    return render_template('sighting_create.html')

@app.route('/sighting/create', methods=['POST'])
def create_sighting():
    if not Sighting.validate_sighting(request.form):
        return redirect('/sighting/add')
    data = {
        "location" : request.form['location'],
        "date" : request.form['date'],
        "time" : request.form['time'],
        "description" : request.form['description'],
        "intensity" : request.form['intensity'],
        "num_of_activities" : request.form['num_of_activities'],
        "reaction" : request.form['reaction']
    }
    Sighting.add_sighting(data)
    return render_template('/sightings')

@app.route('/sighting/edit/<int:id>')
def edit_sighting_page(id):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id" : id
    }
    this_sighting = Sighting.get_one_sighting_by_user(data)
    return render_template('sighting_edit.html', this_sighting=this_sighting)

@app.route('/sighting/update/<int:id>', methods=['POST'])
def update_sighting(id):
    if not Sighting.validate_sighting(request.form):
        return redirect(f'/sighting/edit/{id}')
    data = {
        "location" : request.form['location'],
        "date" : request.form['date'],
        "time" : request.form['time'],
        "description" : request.form['description'],
        "intensity" : request.form['intensity'],
        "num_of_activities" : request.form['num_of_activities'],
        "reaction" : request.form['reaction']
    }
    Sighting.update_sighting(data)
    return render_template('/sightings')

@app.route('/sighting/<int:id>')
def view_sighting(id):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id" : id
    }
    this_sighting = Sighting.get_one_sighting_by_user(data)
    return render_template('sighting_view.html', this_sighting=this_sighting)

@app.route('/sighting/delete/<int:id>')
def delete_sighting(id):
    data = {
        "id" : id
    }
    Sighting.delete_sighting(data)
    return redirect('/sightings')