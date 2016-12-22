import os
import pandas as pd
import matplotlib.pyplot as plt

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
    
    # thin slicing the first and last few rows of the data
    print(stats.head())
    print(stats.tail())
    # plotting using matplotlib.pyplot
    plt.plot(stats.length, stats.unique, "bo")
    plt.loglog(stats.length, stats.unique, "bo")
    # selecting only books with language as English
    print(stats[stats.language == "English"])
    
    # plotting each language with different colors
    plt.figure(figsize = (10, 10))
    subset = stats[stats.language == "English"]
    plt.loglog(subset.length, subset.unique, "o", label="English", color="crimson")
    
    subset = stats[stats.language == "French"]
    plt.loglog(subset.length, subset.unique, "o", label="French", color="forestgreen")
    
    subset = stats[stats.language == "German"]
    plt.loglog(subset.length, subset.unique, "o", label="German", color="orange")
    
    subset = stats[stats.language == "Portuguese"]
    plt.loglog(subset.length, subset.unique, "o", label="Portuguese", color="blueviolet")
    
    plt.legend()
    plt.xlabel("Book Length")
    plt.ylabel("Number of Unique Words")
    plt.savefig("lang_plot.pdf")
