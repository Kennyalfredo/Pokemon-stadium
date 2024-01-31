
import math
import random as rd
from main import pokemons, pokemon_moves, moves_prop

pokemonRocket = rd.choices(pokemons, k=3)
pokemonTeam = rd.choices(pokemons, k=3)

def Welcome():
    print("Welcome to Pokemon Colosseum!")
    PlayerName=input("Enter player name: ")
    print("Team Rocket enters with " +pokemonRocket[0].name+" "+ pokemonRocket[1].name+" "+ pokemonRocket[2].name)
    Teams=["Rocket"]
    print("Team "+PlayerName+" enters with "+pokemonTeam[0].name+" "+pokemonTeam[1].name+" "+pokemonTeam[2].name)
    Teams.append(PlayerName)
    print("Let the battle begin!")
    return Teams

def Battle(teams):
    first=rd.choice(teams)
    print("Coin toss goes to ----- Team " + first)
    val=True
    while(val):
        while first== "Rocket":
            attack(pokemonRocket[0],pokemonTeam[0])
            if int(pokemonTeam[0].HP) == 0:
                print("Now "+ pokemonTeam[0].name+ " faints back to poke ball, and "+ pokemonRocket[0].name+ " has "+ str(pokemonRocket[0].HP))
                del pokemonTeam[0]
                """pokemonTeam[0]=pokemonTeam[1]
                pokemonTeam[1]=pokemonTeam[2]"""
                if(len(pokemonTeam)==0):
                    print("All of Team "+teams[1]+" Pokemon fainted, and Team Rocket prevails!")
                    val=False
                print("Now for Team " + teams[1] + ", " + pokemonTeam[0].name + " enters to battle !! ")
            first=teams[1]

        while first==teams[1]:
            for k in pokemon_moves:
                if k==pokemonTeam[0].name:
                    for index,value in enumerate(pokemon_moves[k],start=1):
                        print(index,value)
                    attack_chosen = int(input("Choose the move for " + pokemonTeam[0].name + ":"))
                    for index1,value2 in enumerate(pokemon_moves[k],start=1):
                        moves_ava=pokemon_moves[k]
                        if attack_chosen==index1:
                            attack2(pokemonTeam[0],pokemonRocket[0],value2)
                            moves_ava.remove(value2)
            if int(pokemonRocket[0].HP) == 0:
                print("Now " + pokemonRocket[0].name + " faints back to poke ball, and " + pokemonTeam[0].name + " has " + str(pokemonTeam[0].HP))
                del pokemonRocket[0]
                if(len(pokemonRocket)==0):
                    print("All of Team Rocket's Pokemon fainted, and Team Rocket prevails!")
                    val=False
                print("Now for Team Rocket, " + pokemonRocket[0].name + " enters to battle !! ")
            first="Rocket"



def attack(attacker,opponent):
    att = chooseAttack(attacker.name)
    print(attacker.name + " " + " cast " + att + " to " + opponent.name)
    damage_done=damage(att,attacker,opponent)
    print("Damage to " + opponent.name + " is "+ str(damage_done))
    opponent.HP= int(opponent.HP) - int(damage_done)
    if opponent.HP<0:
        opponent.HP=0
    print("Now " + attacker.name + " has " + str(attacker.HP) + " ,and " + opponent.name + " has " + str(
            opponent.HP))

def attack2(attacker, opponent, attack):
    print(attacker.name + " " + " cast " + attack + " to " + opponent.name)
    damage_done=damage(attack,attacker,opponent)
    print("Damage to " + opponent.name + " is "+ str(damage_done))
    opponent.HP= int(opponent.HP) - int(damage_done)
    if opponent.HP<0:
        opponent.HP=0
    print("Now " + attacker.name + " has " + str(attacker.HP) + " ,and " + opponent.name + " has " + str(
            opponent.HP))
def chooseAttack(poke):
        for r in pokemon_moves:
            if (r == poke):
                moves_available=pokemon_moves[r]
                attack = rd.choice(moves_available)
                moves_available.remove(attack)
        return attack

def damage(attack, attacker, opponent):
    atta = int(attacker.attack)
    deff = int(opponent.defense)
    for i in moves_prop:
        for j in i:
            if i[0]==attack:
                power=int(i[5])
                attackType=i[1]

    if(attacker.type==attackType):
        Stab=1.5
    else:
        Stab=1

    if (attacker.type == opponent.type):
        temb = 0.5
    elif(attacker.type=="Normal" or opponent.type=="Normal"):
        temb=1
    elif(attacker.type=="Water" and opponent.type=="Fire"):
        temb=2
    elif(attacker.type=="Grass" and opponent.type=="Fire"):
        temb=0.5
    elif(attacker.type=="Electric" and opponent.type=="Fire"):
        temb=1
    elif(attacker.type=="Fire" and opponent.type=="Water"):
        temb=0.5
    elif(attacker.type=="Electric" and opponent.type=="Water"):
        temb=2
    elif(attacker.type=="Grass" and opponent.type=="Water"):
        temb=2
    elif(attacker.type=="Fire" and opponent.type=="Electric"):
        temb=1
    elif(attacker.type=="Water" and opponent.type=="Electric"):
        temb=0.5
    elif (attacker.type == "Grass" and opponent.type == "Electric"):
        temb=1
    elif (attacker.type == "Fire" and opponent.type == "Grass"):
        temb=2
    elif (attacker.type == "Water" and opponent.type == "Grass"):
        temb=0.5
    elif (attacker.type == "Electric" and opponent.type == "Grass"):
        temb=0.5
    else:
        temb=1

    randomVal=rd.uniform(0.5,1)

    totalDamage=power*(atta/deff)*Stab*temb*randomVal
    return math.ceil(totalDamage)




equipos=Welcome()
Battle(equipos)