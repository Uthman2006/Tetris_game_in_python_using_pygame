import pygame
from position import Position
"""
Block class is used to control position of the blocks. 
Usually their movement, rotation angle, color, and drawing them in the field class
"""
class Block:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.cellSize=30
        self.rotationState=0
        self.rowOffset=0
        self.columnOffset=0
        self.colors=[(26,31,40),(47,230,23),(232,18,18),(226,116,17),(237,234,4),(166,0,247),(21,204,209),(13,64,216)]
        """
        Move function is used to move the blocks in the field by the given coordinate
        """
    def move(self,rows, columns):
        self.rowOffset+=rows
        self.columnOffset+=columns
    """
    getCellPos function is used to get the position of a block
    """
    def getCellPos(self):
        tiles = self.cells[self.rotationState]
        movedTiles=[]
        for position in tiles:
            position = Position(position.row+self.rowOffset,position.column+self.columnOffset)
            movedTiles.append(position)
        return movedTiles
    """
    draw function is used for drawing the block in the field using pygame.
    Although I haven't used the pygame library in here, draw takes argument dcreen which is variable which holds pygame.display
    """
    def draw(self,screen,offset_x,offset_y):
        tiles = self.getCellPos()
        for tile in tiles:
            tileRect = pygame.Rect(tile.column*self.cellSize+offset_x,tile.row*self.cellSize+offset_y,self.cellSize-1,self.cellSize-1)
            pygame.draw.rect(screen,self.colors[self.id],tileRect)
    """
    rotate function is used to rotate the blocks with the given direction to rotate which is clockwise or anticlockwise
    """
    def rotate(self,rotation):
        if(rotation == 1):
            self.rotationState+=1
            if self.rotationState == len(self.cells):
                self.rotationState=0
        elif (rotation == -1):
            self.rotationState-=1
            if self.rotationState <0:
                self.rotationState=len(self.cells)-1
    """
    undoRotation is used to undo the roatation if the block that should be rotated, but has a collision with a object
    """
    def undoRotation(self,rotation):
        if(rotation == 1):
            self.rotationState-=1
            if self.rotationState <0:
                self.rotationState=len(self.cells)-1
        elif (rotation == -1):
            self.rotationState+=1
            if self.rotationState == len(self.cells):
                self.rotationState=0