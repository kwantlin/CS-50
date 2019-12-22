from cs50 import get_string

# main function here
def main():
# take text input
    text = get_string("Text: ")

    # count letters, words, and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    #calculated variables
    L = float(letters) / float(words) * 100
    S = float(sentences) / float(words) * 100
    index = float(0.0588 * L - 0.296 * S - 15.8)
    # edge case for below grade 1
    if index < 1:
        print("Before Grade 1", end = "\n")
    # edge case for able grade 16
    elif index > 16:
        print("Grade 16+", end = "\n")
    # main case
    else:
        print("Grade " + str(int(round(index))))

# helper function to count letters
def count_letters(text):
    # check if each character has ascii number corresponding to a letter
    count = 0
    for i in text:
        if ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
            count += 1
    return count

# helper function to count words
def count_words(s):
    # count one word after encountering a space
    count = 0
    for i in s:
        if i == " ":
            count += 1
    # by the given rules, there will be one additional word after the last space
    count += 1
    return count

# helper function to count sentences
def count_sentences(s):
    # after encountering an ending punctuation, you know you just read through one sentence
    count = 0
    for i in s:
        if (i == '.' or i == '!' or i == '?'):
            count += 1
    return count

# call main function
main()


