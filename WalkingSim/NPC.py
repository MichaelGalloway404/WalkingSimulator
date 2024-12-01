import pygame, random, SpriteSheetReader

class Human(pygame.sprite.Sprite):
    def __init__(self,SSPath, speed):
        super().__init__()
        
        sprite_sheet = SpriteSheetReader.SpriteSheet(SSPath)
        
        #                                         x,y,width,height,numImages,imgPerRow
        self.spriteMap = sprite_sheet.make_sprite_array(0,0,32,32,24,3)

        self.image = self.spriteMap[0]
            
        self.rect = self.image.get_rect()
        self.speedX = speed
        self.speedY = speed

        self.change_x = 0
        self.change_y = 0
        
        self.direction = "DOWN"

        self.frame_itter = 0
        
        # random max time to wait until change of direction
        self.changeDir = random.randrange(50,100) 
        self.inc = 0 # time until change in direction
        self.DirList = ['LEFT','RIGHT','UP','DOWN']
        
    def update(self):
        self.frame_itter += 1
        
        self.rect.x += self.change_x  
        self.rect.y += self.change_y
        
        self.move(self.direction)
            
    def move(self, direction):
        # each movement animation only has three frames
        numFrames = 3
        
        #DOWN    
        if direction == 'DOWN':
            self.change_x = 0
            self.change_y = self.speedY
            frame = ((self.frame_itter // 10) % numFrames) + 0 # offset for sprite sheet
            self.image = self.spriteMap[frame]
            self.direction = direction
            
        #RIGHT
        if direction == 'RIGHT':
            self.change_x = self.speedX
            self.change_y = 0
            frame = ((self.frame_itter // 10) % numFrames) + 3 # offset for sprite sheet
            self.image = self.spriteMap[frame]
            self.direction = direction
        
        #UP
        if direction == 'UP':
            self.change_x = 0
            self.change_y = -self.speedY
            frame = ((self.frame_itter // 10) % numFrames) + 6 # offset for sprite sheet
            self.image = self.spriteMap[frame]
            self.direction = direction
            
        #LEFT
        if direction == 'LEFT':
            self.change_x = -self.speedX
            self.change_y = 0
            frame = ((self.frame_itter // 10) % numFrames) + 9 # offset for sprite sheet
            self.image = self.spriteMap[frame]
            self.direction = direction
            
        #NONE
        if direction == 'NONE':
            self.change_x = 0
            self.change_y = 0
            self.image = self.spriteMap[1]
            self.direction = direction
            
            
    def wanderAround(self, minDim, maxDim):
        # boundaries so sprite does not go off screen
        if(self.rect.x+self.rect.width > maxDim[0]):
            self.direction = 'LEFT'
        if(self.rect.x < minDim[0]):
            self.direction = 'RIGHT'
        if(self.rect.y+self.rect.height > maxDim[1]):
            self.direction = 'UP'
        if(self.rect.y < minDim[0]):
            self.direction = 'DOWN'

        self.inc += 1
        # change direction, reset timer, and choose new max decision window
        if(self.inc >= self.changeDir):
            self.direction = self.DirList[random.randrange(0,3)]
            self.changeDir = random.randrange(50,100)
            self.inc = 0


