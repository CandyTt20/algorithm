def find_substring(s, pattern):
    # TODO: Write your code here
    password_map, key_map = {}, {}
    window_length,start,end = len(s)+1,0,0
    
    

    window_start=0
    for key in pattern:
        if key not in password_map:
            password_map[key] = 0
        password_map[key] += 1
    
    for window_end in range(len(s)):
        
        char_end = s[window_end]
        
        if char_end in password_map:
            if char_end not in key_map:
                key_map[char_end] = 0
            key_map[char_end] += 1
        
        while len(key_map) >= len(password_map):
            char_start = s[window_start]
            if window_end - window_start + 1 < window_length:
                window_length, start, end = window_end - window_start + 1, window_start, window_end+1
                
            if char_start in key_map:
                key_map[char_start] -= 1
                if key_map[char_start] == 0:
                    del key_map[char_start]
            window_start += 1
        
    return s[start:end]

String = "adcad"
Pattern="abc"
print(find_substring(String,Pattern))