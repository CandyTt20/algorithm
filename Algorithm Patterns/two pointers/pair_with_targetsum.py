def pair_with_targetsum(arr, target_sum):
    # TODO: Write your code here
    head, tail = 0, len(arr) - 1
    result = []
    while head < tail:
        if arr[head] + arr[tail] > target_sum:
            tail -= 1
        elif arr[head] + arr[tail] < target_sum:
            head += 1
        else:
            result.append(head)
            result.append(tail)
            break

    return result


arr = [2, 5, 9, 11]
target = 11
print(pair_with_targetsum(arr, target))
