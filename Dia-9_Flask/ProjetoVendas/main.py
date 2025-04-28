from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('Index.html', titulo='Página Inicial')

if __name__ == '__main__':
    app.run(debug=True)