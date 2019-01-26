"""
Ex1
Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words
"Sand", "Water", "Fish", and "Sun" appear without overlapping (regardless of the case).

Examples

sum_of_a_beach("WAtErSlIde")                    ==>  1
sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
sum_of_a_beach("cItYTowNcARShoW")               ==>  0
"""

from re import *

def sum_of_a_beach(beach):
    return len(findall('Sand|Water|Fish|Sun', beach, IGNORECASE))


assert sum_of_a_beach("SanD") == 1
assert sum_of_a_beach("sunshine") == 1
assert sum_of_a_beach("sunsunsunsun") == 4
assert sum_of_a_beach("123FISH321") == 1


"""
Ex2
Your task is to remove all duplicate words from string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'
"""


def remove_duplicate_words(s):
    s = s.split(" ")
    w = []
    for i in s:
        if i not in w:
            w.append(i)
    return " ".join(w)


print("Basic tests")
assert remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta") \
       == "alpha beta gamma delta"
assert remove_duplicate_words("my cat is my cat fat") == "my cat is fat"


"""
Ex3
Implement String#digit? (in Java StringUtils.isDigit(String)), 
which should return true if given object is a digit (0-9), false otherwise.
"""


def is_digit(n):
    if n.isdigit() and len(n)==1:
        return True
    else:
        return False

print("Sample tests")
assert is_digit("") == False
assert is_digit("7") == True
assert is_digit(" ") == False
assert is_digit("a") == False
assert is_digit("a5") == False


"""
Ex4
Write a function

vowel_2_index
that takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string. 
E.g: 

vowel_2_index('this is my string') == 'th3s 6s my str15ng'
vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel_2_index('') == ''
"""


def vowel_2_index(string):
    r = ""
    for i in range(len(string)):
        if string[i] in "aeiouAEIOU":
            r += str(i + 1)
        else:
            r += string[i]
    return r

assert vowel_2_index('this is my string') == 'th3s 6s my str15ng'
assert vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
assert vowel_2_index('Tomorrow is going to be raining') == 'T2m4rr7w 10s g1415ng t20 b23 r2627n29ng'
assert vowel_2_index('') == ''
test_str = "90's cornhole Austin, pickled butcher yr messenger bag gastropub next level " \
           "leggings listicle meditation try-hard Vice. Taxidermy gastropub gentrify, " \
           "meh fap organic ennui fingerstache pickled vegan. Seitan sustainable PBR&B " \
           "cornhole VHS. Jean shorts actually bitters ugh blog Intelligentsia. " \
           "Artisan Kickstarter DIY, fixie cliche salvia lo-fi four loko. PBR&B Odd " \
           "Future ugh fingerstache cray Wes Anderson chia typewriter iPhone bespoke four loko, " \
           "Intelligentsia photo booth direct trade. Aesthetic Tumblr Portland XOXO squid, " \
           "synth viral listicle skateboard four dollar toast cornhole Blue Bottle semiotics."
result = "90's c7rnh11l13 1516st19n, p24ckl28d b32tch36r yr m43ss46ng49r b53g g57str61p63b n67xt " \
         "l72v74l l78gg81ngs l87st90cl93 m96d98t100t102103n try-h111rd V116c118. T122x124d126rmy " \
         "g132str136p138b g142ntr146fy, m152h f156p 159rg162n164c 167nn170171 f174ng177rst181ch184 " \
         "p187ckl191d v195g197n. S202203t205n s209st212213n215bl218 PBR&B c227rnh231l233 VHS. " \
         "J241242n sh247rts 252ct255256lly b262tt265rs 269gh bl275g 278nt281ll284g286nts290291. " \
         "294rt297s299n K303ckst308rt311r D315Y, f320x322323 cl327ch330 s333lv336337 l340-f343 f346347r " \
         "l351k353. PBR&B 362dd F367t369r371 373gh f378ng381rst385ch388 cr392y W396s 399nd402rs405n " \
         "ch410411 typ416wr419t421r 424Ph427n429 b432sp435k437 f440441r l445k447, 450nt453ll456g458nts462463 " \
         "ph467t469 b472473th d478r480ct tr486d488. 491492sth496t498c T502mblr P509rtl513nd X518X520 sq524525d, " \
         "synth v536r538l l542st545cl548 sk552t554b556557rd f562563r d567ll570r t574575st " \
         "c580rnh584l586 Bl590591 B594ttl598 s601m603604t606cs."
assert vowel_2_index(test_str) == result


"""
Ex5
Your task is simply to count the total number of lowercase letters in a string.

Examples

lowercaseCount("abc"); ===> 3

lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 3
"""


def lowercase_count(string):
     return len(findall('[a-z]',string))

print("lowercase_count")
print ("works for some examples")
assert lowercase_count("abc") == 3
assert lowercase_count("abcABC123") == 3
assert lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 3
assert lowercase_count("") == 0
assert lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 0
assert lowercase_count("abcdefghijklmnopqrstuvwxyz") == 26


"""
Ex6
Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included).
"""


def validate_usr(username):
    return bool(match(r'^[a-z0-9_]{4,16}$', username))


assert validate_usr('asddsa') is True
assert validate_usr('a') is False
assert validate_usr('Hass') is False
assert validate_usr('Hasd_12assssssasasasasasaasasasasas') is False
assert validate_usr('') is False
assert validate_usr('____') is True
assert validate_usr('012') is False
assert validate_usr('p1pp1') is True
assert validate_usr('asd43 34') is False
assert validate_usr('asd43_34') is True


"""
Ex7
Your computer has forgotten how to speak ASCII! (or Unicode, whatever). 
It can only communicate in binary, and it has something important to tell you. 
Write a function which will receive a long string of binary code and convert it to a string. 
Remember, in Python binary output starts with '0b'.

As an example: binary_to_string('0b10000110b11000010b1110100') == 'Cat'

Input may consist of upper and lower case letters and numbers, in binary form of course, as well as special symbols. 
The input to your function will always be one string of binary.
"""


def binary_to_string(binary):
    b = binary.split('0b')
    r = ''
    for i in b:
        if i != '':
            r += chr(int(i,2))
    return r


assert binary_to_string('0b10000110b11000010b1110100') == 'Cat'
test_str = '0b10010000b11001010b11011000b11011000b11011110b1000000b10101110b11011110b11100100b11011000b11001000b100001'
result_str = 'Hello World!'
assert binary_to_string(test_str) == result_str
test_str = '0b10100110b11001010b11000110b11100100b11001010b11101000b100000' \
           '0b11011010b11001010b11100110b11100110b11000010b11001110b11001010b1000000b110001'
result_str = 'Secret message 1'
assert binary_to_string(test_str) == result_str


"""
Ex8
Challenge:

Given a two-dimensional array of integers, 
return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].
"""


def flatten_and_sort(array):
    lst = []
    for i in array:
        lst += i
    return sorted(lst)


print("should work for some simple example test cases")
assert flatten_and_sort([]) == []
assert flatten_and_sort([[], [1]]) == [1]
assert flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]) == [1, 2, 3, 4, 5, 6, 100]
