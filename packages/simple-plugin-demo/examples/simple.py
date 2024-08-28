from simple_plugin_demo import process_input
from simple_plugin_demo.data_model import In

input_data = In(greeting="Hello, World!", count=5, skip=[2, 4])
output = process_input(input_data)

for message in output.messages:
    print(message)
