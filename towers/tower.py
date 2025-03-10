import arcade
import math
from enum import Enum, auto

class TCat(Enum):
    Projectile = auto()
    Radial = auto()
    Absolute = auto()

class Tower(arcade.BasicSprite):
    def __init__(self, image_list, cost_list, stage, scale, cat: TCat):

        super().__init__(image_list[stage], scale=scale)

        self.name: str
        self.category = cat

        self.image_list = image_list #first sprite is the shop sprite
        self.scale = scale
        self.cost_list = cost_list #first cost is the shop price

        # Tower Stage
        self.stage = stage #starts at 1 when placed, only 0 when in shop
        self.max_stage = len(image_list)
        self.maxxed = self.stage == self.max_stage

        # Tower instance
        #location is center_x and center_y from super

    
    def __str__(self):
        return self.name
    
    def place(self, x, y):
        self.center_x = x
        self.center_y = y

    def upgrade(self):
        if not self.maxxed:
            self.stage += 1
            self.maxxed = self.stage == self.max_stage
        return not self.maxxed
    
    def shop_description(self):
        self.shop_description = [
            f"{self.category.name} Tower", #this line is for tower type
            "", #this line is for stats -- like damage or slowing percentage
            "", # more stats -- like attack speed, radius, or damage tick
            "" # extra text lol
        ]
    
    def salvage(self):
        super().kill()

