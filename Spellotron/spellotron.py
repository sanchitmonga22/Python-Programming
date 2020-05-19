####################
"""
SPELLOTRON- The Spelling Corrector
"""
"""
Project CS-141
Creator: Sanchit Monga
This is an Autocorrect program which tries to correct the words you type by performing the given tasks
"""
####################
import sys
import time
LEGAL_WORD_FILE = "american-english.txt"
KEY_ADJACENCY_FILE = "keyboard-letters.txt"

def check(word, lst):
    if word in lst:# checks if word is in the list
            return True
    return False

def search(word, lst):
    if word[0].isupper():
        return lst[0:16482]
    elif word[0].islower():
        return lst[16483:99153]
    else:
        return lst[99154:]

def check1(word, lst):
    """
        This function uses binary search to check whether the word is in the dictionary or not
        :param word:Word that is to be checked
        :param lst: The list of correct words from the dictionary
        :return: returns true if the word is present in the list else it returns false
    """
    if bin_search(word, lst, 0, len(lst) - 1):
        return True
    return False

def bin_search(word, lst, front, back):
    if front > back:
        return False
    else:
        mid = (front + back) // 2
        if word == lst[mid]:
            return True
        elif word > lst[mid]:
            return bin_search(word, lst, mid + 1, back)
        elif word < lst[mid]:
            return bin_search(word, lst, front, mid - 1)

def remove(word, lst1):
    """
    remove a letter and check whether the illegal word makes any sense or not and returns the correct word
    :param word: The word that has to be corrected
    :param lst1: The list of correct words from the dictionary
    :return: it removes letter from the existing word and returns true and the corrected word if there exists a word in the dictionary
    """
    lst = probable2(len(word)-1, lst1)  # storing the list of words with the same length that has to be checked for
    for j in range(len(word)):  # iterating though each letter
        r = word[0:j] + word[j+1:]  # removing each letter and then making a new word
        if check(r, lst):  # if the new word matches the word in the dictionary
            return True, r  # returning True if the word is found and returing the corrected word
    return False, ""  # returning false and returning empty string

def add(word, lst1):
    """
    adds a letter and check whether the word makes any sense or not
    :param lst1: The list of correct words in the dictionary
    :param word: The words that has to be checked
    :return:it adds a letter and checks whether the word exists in the list and returns true if it does
    """
    lst = probable2(len(word) + 1, lst1)  # storing the list of words with the same length that has to be checked for
    for k in range(26):  # iterating through all the aplhabets
        for j in range(len(word) + 1):  # iterating through the length of the word
            r = word[0:j] + chr(k + 97) + word[j:]  # adding a new aplhabet and making a new word
            if check(r, lst):  # if the new word is in the dictionary
                return True, r  # returns true along with the corrected word
    return False, ""  # returns false if the word could not be corrected and returns an empty string

def replace_with_adjacent(dct, word, lst):
    """
    This function replaces a letter with its adjacent keys and checks whether the word makes any sense or not
    :param dct:dictionary containing the letters and its adjacent letters
    :param word: word that is to be corrected
    :param lst:lst of all the correct words in the dictionary
    :return:returns true along with the corrected word if the word was corrected
    """
    l = probable2(len(word), lst)  # storing the list of probable words
    for i in range(len(word)):  # iterating through each character of the word
        for new_word in l:  # iterating through the length of the word
            if (ord(word[i]) < 97 or ord(word[i]) > 122):  # if the word is not a lower case alphabet
                break
            else:  # only if the given character is a lower case alphabet
                b = new_word[i] in dct[word[i]]  # checks whether the letter is found in the list of adjacent letters to the key
                if word[i] != new_word[i] and b and word[0:i] == new_word[0:i] and word[i + 1:] == new_word[i + 1:]:  # if the word is not same and only and only one letter of the word does not match
                    b = False
                    return True, new_word  # returns the corrected word
    return False, ""

