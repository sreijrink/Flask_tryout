from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "<p>Dit is les 11 van de NHA opeldeiding - Programmeren voor beginners</p>"

if __name__ == '__main__':
    app.run(port=5000,debug=True)