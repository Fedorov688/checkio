def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    start_index = text.find(begin)
    end_index = text.find(end)
    if start_index != -1 and end_index != -1 and start_index > end_index:
        result = ""
    else:
        if begin in text:
            result = text.split(begin)
            bgn_index = 1
        else:
            result = [None]
            result[0] = text
            bgn_index = 0
        try:
            if end in result[bgn_index]:
                result = result[bgn_index].split(end)
                result = result[0]
            else:
                result = result[bgn_index]
        except IndexError:
            result = ""
    return result


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    assert between_markers("No <hi> one",">","<") == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
