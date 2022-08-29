##########################################
################# Import Libraries #######
##########################################

from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from datetime import datetime

import models
import forms

##########################################
################# ROUTING ################
##########################################

# Main Page route
@app.route('/')
def index():
    display_tasks = models.Task.query.all()
    return render_template('index.html', tasks=display_tasks )

# Add Task Page route
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        task_data = models.Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(task_data)
        db.session.commit()
        flash("Task added!!")
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

# Route to edit a task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    form = forms.AddTaskForm()
    task = models.Task.query.get(task_id)
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task updated')
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    flash(f'Task with id {task_id} does not exit')
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    form = forms.DeleteTaskForm()
    task = models.Task.query.get(task_id)
    if task:
        if form.validate_on_submit():
            if form.submit.data:
                db.session.delete(task)
                db.session.commit()
                flash('Task deleted')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    flash(f'Task with id {task_id} does not exit')
    return redirect(url_for('index'))
