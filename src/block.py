import pygame
from position import Position
class Block:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.cellSize=30
        self.rotationState=0
        self.rowOffset=0
        self.columnOffset=0
        self.colors=[(26,31,40),(47,230,23),(232,18,18),(226,116,17),(237,234,4),(166,0,247),(21,204,209),(13,64,216)]
    def move(self,rows, columns):
        self.rowOffset+=rows
        self.columnOffset+=columns
    def getCellPos(self):
        tiles = self.cells[self.rotationState]
        movedTiles=[]
        for position in tiles:
            position = Position(position.row+self.rowOffset,position.column+self.columnOffset)
            movedTiles.append(position)
        return movedTiles
    def draw(self,screen,offset_x,offset_y):
        tiles = self.getCellPos()
        for tile in tiles:
            tileRect = pygame.Rect(tile.column*self.cellSize+offset_x,tile.row*self.cellSize+offset_y,self.cellSize-1,self.cellSize-1)
            pygame.draw.rect(screen,self.colors[self.id],tileRect)
    def rotate(self,rotation):
        if(rotation == 1):
            self.rotationState+=1
            if self.rotationState == len(self.cells):
                self.rotationState=0
        elif (rotation == -1):
            self.rotationState-=1
            if self.rotationState <0:
                self.rotationState=len(self.cells)-1
    def undoRotation(self,rotation):
        if(rotation == 1):
            self.rotationState-=1
            if self.rotationState <0:
                self.rotationState=len(self.cells)-1
        elif (rotation == -1):
            self.rotationState+=1
            if self.rotationState == len(self.cells):
                self.rotationState=0