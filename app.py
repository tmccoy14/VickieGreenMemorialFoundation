from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/signUp")
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()