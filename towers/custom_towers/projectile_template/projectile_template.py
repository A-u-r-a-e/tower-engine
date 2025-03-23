import arcade
import math
from ...projectile import ProjectileTower, Projectile

class ProjectileTemplate(Projectile): #change ProjectileTemplate to your TOWERNAMEProjectile, and change it in the Tower class definition accordingly
    def __init__(self, dx, dy, effect_multiplier, bounding_box):
        # image, scale, base_effect, effect_multiplier, dx, dy, bounding_box
        super().__init__("", #the image file name of your projectile
                         1.0, #the scale that you want to multiply your projectile image by when it is rendered
                         10, # the amount of damage/effect that your projectile does upon impact
                         effect_multiplier, 
                         dx, 
                         dy, 
                         bounding_box)
    def interact(self, collisions):
        for entity in collisions:
            # interact with each entity
            # you only need to change this if you want to
            pass

class ProjectileTowerTemplate(ProjectileTower):
    def __init__(self, stage, scale, effect_multiplier):
        # the template for the tower that shoots out projectiles within a certain range
        super().__init__([""],  # a list of image file names for each upgrade of your tower, 0th is the shop sprite
                         [], # a list of costs for each upgrade of your tower, 0th is the initial purchase cost
                         stage, 
                         scale, 
                         ProjectileTemplate, #change this to be of the name of your projectile defined above
                         effect_multiplier, 
                         600, # how many pixels is the radius of your aiming range
                         20, # the speed that your projectile travels at once launched
                         60 # the number of game ticks between each projectile fire
                         )
    def find_target(self):
        #find targets, returns x, y -- distance to target point
        pass