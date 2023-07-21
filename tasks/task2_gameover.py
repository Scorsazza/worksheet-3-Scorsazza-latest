import pyasge

from game.gamestates.gamestate import GameState
from game.gamestates.gamestate import GameStateID
from game.gamedata import GameData


class GameOver(GameState):

    def __init__(self, data: GameData) -> None:
        super().__init__(data)
        self.id = GameStateID.GAME_OVER

    def click_handler(self, event: pyasge.ClickEvent) -> None:
        print("processing click event")

    def key_handler(self, event: pyasge.KeyEvent) -> None:
        print("processing key event")

    def move_handler(self, event: pyasge.MoveEvent) -> None:
        print("processing mouse move event")

    def fixed_update(self, game_time: pyasge.GameTime) -> None:
        pass

    def update(self, game_time: pyasge.GameTime) -> GameStateID:
        """ If user_clicked go to game menu else return GAME_OVER """
        return GameStateID.GAME_OVER

    def render(self, game_time: pyasge.GameTime) -> None:

        pass

