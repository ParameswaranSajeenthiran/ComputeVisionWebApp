from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("faceMesh.html")


@app.route("/faceMesh")
def faceMesh():
    return render_template("faceMesh.html")

@app.route("/face")
def face():
    return render_template("face.html")


@app.route("/pose")
def pose():
    return render_template("pose.html")

@app.route("/holistic")
def holistics():
    return render_template("holistic.html")

@app.route("/hands")
def hands():
    return render_template("hands.html")


if __name__=="__main__":
    app.run(debug=True)