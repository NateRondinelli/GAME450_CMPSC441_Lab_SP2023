""" Create PyGameAIPlayer class here"""
import random
import pygame
from pathlib import Path
import sys
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab11.turn_combat import CombatPlayer

class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            return ord(str(random.randint(0,9)))
        return ord(str(state.current_city))  # Not a safe operation for >10 cities

""" Create PyGameAICombatPlayer class here"""

class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        #while True:
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #pygame.quit()
                self.weapon = random.randint(0,2)
                return self.weapon
            