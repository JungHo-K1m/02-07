from flask import Flask, render_template
from flask import Response, make_response
import logging

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
	return render_template('index.html')

@app.route("/menu/")
def menu1_flask():
    return render_template('menu.html')


@app.route("/menu2/")
def menu2_flask():
    return render_template('menu2.html')

@app.route("/menu3/")
def menu3_flask():
    return render_template('menu3.html')

@app.route("/romance/")
def romance_flask():
    return render_template('romance.html')


@app.route("/action/")
def action_flask():
    return render_template('action.html')

@app.route("/horror/")
def horror_flask():
    return render_template('horror.html')

@app.route("/thriller/")
def thriller_flask():
    return render_template('thriller.html')

@app.route("/anime/")
def anime_flask():
    return render_template('anime.html')

if __name__ == '__main__':
	app.run(debug=True)