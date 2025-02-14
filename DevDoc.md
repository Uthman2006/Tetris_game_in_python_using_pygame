# Developers Documentation
In this project I used pygame library to code it.
<table>
    <thead>
        <tr>
            <th height="50" width="250">Every .py file</th>
            <th height="50" width="250">Explanation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>main.py</code></td>
            <td>This file is often used for front of the game which means these file solely focuses on pygame library part of the game</td>
        </tr>
        <tr>
            <td><code>game.py</code></td>
            <td>This file holds <code>class Game(x,y)</code> which focuses on controlling the game. Since this file controls all the functions, all other functions imported in to this file.</td>
        </tr>
        <tr>
            <td><code>field.py</code></td>
            <td>This file holds <code>class Field(x,y,volume)</code> which controls the behaviour of the field i.e. drawing the field, clearing the field, and setting boundries for the block</td>
        </tr>
        <tr>
            <td><code>block.py</code></td>
            <td>This file holds <code>class Block(id)</code>which is used for controlling the particular Block i.e. behaviour of the block in the field. Instead of writing every function that is needed for every block, I have just used inheritence in <code>blocks.py</code> to inherit the Block class which is super class for every class in <code>blocks.py</code></td>
        </tr>
        <tr>
            <td><code>blocks.py</code></td>
            <td>This file holds <code>class IBlock(id=1),class SBlock(id=2), class ZBlock(id=3), class OBlock(id=4), class LBlock(id=5), class JBlock(id=6), class TBlock(id=7)</code>. These are the files that inherits every function in <code>class Block(id)</code>. In addtion to these, these classes store the positions of the each block using <code>class Position(row, column)</code></td>
        </tr>
        <tr>
            <td><code>position.py</code></td>
            <td>This file holds the <code>class Position(row, column)</code> which is used for storing the values of the blocks</td>
        </tr>
    </tbody>
</table>
<table>
    <thead>
        <tr>
            <th height="50" width="250">Every class</th>
            <th height="50" width="250">Explanation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>class Game(x,y)</code></td>
            <td>This class serves as the main part of this game's background. This class controls all the other classes i.e. <code>class Field(x,y,volume)</code> and the classes in <code>blocks.py</code>. In addition to this, this class also controls score of the game and resetting the game.</td>
        </tr>
        <tr>
            <td><code>class Field(x,y,volume)</code></td>
            <td>This class is used to draw the field of the game and control its behaviour i.e. resetting the field and removing the full rows</td>
        </tr>
        <tr>
            <td><code>class Block(id)</code></td>
            <td>This class mainly focuses on controlling the bahaviour of a particular block i.e. <code>current_block</code> or <code>next_block</code></td>
        </tr>
        <tr>
            <td><code>class IBlock(id=1),class SBlock(id=2), class ZBlock(id=3), class OBlock(id=4), class LBlock(id=5), class JBlock(id=6), class TBlock(id=7)</code></td>
            <td>These classes store the position of the every block in the game using <code>class Position(row, column)</code></td>
        </tr>
        <tr>
            <td><code>class Position(row, column)</code></td>
            <td>This class is used for storing the values of the blocks</td>
        </tr>
    </tbody>
</table>
<table>
    <thead>
        <tr>
            <th height="50" width="250">Every function</th>
            <th height="50" width="250">Explanation</th>
        </tr>
        <tr>
            <th colspan="2" height="50" style="text-align:center;">Functions in <code>class Game(x,y)</code></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>update_score(lines_cleared:int,move_down_points:int)</code></td>
            <td>This function is used to upadate the user's score when ever he cleares the row or moves the block down.</td>
        </tr>
        <tr>
            <td><code>getRandomBlock()->*Block</code></td>
            <td>This function chooses a random block from the list. In <code>class Game(x,y)</code>, classes that store blocks are in a list. This function chooses a class, creates an object, and returns the object</td>
        </tr>
        <tr>
            <td><code>draw(screen:pygame.display)</code></td>
            <td>This function calls other draw functions from another classes and draws the field and blocks</td>
        </tr>
        <tr>
            <td><code>moveLeft(),moveRight(), moveDown()</code></td>
            <td>These functions help user to interact with the game. These functions move the blocks</td>
        </tr>
        <tr>
            <td><code>lockBlock()</code></td>
            <td>This function is used for fixing the block into place if it has an collision. the function first checks if it has collision If it has, then function locks the block there.</td>
        </tr>
        <tr>
            <td><code>freeCell()->bool</code></td>
            <td>This function checks if the upcoming cell is free so that block can move. if it is, then returns <code>True</code>. Otherwise, <code>False</code></td>
        </tr>
        <tr>
            <td><code>isBlockInside()->bool</code></td>
            <td>This function checks if the block is within the field.</td>
        </tr>
        <tr>
            <td><code>rotateClockwise(), rotateAntiClockwise()</code></td>
            <td>This function is used for rotating the block.</td>
        </tr>
        <tr>
            <td><code>reset()</code></td>
            <td>This function is used for resetting the game after game over. Fields,blocks, and score will be reseted</td>
        </tr>
        <tr>
            <th colspan="2" height="50" style="text-align:center;">Functions in <code>class Field(x,y,volume)</code></th>
        </tr>
        <tr>
            <td><code>isInside(row:int, column:int)->bool</code></td>
            <td>This function is used for checking if the block is inside of the field.</td>
        </tr>
        <tr>
            <td><code>isEmpty(row:int, column:int)->bool</code></td>
            <td>This function is used for checking if the corresponding cell is empty.</td>
        </tr>
        <tr>
            <td><code>IsRowFull(row:int)->bool</code></td>
            <td>This function checks if the that particular row is Full.</td>
        </tr>
        <tr>
            <td><code>clearRow(row:int)</code></td>
            <td>This function is used for clearing the full rows</td>
        </tr>
        <tr>
            <td><code>moveRowDown(row:int, numRows:int)</code></td>
            <td>This function is used for moving the rows down after clearing the full rows.</td>
        </tr>
        <tr>
            <td><code>clearFullRows()->int</code></td>
            <td>This function is the main part for clearing the full rows because it combines all the above functions</td>
        </tr>
        <tr>
            <td><code>draw(screen:pygame.display)</code></td>
            <td>This function is used for drawing the field</td>
        </tr>
        <tr>
            <th colspan="2" height="50" style="text-align:center;">Functions in <code>class Block(id)</code></th>
        </tr>
        <tr>
            <td><code>move(rows:int, columns:int)</code></td>
            <td>This function is used for moving the blocks</td>
        </tr>
        <tr>
            <td><code>getCellPos()->list</code></td>
            <td>This function is used for converting position of the blocks from background to front. Since in the background list of lists is used, on the front pixels are used. So, this functions coverts from list indeces to pixels</td>
        </tr>
        <tr>
            <td><code>draw(screen:pygame.display, offset_x:int, offset_y:int)</code></td>
            <td>This function is used fro drawing the block on the field</td>
        </tr>
        <tr>
            <td><code>rotate(rotation:int)</code></td>
            <td>This function is used for rotating the block.</td>
        </tr>
        <tr>
            <td><code>undoRotation(rotation:int)</code></td>
            <td>This function is used for returning the block to it is original state if it has collision while rotating.</td>
        </tr>
    </tbody>
</table>