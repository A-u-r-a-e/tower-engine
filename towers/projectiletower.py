from tower import Tower, TCat
import math
import arcade

class Projectile(arcade.BasicSprite):
    def __init__(self, image, scale, effect_multiplier, dx, dy, bounding_box):
        super().__init__(image, scale=scale)

        self.dx = dx
        self.dy = dy

        self.base_effect: int
        self.effect_multiplier = effect_multiplier

        self.bounding_box = bounding_box
    def update(self, entity_list):
        self.center_x += self.dx
        self.center_y += self.dy
        collisions = self.collides_with_list(entity_list)
        if len(self.collisions) > 0:
            self.interact(collisions, self.base_effect * self.effect_multiplier)
            self.kill()
    def interact(self, collisions, amount):
        pass

class ProjectileTower(Tower):
    def __init__(self, image_list, cost_list, stage, scale, projectile, effect_multiplier, range: int):
        super().__init__(image_list, cost_list, stage, scale, cat=TCat.Projectile)

        self.projectile = projectile # a class
        self.range = range
        self.effect_multiplier = effect_multiplier
    
    def shoot(self, dx, dy):
        #returns a sprite
        
        range_ratio = self.range(math.sqrt(dx**2 + dy**2))
        bounding_box = (self.center_x, self.center_y, int(self.center_x + range_ratio*dx), int(self.center_y + range_ratio*dy))
        projectile = self.projectile(dx, dy, bounding_box, self.effect_multiplier)

        return projectile