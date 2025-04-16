# [1] Comprehension Problems

# [1.1] Data Types
"""Determine the data type for each variable. (Ex. a = 5, so the data type of a
is an int). If you’re not sure, you can use the type() function to output the
type of the variable."""

variable1 = "Surprised Pikachu is the best meme."
# Type of variable1 = [str]

variable2 = 5
# Type of variable2 = [int]

variable3 = 1.29
# Type of variable3 = [float]

variable6 = [1,2,3]
# Type of variable6 = [list]

variable7 = (1,3,5)
# Type of variable7 = [tuple]

variable8 = {"brand": "Ford", "model": "Mustang", "year": 1964}
# Type of variable8 = [dict]


def g():
    print("beep beep")
    return True

variable4 = g
# Type of variable4 = [function]

variable5 = g()
# Type of variable5 = [boolean]


# [1.2] Using /, //, %
"""Observe what happens in each of the operations below. Recall the differences
between normal, floor, and modulo division and describe those differences."""

print(5/2) # normal division
# It simply is normal division like usual 2.5

print(4//3) # floor division
# the number of time the denominator goes into num (no decimal)

print(459 % 4) # modulo division
# the remainder


# [1.3] Hanging by a String
"""In the following problem use string indexing to turn the words below into
a new word that is part of the original word or a modified version of it."""
# Example: Strongest → Strong

word_1 = "Fastest"
new_word_1 = word_1[0:4] # when you are ready to run this code, uncomment this line. do the same for all answers.
print(new_word_1)

word_2 = "Outside" #two options are acceptable here, try both if you want!
new_word_2 = word_2[3:] 
print(new_word_2)

word_3 = "racecar"
new_word_3 = word_3[4:7]
print(new_word_3)

# [1.4] Palindromes
"""Use string indexing to reverse the palindrome, then use the "print()" function
to print the string out to verify that it is in fact a palindrome."""

palindrome_1 = "tattarrattat"
print('normal:', palindrome_1)
print('reverse:', palindrome_1[::-1]) #there are two :: [start:stop:step] and we are just ignoring the start and stop

palindrome_2 = "madam"
print('normal:', palindrome_2)
print('reverse:', palindrome_2[::-1])


# [2] Application Problems

# [2.1] Your Favorite Equation 
"""Take your favorite equation (or find one on the internet) and turn it into a
function."""


# [2.2] The Last Digit
"""Write a function last digit(num) which returns the last digit of a number as
a string."""

def last_digit(num):
    #str(num[-1])
    #return(str) what i did that was wrong
    num = str(num)
    return num[-1]
print(last_digit(1234))
# Tip: To convert an int or a float to a string, use the str() function. If you want to convert a string to an int or a float, use int() or float() respectively.



# [3] Python Functions
"""For this problem, it would be helpful to know some functions that are already
built-in to Python. In particular, min() and max(). Run the following code (and try
it yourself) to see what they do, and then complete the function two_of_three. This
one is a bit tricky so dont feel bad if you're stuck for a while!"""

min(3, 4, 5), min(-5, 9, -20)
max(3, 4, 5), max(-5, 9, -20)

"""Return x*x + y*y, where x and y are the two largest members of the positive numbers a, b, and c.

two_of_three(1, 2, 3)
expected output: 13
two_of_three(5, 3, 1)
expected output: 34
two_of_three(10, 2, 8)
expected output: 164
two_of_three(5, 5, 5)
expected output: 50
"""



def two_of_three(a, b, c):
    numbers = [a,b,c]
    x = max(numbers)
    numbers.remove(x)
    y = max(numbers)
    return (x * x) + (y * y)
print(two_of_three(1,2,3))



# [4] Coding Hygiene
"""As programmers, we do need to practice good coding. What does that entail you might ask?
We should abide by the following rules of thumb:
1. Use semi-descriptive variables. DO NOT represent every variable
as a single letter. This leads to ambiguity and makes it very difficult to
understand/read your code when you come back to it, it also makes it difficult
for us when we grade your homework. Examples: use temp instead of t,
radius instead of r, etc...
2. Leave comments as frequently as needed to make it easy to understand
for people reading, especially in your functions. We recommend a docstring
under the name of your functions describing what it does.
3. Stay consistent with your line spacing, try to make it as comprehensible
as possible. Cramped up code with no spacing in between is not very pleasing
to the eye and can get overwhelming."""


# [4.1] Pretty Me Up
"""Fix the given code so that it adheres to the coding hygiene guidelines above:"""

def vol(r):
    return 4/3 * 3.14 * r**3
