from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=False, port=80, host="0.0.0.0")
    app.config['TEMPLATES_AUTO_RELOAD'] = True

