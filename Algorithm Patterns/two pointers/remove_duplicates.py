def remove_duplicates(arr):
    # index of the next non-duplicate element
    pos, i = 1, 1
    
    while i<len(arr):
        if arr[i] != arr[pos - 1]:
            arr[pos] = arr[i]
            pos += 1
        i += 1
    return pos
        
            
        
print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))