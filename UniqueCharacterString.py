def unique_char(s):

    duplicate = []
    for char in s:
        if char not in duplicate:
            duplicate.append(char)
        else:
            return False

    return True


print(unique_char('abcdd'))
