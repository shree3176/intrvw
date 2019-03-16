from os import abort

from flask import render_template, redirect, url_for, abort, flash, request, current_app
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from app import db
from app.main.forms import RequirementForm, PostForm, EditProfileForm, ContactForm
from . import main
from ..models import User, Post, ProjectRequirement


@main.route('/cinnamon', methods=['GET', 'POST'])
def cinnamon():
    form = RequirementForm()
    if form.validate_on_submit():
        req = ProjectRequirement(email=form.email.data,
                                 full_name=form.name.data,
                                 contact_no=form.contact_no.data,
                                 project_type=form.project_type.data,
                                 proj_database=form.project_db.data,
                                 proj_lang=form.project_lang.data,
                                 proj_desc=form.description.data)
        db.session.add(req)
        db.session.commit()
        flash('We got your requirements. Will get back to you soon.')
        return redirect(url_for('main.index'))
    return render_template('cinnamon.html', form=form)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.post_date.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('user.html', user=user, posts=posts,
                           pagination=pagination)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        flash('Post saved.')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.post_date.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('index.html', form=form, posts=posts,
                           pagination=pagination)


@main.route('/interview_prep')
def interview_prep():
    return render_template('interview_prep.html')


@main.route('/bootstrap-interview-questions')
def bs_iq():
    return render_template('bootstrap-interview-questions.html')


@main.route('/javascript-interview-questions')
def js_iq():
    return render_template('javascript-interview-questions.html')


@main.route('/python-interview-questions')
def py_iq():
    return render_template('python-interview-questions.html')


@main.route('/contact_us')
def contact_us():
    form = ContactForm()
    return render_template('contact_us.html', form=form)