def probable(word,lst):  # checks all the words in the dictionary and whether the word is in the dictionary and all the same letters except one of the letter
    """
    tested
    :param word:  word that has to be checked whether the word is similar to any other word in the dictionary
    :param lst:  list of words that is to be compared with
    :return: list of words that are probably the same
    """
    c = 0
    l = []
    for wd in lst:
        if len(wd) == len(word):
            for i in range(len(wd)):
                if wd[i] != word[i]:
                    c += 1
            if c == 1:
                l.append(wd)
                c = 0
    return l

def probable2(len1, lst):
    """
    checks and returns the words with the similar length
    :param len1: Length of the word that has to be returned
    :param lst: the list that has to be checked from
    :return:Returns a list of words that have the same length as len1
    """
    l1 = []
    for i in lst:
        if len(i) == len1:  # checking whether the word has the same length or not
            l1.append(i)
    return l1

def create_adjacent_dictionary(filename):
    """
    initializes the dictionary with the alphabets as the key and the adjacent keystrokes as the value of the dictionary
    :param filename:file that contains the information for the adjacent key
    :return:returns a dictionary that has the values of adjacent keystrokes
    """
    d = {}  # empty dictionary
    for line in filename:
        lis = line.strip().split()  # removing any extra spaces from front and back and separating the words and storing them into the list
        d[lis[0]] = lis[1:]  # key: alphabets and value: is the list containing the adjacent keystrokes to the alphabet
    return d  # returning the dictionary

def pun2(char):
    """
    This is a helper function and returns whether the given character is a character other than a alphabet or not
    :param char:character that has to be checked
    :return: boolean value
    """
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):  # returns false if the given character is an alphabet
        return False
    else:
        return True

def punctuation(word):
    """
    for removing the punctuation from the front and end and returning it back
    :param word: the word whose punctuation has to be removed
    :return: the punctuations along with the word with the punctuations removed
    """
    if word[-1] == " ":# because everytime a user types the input there is a space at the end of the last word
        word1 = word[0:-1]
    else:# if there is no space at the end
        word1 = word
    c = len(word1) - 1  # index from the back
    d = 0  # index from the front
    if len(word1) == 1:
        return word1, "", ""  # returns the word along empty strings
    while True:
        if c > d:
            if pun2(word1[d]) and pun2(word1[c]):  # the given word has a punctuation in front and at the end
                d += 1  # updating the front index
                c -= 1  # updating the back index
            elif pun2(word1[d]):  # the given word has the punctuation in the front
                d += 1  # updating the front index
            elif pun2(word1[c]):  # the given word has the punctuation at the end
                c -= 1  # updating the back index
            else:  # if the word has no punctuation
                break
        elif c == d:# if there is only character to be checked
            if pun2(word1[c]):# if that character is a punctuation
                c += 1# so the first index is updated
                break
            else: # if the given character is not a punctuation then the loop breaks
                break
        else:# if the front index becomes greater that the back index
            c -= 1
            break
    return word1[d:c + 1], word1[0:d], word1[c + 1:]  # word,front punctuation, back punctuation

def punc_back(word, p_f, p_b):
    """
    this funtion takes the punctuations and puts them back to the front and the end like the one in the original word
    :param word:original word
    :param p_f: the punctuation in the front
    :param p_b: the punctuation in the back
    :return: returns the word fixed with the punctuations
    """
    new_word = p_f + word + p_b# joining the punctuations with the word
    return new_word

def create_list_of_words(fi):
    """
    This function creates a list of words
    :param fi: name of the file
    :return: returns the list of the words
    """
    li = []
    for word in fi:  # iterating through the words in the file
        li.append(word.strip())
    return li

def correct_words(word, d, lst):
    """
    This function tries to correct the words using the 3 algorithms
    :param word: word to be corrected
    :param d: dictioanry of adjacent keystrokes of the alphabets
    :param lst: A list containing the correct words
    :return: return 0 if the word was returned unchanged, and return 1 if the word was returned changed and was corrected, and return 2 if the word could not be corrected
    """
    b = True
    if check(word, lst):  # checking if the word is in the dictionary
        return word, 0
    else:
        b, word1 = replace_with_adjacent(d, word, lst)  # replaces the letter of the word with the adjacent letters
        if b:
            return word1, 1
        if not b:
            b, word1 = add(word, lst)  # adds a letter and check whether the word is in the list
            if b:
                return word1, 1
        if not b:
            b, word1 = remove(word, lst)  # removes a letter and then check whether the word is in the list
            if b:
                return word1, 1
        if not b:  # if the algorithm does not work then returns the original word without correcting
            return word, 2

