import nltk
nltk.download('abc')

start_word = input("Pick a word: ")

for i in range(len(nltk.corpus.abc.words())):
    if nltk.corpus.abc.words()[i] == start_word:
        print(nltk.corpus.abc.words()[i:i+5])
        i+=1




