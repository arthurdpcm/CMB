

def longestCommonSubsequence(t,s):
  if t == "" or s == "":
    return ""
  elif t[0] == s[0]:
    return t[0] + longestCommonSubsequence(t[1:], s[1:])
  else:
    return max(longestCommonSubsequence(t[1:], s), longestCommonSubsequence(t, s[1:]), key=len)
  
print(longestCommonSubsequence("PORTA", "PORTEIRO"))


