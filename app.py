from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Session use cheyyadaniki secret key
app.secret_key = "my_quiz_secret_key"


questions = [
    {
        "question": "Which language is used to create the structure of a webpage?",
        "options": ["Python", "HTML", "SQL", "Java"],
        "answer": "HTML"
    },
    {
        "question": "Which language is used for styling webpages?",
        "options": ["HTML", "CSS", "Python", "SQL"],
        "answer": "CSS"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "fun", "create"],
        "answer": "def"
    },
    {
        "question": "Which language is commonly used for backend development with Flask?",
        "options": ["Python", "HTML", "CSS", "XML"],
        "answer": "Python"
    },
    {
        "question": "Which data type stores multiple values in an ordered collection?",
        "options": ["String", "Integer", "List", "Boolean"],
        "answer": "List"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start")
def start_quiz():

    session["score"] = 0
    session["question_number"] = 0

    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    # POST request vachinappudu answer check chestam
    if request.method == "POST":

        user_answer = request.form.get("answer")

        current_question = session["question_number"]

        correct_answer = questions[current_question]["answer"]

        if user_answer == correct_answer:
            session["score"] += 1

        # Next question
        session["question_number"] += 1

        return redirect(url_for("quiz"))

    # Quiz complete ayithe result page
    current_question = session.get("question_number", 0)

    if current_question >=len(questions):

        return redirect(url_for("result"))

    question = questions[current_question]

    progress = int(
        (current_question / len(questions)) * 100
    )

    return render_template(
        "quiz.html",
        question=question,
        question_number=current_question + 1,
        total_questions=len(questions),
        progress=progress
    )


@app.route("/result")
def result():

    score = session.get("score", 0)

    total = len(questions)

    percentage = int((score / total) * 100)

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage
    )


@app.route("/restart")
def restart():

    session.clear()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)