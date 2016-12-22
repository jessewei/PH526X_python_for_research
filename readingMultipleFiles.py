import os
import pandas as pd

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
    book_dir = "./Books"
    stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
    title_num = 1
    for language in os.listdir(book_dir):
        for author in os.listdir(book_dir + "/" + language):
            for title in os.listdir(book_dir + "/" + language + "/" + author):
                inputfile = book_dir + "/" + language + "/" + author + "/" + title
                print(inputfile)
                text = read_obok(inputfile)
                (num_unique, counts) = word_stats(count_words(text))
                stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
                title_num += 1
    
    print(stats.head())
    print(stats.tail())
