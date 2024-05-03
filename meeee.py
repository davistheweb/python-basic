secret_no = 76

while True:
    check = int(input("Guess the secret number: "))
    if check == secret_no:
        print(f'Congratulations! You guessed the secret number as {secret_no}.')
        break
    elif check != secret_no:
        print('Try again')
