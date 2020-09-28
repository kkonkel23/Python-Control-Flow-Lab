# exercise-01 Vowel or Consonant
# Write the code that:

# Prompts the user to enter a letter in the alphabet: Please enter a letter from the alphabet (a-z or A-Z):
# Write the code that determines whether the letter entered is a vowel
# Print one of following messages (substituting the letter for x):
# The letter x is a vowel
# The letter x is a consonant
# Hints: Use the in operator to check if a character is in another string For example, if some_char in 'abc':

letter  = input('Enter a letter in the alphabet: ')
low_let = letter.lower()

if low_let == 'a' or low_let =='e' or low_let =='i' or low_let =='o' or low_let =='u':
    print(f'The letter {letter} is a vowel')
else:
    print(f'The letter {letter} is a consonant')

# exercise-02 Length of Phrase
# Write the code that:

# Prompts the user to enter a phrase: Please enter a word or phrase:
# Print the following message:
# What you entered is xx characters long
# Return to step 1, unless the word 'quit' was entered.

while True:
    phrase = input('Enter a word or phrase, enter quit to stop ')
    new_phrase = phrase.lower()
    if new_phrase == 'quit':
        print('Goodbye')
        break
    else:
        print(f'What you entered is {len(phrase)} characters long')


# exercise-03 Calculate Dog Years
# Write the code that:

# Prompts the user to enter a dog's age in human years like this: Input a dog's age in human years:
# Calculates the equivalent dog years, where:
# The first two years count as 10 years each
# Any remaining years count as 7 years each
# Prints the answer in the following format: The dog's age in dog years is xx
# Hint: Use the int() function to convert the string returned from input() into an integer

age = int(input("Enter a dog's age in human years "))

if age <= 2:
    dog_years = age * 10
else:
    dog_years = 20 + age * 7

print("The dog's age in dog years is",dog_years)

# exercise-04 What kind of Triangle?
# Write the code that:

# Prompts the user to enter the three lengths of a triangle (one at a time): Enter the lengths of three side of a triangle: a: b: c:
# Write the code that determines if the triangle is: equalateral - all three sides are equal in length scalene - all three sides are unequal in length isosceles - two sides are the same length
# Print a message such as:
# A triangle with sides of , & is a triangle

a = int(input('Enter the length of the first side of the triangle '))
b = int(input('Enter the length of the second side of the triangle '))
c = int(input('Enter the length of the third side of the triangle '))

if a == b and a == c and b == c:
    print(f'A triangle with sides of {a}, {b} and {c}, is an equalateral triangle')
elif a == b or a == c or b == c:
    print(f'A triangle with sides of {a}, {b} and {c}, is an isosceles triangle')
else:
    print(f'A triangle with sides of {a}, {b} and {c}, is an scalene triangle')


# exercise-05 Fibonacci sequence for first 50 terms
# Write the code that:

# Calculates and prints the first 50 terms of the fibonacci sequence.
# Print each term and number as follows:
#   term: 1 / number: 1
#   term: 2 / number: 1
#   term: 3 / number: 2
#   term: 4 / number: 3
#   term: 5 / number: 5```
#   etc.
# Hint: The next number is found by adding the two numbers before it

n1, n2 = 0,1
count = 1

print(f'term: {count} / number {n2}')
while count < 50:
    term = n1 + n2
    n1 = n2
    n2 = term
    count += 1
    print(f'term: {count} / number {term}')

# exercise-06 What's the Season?
# Write the code that:

# Prompts the user to enter the month (as three characters): Enter the month of the year (Jan - Dec):
# Then prompts the user to enter the day of the month: Enter the day of the month:
# Calculate what season it is based upon this chart: Dec 21 - Mar 19: Winter Mar 20 - Jun 20: Spring Jun 21 - Sep 21: Summer Sep 22 - Dec 20: Fall
# Print the result as follows:

month = input('Enter the month as three characters(Jan-Dec): ')
day = int(input('Enter the day of the month: '))
new_mon = month.lower()
mon_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

if new_mon in mon_list:
    if new_mon == 'dec' or new_mon == 'jan' or new_mon == 'feb' or new_mon == 'mar':
        if new_mon == 'dec' and day >= 21 or new_mon == 'mar' and day <= 19:
            print(f"You're in Winter!")
        elif new_mon == 'dec' and day < 21:
            print("You're in Fall!")
        elif new_mon == 'mar' and day > 19:
            print("You're in Spring!")
        else:
            print("You're in Winter!")
    elif new_mon == 'apr' or new_mon == 'may' or new_mon == 'jun':
        if new_mon == 'jun' and day > 20:
            print(f"You're in Summer!")
        else:
            print("You're in Spring!")
    elif new_mon == 'jul' or new_mon == 'aug' or new_mon == 'sep':
        if new_mon == 'sep' and day > 21:
            print(f"You're in Fall!")
        else:
            print("You're in Summer!")
    elif new_mon == 'oct' or new_mon == 'nov':
            print("You're in Fall!")
else:
    print('Please enter a valid month')
