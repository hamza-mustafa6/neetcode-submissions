class Solution:
    def minWindow(self, s: str, t: str) -> str:
        valid = ""
        if len(s) < len(t):
            return valid
        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c,0) + 1

        s_map = {c: 0 for c in t_map}

        left = right = 0

        need = len(t_map)
        want = 0

        valid = ""

        while right < len(s) or want == need:
            if want != need:
                #keep moving right and adding characters to map
                #with each character thats in t_map, stop and increment want
                char = s[right]
                if char in t_map:
                    s_map[char]+=1
                    #if they're equal, we have finally satisfied another character 
                    if s_map[char] == t_map[char]:
                        want+=1
                right+=1 
            else:
                #we are valid and wanna keep moving left to find shorter valid
                #if shorter valid, edit valid, if not, keep moving
                #if invalid, edit want

                #edit valid (or not)
                if len(s[left:right]) < len(valid) or not valid:
                    valid = s[left:right]
                    
                left+=1
                #move your left then edit map and want
                char = s[left-1]
                if char in t_map:
                    s_map[char]-=1
                    if s_map[char] < t_map[char]:
                        want-=1
                
        return valid 
                    
