import unittest


class TestUnit1(unittest.TestCase):

    def test_1(self):
        assert 1 == 1, 'test error'
        assert 2 == 2, 'test 2 error'

    def test_2(self):
        assert 4 == 4, 'test error'
        assert 5 == 5, 'test 2 error'
