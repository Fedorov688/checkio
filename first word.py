def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    result = text.split()
    if result[0][0] not in [",", ".", "!", "?"]:
        if "." in result[0]:
            result = result[0].split(".")
    elif "." in result[0]:
        result = result[1].split(".")
    if "," in result[0]:
        res = ""
        for i in result[0]:
            if i not in ",":
                res += i
        result[0] = res
    print(result[0])
    return result[0]


if __name__ == '__main__':
    # print("Example:")
    # print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("... and so on ...") == "and"
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
