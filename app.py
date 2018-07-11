from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Instance-W connected<br />Instance-Y connected<br />Instance-Z connected<br />'

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)
