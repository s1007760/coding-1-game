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

def draw_board(stdscr): #was originally screen
    # Print the board and all game elements using curses
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
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
                stdscr.addstr(y, 0, row, curses.color_pair(1))
            except curses.error:
                pass
        
    #I just copied this, but it works.
    try:
        stdscr.addstr(game_data['height'] + 1, 0,
                  f"Moves Survived: {game_data['player']['score']}",
                  curses.color_pair(1))
        stdscr.addstr(game_data['height'] + 2, 0,
                  "Move with W/A/S/D, Q to quit",
                  curses.color_pair(1))
    except curses.error:
        pass # Ignore error if terminal is too small
    stdscr.refresh()


def player_movement(key_pressed):
    x = game_data['player']['x']
    y = game_data['player']['y']
    next_x, next_y = x, y #setting up the old x and y turning into the new location

    key_pressed = key_pressed.lower()
    if key_pressed == "w" and y >= 0:
        next_y -= 1 #moving up
    elif key_pressed == "s" and y < game_data['height'] - 1:
        next_y += 1 #moving down
    elif key_pressed == "a" and x >= 0:
        next_x -= 1 #moving left
    elif key_pressed == "d" and x < game_data['height'] - 1:
        next_x += 1 #moving right
    else:
        return  # Invalid key or move off board

    for wall in game_data['walls']:
        if next_x == wall['x'] and next_y in wall['y']:
            return # return as in don't move but keep checking for more input.

    # Update position and increment score
    game_data['player']['x'] = next_x
    game_data['player']['y'] = next_y
    game_data['player']['score'] += 1


#def spawn_pellets():

#def adding_to_score():

#def move_ghost():
  #  directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
  #  random.shuffle(directions)
  #  ghost_x, ghost_y = game_data['ghost_pos']['x'], game_data['ghost_pos']['y']

 #   for ghost_x, ghost_y in directions:
  #      new_ghost_x = ghost_x + dx
  #      new_y = ey + dy
  #      if 0 <= new_x < game_data['width'] and 0 <= new_y < game_data['height']:
  #          if not any(o['x'] == new_x and o['y'] == new_y for o in game_data['obstacles']):
  #              game_data['eagle_pos']['x'] = new_x
 #               game_data['eagle_pos']['y'] = new_y
   #             break

def main_function(stdscr): #**need a while true loop to keep the game running,
                                 #else it just runs once and stops, not connected to player movement.
    curses.curs_set(0)
    #stdscr.nodelay(True)

    while True:
        draw_board(stdscr)
        try:
            key = stdscr.getkey()
        except:
            continue 
        player_movement(key)

      #  move_ghost()
       # spawn_pellets()

        draw_board(stdscr)
       # time.sleep(0.2)

  #  game_data['player']['score'] = 0


#curses.wrapper(draw_board)
#curses.wrapper(player_movement)  #The curses makes the code recognize keyboard input?
curses.wrapper(main_function)


#-initialize score variable = 0
#-start function, take pacman and pellet as arguments,
#-detect that if pacman_touches_object(pacman, pellet): then 1 is += to global score variable.
#-and also pellet is removed from the screen, pellet number is -= by 1.
#-print score change