from myproject import app
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug = True)