# test_db.py

import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not stricktly necessary since SQLite in-memory databases only live for the duration of the connection, and in the next step we close the connection... but a good practice all the same.
        test_db.drop_tables(MODELS)
        # close connection to db.
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts
        first_post = TimelinePost.create(
            name='John Doe', email='john@example.com', content='Hello World, I\'m John!', image='test')
        assert first_post.id == 1
        second_post = TimelinePost.create(
            name='Jane Doe', email='jane@example.com', content='Hello World, I\'m Jane!',image='test')
        assert second_post.id == 2
        # TODO: Get timeline posts and assert that they are correct
        all_posts = TimelinePost.select()

        self.assertEqual(all_posts.count(), 2)

        retrieved_first_post = all_posts[0]
        self.assertEqual(retrieved_first_post.name, 'John Doe')
        self.assertEqual(retrieved_first_post.email, 'john@example.com')
        self.assertEqual(retrieved_first_post.content, 'Hello World, I\'m John!')
        self.assertEqual(retrieved_first_post.image, 'test')

        retrieved_first_post = all_posts[1]
        self.assertEqual(retrieved_first_post.name, 'Jane Doe')
        self.assertEqual(retrieved_first_post.email, 'jane@example.com')
        self.assertEqual(retrieved_first_post.content, 'Hello World, I\'m Jane!')
        self.assertEqual(retrieved_first_post.image, 'test')

if __name__== '__main__':
    unittest.main()