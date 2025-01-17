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
        self.clear_line_sound=pygame.mixer.Sound("../materials/clear_line.ogg")
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
    def isRowFull(self,row):
        for col in range(self.columns):
            if self.field[row][col] == 0:
                return False
        return True
    def clearRow(self,row):
        for col in range(self.columns):
            self.field[row][col] =0
    def moveRowDown(self,row, numRows):
        for col in range(self.columns):
            self.field[row+numRows][col]=self.field[row][col]
            self.field[row][col]=0
    def clearFullRows(self):
        completed=0
        for i in range(self.rows-1,0,-1):
            if self.isRowFull(i):
                self.clear_line_sound.play(loops=0)
                self.clear_line_sound.set_volume(1)
                self.clearRow(i)
                completed+=1
            elif completed>0:
                self.moveRowDown(i,completed)
        return completed
    def draw(self,screen):
        for i in range(self.rows):
            for j in range(self.columns):
                cellNum = self.field[i][j]
                cellRect = pygame.Rect(j*self.cellSize+self.posInDispX+1,i*self.cellSize+self.posInDispY+1,self.cellSize-1,self.cellSize-1)
                pygame.draw.rect(screen,self.colors[cellNum],cellRect)
    def reset(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.field[i][j]=0