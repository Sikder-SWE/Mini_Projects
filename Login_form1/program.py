from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Login.html")



for __name__ in "__main__":
    app.run(debug=True)