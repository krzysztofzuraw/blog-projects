try:
    import mock
except ImportError:
    from unittest import mock

import unittest

from square import Square


class TestClass(unittest.TestCase):

    @mock.patch('test_class.Square') # depends in witch from is run
    def test_mocking_instance(self, mocked_instance):
        mocked_instance = mocked_instance.return_value
        mocked_instance.calculate_area.return_value = 1
        sq = Square(100)
        self.assertEquals(sq.calculate_area(), 1)


    def test_mocking_classes(self):
        sq = Square
        sq.calculate_area = mock.MagicMock(return_value=1)
        self.assertEquals(sq.calculate_area(), 1)

    @mock.patch.object(Square, 'calculate_area')
    def test_mocking_class_methods(self, mocked_method):
        mocked_method.return_value = 20
        self.assertEquals(Square.calculate_area(), 20)

if __name__ == '__main__':
    unittest.main()
