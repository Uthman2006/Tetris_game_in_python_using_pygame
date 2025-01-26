from field import Field
from blocks import *
from random import choice
import pygame
class Game:
    def __init__(self,posInDispX,posInDispY):
        self.sound_effect_volume=1
        self.field = Field(posInDispX,posInDispY,self.sound_effect_volume)
        self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.currentBlock=self.getRandomBlock()
        self.nextBlock=self.getRandomBlock()
        self.game_over=False
        self.game_over_sound_effect=pygame.mixer.Sound("../materials/game_over_sound_effect.ogg")
        self.game_over_sound_effect.set_volume(self.sound_effect_volume)
        self.score=0
    def update_score(self,lines_cleared,move_down_points):
        if lines_cleared==1:
            self.score+=100
        elif lines_cleared==2:
            self.score+=300
        elif lines_cleared == 3:
            self.score+=500
        self.score+=move_down_points
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
        rows_cleared=self.field.clearFullRows()
        self.update_score(rows_cleared,0)
        if not self.freeCell():
            self.game_over=True
            self.game_over_sound_effect.play(loops=0)
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
    def reset(self):
        self.field.reset()
        self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.currentBlock =self.getRandomBlock()
        self.nextBlock=self.getRandomBlock()
        self.game_over=False
        self.score=0