def words(lst, dct, filen):
    """
    This function checks and prints the words of the file in the WORD format
    :param lst: list of correct words
    :param dct: dictionary including the adjacent words
    :param filen: Name of file which from which the words have to read
    """
    n = 0  # for counting the number of words
    incorrect = []
    unknown = []
    for line in open(filen):
        words = line.strip().split()  # gives us a list of all the words separated by a space
        for i in words:
            n += 1
            word, pun_f, pun_b = punctuation(i)
            word_pun = punc_back(word, pun_f, pun_b)
            if word == "":  # this happens when the given string has only characters other than the alphabets
                continue
            elif word[0].isupper():  # if it is uppercase
                if not check(word, lst):  # if it is not in the list
                    New_Word = word[0].lower() + word[1:]
                    if check(New_Word, lst):  # if the word exists in lower case then print its original form
                        continue
                    else:
                        new_word, a = correct_words(word, dct, lst)
                        new_word_pun = punc_back(new_word, pun_f, pun_b)
                        if a == 0:
                            continue
                        if a == 1:
                            incorrect.append(word_pun)
                            print(word_pun + " -> " + new_word_pun)
                        elif a == 2:
                            word1, a1 = correct_words(New_Word, dct, lst)
                            new_word2 = word1[0].upper() + word1[1:]  # corrected word in the upper case
                            word_pun1 = punc_back(new_word2, pun_f, pun_b)
                            if a1 == 0:
                                continue
                            elif a1 == 1:
                                incorrect.append(word_pun)
                                print(word_pun + " -> " + word_pun1)
                            elif a1 == 2:
                                if new_word[0].isidentifier():
                                    unknown.append(word_pun)
            else:
                new_word, a = correct_words(word, dct, lst)
                new_word_pun = punc_back(new_word, pun_f, pun_b)
                if a == 0:  # if the word exists in the dictionary
                    continue
                elif a == 1:
                    incorrect.append(word_pun)
                    print(word_pun + " -> " + new_word_pun)
                elif a == 2:
                    if new_word[0].isidentifier():
                        unknown.append(word_pun)
    print("")
    print("")# printing in the given order
    print(n, "words read from file.")
    print("")
    print(len(incorrect), "Corrected Words")
    print(incorrect)
    print("")
    print(len(unknown), "Unknown Words")
    print(unknown)

def words_for_string(lst, dct, s):
    """
    This function checks and prints the words of the file in the WORD format
    :param lst: list of correct words
    :param dct: dictionary including the adjacent words
    :param s: List of words which is to be corrected
    """
    n = 0  # for counting the number of words
    incorrect = []
    unknown = []
    for i in s:
        n += 1
        word, pun_f, pun_b = punctuation(i)
        word_pun = punc_back(word, pun_f, pun_b)
        if word == "":  # this happens when the given string has only characters other than the alphabets
            continue
        elif word[0].isupper():  # if it is uppercase
            if not check(word, lst):  # if it is not in the list
                New_Word = word[0].lower() + word[1:]
                if check(New_Word, lst):  # if the word exists in lower case then print its original form
                    continue
                else:
                    new_word, a = correct_words(word, dct, lst)
                    new_word_pun = punc_back(new_word, pun_f, pun_b)
                    if a == 0:  # if the word exists in the dictionary
                        continue
                    elif a == 1:
                        incorrect.append(word_pun)
                        print(word_pun + " -> " + new_word_pun)
                    elif a == 2:
                        word1, a1 = correct_words(New_Word, dct, lst)
                        new_word2 = word1[0].upper() + word1[1:]  # corrected word in the upper case
                        word_pun1 = punc_back(new_word2, pun_f, pun_b)
                        if a1 == 0:
                            continue
                        elif a1 == 1:
                            print(word_pun + " -> " + word_pun1)
                            incorrect.append(word_pun)
                        elif a1 == 2:
                            if new_word[0].isidentifier():
                                unknown.append(word_pun)
        else:
            new_word, a = correct_words(word, dct, lst)
            new_word_pun = punc_back(new_word, pun_f, pun_b)
            if a == 0:  # if the word exists in the dictionary
                continue
            elif a == 1:
                incorrect.append(word_pun)
                print(word_pun + " -> " + new_word_pun)
            elif a == 2:
                if new_word[0].isidentifier():
                    unknown.append(word_pun)
    print("")
    print("")# printing in the given order
    print(n, "words read from file.")
    print("")
    print(len(incorrect), "Corrected Words")
    print(incorrect)
    print("")
    print(len(unknown), "Unknown Words")
    print(unknown)

