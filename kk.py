# Create a list of words
words = ["apple", "banana", "cherry", "watermelon", "grape"]

# Initialize a variable to store the longest word length
longest_word_length = 0

# Loop through each word in the list
for word in words:
    if len(word) > longest_word_length:
        longest_word_length = len(word)

print(f"The length of the longest word is {longest_word_length}")
