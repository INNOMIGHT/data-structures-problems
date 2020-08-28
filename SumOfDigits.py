def sum_of_digits(n):
    if len(str(n)) == 1:
        return n

    else:
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(123))
