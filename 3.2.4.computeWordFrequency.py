# HarvardX PH526X Week 3 Case Study 2 Video 3.2.4
# Note this script skips the counting of the German version of Romeo Und Julia

def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

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


def word_stat(word_counts):
    """
    Return number of unique words and word frequencies.
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

if __name__ == "__main__":
    text = read_book("./romeojuliet.txt")
    word_counts = count_words(text)
    (num_unique, counts) = word_stat(word_counts)
    print("There are %i unique words in Romeo & Juliet" % num_unique)
    print("Total counts: ", sum(counts))
