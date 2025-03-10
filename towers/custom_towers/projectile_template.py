import arcade
import math
from projectile import ProjectileTower, Projectile

class ProjectileTemplate(Projectile):
    def __init__(self, dx, dy, effect_multiplier, bounding_box):
        # image, scale, base_effect, effect_multiplier, dx, dy, bounding_box
        super().__init__("", 1.0, 10, effect_multiplier, dx, dy, bounding_box)
    def interact(self, collisions):
        for entity in collisions:
            # interact with each entity
            # you only need to change this if you want to
            pass

class ProjectileTowerTemplate(ProjectileTower):
    def __init__(self, stage, scale, effect_multiplier):
        # image_list, cost_list, stage, scale, projectile, effect_multiplier, range: int, velocity, cooldown: int
        super().__init__([""], [], stage, scale, ProjectileTemplate, effect_multiplier, 600, 20, 60)
    def find_target(self):
        #find targets, returns x, y -- distance to target point
        pass