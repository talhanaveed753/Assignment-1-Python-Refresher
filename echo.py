# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""

    # Initiate required Variable
    echoText = []
    echoStr = ""
    i = repetitions
    j = 0

    # Use a loop to grab the elements being echoed and concatenate them into a single str
    while i > 0:
        echoText.append(text[-i:])
        echoStr = echoStr + echoText[j] + "\n"
        i = i - 1
        j = j + 1

    # Return the final str and required elements
    return echoStr + "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
