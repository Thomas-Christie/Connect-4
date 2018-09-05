# Connect-4

In this project I created a modified version of the game "Connect 4" at the Cambridge Coding Academy Summer School. The game can be played between two humans by executing the "ConnectFour2Player.py", one human vs a bot by executing the "ConnectFour1Player.py" and between two bots by executing the "ConnectFour0Player.py". During the course we created an AI that used the Minimax search technique to play the game, which was very effective, and the code for this can be seen in "ConnectFourMinimaxAI.py". The search depth of the tree can be adjusted by changing the "ply" parameter in the code. After the course I modified the Minimax AI by adding Alpha-Beta pruning, making the algorithm more efficient and allowing it to search deeper into the search tree without taking too long. The code for this can be seen in "ConnectFourAlphaBeta.py". I also did some tests to compare the efficiency of the pure Minimax AI and the AI which also implemented Alpha-Beta Pruning. The results from these test can be seen in the "Analysis 2" PDF.

### Prerequisites

The following libraries are required to run the project:
```
pygame
```
