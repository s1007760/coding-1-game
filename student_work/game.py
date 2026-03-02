import curses 

game_data = {
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
    'width': 10,
    'height': 10,
    'player': {"x": 0, "y": 0, "score": 0}, #, "energy": 10, "max_energy": 10},
    'ghost_pos': {"x": 4, "y": 4},
    'pellets': [
        {"x": 2, "y": 1, "collected": False},
    ],
    'walls': [
    {"x": 0, "y": [8]},
    {"x": 1, "y": [1, 2, 3, 6]},
    {"x": 2, "y": [3, 5, 6, 7, 9]},        
    {"x": 3, "y": [1, 3, 5, 9]},
    {"x": 4, "y": [1, 5, 6, 7, 9]},
    {"x": 5, "y": [1]},
    {"x": 6, "y": [1, 3, 4, 5, 7, 8]},
    {"x": 7, "y": [1, 8]},
    {"x": 8, "y": [1, 4, 5, 6, 8,]},
    {"x": 9, "y": [6]}
    ],

    # ASCII icons
    'pac_cat_moving': "\U0001F63C",
    'pac_cat_eating': "\U0001F638",
    'pac_cat_dying': "\U0001F640",
    'ghost': "\U0001F47B",
    'wall': "\U0001F4D7",
    'pellet': "\U0001F9C0",
    'empty': "  "
}

def draw_board(screen): #was originally screen
    # Print the board and all game elements using curses
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    screen.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['pac_cat_moving']
            # Ghost
            elif x == game_data['ghost_pos']['x'] and y == game_data['ghost_pos']['y']:
                row += game_data['ghost']
            # Walls
            elif any(o['x'] == x and y in o['y'] for o in game_data['walls']):
                row += game_data['wall']

            # pellets
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['pellets']):
                row += game_data['pellet']
            else:
                row += game_data['empty']
        #screen.addstr(y, 0, row, curses.color_pair(1))
            try:
                screen.addstr(y, 0, row, curses.color_pair(1))
            except curses.error:
                pass
    screen.refresh()
    screen.getkey()  # pause so player can see board

def player_movement():
    x = game_data['player']['x']
    y = game_data['player']['y']

    next_x, next_y = x, y #setting up the old x and y turning into the new location
    key_pressed = key
    if key_pressed == "w" and y >= 0:
        next_y -= 1 #moving up
    elif key_pressed == "s" and y <= 9:
        
    elif key_pressed == "a" and x >= 0:
        next_x -= 1 #moving left
    elif key_pressed

def adding_to_score():

def main_calling_function(game_data):
    game_data['player']['score'] = 0

curses.wrapper(draw_board)
#-initialize score variable = 0
#-start function, take pacman and pellet as arguments,
#-detect that if pacman_touches_object(pacman, pellet): then 1 is += to global score variable.
#-and also pellet is removed from the screen, pellet number is -= by 1.
#-print score change