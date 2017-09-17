from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return rende_template("index.html")

@app.route("/about")
def about():
	return rende_template("about.html")

if __name__ == "__main__":
  app.run(debug=True)