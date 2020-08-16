def anagram(string_one, string_two):
    string_one = string_one.replace(' ', '').lower()
    string_two = string_two.replace(' ', '').lower()

    count = {}

    for letter in string_one:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    print(count)

    for letter in string_two:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagram('dog', 'god'))
