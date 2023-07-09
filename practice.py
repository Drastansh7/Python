'''
Open a new file and name it lab2_p3.py. Write a program that asks the user for a Unicode value and prints out the character associated with it. For example, a sample execution could look like the following. Curious about Unicode? Take a look at why we care: https://docs.python.org/3/howto/unicode.html
Please enter the Unicode value: 65
The value you entered, 65, represents the character: A
'''

# def unicode(value):
#     return chr(value)
#
# print(unicode(98))

"""
Problem 2
In a new file (named lab3_p2.py), write a few lines of code that achieves two goals.
Part A: Parsing the user input
1. Ask the user to input a date of birth (yyyymmdd) (see example input format).
2. Ask the user to input today’s date (see example input format).
3. Display the date of birth and today’s date in the mm/dd/yyyy format
Hint: use divide, div (//) and mod(%) in determining the parts of the date.
Below is an example execution (run) of the program. The bold text represents user input. Your program should display its output exactly as shown below.
Please enter a date of birth: 19951117
Please enter today’s date: 20170901
Date of birth is 11/17/1995 Today’s date is 9/1/2017
Part B: Calculating the user’s age in years, months and days.
1. Using the years, months and days from Part A, calculate the user’s age in years, months and days.
2. You can assume that month is always 30 days.
Below is an example execution (run) of the program. The bold text represents user
input. Your program should display its output exactly as shown below.
You have been alive for 21 years 9 months 19 days.
"""

# user_dob = int(input("Enter a DOB (yyyymmdd): "))
# date = int(input("Enter today's date (yyyymmdd): "))
#
# dob_year = user_dob // 10000
# dob_month = user_dob // 100 % 100
# dob_day = user_dob % 100
#
# date_year = date // 10000
# date_month = date // 100 % 100
# date_day = date % 100
#
# print("Date of birth is " + str(dob_month) + "/" + str(dob_day) + "/" + str(dob_year) + " Today's date is " + str(date_month) + "/" + str(date_day) + "/" + str(date_year))
#
#
# total_days_dob = dob_year * 365 + dob_month * 30 + dob_day
# total_days_date = date_year * 365 + date_month * 30 + date_day
#
# days_user_age = total_days_date - total_days_dob
#
# years = days_user_age // 365
# months = (days_user_age // 365) % 30
# days = days_user_age % 365 % 30
# print("You have been alive for " + str(years) + " years " + str(months) + " months " + str(days) + " days.")


"""
Problem 4
Create a new Python file named lab3_p4.py with the required comment header and write a program that generates random 5-letter strings.
1. Use the randrange function from the random module to generate three random numbers that fall within the ASCII range for lowercase letters. You can refer to the documentation for the random module (https://docs.python.org/3/library/random.html) and the ASCII chart (https://www.asciitable.com)
2. The chr function in Python converts an integer to its character value. For example, chr(97) gives the character ‘a’. Use the chr function to convert your random integers
    3
to their character values. Build a string using these characters via string concatenation. Create a variable name for this string.
3. Generate two possible rotations of the string. In order to generate a rotation of a string, shift each character one position to the right. For example, the rotations of the string abcde are eabcd and deabc. Store each of the variations of the string each in separate variables.
4. Print the original string that you generated followed by each rotation.
For example, for the original string irlno, the output will be:
     irlno
     oirln
     noirl         
              """

# import random
#
# def randomx():
#     alpha1 = random.randrange(97, 123)
#     alpha2 = random.randrange(97, 123)
#     alpha3 = random.randrange(97, 123)
#     alpha4 = random.randrange(97, 123)
#     alpha5 = random.randrange(97, 123)
#
#     result1 = (chr(alpha1) + chr(alpha2) + chr(alpha3) + chr(alpha4) + chr(alpha5))
#     result2 = (chr(alpha5) + chr(alpha1) + chr(alpha2) + chr(alpha3) + chr(alpha4))
#     result3 = (chr(alpha4) + chr(alpha5) + chr(alpha1) + chr(alpha2) + chr(alpha3))
#
#     return result1 + '\n' + result2 + '\n' + result3
#
#
# print(randomx())


'''An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
Create a new file named lab4_p2.py and write a program that asks the user for a year. The program should determine and print the leap year status of the year that the user enters. The conditions for a year to be a leap year are as follows:
● The year divisible by 4 is a leap year, unless:
○ The year is divisible by 100, in which case it is not a leap year, unless:
■ The year is also divisible by 400, then it is a leap year.
This means that the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
(Note: You do not need an if-else statement for this. Try to come up with a boolean expression that will serve the purpose of this problem.)
'''

