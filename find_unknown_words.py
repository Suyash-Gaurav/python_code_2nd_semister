from search_linear import search_linear
from test import test



# Define the vocabulary list and the list of words from the book
vocab = ["apple", "boy", "dog", "down", "felt", "girl", "gross", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()


def find_unknown_words(vocab, wds):
    """
    Return a list of words in wds that do not occur in vocab

    Parameters:
    vocab (list): A list of known vocabulary words.
    wds (list): A list of words to check against the vocabulary.

    Returns:
    list: A list of words from wds that are not found in vocab.
    """

    # Initialize an empty list to store unknown words
    result = []

    # Iterate through each word in the provided words list
    for w in wds:
        # Use linear search to check if the word is in the vocabulary
        if search_linear(vocab, w) < 0:
            # If the word is not found in the vocabulary, add it to the result list
            result.append(w)

    # Return the list of unknown words
    return result


# Test cases to validate the function
# Check if the function correctly identifies unknown words
test(find_unknown_words(vocab, book_words) == ["from", "to"])
# Check if the function returns the entire list when the vocabulary is empty
test(find_unknown_words([], book_words) == book_words)
# Check if the function returns an empty list when all words are in the vocabulary
test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])
