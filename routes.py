from flask import Blueprint, render_template, request, redirect, url_for

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/upload', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        resume = request.files['resume']
        # Process the resume file here
        return redirect(url_for('routes.home'))
    return render_template('upload.html')

@routes.route('/about')
def about():
    return render_template('about.html')

@routes.route('/contact')
def contact():
    return render_template('contact.html')
