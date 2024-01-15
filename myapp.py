from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def greet():
    return ("Welcome from YourExam result.")

@app.route("/result/<int:mark>")
def result(mark):
    if 101> mark >=80:
        return f"You got grade (A) with the mark of {mark}"
    elif 80 > mark >=60:
        return f"You got grade (B) with the mark of {mark}"
    elif 60> mark  >=40:
        return f"You got grade (C) with the mark of {mark}"
    elif 40> mark:
        if mark ==0:
            return f"Try much harder next time. You got D"
        elif mark == 39:
            return f"Failed with just one mark. Gook luck next time. You got D"
        return f"You got grade (D) with the mark of {mark}"
    else:
        return f"This isn't funny"

if __name__=="__main__":
    app.run()