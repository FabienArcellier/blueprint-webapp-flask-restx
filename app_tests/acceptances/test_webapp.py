# coding=utf-8

import unittest
import app.webapp

class WebappTest(unittest.TestCase):
    def setUp(self):
        self.client = app.webapp.app.test_client()

    def test_root_should_display_hello_world(self):
        # Assign
        # Acts
        rv = self.client.get('/hello')

        # Assert
        self.assertEqual({'hello': 'fabien'}, rv.json)
