maths = float(input("enter the marks for maths:"))
english = float(input("enter the marks for english:"))
urdu = float(input("enter the marks for urdu:"))
pst = float(input("enter the marks for pst:"))
total_marks = 500
computer = float(input("enter the marks for computer"))
obtained_marks = float(maths + english + pst + computer + urdu)
print("your obtained marks are:", obtained_marks)
percentage = float(obtained_marks / total_marks * 100)
print("your percentage is : ", percentage)
if percentage < 60:
    print("your grade is F")
if 60 <= percentage < 70:
    print("your grade is C")
if 70 <= percentage < 80:
    print("your grade is B")
if 80 <= percentage < 90:
    print("your grade is A")
elif percentage >= 90:
    print("your grade is A1")
