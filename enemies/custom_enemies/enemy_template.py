import arcade
import math
from ..enemy import Enemy

class EnemyName(Enemy):
    
    def __init__(self, target_entity):
        super().__init__("file/path/to/image", #in the string write the file path to your image relative to this project
                         1.0,  # the scale that is needed to be applied to this image to be of tile size
                         target_entity,
                         10, #how much damage you will deal to the play if you reach the end
                         5, #from the center of your entity, how many pixels away will your enemy be considered to have reached the end
                         2, #how many times the standard speed your thing is
                         50 # hitpoints
                         )

    def update(self, entity_list):
        super().update(entity_list)

        #add extra functionality here if needs be, like buffing nearby enemies etc.

    def kill(self):
        # add extra functionality if needs be, like explosion
        super().kill()