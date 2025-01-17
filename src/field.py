import pygame
class Field:
    def __init__(self,posInDispX,posInDispY):
        self.rows=20
        self.columns = 10
        self.cellSize=30
        self.field = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.colors = [(26,31,40),(47,230,23),(232,18,18),(226,116,17),(237,234,4),(166,0,247),(21,204,209),(13,64,216)]
        self.posInDispX=posInDispX
        self.posInDispY=posInDispY
    def printField(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.field[i][j],end="")
            print()
    def isInside(self,row,column):
        if row>=0 and row<self.rows and column>=0 and column<self.columns:
            return True
        return False
    def isEmpty(self,row ,column):
        if self.field[row][column]==0:
            return True
        return False
    def draw(self,screen):
        for i in range(self.rows):
            for j in range(self.columns):
                cellNum = self.field[i][j]
                cellRect = pygame.Rect(j*self.cellSize+self.posInDispX+1,i*self.cellSize+self.posInDispY+1,self.cellSize-1,self.cellSize-1)
                pygame.draw.rect(screen,self.colors[cellNum],cellRect)