def load_words_from_file(filename):
    # Open the file with the given filename in read mode
    f = open(filename, "r")

    # Read the entire content of the file into a single string
    file_content = f.read()

    # Close the file to free up resources
    f.close()

    # Split the file content into individual words based on whitespace
    wds = file_content.split()

    # Return the list of words
    return wds


def text_to_words(the_text):




# Load the words from the file named "vocab.txt" into the variable vocab
vocab = load_words_from_file("vocab.txt")

# Print the number of words in vocab and the first five words
print("There are {0} words in the vocab, starting with {1}".format(len(vocab), vocab[:5]))
