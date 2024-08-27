import json
import subprocess
import sys

# Define the parameters you want to use
model = "pydantic_schema_sync.cli.SyncCLI"
schema_path = "schema.json"
mjs_kwargs = {"by_alias": False}

# Construct the CLI command as a list
command = [
    "model-schema-sync",
    "--model",
    model,
    "--schema_path",
    schema_path,
    "--mjs_kwargs",
    json.dumps(mjs_kwargs),
]

# Run the command using subprocess.run
result = subprocess.run(command, capture_output=True, text=True)

# Output the result
print("Command Output:")
print(result.stdout)
print("Command Error (if any):")
print(result.stderr)

if result.returncode != 0:
    print("CLI command failed.")
    sys.exit(result.returncode)
else:
    print("CLI command ran successfully.")
