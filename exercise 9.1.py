transactions = []

for i in range(5):
    value = float(input("Enter transaction amount: "))
    transactions.append(value)

largest = max(transactions)
average = sum(transactions) / 5

print("\nTransactions:", transactions)
print("Largest transaction amount:", largest)
print("Average spend:", round(average, 2))