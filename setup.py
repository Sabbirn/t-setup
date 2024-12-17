import os
import shutil

def print_banner():
    # Get the width of the terminal
    terminal_width = shutil.get_terminal_size().columns
    
    # Text for the banner and author's name
    banner_text = "T - Setup"
    author_text = "Author: Md.Sabbir Sheikh"  # Replace with the actual author's name
    
    # Function to center the text
    def center_text(text):
        return text.center(terminal_width)
    
    # Colorful text using ANSI escape codes
    print("\033[1;35m")  # Purple color for the banner
    os.system(f"figlet '{banner_text}'")  # Generates a banner using 'figlet'
    print("\033[1;37m")  # Resetting the color
    
    # Add author's name at the bottom of the banner
    print("\033[1;36m")  # Cyan color for the author's name
    print(center_text(author_text))  # Center the author's name
    print("\033[1;37m")  # Resetting the color

def install_packages():
    # List of commands to execute
    commands = [
        "apt update",
        "apt upgrade -y",
        "pkg install python -y",
        "pkg install python2 -y",
        "pkg install python3 -y",
        "pkg install git -y",
        "pkg install figlet -y",
        "pkg install cmatrix -y",
        "pkg install toilet -y",
        "pkg install nano -y",
        "pkg install php -y",
        "pkg install pip -y",
        "pkg install pip2 -y",
        "pip2 install requests",
        "pip install future",
        "pip2 install requirements",
        "apt install ruby -y",
        "apt install openssh -y",
        "apt install wget -y",
        "apt install curl -y",
        "termux-setup-storage",
        "git clone https://github.com/Sabbirn/termux-banner.git",
        "cd termux-banner && clear && ls && bash t-header.sh",
        "exit"
    ]

    # Execute commands sequentially
    for command in commands:
        print(f"Running: {command}")
        status = os.system(command)
        if status != 0:
            print(f"Command failed: {command}")
            break  # Exit if any command fails

if __name__ == "__main__":
    print_banner()  # Display the banner
    install_packages()
