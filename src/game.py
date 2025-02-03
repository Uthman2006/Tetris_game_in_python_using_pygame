from field import Field
from blocks import *
from random import choice
"""
Game class is the main class for the game.
It controls the behaviour of Filed and blocks, and also helps to draw.
"""
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
    """
    update_score function is used for updating the score of the game. 
    If a player clears the row, he will get corresponding socores for clearing the row.
    By clearing the row I meant filling the row.
    """
    def update_score(self,lines_cleared,move_down_points):
        if lines_cleared==1:
            self.score+=100
        elif lines_cleared==2:
            self.score+=300
        elif lines_cleared == 3:
            self.score+=500
        self.score+=move_down_points
    """
    getRandomBlock function is used to get random block.
    It uses choice function for choosing the block.
    """
    def getRandomBlock(self):
        if (len(self.blocks)==0):
            self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        block = choice(self.blocks)
        self.blocks.remove(block)
        return block
    """
    draw function is used for helping to draw the blocks and field itself
    """
    def draw(self,screen):
        self.field.draw(screen)
        self.currentBlock.draw(screen,20,10)
        self.nextBlock.draw(screen,70,640)
        # self.field.printField()
    """
    moveLeft function is used when the player presses the key that moves the block to the left.
    """
    def moveLeft(self):
        self.currentBlock.move(0,-1)
        if not self.isBlockInside() or not self.freeCell():
            self.currentBlock.move(0,1)
    """
    moveRight function is the same as the moveLeft, but it moves the block to the right.
    """
    def moveRight(self):
        self.currentBlock.move(0,1)
        if not self.isBlockInside() or not self.freeCell():
            self.currentBlock.move(0,-1)
    """
    moveDown function is moving the block down.
    """
    def moveDown(self):
        self.currentBlock.move(1,0)
        if not self.isBlockInside() or not self.freeCell():
            self.currentBlock.move(-1,0)
            self.lockBlock()
    """
    lockBlock function is used for saving the block in the background if it had a collision.
    """
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
    """
    freeCell function is used to check if the particular cell is free.
    If the block moves, it won't hit any object.
    """
    def freeCell(self):
        tiles = self.currentBlock.getCellPos()
        for tile in tiles:
            if not self.field.isEmpty(tile.row, tile.column):
                return False
        return True
    """
    isBlockInside function is used to check if the block is inside the game field.
    """
    def isBlockInside(self):
        tiles=self.currentBlock.getCellPos()
        for tile in tiles:
            if not self.field.isInside(tile.row,tile.column):
                return False
        return True
    """
    rotateClockwise and rotateAntiClockwise functions uses rotate function in the Block class to rotate the block.
    """
    def rotateClockwise(self):
        self.currentBlock.rotate(1)
        if(not self.isBlockInside() or not self.freeCell):
            self.currentBlock.undoRotation(1)
    def rotateAntiClockwise(self):
        self.currentBlock.rotate(-1)
        if(not self.isBlockInside()or not self.freeCell()):
            self.currentBlock.undoRotation(-1)
    """
    reset function is used for reseting the whole game. it is different then field reset.
    this resets the whole game. Meanwhile, the reset in the Field class resets only the filed itself.
    """
    def reset(self):
        self.field.reset()
        self.blocks=[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.currentBlock =self.getRandomBlock()
        self.nextBlock=self.getRandomBlock()
        self.game_over=False
        self.score=0