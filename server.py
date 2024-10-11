from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("home.html", title="Airbnb2", message="Rent my house")

if __name__ == "__main__":
    app.run(debug=True)