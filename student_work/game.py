# Write your game here
import curses 

game_data = {
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
    'width': 10,
    'height': 10,
    'player': {"x": 0, "y": 0, "score": 0}, #, "energy": 10, "max_energy": 10},
    'ghost_pos': {"x": 4, "y": 4},
    'collectibles': [
        {"x": 2, "y": 1, "collected": False},
    ],
    'walls': [
        {"x": 1, "y": 2},
        {"x": 3, "y": 0},
        {"x": 3, "y": 1},
        {"x": 1, "y": 3},
        {"x": 1, "y": 4},
        {"x": 1, "y": 6},
        {"x": 2, "y": 6},
        {"x": 3, "y": 6},
        {"x": 3, "y": 7},
        {"x": 5, "y": 6},
        {"x": 5, "y": 7},
        {"x": 8, "y": 0},
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
            # Eagle
            elif x == game_data['ghost_pos']['x'] and y == game_data['ghost_pos']['y']:
                row += game_data['ghost']
            # Obstacles
            elif any(o['x'] == x and o['y'] == y for o in game_data['walls']):
                row += game_data['wall']
            elif x == 8:
                row += game_data['wall']
            elif y == 8:
                row += game_data['wall']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                row += game_data['pellet']
            else:
                row += game_data['empty']
        screen.addstr(y, 0, row, curses.color_pair(1))

    screen.refresh()
    screen.getkey()  # pause so player can see board

curses.wrapper(draw_board)

# Good Luck!