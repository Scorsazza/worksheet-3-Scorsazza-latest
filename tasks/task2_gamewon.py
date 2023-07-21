import pyasge as pyasge

from game.gamedata import GameData
from game.gamestates.gamestate import GameState, GameStateID


class GameWon(GameState):

    def __init__(self, data: GameData) -> None:
        super().__init__(data)
        self.id = GameStateID.WINNER_WINNER

    def click_handler(self, event: pyasge.ClickEvent) -> None:
        pass

    def key_handler(self, event: pyasge.KeyEvent) -> None:
        pass

    def move_handler(self, event: pyasge.MoveEvent) -> None:
        pass

    def fixed_update(self, game_time: pyasge.GameTime) -> None:
        pass

    def update(self, game_time: pyasge.GameTime) -> GameStateID:
        return GameStateID.WINNER_WINNER

    def render(self, game_time: pyasge.GameTime) -> None:
        pass