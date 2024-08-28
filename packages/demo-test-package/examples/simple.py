from demo_test_package import process_input
from demo_test_package.data_model import InputModel

input_data = InputModel(greeting="Hello, World!", count=5, skip=[2, 4])
output = process_input(input_data)

for message in output.messages:
    print(message)
