import arcade
import math
from absolute import AbsoluteTower

class AbsoluteTowerTemplate(AbsoluteTower):
    def __init__(self, stage, scale):
        # image_list, cost_list, stage, scale, blast_radius, blast_color, blast_fade, effect_multiplier, x_range, y_range, cooldown
        super().__init__([""], [], stage, scale, 20, arcade.color.RED_DEVIL, True, 2.0, 1000, 1000, 2000)

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