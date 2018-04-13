import nltk
nltk.download('abc')
nltk.download('genesis')
nltk.download('webtext')
nltk.download('gutenberg')
nltk.download('state_union')
nltk.download('inaugural')

print("I bet I can read your mind")
print("Choose a word for me to guess and keep it in your head!")


subject = input("what subject is your word?: a. Gutenberg b. Websites c. Speech d. State e. genesis f. Something else ")
start_word = input("what is the first word that comes to mind when you think of your word? ")
word_guessed = False
i=0

if subject == "a":
    while word_guessed == False:
        if nltk.corpus.gutenberg.words()[i] == start_word:
            print(nltk.corpus.gutenberg.words()[i+1])
            correct= input("Is that your word?")
            if correct == "yes":
                word_guessed = True
                print("I read your mind!")
        i+=1
elif subject == "b":
    while word_guessed == False:
        if nltk.corpus.webtext.words()[i] == start_word:
            print(nltk.corpus.webtext.words()[i+1])
            correct= input("Is that your word?")
            if correct == "yes":
                word_guessed = True
                print("I read your mind!")
        i+=1
elif subject == "c":
    while word_guessed == False:
        if nltk.inaugural.abc.words()[i] == start_word:
            print(nltk.corpus.inaugural.words()[i+1])
            correct= input("Is that your word?")
            if correct == "yes":
                word_guessed = True
                print("I read your mind!")
        i+=1
elif subject == "d":
    while word_guessed == False:
        if nltk.corpus.state_union.words()[i] == start_word:
            print(nltk.corpus.state_union.words()[i+1])
            correct= input("Is that your word?")
            if correct == "yes":
                word_guessed = True
                print("I read your mind!")
        i+=1
elif subject == "e":
    while word_guessed == False:
        if nltk.corpus.genesis.words()[i] == start_word:
            print(nltk.corpus.genesis.words()[i+1])
            correct= input("Is that your word?")
            if correct == "yes":
                word_guessed = True
                print("I read your mind!")
        i+=1
elif subject == "f":
    while word_guessed == False:
        if nltk.corpus.abc.words()[i] == start_word:
            print(nltk.corpus.abc.words()[i+1])
            correct= input("Is that your word?")
            if correct == "yes":
                word_guessed = True
                print("I read your mind!")
        i+=1