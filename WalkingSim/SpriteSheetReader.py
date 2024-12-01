import pygame

BLACK = (0, 0, 0)

class SpriteSheet(object): 
    def __init__(self, file_name): 
        try:
            self.sprite_sheet = pygame.image.load(file_name).convert()
        except pygame.error:
            print("Could not load Image!")

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)
        return image
    
    # helper func - makes an array from sprite sheet
    def make_sprite_array(self, x, y, width, height, numImages, imgPerRow):
        spriteList = []
        imgInRowCount = 0
        for i in range(numImages):
            imgInRowCount += 1
            image = self.get_image(x,y,width,height)
            spriteList.append(image)
            
            # grab images in row
            if(imgInRowCount < imgPerRow):
                x += width
            # move down a colm and start at beginning of row
            if(imgInRowCount >= imgPerRow):
                y += height
                x = 0
                imgInRowCount = 0
            
        return spriteList