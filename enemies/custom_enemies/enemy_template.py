import arcade
import math
from ..enemy import Enemy

class EnemyName(Enemy):
    
    def __init__(self, target_entity):
        #image, scale, target, damage, damage_radius, speed, health
        super().__init__("file/path/to/image", 1.0, target_entity, 10, 5, 2, 50)

    def update(self, entity_list):
        super().update(entity_list)

        #add extra functionality here if needs be, like buffing nearby enemies etc.

    def kill(self):
        # add extra functionality if needs be, like explosion
        super().kill()