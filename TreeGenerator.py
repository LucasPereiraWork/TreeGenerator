import os
import random
import pygame
import sys
from typing import List, Tuple


def play_sound(filepath):
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(loops=-1)

def adjust_volume(value: int):
    if value < 0 or value > 10:
        print("Please input valid value")
        adjust_volume_menu()
    pygame.mixer.music.set_volume(value * 0.1)
    main_menu()

def clear_console():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def resource_path(relative_path):
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def select_background_music():

    clear_console()

    print("1 - music 1\n")
    print("2 - music 2\n")
    print("3 - music 3\n")
    print("4 - music 4\n")
    print("5 - music 5\n")
    print("6 - music 6\n")
    print("7 - Exit to main menu\n\n")

    songpath = 'Songs'
    songnumber = int(input("Enter the number of the background song you want to play: ") or "1")
    songname = ''

    match songnumber:
        case 1:
            songname = 'Cristano_s_Ronaldo_siiiiii_but_it_s_jingle_bell_rock.mp3'
        case 2:
            songname = 'Feliz_Bottom_Jeans_-_Jose_Feliciano_1970.mp3'
        case 3:
            songname = 'toad_sings_all_i_want_for_christmas_is_you.mp3'
        case 4:
            songname = 'Ed_Sheeran_Elton_John_-_Merry_Christmas_Official_Video.mp3'
        case 5:
            songname = 'Jose_Feliciano_-_Feliz_Navidad_Official_Audio.mp3'
        case 6:
            songname = 'Mariah_Carey_-_All_I_Want_for_Christmas_Is_You_Make_My_Wish_Come_True_Edition'
        case 7:
            main_menu()
        case _:
            print("Please select a valid option")
            select_background_music()

    sound_file_path = resource_path(os.path.join(songpath, songname))
    play_sound(sound_file_path)
    main_menu()

def main_menu():

    clear_console()

    print("1 - Background Music\n")
    print("2 - Create Tree\n")
    print("3 - Adjust volume\n")
    print("4 - Exit the program\n\n")

    option = int(input("Select a number option: "))

    match option:
        case 1:
            select_background_music()
        case 2:
            try_generate_tree()
        case 3:
            adjust_volume_menu()
        case 4:
            exit()
        case _:
            print("Select valid option")
            main_menu()

def adjust_volume_menu():
    clear_console()
    print("11 - Exit")
    value = int(input("Adjust volume(1 - 10): "))
    if value == 11:
        main_menu()
    adjust_volume(value)

def try_generate_tree():
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

    #main_menu()

