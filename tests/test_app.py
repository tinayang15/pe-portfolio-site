# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Tina Yang</title>" in html
        # TODO Add more tests relating to the home page
        assert "Hello, I'm Tina Yang!" in html
        assert "Product Engineer" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        #TODO add more tests relating to the /api/timeline_post GET and POST apis

        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello World, I\'m John",
            "image": "test"
        }

        response = self.client.post("/api/timeline_post", data=data)
        assert response.status_code == 302

        new_post = TimelinePost.get_or_none(name=data["name"], email=data["email"])
        assert new_post is not None
        assert new_post.content == data ["content"]
        assert new_post.image == data["image"]
        #TODO add more tests relating to the timeline page
    def test_timeline_page_rendering(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h1>My Timeline</h1>" in html
        assert "Create Post" in html

    def test_malformed_timeline_post(self):
        #POST request missing name
        response = self.client.post('/api/timeline_post', data={"name":"", "email": "john@example.com", "content": "Hello World, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        #POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        #POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name":"John Doe", "email": "not-an-email", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html