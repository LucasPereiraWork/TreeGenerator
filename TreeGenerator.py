import os
import random
from typing import List, Tuple
import pygame

def play_sound(filepath):
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()



def generate_tree(height: int, symbol: str = '*') -> List[Tuple[str, List[Tuple[str, str]]]]:
    """
    Generate and display a Christmas tree in the console.
    Returns the tree pattern for potential PNG conversion.
    """
    # ANSI color codes
    colors = [
        '\033[31m',  # Red
        '\033[32m',  # Green
        '\033[33m',  # Yellow
        '\033[34m',  # Blue
        '\033[35m',  # Purple
        '\033[36m',  # Cyan
    ]
    staryellow = '\033[33m'
    white = '\033[37m'    # White color
    reset = '\033[0m'     # Reset color code
    
    # Non-emoji decorations (more reliable for PNG output)
    decorations = ['*', '+', 'o', '°', '⚹', '✦', '✯', '✷']
    
    # Store tree pattern for PNG conversion
    tree_pattern = []
    
    # Generate the tree
    for i in range(height):
        # Calculate spaces before the symbols
        spaces = " " * (height - i - 1)
        # Generate row with random colored ornaments
        row = []
        pattern_row = []  # Store characters and colors for PNG conversion
        
        # Handle the first row (top of tree) specially
        if i == 0:
            color = staryellow
            row.append(f"{color}✯{reset}")
            pattern_row.append(('✯', color))
        else:
            # Generate other rows
            for j in range(2 * i + 1):
                decoration_chance = random.random()
                if decoration_chance < 0.1:  # 10% chance for decoration
                    color = random.choice(colors)
                    decoration = random.choice(decorations)
                    row.append(f"{color}{decoration}{reset}")
                    pattern_row.append((decoration, color))
                elif decoration_chance < 0.3:  # 20% chance for colored symbol
                    color = random.choice(colors)
                    row.append(f"{color}{symbol}{reset}")
                    pattern_row.append((symbol, color))
                else:
                    row.append(f"{white}{symbol}{reset}")
                    pattern_row.append((symbol, white))
        
        # Print the row
        print(f"{spaces}{''.join(row)}")
        tree_pattern.append((spaces, pattern_row))
    
    # Add a simple decorative base (using stars and plus signs)
    base_width = min(2 * (height - 1) + 1, 8)
    base_pattern = []
    for i in range(base_width):
        color = random.choice(colors)
        symbol = random.choice(['*', '+', '✦'])
        base_pattern.append((symbol, color))
    
    # Center the base
    base_space = " " * (height - len(base_pattern)//2 - 1)
    base_row = []
    for symbol, color in base_pattern:
        base_row.append(f"{color}{symbol}{reset}")
    print(base_space + "".join(base_row))
    tree_pattern.append((base_space, base_pattern))
    
    # Add the trunk
    trunk_height = height // 3
    trunk_width = height // 3
    brown = '\033[33m'  # Brown color for trunk
    for i in range(trunk_height):
        trunk_space = " " * (height - trunk_width // 2 - 1)
        trunk_row = []
        pattern_trunk = []
        for j in range(trunk_width):
            trunk_row.append(f"{brown}#{reset}")
            pattern_trunk.append(('#', brown))
        print(trunk_space + "".join(trunk_row))
        tree_pattern.append((trunk_space, pattern_trunk))
    
    return tree_pattern

def save_as_png(tree_pattern: List[Tuple[str, List[Tuple[str, str]]]], height: int, filename: str = 'christmas_tree.png') -> bool:
    """
    Save the tree pattern as a PNG file with proper centering.
    """
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Error: Pillow library not installed. Please install it using:")
        print("pip install Pillow")
        return False

    # Image dimensions with padding
    char_width = 30  # Increased for better spacing
    char_height = 40
    padding = 100  # Additional padding around the tree
    
    # Calculate maximum tree width
    max_tree_width = max(len(pattern_row) for _, pattern_row in tree_pattern) * char_width
    
    # Set image dimensions with padding
    img_width = max_tree_width + (2 * padding)
    img_height = (len(tree_pattern) * char_height) + (2 * padding)
    
    # Create image with dark blue background
    image = Image.new('RGB', (img_width, img_height), (10, 20, 40))
    draw = ImageDraw.Draw(image)
    
    # Try to load a font that supports decorative characters
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", 25)
        except:
            font = ImageFont.load_default()
    
    # Color mapping from ANSI to RGB
    color_map = {
        '\033[31m': (255, 0, 0),     # Red
        '\033[32m': (0, 255, 0),     # Green
        '\033[33m': (255, 255, 0),   # Yellow
        '\033[34m': (0, 0, 255),     # Blue
        '\033[35m': (255, 0, 255),   # Purple
        '\033[36m': (0, 255, 255),   # Cyan
        '\033[37m': (255, 255, 255), # White
    }
    
    # Draw tree centered
    y = padding  # Start with vertical padding
    for spaces, row in tree_pattern:
        # Calculate x position to center the row
        row_width = len(row) * char_width
        x = (img_width - row_width) // 2
        
        for char, color in row:
            # Draw the character
            draw.text((x, y), char, font=font, fill=color_map[color])
            x += char_width
        y += char_height
    
    # Save image
    image.save(filename)
    print(f"Tree saved as {filename}")
    return True

def main():
    print("Christmas Tree Generator")
    print("-----------------------")

    songpath = 'D:\LucasRandomProjects\TreeGenerator\songs'
    print("1 - Cristano_s_Ronaldo_siiiiii_but_it_s_jingle_bell_rock\n2 - Feliz_Bottom_Jeans_-_Jose_Feliciano_1970\n3 - toad_sings_all_i_want_for_christmas_is_you")
    songnumber = int(input("Enter the number of the song you want to play: ") or "1")
    songname = ''

    match songnumber:
        case 1:
            songname = 'Cristano_s_Ronaldo_siiiiii_but_it_s_jingle_bell_rock.mp3'
        case 2:
            songname = 'Feliz_Bottom_Jeans_-_Jose_Feliciano_1970.mp3'
        case 3:
            songname = 'toad_sings_all_i_want_for_christmas_is_you.mp3'


    play_sound(os.path.join(songpath, songname))
    
    try:
        height = int(input("Enter the height of the tree (recommended 10-20): "))
        if height <= 0:
            raise ValueError("Height must be positive")
        
        symbol = input("Enter the base symbol to use (default is *): ") or '*'
        
        # Generate and display the tree
        tree_pattern = generate_tree(height, symbol)
        
        # Ask if user wants to save as PNG
        save_choice = input("\nWould you like to save the tree as a PNG? (y/n): ").lower()
        if save_choice.startswith('y'):
            filename = input("Enter the output filename (default is christmas_tree.png): ") or 'christmas_tree.png'
            save_as_png(tree_pattern, height, filename)
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter a valid positive number for height.")

if __name__ == "__main__":
    main()