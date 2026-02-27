# Write your game here
import curses 

game_data = {
    # Store board dimensions, player/enemy positions, score, energy, collectibles, and icons
    'width': 5,
    'height': 5,
    'player': {"x": 0, "y": 0, "score": 0, "energy": 10, "max_energy": 10},
    'eagle_pos': {"x": 4, "y": 4},
    'collectibles': [
        {"x": 2, "y": 1, "collected": False},
    ],
    'obstacles': [
        {"x": 1, "y": 2},
        {"x": 3, "y": 1}
    ],

    # ASCII icons
    'pac_cat_moving': "\U0001F63C",
    'pac_cat_eating': "\U0001F638",
    'pac_cat_dying': "\U0001F640",
    'ghost': "\U0001F47B",
    'wall': "\U0001F9CD ",
    'pellet': "\U0001F9C0",
    'empty': "  "
}

def draw_board(screen):
    # Print the board and all game elements using curses


# Good Luck!