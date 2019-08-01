import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    b = True
    for s in secret_word:

        if s in letters_guessed:
            pass
        else:
            b = False

    return b
#secret_word = 'apple'
#letters_guessed = ['a','e', 'i', 'k', 'p', 'r', 's']
#print(is_word_guessed(secret_word, letters_guessed))





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    z = ""
    for s in secret_word:

        if s in letters_guessed:
            z += s
        else:
            z += "_ "
    return z
#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    import string
    a = string.ascii_lowercase
    z = list(a)
    for s in letters_guessed:
       if s in z:
        z.remove(s)
    p = "".join(z)
    return p


#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))







def hangman(secret_word):

    print("Welcome to the game hangman ! ")
    print("I am thinking of a word that is",len(secret_word),"letters long")
    warnings = 3
    guesses = 6
    letters_guessed = []
    letters_guesseda = []


    print("You have 3 warnings left")


    while not is_word_guessed(secret_word, letters_guessed) and guesses>0:
        print("--------------------")
        print("You have",guesses," guesses left")
        print("Available letters :",get_available_letters(letters_guessed))
        s = input("Please guess a letter: ")
        s = (str.lower(s))
        letters_guesseda += s


        if  s in letters_guessed :
            if warnings>0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have",warnings,"warnings left")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word, letters_guessed))

        elif s in secret_word :
            print("Good guess:",get_guessed_word(secret_word, letters_guesseda))






        elif s not in "abcdefghijklmnopqrstuvwxyz":
            if warnings>0:
                warnings -= 1
                print("Oops! not a valid letter. You have",warnings,"warnings left")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -= 1
                print("Oops! not a valid letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word, letters_guessed))
        elif s not in secret_word:
            if s in "aeiou":
                guesses -= 2
            else:
                guesses -= 1
            print("Oops! That letter is not in my word: ",get_guessed_word(secret_word, letters_guessed))

        letters_guessed += s
    print("------------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        temp = ""
        for k in secret_word:
            if k not in temp:
                temp += k
        infinitywar = len(temp)


        print("Your total score for this game is:",guesses*infinitywar)

    elif guesses <= 0:
        print("Sorry, you ran out of guesses. The word was",secret_word)




# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_list = list(my_word)
    ml = []
    b = True
    p = ""
    for x in my_list:
        if x !=" ":
            ml += x
    #ml = Without spaces (list)
    #mla Without spaces and underscores(list)

    mla= []
    for y in ml:
        if y !="_":
            mla += y

    mlas = "".join(mla)
    for z in mla:
        if z in other_word and len(ml)==len(other_word):
            pass
        else:
            b = False
    for q in other_word:
        if q not in p:
            p = p + q


    #print(p)
    #print(mlas)

    if p == mlas:
        b = False
    return(b)

#print(match_with_gaps("a_ _ le", "apple"))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    wordlist = load_words()
    my_list = list(my_word)
    ml = []
    pool = False
    for x in my_list:
        if x != " ":
            ml += x

    z = "".join(ml)

    for m in wordlist:
        if len(m) == len(z):
            s = ""
            for n in range(0, len(m)):
                if z[n] != "_":
                    s += m[n]
                elif m[n] not in z:
                    s += "_"

            if s == z:
                print(m,end=" ")
                pool = True
    if not pool:
        print("No matches Found")


#(show_possible_matches("abbbb_ "))




def hangman_with_hints(secret_word):
    print("Welcome to the game hangman ! ")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    warnings = 3
    guesses = 6
    letters_guessed = []
    letters_guesseda = []

    print("You have 3 warnings left")

    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print("--------------------")
        print("You have", guesses, " guesses left")
        print("Available letters :", get_available_letters(letters_guessed))
        s = input("Please guess a letter: ")
        s = (str.lower(s))
        letters_guesseda += s

        if s in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))

        elif s in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guesseda))
        elif s == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guesseda))





        elif s not in "abcdefghijklmnopqrstuvwxyz*":
            if warnings > 0:
                warnings -= 1
                print("Oops! not a valid letter. You have", warnings, "warnings left")
                print(get_guessed_word(secret_word, letters_guessed))
            else:
                guesses -= 1
                print("Oops! not a valid letter. You have no warnings left so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
        elif s not in secret_word:
            if s in "aeiou":
                guesses -= 2
            else:
                guesses -= 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))

        letters_guessed += s
    print("------------------")
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        temp = ""
        for k in secret_word:
            if k not in temp:
                temp += k
        infinitywar = len(temp)

        print("Your total score for this game is:", guesses * infinitywar)

    elif guesses <= 0:
        print("Sorry, you ran out of guesses. The word was", secret_word)

if __name__ == "__main__":


    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
