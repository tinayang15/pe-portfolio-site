import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name="Caleb Aguirre-Leon", url=os.getenv("URL"),)

@app.route ('/experience')
def experience():
    return render_template('experience.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobby2="Photography")