def lines(lst, dct, filen):
    """
    This function accepts the name of the file and it opens it and prints the corrected word in the LINE format
    :param lst: list of correct words
    :param dct: dictionary including the adjacent words
    :param filen: Name of the file from which the word has to be read
    """
    n = 0  # for counting the number of words
    incorrect = []
    unknown = []
    for line in open(filen):
        words = line.strip().split()  # gives us a list of all the words separated by a space
        for i in words:
            n += 1
            word, pun_f, pun_b = punctuation(i)
            word_pun = punc_back(word, pun_f, pun_b)
            if word == "":  # this happens when the given string has only characters other than the alphabets
                print(word_pun, end=" ")
            elif word[0].isupper():  # if it is uppercase
                if not check(word, lst):  # if it is not in the list
                    New_Word = word[0].lower() + word[1:]
                    if check(New_Word, lst):  # if the word exists in lower case then print its original form
                        print(word_pun, end=" ")
                    else:
                        new_word, a = correct_words(word, dct, lst)
                        new_word_pun = punc_back(new_word, pun_f, pun_b)
                        if a == 0:  # if the word exists in the dictionary
                            print(new_word_pun, end=" ")
                        elif a == 1:
                            print(new_word_pun, end=" ")
                            incorrect.append(word_pun)
                        elif a == 2:
                            word1, a1 = correct_words(New_Word, dct, lst)
                            new_word2 = word1[0].upper() + word1[1:]  # corrected word in the upper case
                            word_pun1 = punc_back(new_word2, pun_f, pun_b)
                            if a1 == 0:
                                print(word_pun, end=" ")
                            elif a1 == 1:
                                print(word_pun1, end=" ")
                                incorrect.append(word_pun)
                            elif a1 == 2:
                                print(word_pun, end=" ")
                                if new_word[0].isidentifier():
                                    unknown.append(word_pun)
                else:
                    print(word_pun, end=" ")
            else:
                new_word, a = correct_words(word, dct, lst)
                new_word_pun = punc_back(new_word, pun_f, pun_b)
                if a == 0:  # if the word exists in the dictionary
                    print(word_pun, end=" ")
                elif a == 1:
                    print(new_word_pun, end=" ")
                    incorrect.append(word_pun)
                elif a == 2:
                    print(word_pun, end=" ")
                    if new_word[0].isidentifier():
                        unknown.append(word_pun)
        print("")
    print("")# printing in the given order
    print(n, "words read from file.")
    print("")
    print(len(incorrect), "Corrected Words")
    print(incorrect)
    print("")
    print(len(unknown), "Unknown Words")
    print(unknown)

