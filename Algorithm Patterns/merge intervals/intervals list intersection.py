def merge(intervals_a, intervals_b):
    
    hash_map = find_hash_map(intervals_a, intervals_b)
    
    return merge_hash_map(hash_map,intervals_a,intervals_b)


def find_hash_map(intervals_a, intervals_b):
    i = 0
    hash_map={}
    for k in range(len(intervals_b)):
        while i < len(intervals_a) and (intervals_a[i][0] > intervals_b[k][1] or intervals_a[i][1] < intervals_b[k][0]):
            i += 1
        left = i
        while i < len(intervals_a) and (intervals_a[i][0] <= intervals_b[k][1] and intervals_a[i][1] >= intervals_b[k][0]):
            i += 1
        right = i - 1
        if left <= right:
            hash_map[k] = (left, right)
            i = right
        else:
            i = 0
    return hash_map

def merge_hash_map(hash_map, intervals_a, intervals_b):
    result = []
    for k in hash_map:
        
        left,right = hash_map[k][0],hash_map[k][1]
        for i in range(left, right + 1):
            start, end = intervals_b[k][0], intervals_b[k][1]
            start = max(start, intervals_a[i][0])
            end = min(end, intervals_a[i][1])
            result.append([start, end])
            
    return result



def main():
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    print("Intervals Intersection: " + str(merge(A,B)))
    # print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))

main()
# print(find_hash_map([[1, 3], [5, 6], [7, 9]], [[-1, 0], [5, 7]]))