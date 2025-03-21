#!./venv/bin/python

"""
Write a program that asks the user three questions.

Ask the user:
1. Are you a student?
2. Do you have pets?
3. Do you smoke?

The program automatically decides whether a property you've applied to rent is available to you.

It should print an appropriate response, like "Property available" or "Property unavailable".

The program applies these criteria:

If you're a student, you can only rent the property if you don't have pets and don't smoke.

If you're not a student, you can rent the property if you smoke or have pets, but not if you
both smoke and also have pets.

"""

student = input("Are you a student? (y/n) : ")
pets = input("Do you have pets? (y/n) : ")
smokes = input("Do you smoke? (y/n) : ")

is_student = student == "y"
has_pets = pets == "y"
does_smoke = smokes == "y"

student_can_rent = is_student and not has_pets and not does_smoke
non_student_can_rent = not is_student and not (does_smoke and has_pets)

can_rent = student_can_rent or non_student_can_rent

print("Can rent: " + str(can_rent))