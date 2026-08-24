name = (input("enter student name"))
s1 = float(input("enter subject 1 marks :"))
s2 = float(input("enter subject 2 marks:"))
s3 = float(input("enter subject 3  marks :"))

subject = s1 + s2 +s3
average = subject/3

print("_____student score card______")
print("student name:",name)
print("subject1:",s1)
print("subject2:",s2)
print("subject3:",s3)
print("total marks:",subject)
print("average marks:",average)