def lines_for_string(lst, dct, s):
    """
    This function accepts the name of the list of the words and prints the corrected word in the LINE format
    :param lst: list of correct words
    :param dct: dictionary including the adjacent words
    :param s: List of words which is to be corrected
    """
    n = 0  # for counting the number of words
    incorrect = []
    unknown = []
    for i in s:
        n += 1
        word, pun_f, pun_b = punctuation(i)
        word_pun = punc_back(word, pun_f, pun_b)
        if word == "":  # this happens when the given string has only characters other than the alphabets
            print(word_pun, end=" ")
        elif word[0].isupper():  # if it is uppercase
            if not check(word, lst):  # if it is not in the list
                New_Word = word[0].lower() + word[1:]
                if check(New_Word, lst):  # if the word exists in lower case then print its original form
                    print(word_pun, end=" ")
                else:
                    new_word, a = correct_words(word, dct, lst)
                    new_word_pun = punc_back(new_word, pun_f, pun_b)
                    if a == 0:  # if the word exists in the dictionary
                        print(new_word_pun, end=" ")
                    elif a == 1:
                        print(new_word_pun, end=" ")
                        incorrect.append(word_pun)
                    elif a == 2:
                        word1, a1 = correct_words(New_Word, dct, lst)
                        new_word2 = word1[0].upper() + word1[1:]  # corrected word in the upper case
                        word_pun1 = punc_back(new_word2, pun_f, pun_b)
                        if a1 == 0:
                            print(word_pun, end=" ")
                        elif a1 == 1:
                            print(word_pun1, end=" ")
                            incorrect.append(word_pun)
                        elif a1 == 2:
                            print(word_pun, end=" ")
                            if new_word[0].isidentifier():
                                unknown.append(word_pun)
            else:
                print(word_pun, end=" ")
        else:
            new_word, a = correct_words(word, dct, lst)
            new_word_pun = punc_back(new_word, pun_f, pun_b)
            if a == 0:  # if the word exists in the dictionary
                print(word_pun, end=" ")
            elif a == 1:
                print(new_word_pun, end=" ")
                incorrect.append(word_pun)
            elif a == 2:
                print(word_pun, end=" ")
                if new_word[0].isidentifier():
                    unknown.append(word_pun)
    print("")
    print("")# printing in the given order
    print(n, "words read from file.")
    print("")
    print(len(incorrect), "Corrected Words")
    print(incorrect)
    print("")
    print(len(unknown), "Unknown Words")
    print(unknown)

def split_the_string(s):
    """
    This function returns the words in the string in the form of a list
    :param s: Accepts the string
    :return: returns the list of words
    """
    s1 = s+" "
    l = []
    j = 0
    j1 = 0
    for i in s1:# iterating through the string
        j1 += 1
        if i == " ":# if there is a space
            l.append(s[j:j1])# appending the word
            j = j1
    return l# returning the list of the words

def main():
    """
    The main function invokes all the other functions and performs the required task
    It takes the user input through the command prompt
    Then runs the algorithms according to the given priorities
    """
    start = time.time()
    dct = create_adjacent_dictionary(open(KEY_ADJACENCY_FILE))  # storing the adjacent alphabets in the dictionary
    lst = create_list_of_words(open(LEGAL_WORD_FILE, encoding="UTF-8"))  # list of correct words
    if len(sys.argv) == 3:# checking if the user enters the name of the file or not
        mode = sys.argv[1]
        filen = sys.argv[2]# storing the name of the file
        if mode == "lines":# if the mode is lines
            lines(lst, dct, filen)# invoking the lines function by passing the list, dictionary and the word as the argument
        elif mode == "words":# if the mode is words
            words(lst, dct, filen)# invoking the words function by passing the list, dictionary and the word as the argument
        else:# if the input is incorrect then prints the error message
            print("Error: Enter Valid Mode")
    else:
        s = input("Enter text here: ")
        lst_of_words = split_the_string(s)# splitting the given string into the list and then passing it into other functions for the correction
        mode = sys.argv[1]
        if mode == "lines":# if the mode is lines
            lines_for_string(lst, dct, lst_of_words)# lines the words_for_string function by passing the list, dictionary and the word as the argument
        elif mode == "words":# if the mode is words
            words_for_string(lst, dct, lst_of_words)# invoking the words_for_string function by passing the list, dictionary and the word as the argument
        else:# if the input is incorrect then prints the error message
            print("Error: Enter Valid Mode")
    end = time.time()
    print(end - start)
main()

