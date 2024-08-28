import json
import subprocess
import sys

command = [
    "model-schema-sync",
    "--model",
    "pydantic_schema_sync.cli.SyncCLI",
    "--schema_path",
    "schema.json",
    "--mjs_kwargs",
    json.dumps({"by_alias": False}),
]

result = subprocess.run(command, capture_output=True, text=True)

print("Command Output:")
print(result.stdout)
print("Command Error (if any):")
print(result.stderr)

if result.returncode != 0:
    print("CLI command failed.")
    sys.exit(result.returncode)
else:
    print("CLI command ran successfully.")
