#echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoText = text
    int = repetitions
    while int > 0:
        echoText = text[-int:]
        print(echoText)
        int = int - 1
    return print(".")



if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))