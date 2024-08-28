from pytest import importorskip
from inline_snapshot import snapshot


def test_simple(capsys):
    importorskip("examples.simple")
    captured = capsys.readouterr()
    assert captured.out == snapshot(
        """\
text='Hello, World!'
text='Count: 1'
text='Count: 3'
text='Count: 5'
"""
    )
