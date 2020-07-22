def popular_words(text: str, words: list) -> dict:
    # your code here
    result = {}
    for w in range(len(words)):
        result[words[w]] = 0
    text = text.lower().split()
    for word in text:
        if word in words:
            result[word] = result.get(word) + 1

    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
