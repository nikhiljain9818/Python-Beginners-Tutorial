n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    numbers = list(map(float, line))
    student_marks[name] = numbers
ques_name = input()
print(student_marks[ques_name])

if ques_name in student_marks:
    x = (float(student_marks[ques_name][0]) + float(student_marks[ques_name][1]) + float(student_marks[ques_name][2]))/3
    
print('%.2f' % x)