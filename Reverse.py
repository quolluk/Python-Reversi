#Reverse a String - Enter a string and the program will reverse it and print it out.
def reverse_words(word):

    output = ""
    i = len(word) - 1
    for letter in word:
        output += word[i]
        i -= 1
    return(output)