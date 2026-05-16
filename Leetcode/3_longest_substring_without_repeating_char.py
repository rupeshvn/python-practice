"""
Given a string s, find the length of the longest without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""
# s = "abcabcbb"
def return_final_substr(s):
    final_substr = ""
    new_substr = ""
    final_len = 0
    search_dict = {}
    for i in range(len(s)):
        val=search_dict.get(s[i],-1)
        if val==-1:
            new_substr = new_substr+s[i]
            search_dict[s[i]]=i
        else:
            if len(new_substr)>len(final_substr):
                final_substr = new_substr[:]
                new_substr = new_substr[val+1:]
                search_dict.popitem()
                search_dict[s[i]]=1

    return final_substr

val = return_final_substr("pwwkew")
print(val)
        


