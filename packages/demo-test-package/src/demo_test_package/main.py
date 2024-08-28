from .data_model import InputModel, OutputModel

__all__ = ("process_input",)


def process_input(input_data: InputModel) -> OutputModel:
    messages = [input_data.greeting]
    for i in range(1, input_data.count + 1):
        if i not in input_data.skip:
            messages.append(f"Count: {i}")
    return OutputModel(messages=messages)


def main():
    # Example usage
    input_data = InputModel(greeting="Hello, World!", count=5, skip=[2, 4])
    output = process_input(input_data)

    for message in output.messages:
        print(message)


if __name__ == "__main__":
    main()
