no_of_subjects = int(input("Enter the number of subjects : "));
total = 0;
marks_got = 0;
while(marks_got < no_of_subjects):
    mark = int(input("mark = "));
    total = total + mark;
    marks_got = marks_got + 1;
print("Total is ",total);
average = total/no_of_subjects;
print("Percentage is ",round(average,2),"%");
print("Percentage is ",round(average),"%");
