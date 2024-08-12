from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/scripts.js')
def scripts():
    return send_from_directory('.', 'scripts.js')

@app.route('/potato.png')
def potato():
    return send_from_directory('.', 'potato.png')

if __name__ == '__main__':
    app.run(debug=True)
