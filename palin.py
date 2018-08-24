def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def palindrome(word):
    if first(word) == last(word):
        if len(middle(word)) > 1:
            print first(word),middle(word),last(word)
            return palindrome(middle(word))
        else:
            print first(word),middle(word),last(word)
            return True
    else:
        print first(word),middle(word),last(word)
        return False

def is_palindrome(word):
    if len(word) <= 1:
        print first(word),middle(word),last(word)
        return True
    if first(word) != last(word):
        print first(word),middle(word),last(word)
        return False
    print first(word),middle(word),last(word)
    return is_palindrome(middle(word))

print palindrome('allen')
print palindrome('bob')
print palindrome('otto')
print palindrome('redivider')
