class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        for i in range(len(s)):
            if i < len(s)-1:
                if roman_dict[s[i+1]] <= roman_dict[s[i]]:
                    result += roman_dict[s[i]]
                else:
                    result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        
        return result