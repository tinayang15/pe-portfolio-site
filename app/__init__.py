import os, re
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == 'true':
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    image = CharField()
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

# @app.route('/timeline')
# def timeline():
#     return render_template('timeline.html', title="Timeline")

@app.route('/timeline')
def timeline():
    timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template('timeline.html', timeline_posts=timeline_posts)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():

    name = request.form['name']
    if not name or name == "":
        return "Invalid name", 400
    
    email = request.form['email']
    if not email or email == "" or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return "Invalid email", 400
    
    content = request.form['content']
    if not content or content == "":
        return "Invalid content", 400
    
    image = request.form['image']

    timeline_post = TimelinePost.create(name=name, email=email, content=content, image=image)

    return redirect(url_for('timeline'))

@app.route('/api/timeline_post', methods = ['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<post_id>', methods=['DELETE'])
def delete_time_line_post(post_id):
    try:
        timeline_post = TimelinePost.get_by_id(post_id)
        timeline_post.delete_instance()

        return {'message': 'Timeline post deleted successfully'}
    except TimelinePost.DoesNotExist:
        return {'error': 'Timeline post not found'}, 404
    except:
        return {'error': 'Failed to delete timeline post'}, 500

