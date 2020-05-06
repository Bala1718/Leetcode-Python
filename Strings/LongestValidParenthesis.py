def longestValidParentheses(self, s):
    if not s: 
        return 0
    #position represents the starting point of LVP ending at i
    # set the position[i] = i+1 to avoid the corner case
    position, result = range(1, len(s)+1), 0
    
    for i in range(1, len(s)):
        j = position[i-1] - 1
        if s[i] == ")" and j >= 0 and s[j] == "(":
            position[i] = j if position[j-1] > j-1 else position[j-1]
            result = max(result, i - position[i] + 1)
    return result
