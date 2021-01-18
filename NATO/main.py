import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = {row.letter:row.code for index, row in data.iterrows()}
def generate_nato():
    text = input("Say something: ").upper()
    try:
        code = [nato[letter] for letter in text]
    except KeyError:
        print("Sorry, alphabets only")
        generate_nato()
    else:
        print(code)

generate_nato()


