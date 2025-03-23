import arcade
import math
from ..absolute import AbsoluteTower

class AbsoluteTowerTemplate(AbsoluteTower):
    def __init__(self, stage, scale, effect_multiplier):
        # the tower that interacts with any position on a map indiscriminate of where it is located
        super().__init__([""], # a list of image file locations for each upgrade of your tower, 0th is the shop sprite
                         [], # a list of costs for each upgrade of your tower, 0th is the initial purchase cost
                         stage,
                         scale, 
                         20, # when your attack hits the map, the radius around that point that will be affected
                         arcade.color.RED_DEVIL, #when your attack hits the map, the color that of the circle that will be drawn to indicate a successful attack
                         True, #will the above color fade our as it moves away from the center of your attack
                         effect_multiplier,
                         1000, # the amount of pixels to the left and right of the placed tower will be considered within range (big number is good)
                         1000, # the amount of pixels up and below of the placed tower will be considered within range (big number good)
                         2000 # the number of game ticks between each attempt of interaction
                         )

    def interact(self, x, y, collisions):
        #x and y are target coordinates
        # this overrides AbsoluteTower.interact()
        for entity in collisions:
            #interact with entities
            pass

    def choose_position(self, bounding_box):
        # this overrides AbsoluteTower.choose_position()
        #returns absolute x and y coordinate to be used in interact
        pass