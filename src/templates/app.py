from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/form_clients')
def form_clients():
    return render_template('form_clients.html')

@app.route('/List_clients')
def list_clients():
    return render_template('List_clients.html')

if __name__ == '__main__':
    app.run(debug=True)