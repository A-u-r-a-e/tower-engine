import arcade
import math

class Enemy(arcade.BasicSprite):
    def __init__(self, image, scale, target_entity, damage, damage_radius, speed, health):
        super().__init__(image, scale=scale)

        self.speed = speed
        self.health = health
        self.damage = damage

        self.target_entity = target_entity #reference

        self.damage_radius = damage_radius

    def scale_vector(self, dx, dy, dd):
        value = dd/math.sqrt(dx**2 + dy**2)
        return int(value*dx), int(value*dy)
    
    def update(self):
        dx, dy = self.calculate_movement_vector(self.center_x, self.center_y)
        dx, dy = self.scale_vector(dx, dy, self.speed)

        self.center_x += dx
        self.center_y += dy

        damage_hitbox = arcade.SpriteCircle(self.damage_radius, arcade.color.WHITE, False, center_x = self.center_x, center_y = self.center_y)
        if damage_hitbox.collides_with_sprite(self.target_entity):
            self.interact()
            super().kill()

        if self.health <= 0:
            self.kill()
    
    def interact(self):
        #interacts with target entity
        pass

    def calculate_movement_vector(self, x, y):
        #returns dx, dy (general direction)
        pass