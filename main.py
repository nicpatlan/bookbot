def report_counts(path):
    text = get_book_text(path)
    word_count = count_words(text)
    letter_dict = count_letters(text)
    sorted_dict = sorted(letter_dict.items(), key=lambda k:k[1], reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for key, value in sorted_dict:
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def count_letters(text):
    letter_dict = {}
    for c in text:
        if c.isalpha():
            lower_c = c.lower()
            letter_dict[lower_c] = letter_dict.get(lower_c, 0) + 1

    return letter_dict

def count_words(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"
    report_counts(path)

main()