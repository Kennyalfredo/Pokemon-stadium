Pokemon Colosseum Battle Simulator
This Python script simulates a battle in the Pokemon Colosseum between Team Rocket and the Player's team. It randomly selects Pokemon for each team and conducts the battle with moves and damage calculations.

Code Overview
The code performs the following steps:

Initialization: It imports necessary modules (math and random) and imports data about Pokemon, their moves, and move properties from main.

Team Selection: It randomly selects three Pokemon for Team Rocket (pokemonRocket) and three Pokemon for the Player's team (pokemonTeam).

Welcome Function: The Welcome() function greets the player, prompts for their name, and introduces the teams for the battle.

Battle Function: The Battle(teams) function initiates the battle. It starts with a coin toss to determine which team attacks first. Then, it iterates through turns until one team's Pokemon faints. It also handles move selection and damage calculation.

Attack Functions: These functions handle the attack logic, move selection, and damage calculation.

Damage Calculation: The damage() function calculates the damage inflicted by an attack based on various factors like attack type, opponent's type, and random factors.

Move Selection: The chooseAttack(poke) function randomly selects a move for a Pokemon from its available moves.

Usage
To use this script, simply run it in a Python environment. It will prompt you to enter your name and simulate a battle between Team Rocket and your team.

Feel free to modify the code and add additional features as needed!

Note: Ensure that the necessary data about Pokemon and moves is available in the main module for the script to work correctly.

Author: Kenny Aranda

Date: 1/31/2024