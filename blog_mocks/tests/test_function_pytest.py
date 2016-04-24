from function import square, main


def test_function(monkeypatch):
    monkeypatch.setattr("test_function_pytest.square", lambda x: 1)
    assert square(5) == 1
 
def test_main_function(monkeypatch):
    monkeypatch.setattr('function.square', lambda x: 1)
    monkeypatch.setattr('function.cube', lambda x: 0)
    assert main(5) == 1

