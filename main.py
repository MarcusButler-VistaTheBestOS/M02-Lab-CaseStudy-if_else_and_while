# AUTHOR: Marcus Ed. Butler
# FILE: main.py

# VERSION: 2024-8-29
# VERSION HISTORY:
#     2024-8-29 = INIT

# DESCRIPTION: Checks if a student qualifies for Dean's List or Honor Roll.
#              Asks the user for students first and last name, as well as
#              their GPA in float form.


# GPA needed to be on Honor Roll or Dean's List.
HONOR_ROLL = 3.25
DEANS_LIST = 3.5


"""== MAIN LOOP =="""
while True:
    # Ask for a student's last name. If last name == 'ZZZ' then terminate program.
    last_name = input("\nWhat is the student's last name?\n\t>")
    if last_name == "ZZZ":
        break

    # Ask for a student's first name.
    first_name = input("What is the student's first name?\n\t>")
    
    # Ask for a student's GPA as a float.
    gpa = float(input("What is the students GPA?\n\t>"))
    
    # GPA >= 3.5 tell the user the student made the Dean's List.
    if gpa >= DEANS_LIST:
        print(f"{first_name} {last_name} made the Dean's List!")
    # GPA >= 3.25 tell the user the student made the Honor Roll.
    if gpa >= HONOR_ROLL:
        print(f"{first_name} {last_name} made the Honor Roll!")

# Runs on exit.
print('exiting...\n')
exit(0)
