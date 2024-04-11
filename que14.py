marks = []

for i in range(5):
    subject_mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(subject_mark)

total_marks = sum(marks)
average_score = total_marks / 5
percentage = (total_marks / (5 * 70)) * 100

grade = ""
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Average score:", average_score)
print("Percentage:", percentage)
print("Grade:", grade)
