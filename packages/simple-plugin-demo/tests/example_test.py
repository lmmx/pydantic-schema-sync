from pytest import importorskip
from inline_snapshot import snapshot


def test_simple(capsys):
    importorskip("examples.simple")
    captured = capsys.readouterr()
    assert captured.out == snapshot(
        """\
content='Hello, World!'
content='Count: 1'
content='Count: 3'
content='Count: 5'
""",
    )
