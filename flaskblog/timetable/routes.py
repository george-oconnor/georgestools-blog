from flask import render_template, request, Blueprint
from flask_login import login_required
from flaskblog.timetable.forms import RefreshForm
from flaskblog.timetable.utils import getTimetableFile, countScheduledClasses
from flaskblog.models import Class
from flaskblog import db

timetable = Blueprint('timetable', __name__)

times = ["08:33:00", "09:33:00", "10:33:00", "11:33:00", "12:33:00", "13:33:00", "14:33:00", "15:33:00", "16:33:00", "17:33:00", "18:33:00"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

@timetable.route("/timetable", methods=['GET', 'POST'])
@login_required
def home():
    classes = Class.query.all()
    refresh_form = RefreshForm()
    if refresh_form.validate_on_submit():
        df = getTimetableFile()
    return render_template('timetable.html', 
                title="Full", 
                refresh_form=refresh_form, 
                classes=classes, 
                times=times,
                days=days,
                scheduled_classes=countScheduledClasses(classes, times, days),
                total_classes=len(classes))

@timetable.route("/timetable/teacher/<string:acronym>", methods=['GET', 'POST'])
@login_required
def teacher_timetable(acronym):
    classes = Class.query.filter_by(acronym=acronym).all()
    refresh_form = RefreshForm()
    if refresh_form.validate_on_submit():
        df = getTimetableFile()
    return render_template('timetable.html', 
                title=acronym, 
                refresh_form=refresh_form, 
                classes=classes, 
                times=times,
                days=days,
                scheduled_classes=countScheduledClasses(classes, times, days),
                total_classes=len(classes))

@timetable.route("/timetable/subject/<string:subject>", methods=['GET', 'POST'])
@login_required
def subject_timetable(subject):
    classes = Class.query.filter_by(subject=subject).all()
    refresh_form = RefreshForm()
    if refresh_form.validate_on_submit():
        df = getTimetableFile()
    return render_template('timetable.html', 
                title=subject, 
                refresh_form=refresh_form, 
                classes=classes, 
                times=times,
                days=days,
                scheduled_classes=countScheduledClasses(classes, times, days),
                total_classes=len(classes))

@timetable.route("/timetable/group/<string:group>", methods=['GET', 'POST'])
@login_required
def group_timetable(group):
    classes = Class.query.filter_by(group=group).all()
    refresh_form = RefreshForm()
    if refresh_form.validate_on_submit():
        df = getTimetableFile()
    return render_template('timetable.html', 
                title="Timetable", 
                refresh_form=refresh_form, 
                classes=classes, 
                times=times,
                days=days,
                scheduled_classes=countScheduledClasses(classes, times, days),
                total_classes=len(classes))

@timetable.route("/timetable/room/<string:room>", methods=['GET', 'POST'])
@login_required
def room_timetable(room):
    classes = Class.query.filter_by(room=room).all()
    refresh_form = RefreshForm()
    if refresh_form.validate_on_submit():
        df = getTimetableFile()
    return render_template('timetable.html', 
                title="Timetable", 
                refresh_form=refresh_form, 
                classes=classes, 
                times=times,
                days=days,
                scheduled_classes=countScheduledClasses(classes, times, days),
                total_classes=len(classes))
