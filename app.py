from flask import Flask, request, render_template, redirect, session, url_for, flash

import data

app = Flask(__name__)
app.config["SECRET_KEY"] = "uF_a0HhS1HAneoA0Xe8Gw"


@app.route("/")
def index():
    if 'logged_in' in session:
        username = session['username']
    return render_template("index.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        users = data.users
        for user in users:
            if username in user:
                hashed_password = user[username]
                if data.verify_password(password, hashed_password):
                    session['username'] = username
                    session['logged_in'] = True
                    session['index'] = 0
                    return redirect("/")
                else:
                    flash("Wrong username or password")
                    return render_template("login.html", users=data.users, err="err")
        else:
            flash("Wrong username or password")
            return render_template("login.html", users=data.users, err="err")
    return render_template("login.html", users=data.users, err=0)


@app.route("/test", methods=["GET", "POST"])
def test():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    questions = data.questions
    number_of_question = len(questions)
    if request.method == 'GET':
        session['corect_answers'] = 0
        session['question_nr'] = 0
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer == 'True':
            session['corect_answers'] += 1
        session['question_nr'] += 1
    if session['question_nr'] == len(questions):
        return redirect("/result")
    question = list(questions.keys())[session['question_nr']]
    return render_template("test.html", questions=questions, question=question, number_of_question=number_of_question)


@app.route("/result")
def result():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    questions = data.questions
    number_of_question = len(questions)
    return render_template("result.html", number_of_question=number_of_question)


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop('logged_in', None)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
