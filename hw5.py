import random

def topirate(string):
    greetings = {'hello':'avast','excuse': 'arr'}
    people =  {'sir': 'matey', 'boy': 'matey', 'man': 'matey', 'madam': 'proud beauty', 'officer': 'foul blaggard', 'friends' : 'hearties', 'daredevil' : 'swashbuckler', 'pirate flag': 'black jack'}
    articles = {'the':"th'", 'my': 'me', 'your': 'yer','is':'be','are': 'be', 'this': "this 'ere"}
    places = {'restroom':'head', 'restaurant' : 'galley', 'hotel': 'fleabag inn', 'ocean':'briney deep'}

    words = string.split()
    pirate_string = ''
    for word in words:
        if word in greetings:
            pirate_string += greetings[word] + ' '
        elif word in people:
            pirate_string += people[word] + ' '
        elif word in articles:
            pirate_string += articles[word] + ' '
        elif word in places:
            pirate_string += places[word] + ' '
        else:
            pirate_string += word + ' '
    return pirate_string

def country_data(filename):
    data = {}
    file = open(filename, "r")
    for line in file:
        country, capital = line.strip().split(',')
        data[country] = capital
    return data

def play_game(data):
    country = random.choice(list(data.keys()))
    capital = data[country]

    max_guess = 5
    num_guess = 0
    hints = 2

    while num_guesses < max_guesses:
        guess = input("what is the capital of" + country + "?")

        if guess.lower() == capital.lower():
            print('Correct!')
            return
        else:
            num_guess += 1
            if num_guess < max_guess:
                hint = capital[:hint_length]
                print("Incorrect. Here is a hint: ", hint.upper())
                hints += 2

    print("Sorry, you are out of guesses. The capital of", country, 'is', capital)

if __name__ == "__main__":
    data = country_data(country-capital.csv)

    play_game(data)





