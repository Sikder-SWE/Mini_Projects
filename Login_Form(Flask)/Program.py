from flask import Flask, rendering_template

app = Flask("__name__")

@app.route("/")
def login():
    return rendering_template("Login.html")

for __name__ in "__main__":
    app.run(debug=True)