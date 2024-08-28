# demo-test-package

Simple program to demonstrate the use of `pytest-pydantic-schema-sync` pytest plugin:

- Prints a `greeting` then counts up to the given number `count` and skips any of the numbers in `skip`.
- Input is specified as a Pydantic model `InputModel`
- Output is simply a list of `messages` as specified by the Pydantic model `OutputModel`

These two models' schemas are synced as JSON files under the `schemas` directory
