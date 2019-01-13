'''
Ex1
The first input array contains the correct answers to an exam, like ["a", "a", "b", "d"]. The second one is "answers" array and contains student's answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty 
string).

If the score < 0, return 0.

For example:

checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
'''


def check_exam(arr1,arr2):
    points = 0
    for i in range(4):
        if arr1[i] == arr2[i]:
            points += 4
        elif arr1[i] == "" or arr2[i] == "":
            points += 0         
        elif arr1[i] != arr2[i]:
            points -= 1
    return points if points >= 0 else 0


assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) == 6
assert check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) == 7
assert check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) == 16
assert check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) == 0


'''
Ex2
You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:
get_middle("test") should return "es"
get_middle("testing") should return "t"
get_middle("middle") should return "dd"

#Input
A word (string) of length 0 < str < 1000.

#Output
The middle character(s) of the word represented as a string.
'''


def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
    
    
assert get_middle("test") == "es"
assert get_middle("testing") == "t"
assert get_middle("middle") == "dd"
assert get_middle("A") == "A"
assert get_middle("of") == "of"


'''
Ex3
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''


def high_and_low(numbers):
    nums = [int(x) for x in numbers.split()]
    high = str(max(nums))
    low = str(min(nums))
    return str(high + " " + low)
    
    
assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
assert high_and_low("1 2 -3 4 5") == "5 -3"


'''
Ex4
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. 
When writing on Twitter, he is known for almost always capitalizing every word.

Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not 
capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
'''


def toJadenCase(string):
    # Your code here
    return
    

assert toJadenCase(quote) == "How Can Mirrors Be Real If Our Eyes Aren't Real"


'''
Ex5
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.

The binary number returned should be a string
'''


def add_binary(a,b):
    return bin(a+b)[2:]
    
    
assert add_binary(1,1) == "10"
assert add_binary(0,1) == "1"
assert add_binary(1,0) == "1"
assert add_binary(2,2) == "100"
assert add_binary(51,12) == "111111"


'''
Ex6*
Complete the function that counts the number of unique consonants in a string (made up of printable ascii characters).

Consonants are letters used in English other than "a", "e", "i", "o", "u". We will count "y" as a consonant.

Remember, your function needs to return the number of unique consonants - disregarding duplicates. 
For example, if the string passed into the function reads "add", 
the function should return 1 rather than 2, since "d" is a duplicate.

Similarly, the function should also disregard duplicate consonants of differing cases. 
For example, "Dad" passed into the function should return 1 as "d" and "D" are duplicates.

Examples

"add" ==> 1
"Dad" ==> 1
"aeiou" ==> 0
"sillystring" ==> 7
'''


def count_consonants(text):
    cons = 0
    for i in set(text.lower()):
        if i not in "aeiou" and i.isalpha():
            cons += 1
    return cons
    
assert count_consonants('sillystring') == 7
assert count_consonants('aeiou') == 0
assert count_consonants('abcdefghijklmnopqrstuvwxyz') == 21
assert count_consonants('Count my unique consonants!!') == 7


'''
Ex7
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.
'''


def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result
    
    
tests = [
    # [expected, input]
    ["01011110001100111", "45385593107843568"],
    ["101000111101101", "509321967506747"],
    ["011011110000101010000011011", "366058562030849490134388085"],
    ["01111100", "15889923"],
    ["100111001111", "800857237867"],
]

for exp, inp in tests:
    assert fake_bin(inp) == exp


'''
Ex8
In your class, you have started lessons about arithmetic progression. 
Since you are also a programmer, you have decided to write a function 
that will return the first n elements of the sequence with the given 
common difference d and first element a. Note that the difference may be zero!

The result should be a string of numbers, separated by comma and space.

Example

# first element: 1, difference: 2, how many: 5
arithmetic_sequence_elements(1, 2, 5) == "1, 3, 5, 7, 9"
'''


def arithmetic_sequence_elements(a, r, n):
    z = str(a)
    for i in range(n - 1):
        a = a + r
        z = z + ", " + str(a)
    return z
    
    
assert arithmetic_sequence_elements(1, 2, 5) == '1, 3, 5, 7, 9'
assert arithmetic_sequence_elements(1, 0, 5) == '1, 1, 1, 1, 1'
assert arithmetic_sequence_elements(1, -3, 10) == '1, -2, -5, -8, -11, -14, -17, -20, -23, -26'


'''
Ex9
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
'''


def solution(number):
    result = 0
    for i in range(number):
        if i % 5 == 0 or i % 3 == 0:
            result += i
    return result


    
assert solution(10) == 23


'''
Ex10
My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

In honor of my grandfather's memory we will write a function using his formula!

Take a list of ages when each of your great-grandparent died.
Multiply each number by itself.
Add them all together.
Take the square root of the result.
Divide by two.
Example

predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
Note: the result should be rounded down to the nearest integer.
'''


def predict_age(*age):
    return sum(a*a for a in age)**0.5//2

    
assert predict_age(65,60,75,55,60,63,64,45) == 86


'''
Ex11
Complete the function so that it takes an array of keys and a default value and returns a dictionary 
with all keys set to the default value.

Example

["draft", "completed"], 0   # should return {"draft": 0, "completed: 0}
'''


def populate_dict(keys, default):
    d = {}
    for i in keys:
        d[i] = default
    return d
    
    
assert populate_dict(["draft", "completed"], 0) == {"completed": 0, "draft": 0}
assert populate_dict(["a", "b", "c"], None) == {"c": None, "b": None, "a": None}
assert populate_dict([1, 2, 3, 4], "OK") == {1: "OK", 2: "OK", 3: "OK", 4: "OK"}

