from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, TextAreaField, validators
from wtforms.validators import DataRequired, Length
import pickle
import sqlite3
import os
import numpy as np
import joblib

app = Flask(__name__)

class Formdata(Form):
 inputvalue = TextAreaField('',validators = [DataRequired(), Length(min=2, max=120)])
 
@app.route("/", methods= ['GET','POST'])
def index():
    form = Formdata (request.form)
    if request.method == 'POST':
       inputvalue = request.form['inputvalue']
       return redirect(url_for('results', data = inputvalue))
    return render_template('index.html', title = 'Tweet',form=form)


@app.route('/results')
def results(data):
    form = Formdata()
    return render_template('display.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