def generate_tree(height: int, symbol: str = '*') -> List[Tuple[str, List[Tuple[str, str]]]]:
    """
    Generate and display a Christmas tree in the console using emojis and Unicode decorations.
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
    
    # Emoji decorations
    decorations = ['🎄', '🎁', '⭐', '✨', '🎀', '🌟', '❄️', '🎅']
    
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
            row.append(f"{staryellow}⭐{reset}")
            pattern_row.append(('⭐', staryellow))
        else:
            # Generate other rows
            for j in range(2 * i + 1):
                decoration_chance = random.random()
                if decoration_chance < 0.2:  # 20% chance for emoji decoration
                    decoration = random.choice(decorations)
                    row.append(decoration)
                    pattern_row.append((decoration, ''))
                elif decoration_chance < 0.4:  # 20% chance for colored symbol
                    color = random.choice(colors)
                    row.append(f"{color}{symbol}{reset}")
                    pattern_row.append((symbol, color))
                else:
                    row.append(f"{white}{symbol}{reset}")
                    pattern_row.append((symbol, white))
        
        # Print the row
        print(f"{spaces}{''.join(row)}")
        tree_pattern.append((spaces, pattern_row))
    
    # Add a simple decorative base
    base_width = min(2 * (height - 1) + 1, 8)
    base_pattern = [(random.choice(['🪵', '🪓']), '') for _ in range(base_width)]
    
    # Center the base
    base_space = " " * (height - len(base_pattern)//2 - 1)
    base_row = []
    for symbol, _ in base_pattern:
        base_row.append(symbol)
    print(base_space + "".join(base_row))
    tree_pattern.append((base_space, base_pattern))
    
    # Add the trunk
    trunk_height = height // 3
    trunk_width = height // 3
    for i in range(trunk_height):
        trunk_space = " " * (height - trunk_width // 2 - 1)
        trunk_row = ['🪵'] * trunk_width
        print(trunk_space + "".join(trunk_row))
        tree_pattern.append((trunk_space, [(char, '') for char in trunk_row]))
    
    return tree_pattern


def save_as_png(tree_pattern, height, filename='christmas_tree.png'):
    from PIL import Image, ImageDraw, ImageFont
    import platform
    
    # Set dimensions
    char_width = 40  # Increased for emoji visibility
    char_height = 40
    padding = 100
    img_width = (max(len(row[1]) for row in tree_pattern) * char_width) + (2 * padding)
    img_height = (len(tree_pattern) * char_height) + (2 * padding)

    # Create the image with a dark background
    image = Image.new('RGB', (img_width, img_height), (10, 20, 40))
    draw = ImageDraw.Draw(image)

    # Try to find and load a system emoji font
    try:
        if platform.system() == 'Windows':
            possible_fonts = [
                "seguiemj.ttf",  # Segoe UI Emoji
                "segoe ui emoji.ttf",
                "C:\\Windows\\Fonts\\seguiemj.ttf"
            ]
        elif platform.system() == 'Darwin':  # macOS
            possible_fonts = [
                "/System/Library/Fonts/Apple Color Emoji.ttc",
                "/System/Library/Fonts/AppleColorEmoji.ttf"
            ]
        else:  # Linux
            possible_fonts = [
                "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",
                "/usr/share/fonts/noto-emoji/NotoColorEmoji.ttf",
                "/usr/share/fonts/google-noto/NotoColorEmoji.ttf",
                "/usr/share/fonts/emoji/NotoColorEmoji.ttf"
            ]

        font = None
        for font_path in possible_fonts:
            try:
                font = ImageFont.truetype(font_path, 30)
                print(f"Successfully loaded emoji font: {font_path}")
                break
            except OSError:
                continue

        if font is None:
            raise Exception("No emoji font found")

    except Exception as e:
        print(f"Warning - font loading issue: {e}")
        print("Attempting to use system default font...")
        font = ImageFont.load_default()

    # Define colors
    color_map = {
        '\033[31m': (255, 50, 50),    # Red
        '\033[32m': (50, 255, 50),    # Green
        '\033[33m': (255, 255, 50),   # Yellow
        '\033[34m': (50, 50, 255),    # Blue
        '\033[35m': (255, 50, 255),   # Purple
        '\033[36m': (50, 255, 255),   # Cyan
        '\033[37m': (255, 255, 255),  # White
    }

    # Draw tree
    y = padding
    try:
        for spaces, row in tree_pattern:
            # Center the row
            total_row_width = len(row) * char_width
            x = (img_width - total_row_width) // 2

            for char, color in row:
                # Preserve emoji characters
                rgb_color = color_map.get(color, (255, 255, 255))
                
                # Handle both emojis and regular characters
                try:
                    draw.text((x, y), char, font=font, fill=rgb_color, embedded_color=True)
                except:
                    # Fallback for older Pillow versions
                    draw.text((x, y), char, font=font, fill=rgb_color)
                
                x += char_width
            y += char_height

        # Save image
        image.save(filename)
        print(f"Tree successfully saved as {filename}")
        print("Note: If emojis aren't visible, please install an emoji font:")
        print("Windows: Segoe UI Emoji")
        print("macOS: Apple Color Emoji")
        print("Linux: Noto Color Emoji (package: fonts-noto-color-emoji)")
        return True

    except Exception as e:
        print(f"Error creating image: {e}")
        return False

def main():

    clear_console()

    print("Christmas Tree Generator")
    print("-----------------------\n")

    main_menu()


if __name__ == "__main__":
    main()
