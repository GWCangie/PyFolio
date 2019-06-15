from flask import Flask


app = Flask(__name__)

@app.route("/")
def Web():
    return "PyFolio!"

if __name__ == "__main__":
    app.run()