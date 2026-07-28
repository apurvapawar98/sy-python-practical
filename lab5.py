print("first code")

n= int(input("enter a number"))
if n<5:
    print(n,"is less than 5")

    print("secound code")

    n = int(input("enter a number"))
    if n<5:
        print(n,"is less than 5")
    else:
        print(n,"is not less than 5")  

print("third no")

n = int(input("enter a number"))
if n<5:
    print(n,"is less than 5")
elif n>5:
    print(n,"is greter than 5")           
else:
    print(n,"is equal to 5")   

print("forth code")
number = [1,2,3,4,5,6,7]
sq = 0
for vol in number:
        sq = vol * vol
        print(sq)