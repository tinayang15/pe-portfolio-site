#!/bin/bash

# curl http://127.0.0.1:5000/api/timeline_post

# curl -X POST http://127.0.0.1:5000/api/timeline_post -d "content=Hi&email=testing@email.com&image=./static/img/MatchEnchanter.png&name=Math Enchanter"

cd /Users/tinayang/MLH/Portfolio/pe-portfolio-site

# Variables = API endpoint URLs
GET_ENDPOINT="http://127.0.0.1:5000/api/timeline_post"
POST_ENDPOINT="http://127.0.0.1:5000/api/timeline_post"
DELETE_ENDPOINT="http://127.0.0.1:5000/api/timeline_post/2"

# Function to create a random timeline post
create_timeline_post() {
    local name="Test Post $RANDOM"
    local email="Test email"
    local content="This is a test post."
    local image="../static/img/annoymous.png"


    # Send POST request using curl with form-data
curl -X POST -F "name=$name" -F "email=$email" -F "content=$content" -F "image=$image" $POST_ENDPOINT

}

# Function to retrieve and display all posts
get_timeline_posts() {
    curl $GET_ENDPOINT
}

# Function to delete post
delete_timeline_post() {
    curl -X DELETE $DELETE_ENDPOINT
}

# Call the functions to test the endpoints
# create_timeline_post
get_timeline_posts
# delete_timeline_post

