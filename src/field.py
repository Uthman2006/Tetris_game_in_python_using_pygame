import pygame
"""
Field class is used for drawing the field and dividing it to coordinates 
because program won't move on the background, but on the front.
"""
class Field:
    def __init__(self,posInDispX,posInDispY,soundEffectVolume):
        self.rows=20
        self.columns = 10
        self.cellSize=30
        self.field = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.colors = [(26,31,40),(47,230,23),(232,18,18),(226,116,17),(237,234,4),(166,0,247),(21,204,209),(13,64,216)]
        self.posInDispX=posInDispX
        self.posInDispY=posInDispY
        self.clear_line_sound=pygame.mixer.Sound("../materials/clear_line.ogg")
        self.sound_effect_volume=soundEffectVolume
        self.clear_line_sound.set_volume(self.sound_effect_volume)
    def printField(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.field[i][j],end="")
            print()
    """
    isInside function is used for checking if the object is in the field
    """
    def isInside(self,row,column):
        if row>=0 and row<self.rows and column>=0 and column<self.columns:
            return True
        return False
    """
    isEmpty function is used for checking if the particular cell in the filed is free
    """
    def isEmpty(self,row ,column):
        if self.field[row][column]==0:
            return True
        return False
    """
    isRowFull function is used for checking if the row is full.
    This function is used during the clearing of the full row and adding a point.
    """
    def isRowFull(self,row):
        for col in range(self.columns):
            if self.field[row][col] == 0:
                return False
        return True
    """
    clearRow function is used for clearing the full rows.
    """
    def clearRow(self,row):
        for col in range(self.columns):
            self.field[row][col] =0
    """
    moveRowDown function is used for moving the row down after clearing the full rows
    """
    def moveRowDown(self,row, numRows):
        for col in range(self.columns):
            self.field[row+numRows][col]=self.field[row][col]
            self.field[row][col]=0
    """
    clearFullRows function is the main function used for clearing the full rows.
    This function checks the full rows and clears it and moves the rows down
    """
    def clearFullRows(self):
        completed=0
        for i in range(self.rows-1,0,-1):
            if self.isRowFull(i):
                self.clear_line_sound.play(loops=0)
                self.clearRow(i)
                completed+=1
            elif completed>0:
                self.moveRowDown(i,completed)
        return completed
    """
    draw function is used to draw the agme field.
    """
    def draw(self,screen):
        for i in range(self.rows):
            for j in range(self.columns):
                cellNum = self.field[i][j]
                cellRect = pygame.Rect(j*self.cellSize+self.posInDispX+1,i*self.cellSize+self.posInDispY+1,self.cellSize-1,self.cellSize-1)
                pygame.draw.rect(screen,self.colors[cellNum],cellRect)
    """
    reset function is used to reset the field.
    If the player loses the game, this function will clear the field.
    """
    def reset(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.field[i][j]=0