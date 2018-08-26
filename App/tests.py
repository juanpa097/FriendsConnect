from django.test import TestCase


class DummyTest(TestCase):

    def test_travis(self):
        self.assertEqual('Hello', 'Hello')
