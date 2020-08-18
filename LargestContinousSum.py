def largest_continous_sum(arr):

    if(len(arr) == 0):
        return 0

    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, current_sum)

        max_sum = max(current_sum, max_sum)

    return max_sum


print(largest_continous_sum([1, 2, 3, -2, -4]))
