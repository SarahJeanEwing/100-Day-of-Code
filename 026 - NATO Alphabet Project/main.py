import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

phrase = input("Enter a word or phrase to spell phonetically: ")
words_list = phrase.split()
phonetic_words = [
    ' - '.join([nato_alphabet_dict[item.upper()] if item.isalpha() else item for item in single_word])
    for single_word in words_list
]
print()
print(f"The phonetic spelling of {phrase} is:")
print('\n'.join(phonetic_words))