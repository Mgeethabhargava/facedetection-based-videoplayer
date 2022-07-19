from flask import Flask
from flask import render_template

app = Flask(__name__)
app.secret_key = 'Alexas'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
