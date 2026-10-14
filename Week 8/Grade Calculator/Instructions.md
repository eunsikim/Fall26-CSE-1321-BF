# Input Validator
- Create a function called `input_grade`. 
- This function does not take any parameters.
- The function should ask the user for a grade.
- If the grade is between 0 and 100, the function should return it.
- If the grade is not valid, the function should keep asking the user for a grade until the user inputs a valid value.
## Test:
- Once the function is called, is should keep prompting the user for an input until a value between 0 and 100 is entered.
- The function call should then be expressed as a numeric value between 0 and 100.

# Check Lowest
- Create a function called `check_lowest`.
- This function takes two parameters:
    - Both parameters will hold a numeric grade value [0, 100]
- The function should return the lower value of both parameters.
## Test
- `check_lowest(90, 80)` => `80`
- `check_lowest(80, 90)` => `80`

# Quiz Average Calculator
- Create a function called `quiz_avg()`.
- This function takes no parameters.
- The function should ask the user for 11 grades using the function `input_grade()`.
- The function should keep track of the single lowest grade inputted and subtract it from the sum using the function `check_lowest()` for each inputted grade value.
- The function should return the average of 10 quizzes (not 11 since we drop the lowest one).

# Test policy
- Create a function called `test_policy`.
- This function takes 3 optional parameters:
    - The first parameter will hold the grade value for Test 1.
    - The second parameter will hold the grade value for Test 2.
    - The third parameter will hold the value for the Final Exam.
    - All three parameters will have as default value the boolean value of `False`
- This function should check which test the policy is being applied:
    - For Test 1, all three parameters should have a numeric grade value [0, 100].
    - For Test 2, only the second and third parameters should have a numeric grade value [0, 100]
- If the test policy evaluated is for Test 1, the function should return the highest grade value between Test 1, Test 2, and Final Exam.
- If the test policy evaluated is for Test 2, the functio should return the highest grade value between Test 2 and Final Exam.
## Test
- `test_policy(t1 = 80, t2 = 100, f = 90)` => `100`
- `test_policy(t1 = 80, t2 = 90, f = 95)` => `95`
- `test_policy(t1 = 90, t2 = 80, f = 70)` => `100`
- `test_policy(t2 = 80, f = 100)` => `100`
- `test_policy(t2 = 80, f = 60)` => `80`

# Input Bonus
- Create a function called `input_bonus`.
- This function does not take any parameters.
- This function should ask the user how many times they been at the tutoring center.
- Each visit will account for 0.5 bonus points.
- This bonus point can be accumulated up to 5 points.
- The function should calculate and return the corresponding bonus points.
## Test
- If the user inputs `10`, `input_bonus()` => `5.0` 
- If the user inputs `3`, `input_bonus()` => `1.5` 
- If the user inputs `100`, `input_bonus()` => `5` 

# Final Grade Calculator
- Create a function called `final_grade`.
- This function should take in 4 parameters:
    - The first parameter will hold the quiz average grade.
    - The second parameter will hold the Test 1 grade.
    - The third parameter will hold the Test 2 grade.
    - The fourth parameter will hold the Final Exam grade.
- The function should calculate and return the final class grade.
    - Each grading item is worth 25% of the final grade.
## Test
- `input_bonus(100, 100, 100, 100)` => `100.0` 
- `input_bonus(100, 90, 80, 70)` => `85.0` 

# Letter Grade Conversion
- Create a function called `convert_letter_grade`.
- This function should take in 1 parameter that will hold a grade value [0, 100].
- The function should return the respective letter grade.
    - A >= 89.5
    - B >= 79.5
    - C >= 69.5
    - D >= 59.5
    - F <= 59.5
## Test
- `convert_letter_grade(90)` => `"A"`
- `convert_letter_grade(54)` => `"F"`
- `convert_letter_grade(79.4)` => `"C"`
- `convert_letter_grade(79.5)` => `"B"`

# Grade Output
- Create a function called `print_grade`.
- This function should take in 2 parameters:
    - The first parameter will hold a numerical grade value
    - The second parameter will hold a letter grade value
- The function should print:
    - `"Your CSE 1321 Final Grade is: {grade_num} ({grade_let})"`