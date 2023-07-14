#!/bin/zsh

tmux kill-session -a

cd /Users/tinayang/MLH/Portfolio/pe-portfolio-site

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s flask-server
tmux send-keys "source python3-virtualenv/bin/activate" C-m
tmux send-keys "flask run --host=0.0.0.0" C-m