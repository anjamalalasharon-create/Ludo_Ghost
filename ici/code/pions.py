import pygame


class Ghost:
    def __init__(self, color_name,color_type, image, start_pos):
        self.color_name = color_name
        self.color_type = color_type
        self.image = image
        self.grid_pos = start_pos 
        self.start_pos = start_pos
        self.is_home = True
        self.path_index = -1
        
        
    def draw(self, screen, CASE_SIZE, X, Y):
        x = X + self.grid_pos[1] * CASE_SIZE + (CASE_SIZE - self.image.get_width()) // 2
        y = Y + self.grid_pos[0] * CASE_SIZE + (CASE_SIZE - self.image.get_height()) // 2
        screen.blit(self.image, (x, y))


    def move(self, steps, full_path):
        
        if self.is_home:
            if steps == 6: 
                self.is_home = False
                self.path_index = 0
        else:
            self.path_index += steps
            if self.path_index >= len(full_path):
                self.path_index = len(full_path) - 1
        
        if not self.is_home:
            self.grid_pos = full_path[self.path_index]

    
    