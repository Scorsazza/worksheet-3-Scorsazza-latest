"""
This is the pathfinding script.

You will need to complete the resolve function in order to
get movement to work correctly. You should start with
BFS and consider more advanced approaches if you have time.

The function will take a player's mouse click and return a
list of tile locations it needs to visit in order to get
to its destination.

note: you should also use this pathfinding function for task4
"""

import pyasge
from game.gamedata import GameData


def resolve(xy: pyasge.Point2D, data: GameData):




    # convert point to tile location
    tile_loc = data.game_map.tile(xy)
    tile_cost = data.game_map.costs[tile_loc[1]][tile_loc[0]]

    # use these to make sure you don't go out of bounds when checking neighbours
    map_width = data.game_map.width
    map_height = data.game_map.height

    # here's an example of tiles that the player should visit
    tiles_to_visit = [data.game_map.world(tile_loc)]

    # return a list of tile positions to follow
    path = []
    if tile_cost ==1:
     for tile in tiles_to_visit:
        path.append(tile)
    return path

