from collections import defaultdict


button_system = defaultdict(int)
user_database_file = '../files/user_database.db'
usage_database_file = '../files/usage_database.db'

place_holder = ""

# Protein Color Separators
colors_1 = ["green", "black","blue", "red"]
colors_2 = ['purple', 'grey', 'violet', 'maroon']
colors_3 = ['indigo', 'magenta', 'teal', 'brown']

# Useful Variables
color_scheme = 'black'
text_color = 'orange'
window_font = "Menlo"
font_style = 'bold'

# No Going Subtraction Above 30
window_font_size = 30

# When Window Is Dark, The Colors Are Bright
bright_colors = ["cyan", "red", "yellow", "lime", "blue", "white"]
# When Window Is Bright, The Colors Are Dark
dull_colors = ['teal', 'brown', 'darkblue', 'gold', 'violet', 'black']

# Not below 2
corner = 5

# Not Below 0
border = 5

# viewport limit
view_limit = 5

# Frames - window background
# Scrollable or Success - gold / lime 3
# Label - white / black 5
# Buttons - blue / violet 4
# Entry - cyan / teal 0
# Errors - red / brown 1
# Text - orange
# Any or Hovers - yellow / lightblue 2

tip_switch = 0
tips = [f"The Above Frame Accumulates Only {view_limit} Graphs",
        "Commas Are Database Delimiters",
        "GUI Colors Are Used For Differentiation"]