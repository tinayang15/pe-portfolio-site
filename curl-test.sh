#!/bin/zsh

# curl http://127.0.0.1:5000/api/timeline_post

# curl -X POST http://127.0.0.1:5000/api/timeline_post -d "content=Math Enchanter is a game that tests your ability to do addition math using single and double digit numbers. This game consist of 3 different levels and your end-goal is to become a pure-blood Enchanter.&deploy=http://math-enchanter.surge.sh/index.html&github=https://github.com/tinayang15/Math-Enchanter&image=./static/img/MatchEnchanter.png&name=Math Enchanter&tool=HTML | CSS | JavaScript"

cd /Users/tinayang/MLH/Portfolio/pe-portfolio-site

# Variables = API endpoint URLs
GET_ENDPOINT="http://127.0.0.1:5000/api/timeline_post"
POST_ENDPOINT="http://127.0.0.1:5000/api/timeline_post"
DELETE_ENDPOINT="http://127.0.0.1:5000/api/timeline_post/9"

# Function to create a random timeline post
create_timeline_post() {
    local name="Test Post $RANDOM"
    local tool="Test Tool"
    local content="This is a test post."
    local image="../random/test.jpg"
    local github="https://github.com/test/nowork"
    local deploy="https://test.com/nowork"

    # Send POST request using curl with form-data
curl -X POST -F "name=$name" -F "tool=$tool" -F "content=$content" -F "image=$image" -F "github=$github" -F "deploy=$deploy" $POST_ENDPOINT

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

