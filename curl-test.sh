#!/bin/zsh

# curl http://127.0.0.1:5000/api/timeline_post

# curl -X POST http://127.0.0.1:5000/api/timeline_post -d "content=Med-Minder is an application that allows healthcare administration to personalize a list of medications for each patient. Within each medication added, you are able to include prescription directions.&deploy=https://swish-sesh.herokuapp.com/&github=https://github.com/mannyaalonso/swish-sesh&image=../static/img/Swish-sesh.png&name=Med-Minder&tool=React | MongoDB | Express | Node | CSS"

cd /Users/tinayang/MLH/Portfolio/pe-portfolio-site

# Variables for API endpoint URLs
GET_ENDPOINT="http://127.0.0.1:5000/api/timeline_post"
POST_ENDPOINT="http://127.0.0.1:5000/api/timeline_post"
DELETE_ENDPOINT="http://127.0.0.1:5000/api/timeline_post/<post_id>"

# Function to create a random timeline post
create_timeline_post() {
    local name="Test Post $RANDOM"
    local tool="Test Tool"
    local content="This is a test post."
    local image="../random/test.jpg"
    local github="https://github.com/test/nowork"
    local deploy="https://test.com/nowork"

    # Send POST request using curl
    # Send POST request using curl with form-data
curl -X POST -F "name=$name" -F "tool=$tool" -F "content=$content" -F "image=$image" -F "github=$github" -F "deploy=$deploy" $POST_ENDPOINT

}

# Function to retrieve and display all timeline posts
get_timeline_posts() {
    # Send GET request using curl
    curl $GET_ENDPOINT
}

# Function to delete a timeline post
delete_timeline_post() {
    local post_id="<post_id>"

    # Send DELETE request using curl
    curl -X DELETE $DELETE_ENDPOINT
}

# Call the functions to test the endpoints
create_timeline_post
#get_timeline_posts

# Uncomment the line below to test the DELETE endpoint
# delete_timeline_post

