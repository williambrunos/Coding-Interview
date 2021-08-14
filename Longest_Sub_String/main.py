'''
LEET CODE

Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) != 0:
            lst = []
            major = 0
            count = 0
            for i in range(len(s)):
              lst_char = []
              hashMap = {}
              hashMap[s[i]] = i
              lst_char.append(s[i])
              for j in range(i+1, len(s)):
                if s[j] in hashMap:
                  break
                else:
                  hashMap[s[j]] = j
                  lst_char.append(s[j])
              lst.append(''.join(lst_char))
              major = max(major, len(lst[count]))
              count += 1
            
            return major
        else:
            return 0