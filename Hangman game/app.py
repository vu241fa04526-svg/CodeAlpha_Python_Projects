from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret_key"

easy_words = ["cat", "dog", "sun", "car"]
medium_words = ["python", "coding", "laptop"]
hard_words = ["developer", "algorithm", "internship"]


@app.route("/", methods=["GET", "POST"])
def home():

    if "score" not in session:
        session["score"] = 0

    if request.method == "POST":

        # Start Game
        if "difficulty" in request.form:

            level = request.form["difficulty"]

            if level == "Easy":
                session["word"] = random.choice(easy_words)
            elif level == "Medium":
                session["word"] = random.choice(medium_words)
            else:
                session["word"] = random.choice(hard_words)

            session["guessed"] = []
            session["wrong"] = 0
            session["rewarded"] = False

        # Guess Letter
        elif "letter" in request.form and "word" in session:

            letter = request.form["letter"].lower()

            guessed = session.get("guessed", [])

            if letter not in guessed:
                guessed.append(letter)
                session["guessed"] = guessed

                if letter in session["word"]:
                    session["score"] += 10
                else:
                    session["wrong"] += 1
                    session["score"] -= 5

        # Restart
        elif "restart" in request.form:
            session.clear()
            session["score"] = 0

    word = session.get("word", "")
    guessed = session.get("guessed", [])
    wrong = session.get("wrong", 0)

    display_word = " ".join(
        [letter if letter in guessed else "_" for letter in word]
    )

    win = word and all(letter in guessed for letter in word)

    if win and not session.get("rewarded", False):
        session["score"] += 50
        session["rewarded"] = True

    lose = wrong >= 6

    return render_template(
        "index.html",
        word=display_word,
        score=session["score"],
        wrong=wrong,
        win=win,
        lose=lose,
        actual_word=word
    )


if __name__ == "__main__":
    app.run(debug=True)