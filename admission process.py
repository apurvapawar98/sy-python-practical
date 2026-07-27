print("==========Student  Details==========")
age=int(input("Enter your age:"))
marks=float(input("Enter your Marks:"))

if age>=18 and age<=25:
    print("You are eligible for college admission based on marks.")
    if marks >=65:
        print(" You are eligible for the addmision")

        if marks >=85:
            print("You are eligible for AIML.")
        elif marks >=75:
            print("You are eligible for CSE")
        else:
            print("You are not eligible for other courses.")
    else:
        print("You  are not eligible for college admission due to age.")
else: 
    print("You are not eligible for college admission due to age.")  



 
