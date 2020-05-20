def find_permutation(tag, pattern):
    password_map = {}
    for key in pattern:
        if key not in password_map:
            password_map[key] = 0
        password_map[key]+=1
   
    window_start, flag = 0, -1
    
    for window_end in range(len(tag)):
        char_end = tag[window_end]
        char_start = tag[window_start]
        
        if char_end not in password_map:
            password_map[char_end] = 0
        password_map[char_end] += flag
        
        if window_end - window_start + 1 > len(pattern):
            password_map[char_start] -= flag
            
            window_start += 1
        if password_map == dict(zip([i for i in set(pattern)],[0 for i in set(pattern)])):
            return True
    return False

String = "aaacb"
Pattern="abc"
print(find_permutation(String,Pattern))