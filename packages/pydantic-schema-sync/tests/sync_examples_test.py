from pathlib import Path

from pydantic import FilePath, validate_call
from pytest import fixture, importorskip, mark


@validate_call
def remove_if_exists(file_paths: list[Path]) -> None:
    for path in file_paths:
        path.unlink(missing_ok=True)


@validate_call
def assert_files_exist(file_paths: list[FilePath]) -> None:
    return


@fixture(autouse=True)
def cleanup(request):
    """Pre- and post-test cleanup of the files to be checked."""
    artifacts = request.node.callspec.params["files_to_check"]
    remove_if_exists(artifacts)
    yield
    remove_if_exists(artifacts)


@mark.parametrize(
    "module_to_import, files_to_check",
    [
        ("examples.sync_model", ["FooModel_1.json", "FooModel_2.json"]),
        ("examples.sync_model_from_path", ["schema.json"]),
        ("examples.sync_model_cli", ["schema.json"]),
    ],
)
def test_sync(module_to_import, files_to_check):
    importorskip(module_to_import)
    assert_files_exist(files_to_check)
