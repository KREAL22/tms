'''
Ex1
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between numbers x and y (both included). Return list of this numbers.
Use list comprehension.
'''

def divisor(x: int, y: int):
    nlst = []
    for i in range(x, y):
        if (i % 7 == 0) and (i % 5 != 0) :
            nlst.append(i)
    return nlst
    
    
assert divisor(0, 36) == [7, 14, 21, 28]
assert divisor(9, 13) == []
assert divisor(-100, 100) == [-98, -91, -84, -77, -63, -56, -49, -42, -28, -21, -14, -7, 7, 14, 21, 28, 42, 49, 56, 63, 77, 84, 91, 98]


'''
Ex2
With a given number n, write a program to generate a dictionary that contains (i, i*i) such that is number 
between 1 and n (both included). The program returns the dictionary. Use dict comprehension.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''


def dict_gen(n: int):
    d = {n: n * n for n in range(n + 1)}
    d.pop(0)
    return d
    
   
assert dict_gen(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


'''
Ex3
Return a list of integers from 0 to n with step m. Use list comprehension.
'''

def list_gen(n, m):
    a = [i for i in range(0,n,m)]
    return a
    
    
assert list_gen(10, 2) == [0, 2, 4, 6, 8]
assert list_gen(-25, -2) == [0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24]
assert list_gen(1, 3) == [0]
assert list_gen(1, -1) == []


'''
Ex4
Suppose you have a dictionary where the keys are integers, return a list of values where the key is an odd number.
'''

def odd_keys(dict_):
    nlst = []
    for k, v in dict_.items():
        if k % 2 != 0:
            nlst.append(v)
    return nlst
    
    
assert odd_keys({1: 'One', 2: 'Two', 4: 'Four', 7: 'Seven'}) == ['One', 'Seven']
assert odd_keys({12: [1, 2, 3], 2: 'str', 9: ['Hello', 'name', '?']}) == [['Hello', 'name', '?']]
assert odd_keys({}) == []
assert odd_keys({34: 234, 78: 99}) == []


'''
Ex5
Given a phrase, count the occurrences of each word in that phrase and return result as a dictionary where key is a word 
and value is a count the occurrences.
For example for the input "olly olly in come free"
olly: 2
in: 1
come: 1
free: 1
'''


def words_counter(line):
    counts = dict()
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    
    
assert words_counter("olly olly in come free") == {"olly": 2, "in": 1, "come": 1, "free": 1}
assert words_counter("") == {}


'''
Ex6
Convert a phrase to its acronym.
Techies love their TLA (Three Letter Acronyms)!
Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).
'''

def acronym(phrase):
    arc = []
    ph = phrase.split(' ')
    for i in ph:
        arc.append(i[0])
    newarc = ''.join(arc)        
    return newarc

    
    
assert acronym("World Wide Web") == "WWW"
assert acronym("Portable Network Graphics") == "PNG"

