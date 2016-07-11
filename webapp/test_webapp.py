import tempfile
import unittest
from unittest import mock

import os

from webapp import app, get_db


class TestWebapp(unittest.TestCase):
    def setUp(self):
        super(TestWebapp, self).setUp()

        self.p = mock.patch("webapp.ads")
        self.p.return_value = []
        self.p.start()

        self.test_fd, app.config["DB"] = tempfile.mkstemp()
        with app.app_context():
            get_db().executescript("create table user(id integer primary key autoincrement, name varchar)")
            get_db().executescript("insert into user (name) values ('ura'), ('masha')")


    def tearDown(self):
        super(TestWebapp, self).tearDown()
        self.p.stop()

        os.close(self.test_fd)
        os.unlink(app.config["DB"])

    def test_ok(self):
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)

    def test_inner(self):
        raise Exception("test error")
        with app.test_client() as client:
            resp = client.get("/")
            self.assertIn(b"masha", resp.data)
