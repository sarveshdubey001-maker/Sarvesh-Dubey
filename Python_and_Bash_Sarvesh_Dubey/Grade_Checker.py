# Step 1: Take score as input
score = int(input("Enter your score: "))

if score >= 90:        # Use if/else to determine grade
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)
    