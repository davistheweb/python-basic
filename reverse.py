original_string = "Hello man"
words = original_string.split()  # Split the string into words

# Iterate through the words and reverse "Hello" if it exists
for i, word in enumerate(words):
    if word == "Hello":
        words[i] = word[::-1]  # Reverse the word "Hello"

reversed_string = ' '.join(words)  # Join the words back into a string
print(reversed_string)