import collections


def find_element(arr_one, arr_two):

    d = collections.defaultdict(int)

    for num in arr_two:
        d[num] += 1

    for num in arr_one:
        if(d[num] == 0):
            return num


print(find_element([1, 2, 3, 4], [1, 2, 3]))
