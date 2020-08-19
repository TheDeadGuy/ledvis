from flask import Flask, redirect, render_template, session, request, url_for
import socket
import json

olstate = 9
state = 0
FlaRed = 0
FlaGreen = 0
FlaBlue = 0


app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')


@app.route('/btn_click')
def btn_click():
        global state
        global olstate
        if request.args['vis_index'] != 0:
            olstate = request.args['vis_index']
        state = request.args['vis_index']
        return render_template('index.html')

@app.route('/get_settings', methods=['GET'])
def get_settings():
        return json.dumps({'vis_index': state})

@app.route('/rgb_sender', methods=['POST', 'GET'])
def handle_data():
    global FlaRed
    global FlaGreen
    global FlaBlue
    if request.method == 'POST':
       #result = request.form
       #return render_template("result.html",result = result)
       if request.form['Red'] != "":
           FlaRed = request.form['Red']
       if request.form['Green'] != "":
           FlaGreen = request.form['Green']
       if request.form['Blue'] != "":
           FlaBlue = request.form['Blue']
       #return render_template("result.html",result = result)
       #return render_template('index.html')
       return redirect(url_for('index'))

@app.route('/get_colour', methods=['GET'])
def get_colour():
	return json.dumps({'FlaRed': FlaRed,'FlaGreen': FlaGreen,'FlaBlue': FlaBlue})

@app.route('/on')
def on():
    global state
    global olstate
    state = olstate
    return "Okay"

@app.route('/off')
def off():
    global state
    state = 0
    return "Okay"

if __name__ == '__main__':
        app.run(host='0.0.0.0')
