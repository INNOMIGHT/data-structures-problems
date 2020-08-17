def array_pair_sum(arr, sum):
    seen = set()
    output = set()

    for num in arr:

        target = sum - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print('/n'.join(map(str, list(output))))


array_pair_sum([1, 2, 3], 4)
