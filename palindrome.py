def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward (ignoring spaces, punctuation,
    and capitalization in typical use cases).
    
    Args:
        s (str): The string to check for palindrome property.
    
    Returns:
        bool: True if the string is a palindrome (reads the same forwards and 
              backwards), False otherwise.
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("a")
        True
        >>> is_palindrome("")
        True
    
    Note:
        This function performs a case-sensitive comparison. For case-insensitive
        palindrome checking, convert the string to lowercase first.
        This implementation does not ignore spaces or special characters.
    """
    reversed_s = s[::-1]
    return s == reversed_s

if is_palindrome("racecar"):  # Output: True
    print("Yes")
else:
    print("No")
    
if is_palindrome("radar"):  # Output: True
    print("Yes")
else:
    print("No")