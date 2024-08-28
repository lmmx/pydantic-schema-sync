from pytest import importorskip


def test_simple(capsys):
    importorskip("examples.simple")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\nCount: 1\nCount: 3\nCount: 5\n"
