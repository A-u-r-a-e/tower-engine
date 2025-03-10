from tower import Tower, TCat
import math
import arcade

class AbsoluteTower(Tower):
    def __init__(self, image_list, cost_list, stage, scale, blast_radius: int, blast_color, blast_fade: bool, effect_multiplier, x_range, y_range, cooldown):
        super().__init__(image_list, cost_list, stage, scale, cat=TCat.Absolute)

        self.blast_radius = blast_radius
        self.blast_color = blast_color
        self.blast_fade = blast_fade
        self.effect_multiplier = effect_multiplier
        
        self.cooldown = cooldown
        self.current_tick = self.cooldown

        self.x_range = x_range # x "radius"
        self.y_range = y_range # y "radius"

    def update(self, entity_list):
        if self.stage != 0:
            if self.current_tick <= 0:
                x, y = self.choose_position((self.center_x - self.x_range, self.center_y - self.y_range, self.center_x + self.x_range, self.center_y + self.y_range))
                blast = arcade.SpriteCircle(self.blast_radius, self.blast_color, soft=self.blast_fade, center_x=x, center_y=y, visible=False)
                collision_list = blast.collides_with_list(entity_list)
                if len(collision_list) > 0:
                    self.interact(x, y, collision_list)

            if self.current_tick > 0:
                self.current_tick = self.cooldown

    def interact(self, x, y, collisions):
        for entity in collisions:
            #interact with entities
            pass

    def choose_position(self, bounding_box):
        #returns absolute x and y coordinate
        pass