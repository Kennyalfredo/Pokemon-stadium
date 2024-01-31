import ast
import csv

from Pokemon import Pokemon
header = []
pokemon_moves = {} #List of moves
pokemons = [] #List of pokemons
moves_prop=[]
def readAndCreate():
    pokemon_filename = 'pokemon-data.csv'

    with open(pokemon_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        for row in reader:
            moves = ''
            end_of_moves = False
            pokemons.append(Pokemon(row[0], row[1], row[2], row[3], row[4], row[7]))
            for s in row:
                if s[0] == '[':
                    end_of_moves = True
                    moves = s
                elif end_of_moves == True:
                    moves += ',' + s
                    if s[-1] == ']':
                        end_of_moves = False
            # print(moves)
            pokemon_moves[row[0]] = ast.literal_eval(moves)  # string to list
    print(pokemon_moves)



def getProp():

    with open('moves-data.csv', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            moves_prop.append(row)
    print(moves_prop)
    return moves_prop


readAndCreate()
getProp()