# def leap_year(year):
#
#     if year % 4 == 0:
#         if year % 400 == 0:
#             return True
#         elif year % 100 == 0:
#             return False
#         else:
#             return True
#     else:
#         return False
#
# print(leap_year(2200))
#
#
'''
In a new Python file called lab4_p3.py, write a program that asks the user for a student’s scores in five different assessments. Print out the average score of the student and an assigned gradethatfollowsthecriteriadefinedbelow. YoursolutionshouldNOTmakeuseofif-elif, and only rely on if-else for this lab. We'll get to elif next week.
● Ascoreabove90isanA
● Ascorebetween90andan87isanA- ● Ascorebetween87and84isaB+
● Ascorebetween84and80isaB
● Ascorebetween80and77isaB-
● Ascorebetween77and74isaC+
● Ascorebetween74and70isaC
● Ascorebetween70and67isaC-
● Ascorebetween67and64isaD+
● Ascorebetween64and55isaD
● Ascorebelow55isanF
A sample execution is shown below (the bolded text represents user input):
Please enter the score for assessment 1: 90 Please enter the score for assessment 2: 65 Please enter the score for assessment 3: 87 Please enter the score for assessment 4: 98 Please enter the score for assessment 5: 77
3
The average score is: 83.4 The assigned grade is: B

'''

# def gradex(score1, score2, score3, score4, score5):
#     avg_score = (score1 + score2 + score3 + score4 + score5)/\5
#
#     if avg_score > 90:
#         grade = 'A'
#     elif  87 < avg_score <= 90:
#         grade = 'A-'
#     elif 84 < avg_score <= 87:
#         grade = 'B+'
#     elif 80 < avg_score <= 84:
#         grade = 'B'
#     elif 77 < avg_score <= 80:
#         grade = 'B-'
#     elif 74 < avg_score <= 77:
#         grade = 'C+'
#     elif 70 < avg_score <= 74:
#         grade = 'C'
#     elif 67 < avg_score <= 70:
#         grade = 'C-'
#     elif 64 < avg_score <= 67:
#         grade = 'D+'
#     elif 55 <= avg_score <= 64:
#         grade = 'D'
#     elif 0 <= avg_score < 55:
#         grade = 'F'
#
#
#     return "The average score is: " + str(avg_score) + '\n' + "The grade is: " + grade
#
#
#
# print(gradex(90,65,87,98,77))


'''Suppose you are writing software to run an elevator in a 26 floor hotel in NYC. Because of triskaidekaphobia, the buttons in the elevator do not include 13. So when a guest pushes the elevator button 14, the elevator actually takes them to the 13th floor. In addition, a club card is necessary to go to the 26th floor. Without a club card, the elevator will not take you to the 26th floor.
When asked if they have a club card, the user should input “Y” for yes and “N” for no. (In this scenario, assume that the user can’t get to the 14th floor directly.). Write your code in a Python file named lab4_p4.py.
For example, some sample executions would look like this (user input is bolded):
Which floor are you going to? 14 Taking you to the 13th floor. -------------------------------------- Which floor are you going to? 26
Do you have a club card? N
Sorry you are not authorized. Please check with the front desk. --------------------------------------
Which floor are you going to? 26
Do you have a club card? Y
Taking you to the 26th floor. --------------------------------------
Which floor are you going to? 15
Taking you to the 15th floor.'''

# def elevator():
#
#     user_input = int(input("Which floor are you going to: "))
#
#     if 1 <= user_input <= 12:
#         print("Taking you to the " + str(user_input) + " floor")
#
#     elif user_input == 14:
#         print("Taking you to the 13 floor")
#
#     elif 14 < user_input <= 25:
#         print("Taking you to the " + str(user_input) + " floor")
#
#     elif user_input == 26:
#         club_card = input("Do you have the club card? (Y/N) ")
#         if club_card == "Y" or club_card == "y":
#             print("Taking you to the 26 floor")
#         else:
#             print("Sorry you are not authorized. Please check with the front desk.")
#
#     else:
#         print("Invalid floor number")
#
# elevator()

'''Create a new python file named lab5_p3.py and write code that asks the user for 3 inputs side_a, side_b and side_c, each representing a length in inches. Your code will check whether it is possible to make a right triangle using these 3 side lengths.
Use the Pythagorean theorem in order to determine if the sides can create a right triangle. You will first need to find the longest side of the triangle which could be side_a, side_b or side_c. Do not use any function to determine the longest side of the triangle, build an appropriate if-elif-else statement to do so.
A sample program execution is shown below (the bold text represents user input):
Enter the length of side_a: 4
Enter the length of side_b: 3
Enter the length of side_c: 5
It is possible to make a right triangle with the side lengths 4, 3 and 5. --------------------------------------------------------------- --
Enter the length of side_a: 4
Enter the length of side_b: 9
Enter the length of side_b: 5
It is not possible to make a right triangle with the side lengths 4, 9 and 5.'''

