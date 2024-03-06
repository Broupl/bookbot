def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = count(words)
    check = letter_check(words)
    report(book,word_count,check)

def count(words):
    return len(words)

def letter_check(words):
    check = {}
    for word in words:
        word = word.lower()
        for i in range (0,len(word)):
            if word[i] not in check:
                check[word[i]] = 1
            else:
                check[word[i]] += 1
    return check

def report(book,word_count,check):
    print(f"-- Begin report of {book}--")
    print(f"{word_count} words found in the document")
    print()
    letter_list = []
    for letter in check:
        if letter.isalpha() == True:
            letter_list += [{"letter":letter,"num":check[letter]}]
    letter_list.sort(reverse=True, key=sort_on)
    for letters in letter_list:
        print(f"The '{letters["letter"]}' character was found {letters["num"]} times")
    print("--End of report--")

def sort_on(dict):
    return dict["num"]


main()