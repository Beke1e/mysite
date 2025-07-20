from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/social')
def social():
    return render_template('social.html')

if __name__ == '__main__':
    app.run(debug=True)