# def right_triangle():
#
#     side1 = int(input("Enter the length of side_a: "))
#     side2 = int(input("Enter the length of side_b: "))
#     side3 = int(input("Enter the length of side_c: "))
#
#
#     if (side1 ** 2) + (side2 ** 2) == side3 ** 2:
#         print("It is possible to make a right triangle with the side lengths " + str(side1) + ", " + str(
#             side2) + " and " + str(side3))
#
#     elif side2 ** 2 + side3 ** 2 == side1 ** 2:
#         print("It is possible to make a right triangle with the side lengths " + str(side1) + ", " + str(
#             side2) + " and " + str(side3))
#     elif side1 ** 2 + side3 ** 2 == side2 ** 2:
#         print("It is possible to make a right triangle with the side lengths " + str(side1) + ", " + str(
#             side2) + " and " + str(side3))
#     else:
#         print("It is not possible to make a right triangle with the side lengths " + str(side1) + ", " + str(
#             side2) + " and " + str(side3))
#
#
#
#
# right_triangle()

'''Write a program that prompts the user to enter a natural number (non-negative integer). The program should use a while loop to calculate the sum of the natural numbers from 1 up to and including the value entered by the user. Once calculated, the program should print that result. Place the program in a file named lab6_p2.py. A sample execution is shown below (the bold text represents user input). Be sure to test your program for many different inputs.
Enter a natural number: 5
The sum of the natural numbers from 1 to 5 is 15.
Enter a natural number: 10
The sum of the natural numbers from 1 to 10 is 55.'''

# def sum():
#     user_input = int(input("Enter a number: "))
#     counter = 1
#     sum = 0
#     while counter <= user_input:
#
#         sum += counter
#         counter += 1
#
#     print(sum)
#
# sum()


'''Write a program to print hollow right triangle star pattern series using while loops. The program should prompt the user to enter the number of rows of the pattern and then generate the pattern. Place the program in a file named lab6_p3.py. A sample execution is shown below (the bold text represents user input). Be sure to test your program for many different inputs
Input the number of rows: 5
*
** ** ** *****'''

# def astrisk():
#
#     user_rows = int(input("Enter the number of rows: "))
#
#     user_columns = user_rows
#
#     columns = 1
#
#     while columns <= user_columns:
#         rows = 1
#         while rows <= user_rows:
#             if columns == rows or rows == 1 or columns == user_rows:
#                 print("*", end=" ")
#             else:
#                 print(" ", end =" ")
#
#             rows += 1
#
#         print()
#         columns += 1
#
#
# astrisk()
#
'''Write a program to print the symbols of the Latin alphabet from a to z (lowercase) using a while loop. Place the program in a file named lab6_p4.py. Use a while loop to loop over the values of the symbols. Hint: recall that each alphabet symbol corresponds to an integer value. A sample execution is shown below.
Latin alphabet symbols: a, b, c, ... , x, y, z'''


# def latin():
#
#     counter = 97
#     print("Latin alphabet symbols: ", end="")
#     while counter <= 122:
#         print(chr(counter), end=" ")
#         counter += 1
#
# latin()
#

'''Write a program to print the square roots of the first 25 odd positive integers (starting at 1). Place the program in a file named lab6_p5.py. Use a while loop to loop over the values of the symbols. The output of the program should look something like this:
The square roots of the first 25 odd integers are: 1.0, 1.7320508075688772, 2.23606797749979, 2.6457513110645907, 3.0, 3.3166247903554, ...'''

# import math
#
# def square_root():
#
#     counter = 1
#
#     while counter <= 25:
#         print(math.sqrt(counter))
#         counter += 2
#
# square_root()

'''Open a new file called lab7_p2.py and write code that asks the user for a four digit positive integer, n, and prints the sum of all of the digits of the number. Recall that you can use the // and % operators to isolate digits in a number. DO NOT use indexing to access the elements of the user's input.
Below is a sample code execution (user input has been bolded):
Please enter a number: 6315
The sum of the digits of 6315 is: 15'''

def sumx():

    user_input = int(input('Enter a four digit number: '))

    listx = []

    for digit in str(user_input):
        listx.append(digit)
    print(listx)

    sum = 0

    for num in listx:
        sum += int(num)

    print(sum)

sumx()









