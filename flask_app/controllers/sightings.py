from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.sighting import Sighting
from flask_app.models.comment import Comment
from flask_app.models.believer import Believer
from flask_app.models.non_believer import Non_believer

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
        "title" : request.form['title'],
        "location" : request.form['location'],
        "date" : request.form['date'],
        "time" : request.form['time'],
        "description" : request.form['description'],
        "intensity" : request.form['intensity'],
        "num_of_activities" : request.form['num_of_activities'],
        "reaction" : request.form['reaction'],
        "user_id" : session['user_id']
    }
    Sighting.add_sighting(data)
    return redirect('/sightings')

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
        "id" : id,
        "title" : request.form['title'],
        "location" : request.form['location'],
        "date" : request.form['date'],
        "time" : request.form['time'],
        "description" : request.form['description'],
        "intensity" : request.form['intensity'],
        "num_of_activities" : request.form['num_of_activities'],
        "reaction" : request.form['reaction']
    }
    Sighting.update_sighting(data)
    return redirect(f'/sighting/{id}')

@app.route('/sighting/<int:id>')
def view_sighting(id):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id" : id
    }
    data2 = {
        "sighting_id": id
    }
    this_sighting = Sighting.get_one_sighting_by_user(data)
    all_comments = Comment.get_comment_by_sighting_and_user(data)
    num_of_believers = Believer.get_num_believers(data2)
    num_of_non_believers = Non_believer.get_num_non_believers(data2)
    all_believers = Believer.get_all_believer()
    print(all_believers)
    all_non_believers = Non_believer.get_all_non_believer()
    return render_template(
        'sighting_view.html', 
        this_sighting=this_sighting, 
        all_comments=all_comments,  
        num_of_believers= num_of_believers, 
        num_of_non_believers=num_of_non_believers,
        all_believers = all_believers,
        all_non_believers = all_non_believers
        )

@app.route('/sighting/delete/<int:id>/<int:user_id>')
def delete_sighting(id, user_id):
    data = {
        "id" : id
    }
    Sighting.delete_sighting(data)
    return redirect(f'/user/{user_id}')