def sentence_reversal(s):

    words_list = []
    spaces = [' ']
    length = len(s)

    i = 0

    while i < length:

        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1

            words_list.append(s[word_start:i])

        i += 1

    return ' '.join(reversed(words_list))


print(sentence_reversal('My name is Vaibhav'))
