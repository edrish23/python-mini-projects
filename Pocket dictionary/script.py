from PyDictionary import PyDictionary

dictionary = PyDictionary()

word = input("Enter a word you want to search:")
meaning = (dictionary.meaning(word))
print(meaning)
