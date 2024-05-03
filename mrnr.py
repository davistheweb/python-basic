totalNumbers = 0

while True:
    num = int(input("Enter numbers and enter 0 to stop and sum up: "))

    if num == 0:
        break
    totalNumbers += num

print(totalNumbers)