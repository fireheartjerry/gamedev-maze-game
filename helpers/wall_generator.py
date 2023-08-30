wallData = []

def update_walls(new_walls):
    global wallData
    wallData = new_walls

def print_walls():
    print(wallData)

def get_walls():
    return wallData