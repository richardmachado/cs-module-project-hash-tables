"""
# Count the words in an input string

## Input

This function takes a single string as an argument.

```
Hello, my cat. And my cat doesn't say "hello" back.
```

## Output

It returns a dictionary of words and their counts:

```
{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
```

Case should be ignored. Output keys must be lowercase.

Key order in the dictionary doesn't matter.

Split the strings into words on any whitespace.

Ignore each of the following characters:

```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

If the input contains no ignored characters, return an empty dictionary.

"""

def word_count(s):
    # Your code here
    tally = {}
    regex = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    new_str_arr = []

    for c in s:
        #! this filters special characters
        if c in regex:
            c == ""
        else:
            new_str_arr.append(c)

    #! this sets other characters to lowercase
    new_str = "".join(new_str_arr).lower()

    #! split the string into an array
    for word in new_str.split():
        #? if key exists
        if word in tally:
            tally[word.lower()] += 1
        #? else create the key and assign one count
        else:
            tally[word.lower()] = 1
    return tally


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))