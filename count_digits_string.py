text = input("Enter a string: ")

count = 0

for char in text:
    if char.isdigit():
        count += 1

print("Total digits:", count)
