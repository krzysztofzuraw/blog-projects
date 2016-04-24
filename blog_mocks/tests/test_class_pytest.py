try:
    from mock import MagicMock
except ImportError:
    from unittest.mock import MagicMock

from square import Square


def test_mocking_class_methods(monkeypatch):
    monkeypatch.setattr('test_class_pytest.Square.calculate_area', lambda: 1)
    assert Square.calculate_area() ==  1


def test_mocking_classes(monkeypatch):
    monkeypatch.setattr('test_class_pytest.Square', MagicMock(Square))
    sq = Square
    sq.calculate_area.return_value = 1
    assert sq.calculate_area() ==  1
