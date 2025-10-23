def lengthOfLongestSubstring(s: str) -> int:
    seen = set()          # store characters in current window
    left = 0              # left boundary of window
    max_len = 0

    for right in range(len(s)):
        # print("right -> ", s[right], " left -> ", left, " right -> ", right, "seen -> ", seen)
        while s[right] in seen:
            # print("to remove -> ", s[left] )
            seen.remove(s[left])
            left += 1
            #print("after remove seen -> ", seen, " left -> ", left, " right -> ", right)
        
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
        # print("seen -> ", seen, " left -> ", left, " right -> ", right, " max_len -> ", max_len)


    return max_len


# Example usage
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3 ("wke")
print(lengthOfLongestSubstring(""))          # Output: 0


'''
Given a string s, find the length of the longest substring without duplicate characters.

Explanation
***********

We use a sliding window defined by indices left and right.

The set seen keeps track of unique characters in the current window.

When we hit a duplicate (s[right] already in seen), we move left forward until the duplicate is removed.

For each iteration, we update max_len with the current window size.

⏱️ Time Complexity
*******************

O(n) — each character is added and removed from the set at most once.

O(min(n, charset)) space — since we store only unique characters in the window.
'''