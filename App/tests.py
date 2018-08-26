from django.test import TestCase


class DummyTest(TestCase):

    #   This is a dummy test to test Travis
    def test_travis(self):
        self.assertEqual('Hello', 'Hello')
