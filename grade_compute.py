"""
Python Module File for Assignment 2

main(), grade_list(), lowest_grade(), grade_average()
"""

def process_line():
    """Returns letter grades from user input and value"""
    check = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "D+", "F", "a+", "a", "b+", "b", "c+", "c", "d+", "d", "f"]
    grades = []
    i = 0
    while i < 4:
        user_input = input("Please input grade(a+, B, c+, D+, f) or (q)uit: ")
        #makes sure that input is within expected range
        if user_input.capitalize() == "Q":
            #If input is equal, send output to cancel program
            return -1
        if user_input in check:
            #returns tuple of letter grade and its respective value
            grades.append((user_input.capitalize(), grade_to_number(user_input.capitalize())))
            i +=1
        else:
            print("Misinput of grade please try again")
    return grades

def grade_to_number(user_input):
    """Returns a number value to express grade letter"""
    #dictionary of letter grade to their respective number value
    grades_val = {"A+":100, "A":95, "B+":90, "B":85, "C+":80, "C":75, "D+":70, "D":65, "F":60}
    return grades_val[user_input]

def number_to_grade(grades):
    """Returns a letter value to express grade number value. Expects reduced list of grades."""
    val_grades = {100:"A+", 95:"A", 90:"B+", 85:"B", 80:"C+", 75:"C", 70:"D+", 65:"D", 60:"F"}
    num = 0
    for i in grades:
        num += i[1]
    num /= 3
    return val_grades[(int(num/5))*5]

def main():
    """Main function. Used to create a list of grades with both letter and number value. Prints values out to user"""
    grades = process_line()
    if grades == -1:
        return -1
    print(f"Grades put in:\n{grades[0][0]}, {grades[1][0]}, {grades[2][0]}, {grades[3][0]}")
    lowest = 0
    #checks for grade with the lowest value
    for i in range(0,3):
        if grades[i][1] > grades[i+1][1]:
            lowest = i+1
    #prints and removes the lowest grade from the grades
    print(f"The lowest grade is: {grades.pop(lowest)[0]}")
    print(f"The average is: {number_to_grade(grades)}")
    return 0