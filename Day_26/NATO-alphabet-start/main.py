import pandas as pd
nato_data = pd.read_csv('nato_phonetic_alphabet.csv')
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
First_try = { row.letter : row.code for (index,row) in nato_data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter a word : ').upper()
list_user = [ First_try[letter] for letter in user_input ]
print(list_user)
