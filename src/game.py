from field import Field
from blocks import *
from random import choice
class Game:
    def __init__(self,posInDispX,posInDispY):
        self.field = Field(posInDispX,posInDispY)
        self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.currentBlock=self.getRandomBlock()
        self.nextBlock=self.getRandomBlock()
    def getRandomBlock(self):
        if (len(self.blocks)==0):
            self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        block = choice(self.blocks)
        self.blocks.remove(block)
        return block
    def draw(self,screen):
        self.field.draw(screen)
        self.currentBlock.draw(screen)
        # self.field.printField()
    def moveLeft(self):
        self.currentBlock.move(0,-1)
        if not self.isBlockInside() or not self.freeCell():
            self.currentBlock.move(0,1)
    def moveRight(self):
        self.currentBlock.move(0,1)
        if not self.isBlockInside() or not self.freeCell():
            self.currentBlock.move(0,-1)
    def moveDown(self):
        self.currentBlock.move(1,0)
        if not self.isBlockInside() or not self.freeCell():
            self.currentBlock.move(-1,0)
            self.lockBlock()
    def lockBlock(self):
        tiles = self.currentBlock.getCellPos()
        for position in tiles:
            self.field.field[position.row][position.column]=self.currentBlock.id
        self.currentBlock = self.nextBlock
        self.nextBlock=self.getRandomBlock()
    def freeCell(self):
        tiles = self.currentBlock.getCellPos()
        for tile in tiles:
            if not self.field.isEmpty(tile.row, tile.column):
                return False
        return True
    def isBlockInside(self):
        tiles=self.currentBlock.getCellPos()
        for tile in tiles:
            if not self.field.isInside(tile.row,tile.column):
                return False
        return True
    def rotateClockwise(self):
        self.currentBlock.rotate(1)
        if(not self.isBlockInside() or not self.freeCell):
            self.currentBlock.undoRotation(1)
    def rotateAntiClockwise(self):
        self.currentBlock.rotate(-1)
        if(not self.isBlockInside()or not self.freeCell()):
            self.currentBlock.undoRotation(-1)