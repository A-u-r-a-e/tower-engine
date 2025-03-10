import arcade
import math
from ..radial import RadialTower

class RadialTowerTemplate(RadialTower):
    def __init__(self, stage):
        # image_list, cost_list, stage, scale, radius, aoe_color, aoe_fade, tick_rate
        super().__init__([""], [], stage, 1.0, 50, arcade.color.AERO_BLUE, True, 2)
    def interact(self, collisions):
        for entity in collisions:
            #interact with entities
            pass