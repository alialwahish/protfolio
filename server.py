from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def myProtfolio():
    return render_template('index.html')
@app.route('/about_me')
def aboutMw():
    return render_template('aboutMe.html')
@app.route('/project')
def project():
    return render_template('projects.html')
app.run(debug=True)