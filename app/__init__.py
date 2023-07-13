import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    tool = CharField()
    content = TextField()
    image = CharField()
    github = CharField()
    deploy = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', name="Tina Yang", url=os.getenv("URL"),)

@app.route ('/experience')
def experience():
    return render_template('experience.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', hobby2="Photography")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    tool = request.form['tool']
    content = request.form['content']
    image = request.form['image']
    github = request.form['github']
    deploy = request.form['deploy']
    timeline_post = TimelinePost.create(name=name, tool=tool, content=content, image=image, github=github, deploy=deploy)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods = ['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }