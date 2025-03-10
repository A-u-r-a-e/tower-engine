from tower import Tower, TCat
import math
import arcade

class Projectile(arcade.BasicSprite):
    def __init__(self, image, scale, base_effect, effect_multiplier, dx, dy, bounding_box):
        super().__init__(image, scale=scale)

        self.dx = dx
        self.dy = dy

        self.base_effect = base_effect
        self.effect_multiplier = effect_multiplier

        self.bounding_box = bounding_box
    def update(self, entity_list):
        self.center_x += self.dx
        self.center_y += self.dy
        collisions = self.collides_with_list(entity_list)
        if len(self.collisions) > 0:
            self.interact(collisions)
            self.kill()
    def interact(self, collisions):
        for entity in collisions:
            # interact with each entity
            pass

class ProjectileTower(Tower):
    def __init__(self, image_list, cost_list, stage, scale, projectile, effect_multiplier, range: int, velocity, cooldown: int):
        super().__init__(image_list, cost_list, stage, scale, cat=TCat.Projectile)

        self.projectile = projectile # a class
        self.range = range
        self.velocity = velocity
        self.effect_multiplier = effect_multiplier


        self.cooldown = cooldown
        self.current_tick = self.cooldown

    def scale_vector(self, dx, dy, dd):
        value = dd/math.sqrt(dx**2 + dy**2)
        return int(value*dx), int(value*dy)
    
    def shoot(self, dx, dy):
        #returns a sprite

        add_x, add_y = self.scale_vector(dx, dy, self.range)
        bounding_box = (self.center_x, self.center_y, self.center_x+add_x, self.center_y+add_y)
        
        projectile = self.projectile(dx, dy, bounding_box, self.effect_multiplier)

        return projectile
    
    def find_target(self):
        #user written code, returns distance of x and y to the point
        pass

    def update(self):
        if self.stage != 0: #if it is 0, means no ai
            if self.current_tick <= 0:
                dx, dy = self.find_target()
                dx, dy = self.scale_vector(dx, dy, self.speed)
                self.shoot(dx, dy)
                self.current_tick = self.cooldown
            if self.current_tick > 0:
                self.current_tick += 1
