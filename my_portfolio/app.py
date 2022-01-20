from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("about.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/interests")
def interests():
    return render_template("interests.html")

@app.route("/awards")
def awards():
    return render_template("awards.html")

if __name__ == '__main__':
    app.run()