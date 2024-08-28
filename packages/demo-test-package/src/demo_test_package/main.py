from .data_model import In, Out

__all__ = ("process_input",)


def process_input(input_data: In) -> Out:
    messages = [{"text": input_data.greeting}]
    for i in range(1, input_data.count + 1):
        if i not in input_data.skip:
            messages.append({"text": f"Count: {i}"})
    return Out(messages=messages)


def main():
    # Example usage
    input_data = In(greeting="Hello, World!", count=5, skip=[2, 4])
    output = process_input(input_data)

    for message in output.messages:
        print(message.text)


if __name__ == "__main__":
    main()
