def reverse(word):
    result = ""
    for i in word:
        result = i + result
    print(result)
    return result

def backward_string_by_word(text: str) -> str:
    # your code here
    tmp_word = ""
    result = ""
    for i in text:
        if i not in [" ", ",", "."]:
            tmp_word += i
        else:
            if tmp_word != "":
                result += reverse(tmp_word)
                tmp_word = ""
            result += i
    if tmp_word != "":
        result += reverse(tmp_word)
        tmp_word = ""
    return result


if __name__ == '__main__':
    print("Example:")
    # print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
