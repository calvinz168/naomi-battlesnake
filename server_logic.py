import random
from typing import List, Dict
import math


def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:

    # The segment of body right after the head is the 'neck'
    my_neck = my_body[1]

    if my_neck["x"] < my_head["x"]:     # my neck is left of my head
        while "left" in possible_moves:
            possible_moves.remove("left")

    elif my_neck["x"] > my_head["x"]:   # my neck is right of my head
        while "right" in possible_moves:
            possible_moves.remove("right")

    elif my_neck["y"] < my_head["y"]:   # my neck is below my head
        while "down" in possible_moves:
            possible_moves.remove("down")

    elif my_neck["y"] > my_head["y"]:   # my neck is above my head
        while "up" in possible_moves:
            possible_moves.remove("up")

    return possible_moves


def avoid_borders(width, height, my_head: Dict[str, int], possible_moves: List[str]) -> List[str]:
    if my_head["x"] + 1 == width:       # the head will hit right side of board
        while "right" in possible_moves:
            possible_moves.remove("right")

    if my_head["x"] - 1 == -1:           # the head will hit left side of board
        while "left" in possible_moves:
            possible_moves.remove("left")

    if my_head["y"] + 1 == height:      # the head will hit top side of board
        while "up" in possible_moves:
            possible_moves.remove("up")

    if my_head["y"] - 1 == -1:           # the head will hit bottom side of board
        while "down" in possible_moves:
            possible_moves.remove("down")

    return possible_moves


