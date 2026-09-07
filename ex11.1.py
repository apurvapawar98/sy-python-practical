
seats = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]


def display_seats():
    print("\nSeating Layout:")
    for row in seats:
        print(" ".join(row))


display_seats()

row = int(input("Enter row (1-3): "))
column = int(input("Enter column (1-3): "))

row -= 1
column -= 1

if seats[row][column] == "O":
    seats[row][column] = "X"
    print("Seat reserved successfully!")
else:
    print("Sorry, that seat is already reserved.")

display_seats()
