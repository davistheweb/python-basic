def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n - 1)

def fractriol(n):
    result = 0
    for i in range(n + 1):
        result += factor(i)
    return result

# Input a number from the user
num = int(input("Enter a number: "))

# Calculate the fractriol of the input number
result = fractriol(num)

# Print the fractriol
print("The fractriol of", num, "is:", result)
