def check_balance(s):

    opening = set('([{')

    matches = set([('(',')'), ('[',']'), ('{','}')])

    stack = []

    if len(s) % 2 != 0:
        return False

    for paren in s:

        if paren in opening:
            stack.append(paren)

        else:

            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if(last_open, paren) not in matches:
                return False
            else:
                return True

    return len(stack) == 0


print(check_balance('[]'))
