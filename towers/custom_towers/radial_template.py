import arcade
import math
from ..radial import RadialTower

class RadialTowerTemplate(RadialTower):
    def __init__(self, stage, scale):
        # the template for towers that affect things in a radius around itself indiscriminately
        super().__init__([""], # a list of image file locations for each upgrade of your tower, 0th is the shop sprite
                         [], # a list of costs for each upgrade of your tower, 0th is the initial purchase cost
                         stage, 
                         scale,
                         50, # the radius around your tower that will be affected by its effect
                         arcade.color.AERO_BLUE, # the color of the circle that appears to indicate the area of effect
                         True, # whether or not the color fades out the further away from the center
                         2 # the equivalent of "effect_multiplier", indicates how many ticks before you reapply your effect
                         )
    def interact(self, collisions):
        for entity in collisions:
            #interact with entities
            #YOU MUST WRITE THIS ONE
            pass