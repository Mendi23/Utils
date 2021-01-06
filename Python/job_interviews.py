def reverse_integer(i):
    """
    Given an integer, return the integer with reversed digits.
    Note: The integer could be either positive or negative.
    """
    return str(i)[::-1] if i >= 0 else '-'+str(-1*i)[::-1]

def average_words_length(s):
    """
    For a given sentence, return the average word length. 
    Note: Remember to remove punctuation first.
    """
    seq = s.split()
    return sum(len(list(filter(str.isalpha, w))) for w in seq)/len(seq)

def add_strings(s1, s2):
    """
    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

    Notes:
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    """

    from itertools import zip_longest
    
    conv_int = lambda e: ord(e)-ord('0')
    final, carry = [], 0
    
    for i, j in zip_longest(s1[::-1], s2[::-1], fillvalue='0'):
        carry, res = divmod(conv_int(i)+conv_int(j)+carry, 10)
        final.append(str(res))
    
    if carry > 0:
        final.append(str(carry))

    return ''.join(reversed(final))

def first_unique_character(s):
    """
    Given a string, find the first non-repeating character in it and return its index. 
    If it doesn't exist, return -1.
    Note: all the input strings are already lowercase.
    """
    from collections import OrderedDict
    res = OrderedDict()
    for i,letter in enumerate(s):
        if letter in res:
            res[letter][1] += 1
        else:
            res[letter] = [i,1]

    return next((v[0] for v in res.values() if v[1]==1), -1)

def valid_palindrome(s):
    """
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
    The string will only contain lowercase characters a-z.
    """
    
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True
    return s == s[::-1]

