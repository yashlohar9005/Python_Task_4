print("-------- LOOP PROGRAM --------\n")

# 1. Use for loop to print numbers 1–100
print("1) Printing numbers from 1 to 100 :")
for i in range(1, 101):
    print(i, end=" ")

print("\n\n----------------------------------")


# 2. Use while loop for countdown timer
print("2) Countdown :")
count = 10
while count > 0:
    print("Countdown:", count)
    count -= 1
print("----------------------------------")


# 3. Implement break and continue
print("3) break and continue:")
for i in range(1, 11):
    if i == 5:   
        continue
    if i == 8:
        break
    print("Number:", i)
print("----------------------------------\n")


# 4. Iterate over string characters
print("4) Iterating over characters in a string:")
name = "Yash"
for ch in name:
    print(ch)
print("----------------------------------\n")


# 5. Generate multiplication table
print("5) Multiplication table of 2:")
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)
print("----------------------------------\n")


# 6. Use range with steps
print("6) Even numbers from 2 to 20 (Use range with steps):")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n----------------------------------\n")


# 7. Combine loop with conditions
print("7) Odd numbers between 1 and 20 (Combine loop with conditions):")
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=" ")
print("\n----------------------------------\n")


# 8. Real-world example: Shopping cart total
print("8) Real-world example for shopping cart total calculation")
prices = [100, 250, 75, 50]
total = 0

for price in prices:
    total += price

print("Items prices:", prices)
print("Total bill amount:", total)
print("----------------------------------\n")
