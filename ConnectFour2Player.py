import ConnectFourEngine
import ConnectFourMinimaxAI
import ConnectFourAlphaBeta

if __name__ == '__main__':
    # Initialise the game engine
    # Modify these parameters to tweak the game
    app = ConnectFourEngine.ConnectFour(
            red_player = ConnectFourAlphaBeta.AIcheck,
            blue_player = ConnectFourMinimaxAI.AIcheck,
            )
        # start the game engine
    app.game_loop()
