"""
# No Duplicates

Input: a string of words separated by spaces. Only the letters `a`-`z`
are utilized.

Output: the string in the same order, but with subsequent duplicate
words removed.

There must be no extra spaces at the end of your returned string.

The solution must be `O(n)`.
"""

def no_dups(s):
    # Your code here
    #? dictionary
    cache = {}

    if s == "":
        return ""

    str_arr = s.split()
    #? create new arr / str
    new_arr = []
    #? print (1, str_arr)
    for word in str_arr:
        if word not in cache:
            cache[word] = word
            new_arr.append(word)
    return " ".join(new_arr)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))