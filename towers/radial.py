from tower import Tower, TCat
import math
import arcade

class RadialTower(Tower):
    
    def __init__(self, image_list, cost_list, stage, scale, radius: int, aoe_color, aoe_fade: bool, tick_rate: int):
        super().__init__(image_list, cost_list, stage, scale, TCat.Radial)
        
        self.circle = arcade.SpriteCircle(radius, aoe_color, aoe_fade) # in pixels
        self.circle.visible = False
        

        self.tick_rate = tick_rate # frames between ticks
        self.current_tick = tick_rate

    def update(self, entity_list):
        if self.stage != 0:

            self.circle.center_x = self.center_x
            self.circle.center_y = self.center_y

            collision_list = self.circle.collides_with_list(entity_list)
            if len(collision_list) > 0:
                self.circle.visible = True
                if self.current_tick <= 0:
                    self.interact(collision_list)
                    self.current_tick = self.tick_rate
            if self.current_tick > 0:
                self.current_tick -= 1

    def interact(self, collisions):
        for entity in collisions:
            #interact with entities
            pass


