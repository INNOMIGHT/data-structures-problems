def compress(s):

    length = len(s)
    i = 1
    r = ''
    count = 1
    while i < length:

        if s[i] == s[i-1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
            count = 1

        i += 1

    r = r + s[i-1] + str(count)

    return r


print(compress('AAAAADDDDDDDD'))
