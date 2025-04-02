import arcade

class Game(arcade.Window):
    def __init__(self, W_W, W_H, TITLE):
        super().__init__(W_W, W_H, TITLE)

    def setup(self, tile_map, tile_size, tile_texturemap):

        '''storing input parameters'''
        self.tile_map=tile_map # a 2d list of the tiles
        self.tile_texturemap=tile_texturemap # a dictionary, key is number on the tilemap, value is image location
        self.tile_count=(len(tile_map), len(tile_map[0])) # as 0, 0 is 0, 0, the formatting works, just that we have to view the map when creating it sideways
        self.tile_size=tile_size #how many pixels wide/tall per tile
    
        '''defining global constants'''
        self.dormant_sprites = arcade.SpriteList(True) #non-moving "sprites"
        self.camera_coordinate = (0, 0) #where the center of the screen is looking at on the tile_map relative to its center

        '''actual setup'''
        self.dormant_sprites.append(self.render_tile_map()) # render tilemap DONE
        # render towers
        # render enemies
        # render shop - includes additional gui


    def render_tile_map(self):
        tile_sprites = arcade.SpriteList(True)
        base_coordinates = (
                    -self.camera_coordinate[0] + 0.5*(self.width-self.tile_size*self.tile_count[0]),
                    -self.camera_coordinate[1] + 0.5*(self.height-self.tile_size*self.tile_count[1])
                ) #-shift + origin
        for i in range(self.tile_count[0]):
            for j in range(self.tile_count[1]):
                tile_sprites.append(arcade.BasicSprite(
                    texture=self.tile_texturemap[self.tile_map[i][j]],
                    scale=1.0,
                    center_x=base_coordinates[0]+(self.tile_size*(i+0.5)),
                    center_y=base_coordinates[1]+(self.tile_size*(j+0.5))
                )) # centers = new origin + relative location
        return tile_sprites

    def render_towers(self):
        pass
    
    def render_enemies(self):
        pass

    def render_shop(self):
        pass





        
