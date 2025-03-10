class HelloWorld:
    def __init__(self, message="World") -> None:
        self.message = message

    def hello(self) -> str:
        hello_message = f"Hello {self.message}"
        print(hello_message)

        return hello_message
