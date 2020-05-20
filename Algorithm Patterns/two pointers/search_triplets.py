def search_triplets(arr):
    arr.sort()
    triplets=[]
    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i - 1]:
            continue
        else:
            pairs = search_pair(arr, i + 1, -arr[i])
            for item in pairs:
                triplets.append([arr[i],item[0],item[1]])


    return triplets


def search_pair(arr,init,target_num):
    pairs = []
    left, right = init, len(arr) - 1
    while left<right:
        if arr[left] + arr[right] > target_num:
            right -= 1
        elif arr[left] + arr[right] < target_num:
            left += 1
        else:
            pairs.append([arr[left], arr[right]])
            left += 1
            right -= 1
    return pairs



arr = [-3, 0, 1, 2, -1, 1, -2]
print(search_triplets(arr))