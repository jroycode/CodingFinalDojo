from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.sighting import Sighting
from flask_app.models.user import User

@app.route('/sighting/report')
def report_sighting():
    if 'user_id' not in session:
        return redirect ('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('report_sighting.html', user=User.get_user_by_id(data))

@app.route('/sighting/create', methods=['POST'])
def create_sighting():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sighting.validate_sighting(request.form):
        return redirect('/sighting/report')
    data = {
        "location": request.form["location"],
        "date_made": request.form["date_made"],
        "description": request.form["description"],
        "sasquatches_seen": int(request.form["sasquatches_seen"]),
        "user_id": session["user_id"],
    }
    Sighting.create_sighting(data)
    return redirect('/user/dashboard')

@app.route('/sighting/edit/<int:id>')
def edit_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_sighting.html", edit=Sighting.get_one(data), user=User.get_user_by_id(user_data))

@app.route('/sighting/update', methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Sighting.validate_sighting(request.form):
        return redirect('/sighting/report')
    data = {
        "location": request.form["location"],
        "date_made": request.form["date_made"],
        "description": request.form["description"],
        "sasquatches_seen": int(request.form["sasquatches_seen"]),
        "id": request.form['id']
    }
    Sighting.update(data)
    return redirect('/user/dashboard')

@app.route('/sighting/<int:id>')
def view_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("view_sighting.html",sighting=Sighting.get_one(data),user=User.get_user_by_id(user_data))

@app.route('/sighting/destroy/<int:id>')
def destroy_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Sighting.destroy(data)
    return redirect('/user/dashboard')