def avoid_body(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
    for i in range(len(my_body)):
        if ((my_head["x"] + 1 == my_body[i]["x"]) and (my_head["y"] == my_body[i]["y"])):
            while "right" in possible_moves:
                possible_moves.remove("right")

        if ((my_head["x"] - 1 == my_body[i]["x"]) and (my_head["y"] == my_body[i]["y"])):
            while "left" in possible_moves:
                possible_moves.remove("left")

        if ((my_head["y"] + 1 == my_body[i]["y"]) and (my_head["x"] == my_body[i]["x"])):
            while "up" in possible_moves:
                possible_moves.remove("up")

        if ((my_head["y"] - 1 == my_body[i]["y"]) and (my_head["x"] == my_body[i]["x"])):
            while "down" in possible_moves:
                possible_moves.remove("down")

    return possible_moves


def avoid_snakes(my_head: Dict[str, int], other_snakes_body, other_snakes_head, possible_moves: List[str]) -> List[str]:
    # print("other_snakes_body",other_snakes_body)
    # print("len(other_snakes_body)",len(other_snakes_body))
    for a in range(len(other_snakes_body)):
        for b in range(len(other_snakes_body[a])):
            # print("my_head",my_head)
            # print("other_snakes_body[a][b]", other_snakes_body[a][b])

            if ((my_head["x"] + 1 == other_snakes_body[a][b]["x"]) and (my_head["y"] == other_snakes_body[a][b]["y"])):
                while "right" in possible_moves:
                    possible_moves.remove("right")

            if ((my_head["x"] - 1 == other_snakes_body[a][b]["x"]) and (my_head["y"] == other_snakes_body[a][b]["y"])):
                while "left" in possible_moves:
                    possible_moves.remove("left")

            if ((my_head["y"] + 1 == other_snakes_body[a][b]["y"]) and (my_head["x"] == other_snakes_body[a][b]["x"])):
                while "up" in possible_moves:
                    possible_moves.remove("up")

            if ((my_head["y"] - 1 == other_snakes_body[a][b]["y"]) and (my_head["x"] == other_snakes_body[a][b]["x"])):
                while "down" in possible_moves:
                    possible_moves.remove("down")

    # head to head direct
    for i in range(len(other_snakes_head)):
        if ((my_head["x"] + 2 == other_snakes_head[i]["x"]) and (my_head["y"] == other_snakes_head[i]["y"])):
            while "right" in possible_moves:
                possible_moves.remove("right")

        if ((my_head["x"] - 2 == other_snakes_head[i]["x"]) and (my_head["y"] == other_snakes_head[i]["y"])):
            while "left" in possible_moves:
                possible_moves.remove("left")

        if ((my_head["y"] + 2 == other_snakes_head[i]["y"]) and (my_head["x"] == other_snakes_head[i]["x"])):
            while "up" in possible_moves:
                possible_moves.remove("up")

        if ((my_head["y"] - 2 == other_snakes_head[i]["y"]) and (my_head["x"] == other_snakes_head[i]["x"])):
            while "down" in possible_moves:
                possible_moves.remove("down")

        # head to head but corner:
        if ((my_head["x"] + 1 == other_snakes_head[i]["x"]) and (my_head["y"] + 1 == other_snakes_head[i]["y"])):
            while "right" in possible_moves:
                possible_moves.remove("right")
            while "up" in possible_moves:
                possible_moves.remove("up")
            if len(possible_moves) == 0:
                possible_moves.append(random.choice(["right", "up"]))

        if ((my_head["x"] - 1 == other_snakes_head[i]["x"]) and (my_head["y"] + 1 == other_snakes_head[i]["y"])):
            while "left" in possible_moves:
                possible_moves.remove("left")
            while "up" in possible_moves:
                possible_moves.remove("up")
            if len(possible_moves) == 0:
                possible_moves.append(random.choice(["right", "up"]))

        if ((my_head["x"] + 1 == other_snakes_head[i]["x"]) and (my_head["y"] - 1 == other_snakes_head[i]["y"])):
            while "right" in possible_moves:
                possible_moves.remove("right")
            while "down" in possible_moves:
                possible_moves.remove("down")
            if len(possible_moves) == 0:
                possible_moves.append(random.choice(["right", "down"]))

        if ((my_head["x"] - 1 == other_snakes_head[i]["x"]) and (my_head["y"] - 1 == other_snakes_head[i]["y"])):
            while "left" in possible_moves:
                possible_moves.remove("left")
            while "down" in possible_moves:
                possible_moves.remove("down")
            if len(possible_moves) == 0:
                possible_moves.append(random.choice(["left", "down"]))

    return possible_moves


# def foresight(my_head, my_body, other_snakes_body,possible_moves):
# 	# can i make a trail back to tail?
# 		# if not then optimize with hamiltonion cycle
# 	badTile = my_body + other_snakes_body
# 	area = 0
# 	print("badTile",badTile)
# 	print("badTile[x]",badTile["x"])
# 	print("badTile[y]",badTile["y"])

# 	uniqueDir = []
# 	for i in range(len(possible_moves)):
# 		if possible_moves[i] not in uniqueDir:
# 			if possible_moves[i] == "right":
# 				for a in range(len(my_body)):
# 					for tile in (badTile):
# 						if ((my_head["x"] + a == tile["x"]) and (my_head["y"] == tile["y"]))
# 							break
# 						else:
# 							area +=1
# 					break


# def foresight(my_head, my_body, other_snakes_body,possible_moves):
# 	# can i make a trail back to tail?
# 		# if not then optimize with hamiltonion cycle
# 	badTile = my_body + other_snakes_body
# 	area = 0
# 	print("badTile",badTile)
# 	print("badTile[x]",badTile["x"])
# 	print("badTile[y]",badTile["y"])

# 	uniqueDir = []
# 	for i in range(len(possible_moves)):
# 		if possible_moves[i] not in uniqueDir:
# 			if possible_moves[i] == "right":


# 				for a in range(len(my_body)):
# 					for tile in (badTile):
# 						if ((my_head["x"] + 1 == tile["x"]) and (my_head["y"] == tile["y"])):
# 							while "right" in possible_moves:
# 								possible_moves.remove("right")

# 	return possible_moves


def foresight(my_head, my_body, other_snakes_body, possible_moves):
    # can i make a trail back to tail?
    # if not then optimize with hamiltonion cycle
    leftBorder = [[-1, 0], [-1, 1], [-1, 2], [-1, 3], [-1, 4],
                  [-1, 5], [-1, 6], [-1, 7], [-1, 8], [-1, 9], [-1, 10]]
    rightBorder = [[11, 0], [11, 1], [11, 2], [11, 3], [11, 4],
                   [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10]]
    topBorder = [[0, 11], [1, 11], [2, 11], [3, 11], [4, 11],
                 [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]]
    bottomBorder = [[0, -1], [1, -1], [2, -1], [3, -1], [4, -1],
                    [5, -1], [6, -1], [7, -1], [8, -1], [9, -1], [10, -1]]

    badTile = my_body + other_snakes_body
    badTileMatrix = []
    area = 0
    for a in range(len(my_body), len(badTile)):
        #     print("badTile[a]", badTile[a])
        for b in badTile[a]:
            temp = []
            temp.append(b["x"])
            temp.append(b["y"])
            badTileMatrix.append(temp)
    for i in range(11):
        badTileMatrix.append(leftBorder[i])
        badTileMatrix.append(rightBorder[i])
        badTileMatrix.append(topBorder[i])
        badTileMatrix.append(bottomBorder[i])

    # print("badTileMatrix",badTileMatrix)
    # print("badTile",badTile)
    for i in possible_moves:
        if ((queryTiles(0, i, my_head["x"], my_head["y"], my_body, badTileMatrix, possible_moves) == 0) or (len(my_body) < queryTiles(0, i, my_head["x"], my_head["y"], my_body, badTileMatrix, possible_moves))):
            while f"{i}" in possible_moves:
                possible_moves.remove(f"{i}")

    return possible_moves


def queryTiles(area, direction, x_pos, y_pos, my_body, badTileMatrix, possible_moves):

    if direction == "right":
        queryMatrix = [[x_pos + 1, y_pos], [x_pos +
                                            1, y_pos + 1], [x_pos + 1, y_pos - 1]]
    elif direction == "left":
        queryMatrix = [[x_pos - 1, y_pos], [x_pos -
                                            1, y_pos + 1], [x_pos - 1, y_pos - 1]]
    elif direction == "up":
        queryMatrix = [[y_pos + 1, x_pos], [y_pos +
                                            1, x_pos + 1], [y_pos + 1, x_pos - 1]]
    elif direction == "down":
        queryMatrix = [[y_pos - 1, x_pos], [y_pos -
                                            1, x_pos + 1], [y_pos - 1, x_pos - 1]]

    for i in range(len(queryMatrix)):
        print("queryMatrix[i]", queryMatrix[i])
        print("badTileMatrix", badTileMatrix)
        if (queryMatrix[i] not in badTileMatrix):
            area += 1
        else:
            area = 0
            return area
    print("area", area)
    if ((direction == "right") and (x_pos < 10) and (y_pos < 10)):
        queryTiles(area, "right", x_pos + 1, y_pos, my_body,
                   badTileMatrix, possible_moves)
        queryTiles(area, "up", x_pos + 1, y_pos, my_body,
                   badTileMatrix, possible_moves)
        queryTiles(area, "down", x_pos + 1, y_pos, my_body,
                   badTileMatrix, possible_moves)

    elif ((direction == "left") and (x_pos < 10) and (y_pos < 10)):
        queryTiles(area, "left", x_pos - 1, y_pos, my_body,
                   badTileMatrix, possible_moves)
        queryTiles(area, "up", x_pos - 1, y_pos, my_body,
                   badTileMatrix, possible_moves)
        queryTiles(area, "down", x_pos - 1, y_pos, my_body,
                   badTileMatrix, possible_moves)

    elif ((direction == "up") and (x_pos < 10) and (y_pos < 10)):
        queryTiles(area, "up", x_pos, y_pos + 1, my_body,
                   badTileMatrix, possible_moves)
        queryTiles(area, "left", x_pos, y_pos + 1, my_body,
                   badTileMatrix, possible_moves)
        queryTiles(area, "right", x_pos, y_pos + 1, my_body,
                   badTileMatrix, possible_moves)

    elif ((direction == "down") and (x_pos < 10) and (y_pos < 10)):
        queryTiles(area, "down", x_pos, y_pos - 1, my_body,
                   badTileMatrix, possible_moves)
        queryTiles(area, "left", x_pos, y_pos - 1, my_body,
                   badTileMatrix, possible_moves)
        queryTiles(area, "right", x_pos, y_pos - 1, my_body,
                   badTileMatrix, possible_moves)

    return area


def lookahead(my_head, my_body, other_snakes_body, possible_moves):
    x_pos = my_head["x"]
    y_pos = my_head["y"]
    leftBorder = [[-1, 0], [-1, 1], [-1, 2], [-1, 3], [-1, 4],
                  [-1, 5], [-1, 6], [-1, 7], [-1, 8], [-1, 9], [-1, 10]]
    rightBorder = [[11, 0], [11, 1], [11, 2], [11, 3], [11, 4],
                   [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10]]
    topBorder = [[0, 11], [1, 11], [2, 11], [3, 11], [4, 11],
                 [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11]]
    bottomBorder = [[0, -1], [1, -1], [2, -1], [3, -1], [4, -1],
                    [5, -1], [6, -1], [7, -1], [8, -1], [9, -1], [10, -1]]

    badTile = my_body + other_snakes_body
    badTileMatrix = []
    area = 0
    for a in range(len(my_body), len(badTile)):
        #     print("badTile[a]", badTile[a])
        for b in badTile[a]:
            temp = []
            temp.append(b["x"])
            temp.append(b["y"])
            badTileMatrix.append(temp)
    for i in range(11):
        badTileMatrix.append(leftBorder[i])
        badTileMatrix.append(rightBorder[i])
        badTileMatrix.append(topBorder[i])
        badTileMatrix.append(bottomBorder[i])

    for direction in possible_moves:
        if direction == "right":
            queryMatrix = [[x_pos + 1, y_pos], [x_pos +
                                                1, y_pos + 1], [x_pos + 1, y_pos - 1]]
        elif direction == "left":
            queryMatrix = [[x_pos - 1, y_pos], [x_pos -
                                                1, y_pos + 1], [x_pos - 1, y_pos - 1]]
        elif direction == "up":
            queryMatrix = [[y_pos + 1, x_pos], [y_pos +
                                                1, x_pos + 1], [y_pos + 1, x_pos - 1]]
        elif direction == "down":
            queryMatrix = [[y_pos - 1, x_pos], [y_pos -
                                                1, x_pos + 1], [y_pos - 1, x_pos - 1]]
        counter = 0
        for i in range(len(queryMatrix)):
            # print("queryMatrix[i]", queryMatrix[i])
            # print("badTileMatrix", badTileMatrix)
            if (queryMatrix[i] in badTileMatrix):
                counter += 1
                if counter == 3:
                    while f"{direction}" in possible_moves:
                        possible_moves.remove(f"{direction}")

    return possible_moves


def get_food(my_head: Dict[str, int], food, possible_moves: List[str]) -> List[str]:
    closestDist = 99
    closestIndex = None
    for i in range(len(food)):
        # pythag therom to get closest food
        xdist = abs((food[i]["x"] - my_head["x"])
                    * (food[i]["x"] - my_head["x"]))
        ydist = abs((food[i]["y"] - my_head["y"])
                    * (food[i]["y"] - my_head["y"]))
        pyth = math.sqrt(xdist + ydist)
        if pyth <= closestDist:
            closestDist = pyth
            closestIndex = i
        # add a move to increase odds of obtaining food
        # not necessary to go direct, can survive for a long time, and also enemy might gatekeep
    if my_head["x"] > food[closestIndex]["x"]:
        if "left" in possible_moves:
            possible_moves.append("left")
            possible_moves.append("left")

    if my_head["x"] < food[closestIndex]["x"]:
        if "right" in possible_moves:
            possible_moves.append("right")
            possible_moves.append("right")

    if my_head["y"] > food[closestIndex]["y"]:
        if "down" in possible_moves:
            possible_moves.append("down")
            possible_moves.append("down")

    if my_head["y"] < food[closestIndex]["y"]:
        if "up" in possible_moves:
            possible_moves.append("up")
            possible_moves.append("up")

    return possible_moves


def choose_move(data: dict) -> str:
    print("")
    print("")
    print("")

    # A dictionary of x/y coordinates like {"x": 0, "y": 0}
    my_head = data["you"]["head"]
    # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]
    my_body = data["you"]["body"]
    food = data["board"]["food"]

    other_snakes_body = []
    other_snakes_head = []
    for i in range(len(data["board"]["snakes"])):
        # print(data["board"]["snakes"])
        if data["board"]["snakes"][i]["name"] != "naomi.py":
            other_snakes_body.append(data["board"]["snakes"][i]["body"])
            other_snakes_head.append(data["board"]["snakes"][i]["head"])

    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    # print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")

    # print(f"All board data this turn: {data}")

    # print("")
    # print(f"My Battlesnakes head this turn is: {my_head}")
    # print(f"My Battlesnakes body this turn is: {my_body}")
    # print("")
    # print(other_snakes_body)

    # TODO: Using information from 'data', find the edges of the board and don't let your Battlesnake move beyond them
    board_height = data["board"]["height"]
    board_width = data["board"]["width"]

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with another Battlesnake

    possible_moves = ["up", "down", "left", "right"]

    # move towards food
    possible_moves = get_food(my_head, food, possible_moves)
    print("possible_moves after food", possible_moves)

    # Don't allow your Battlesnake to move back in on it's own neck
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)
    print("possible_moves after avoid_my_neck", possible_moves)

    # avoid borders
    possible_moves = avoid_borders(
        board_width, board_height, my_head, possible_moves)
    print("possible_moves after avoid_borders", possible_moves)

    # avoid body
    possible_moves = avoid_body(my_head, my_body, possible_moves)
    print("possible_moves after avoid_body", possible_moves)

    # aovid other snakes
    possible_moves = avoid_snakes(
        my_head, other_snakes_body, other_snakes_head, possible_moves)
    print("possible_moves after avoid_snakes", possible_moves)

    print("A")
    # possible_moves = foresight(
    #     my_head, my_body, other_snakes_body, possible_moves)
    print("B")

    possible_moves = lookahead(
        my_head, my_body, other_snakes_body, possible_moves)
    print("possible_moves after lookahead", possible_moves)

    # Choose a random direction from the remaining possible_moves to move in, and then return that move
    print("possible_moves: ", possible_moves)
    if len(possible_moves) != 0:
        move = random.choice(possible_moves)
    else:
        possible_moves = ["up", "down", "left", "right"]
        move = random.choice(avoid_body(my_head, my_body, possible_moves))
    # TODO: Explore new strategies for picking a move that are better than random

    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")

    return move
