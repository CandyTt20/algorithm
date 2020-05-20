def make_squares(arr):
    squares = []
    # TODO: Write your code here
    left, right = 0, len(arr) - 1
    while left <= right:

        if arr[left]*arr[left] > arr[right]*arr[right]:
            squares.append(arr[left] ** 2)
            left += 1

        else:
            squares.append(arr[right] ** 2)
            right -= 1
    squares.reverse()
    return squares


arr = [-3, -1, 0, 1, 2]
print(make_squares(arr))
