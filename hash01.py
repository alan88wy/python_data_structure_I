hash_size = 10
hash_table = [[], [], [], [], [], [], [], [], [], []]

"""
The ord() function in Python is a built-in function that takes a single Unicode 
character as input and returns its corresponding integer Unicode code point value. 
It is the inverse of the chr() function, which converts an integer Unicode code 
point back to its character representation. 

Functionality:
**************
1. Input: The ord() function requires a single-character string as its argument. 
2. Output: It returns an integer representing the Unicode code point of that character. 
3. Error Handling: If the input string contains more than one character, a TypeError will 
   be raised.
   
Example:
*********
# Get the Unicode code point of 'A'
print(ord('A'))  # Output: 65

# Get the Unicode code point of 'z'
print(ord('z'))  # Output: 122

"""
def hash_function(str):
    hash = 0
    for char in str:
        hash += ord(char)
        
    return hash % hash_size

def display_hash_table():
    for index, value in enumerate(hash_table):
        print(f"Index {index}: {value}")
        
def key_exist(key):
    idx = hash_function(key)

    return "Key exists" if key in hash_table[idx] else "Key does not exist"

        
def add(value):
    idx = hash_function(value)
    hash_table[idx].append(value)

def main():
    add("apple")
    add("banana")
    add("cherry")
    add("date")
    add("elderberry")
    add("fig")
    add("grape")
    add("honeydew")
    add("kiwi")
    add("lemon")
    add("mango")
    add("nectarine")
    add("orange")
    display_hash_table()
    
    # Check if key exists
    if key_exist("apple"):
        print("Key apple exists")
    else:
        print("Key apple does not exist")
    
if __name__ == "__main__":
    main()
    