



class WordProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.words = self.load_words_from_file()

    def load_words_from_file(self):
        """
        Load words from a file.

        This method opens the file specified by the filename attribute,
        reads its entire content, splits the content into individual words
        based on whitespace, and returns the list of words.

        Returns:
        list: A list of words read from the file.
        """
        # Open the file with the given filename in read mode
        with open(self.filename, "r") as f:
            # Read the entire content of the file into a single string
            file_content = f.read()

        # Split the file content into individual words based on whitespace
        wds = file_content.split()

        # Return the list of words
        return wds

    def search_linear(self, xs, target):
        """
        Perform a linear search to find the index of target in xs

        Parameters:
        xs (list): The list in which to search.
        target: The item to search for.

        Returns:
        int: The index of target in xs if found, otherwise -1.


        """
        # Iterate over the list with index and value
        for (i, v) in enumerate(xs):
            # If the current value matches the target, return the index
            if v == target:
                return i
        # If the target is not found, return -1
        return -1

    def find_unknown_words(self, vocab):
        """
        Return a list of words in wds that do not occur in vocab

        Parameters:
        vocab (list): A list of known vocabulary words.

        Returns:
        list: A list of words from wds that are not found in vocab.
        """
        # Initialize an empty list to store unknown words
        result = []

        # Iterate through each word in the provided words list
        for w in self.words:
            # Use linear search to check if the word is in the vocabulary
            if self.search_linear(vocab, w) < 0:
                # If the word is not found in the vocabulary, add it to the result list
                result.append(w)

        # Return the list of unknown words
        return result


wp = WordProcessor("vocab.txt")

words = wp.load_words_from_file()

print(words)



