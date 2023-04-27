from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)
import subprocess

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z_beep_beep_boop_boop'


@app.route('/')
def index():
    return redirect(url_for('fortune'))


@app.route('/fortune/')
def fortune():
    # subprocess.check_output captures the output of running the command
    # so instead of writing to a file like before we can just capture it here
    output = subprocess.check_output('fortune | cowsay',
                                     shell=True).decode()
    return '<pre>' + output + '</pre>'


@app.route('/cowsay/<message>/')
def cowsay(message):
    output = subprocess.check_output('cowsay %s' %message,
                                     shell=True).decode()
    return '<pre>' + output + '</pre>'
