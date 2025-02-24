def solitaire_banner(color=False):
    # Card designs for each letter in "SOLITAIRE"
    cards = [
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♥' if color else 'H', 'S', '♥' if color else 'H'),
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♦' if color else 'D', 'O', '♦' if color else 'D'),
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♣' if color else 'C', 'L', '♣' if color else 'C'),
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♠' if color else 'S', 'I', '♠' if color else 'S'),
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♥' if color else 'H', 'T', '♥' if color else 'H'),
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♦' if color else 'D', 'A', '♦' if color else 'D'),
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♣' if color else 'C', 'I', '♣' if color else 'C'),
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♠' if color else 'S', 'R', '♠' if color else 'S'),
        """
        .------.
        |{}    |
        |  {}  |
        |    {}|
        `------´""".format('♥' if color else 'H', 'E', '♥' if color else 'H'),
    ]

    # Combine cards horizontally
    banner_lines = [""] * 5
    for card in cards:
        lines = card.strip().split('\n')
        for i in range(5):
            banner_lines[i] += lines[i] + "  "

    # Add color if requested (red for hearts/diamonds, black for clubs/spades)
    if color:
        colored_banner = []
        for line in banner_lines:
            colored_line = line
            colored_line = colored_line.replace('♥', '\033[91m♥\033[0m')
            colored_line = colored_line.replace('♦', '\033[91m♦\033[0m')
            colored_line = colored_line.replace('♣', '\033[90m♣\033[0m')
            colored_line = colored_line.replace('♠', '\033[90m♠\033[0m')
            colored_banner.append(colored_line)
        return "\n".join(colored_banner)

    return "\n".join(banner_lines)


# Print the banner (with color if supported)
print(solitaire_banner(color=True))

# multiple banners
def display_welcome_banner(choice):
    if choice == "Solitaire":
        banner_one = """*************
* Solitaire *
*************"""
        return banner_one
    else:
        return ""


def display_banner(name):
    name_part = f"{{{name}}}"
    total_length = 35
    content_length = total_length - 2  # Accounting for the two '#' characters
    name_length = len(name_part)

    # Handle cases where the name is too long by truncating (optional)
    if name_length > content_length:
        name_part = name_part[:content_length]
        name_length = content_length

    total_dashes = content_length - name_length
    left_dashes = total_dashes // 2
    right_dashes = total_dashes - left_dashes

    middle_line = f"#{'-' * left_dashes}{name_part}{'-' * right_dashes}#"
    top_bottom = '#' * total_length

    return f"{top_bottom}\n{middle_line}\n{top_bottom}"


def main():
    # Call the display_banner function with different game names
    print(display_banner("Solitaire"))
    print(display_banner("PacMan"))
    print(display_banner("Tetris"))
    print(display_banner("Super Mario"))


# Ensure the main function is called when the script is run
if __name__ == "__main__":
    main()


# def solitaire_banner():
#     banner = '      \u2554' + '\u2550'*59 + '\u2557' + '\n'
#     banner += "\u2551  \u2660  \u2665  \u2666  \u2663    L E T ' S   P L A Y   S O L I T A I R E    \u2663  \u2666  \u2665  \u2660  \u2551\n"
#     banner += '      \u255a' + '\u2550'*59 + '\u255D'
#     return banner

# def solitaire_banner():
#     banner = f"""
#           ╔═══════════════════════════════════════════════════════════╗
#     ║  ♠  ♥  ♦  ♣    L E T ' S   P L A Y   S O L I T A I R E    ♣  ♦  ♥  ♠  ║
#           ╚═══════════════════════════════════════════════════════════╝
#     """
#     return banner
