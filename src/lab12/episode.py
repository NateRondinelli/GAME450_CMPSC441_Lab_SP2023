''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab11.pygame_ai_player import PyGameAICombatPlayer
from lab11.pygame_combat import PyGameComputerCombatPlayer, run_turn
from lab11.turn_combat import Combat


def run_episode(player1,player2):
    players = [player1,player2]
    episode = Combat()
    history = []

    while not episode.gameOver:
        observation = tuple(player.health for player in players)
        reward = run_turn(episode,player1,player2)
        history.append((observation,player1.weapon,reward))
    return history

if __name__ =="__main__":
    p1 = PyGameAICombatPlayer("p1")
    p2 = PyGameComputerCombatPlayer("p2")
    print(run_episode(p1,p2))
    