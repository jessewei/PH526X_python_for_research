def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

if __name__ == "__main__":
    text = read_book("romeojuliet.txt")
    print("Length of Romeo & Juliet is: ", len(text))
    
    index = text.find("What's in a name?")
    print("Index of 'What's in a name' is: ", index)
    
    sample = text[index : index + 1000]
    print(sample)
