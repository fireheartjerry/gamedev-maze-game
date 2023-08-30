wallData = []

def getColour(type):
    if type == "win":
        return (0, 255, 0)
    elif type == "lose":
        return (255, 0, 0)
    else:
        return (136, 255, 255)

def update_walls(new):
    global wallData
    wallData = [{"wall_data": wall[0:4], "colour": getColour(wall[4])} for wall in new]

def get_walls():
    return wallData