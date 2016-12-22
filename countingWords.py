from collections import Counter

text = "This is my test text. We're keeping this text short to keep things manageable."

# function that counts words in a given string
def count_words(text):
    """
    Count the number of times each word occurs in the
    text (str). Return dictionary where keys are unique
    words and values are word counts. Skip punctuations.
    """
    text = text.lower()
    skips = [".",",",";",":","'",'"']
    
    for char in skips:
        text = text.replace(char, "")
    
    word_counts = {}
    for word in text.split(" "):
        # case 1: known word
        if word in word_counts:
            word_counts[word] += 1
        # case 2: unknown word
        else:
            word_counts[word] = 1
    return word_counts

# same function as above but uses collections.Counter object
def count_words_fast(text):
    """
    Count the number of times each word occurs in the
    text (str). Return dictionary where keys are unique
    words and values are word counts. Skip punctuations.
    """
    text = text.lower()
    skips = [".",",",";",":","'",'"']
    
    for char in skips:
        text = text.replace(char, "")
    
    word_counts = Counter(text.split(" "))
    return word_counts

if __name__ == "__main__":
    print(count_words(text))
    print(count_words_fast(text))
    print(count_words(text) == count_words_fast(text))
    print(count_words(text) is count_words_fast(text))
    print(len(count_words("This comprehension check is to check for comprehension.")))
