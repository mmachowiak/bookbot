# open file and place it in a variable
with open("books/frankenstein.txt", "r") as file:
    text = file.read()


def count_words(text):
    # create variable to store number of words
    num_words = 0
    # split the text into words
    words = text.split()
    # loop through the words and increment the number of words
    for word in words:
        num_words += 1
    return num_words


print(f"Number of words: {count_words(text)}")


# function returns the number of times each character appears in the string
# characters should be lowercase
def count_characters(text):
    # create a dictionary to store the character count
    char_count = {}
    # loop through the text
    for char in text:
        # if the character is a letter
        # if char.isalpha():
        # convert the character to lowercase
        char = char.lower()
        # if the character is already in the dictionary
        if char in char_count:
            # increment the count
            char_count[char] += 1
        else:
            # add the character to the dictionary
            char_count[char] = 1
    return char_count


def report():
    print("--- Begin report of {file} ---")
    print(f"{count_words(text)} words found in the text.")

    char_count = count_characters(text)
    total_chars = sum(char_count.values())
    print(f"Character count: {total_chars}")

    for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{char}' character was found {count} times")
    print("--- End of report ---")


report()
