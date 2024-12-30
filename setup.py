import os

def run_commands():
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
        "termux-setup-storage"
    ]

    for command in commands:
        print(f"Running: {command}")
        os.system(command)

if __name__ == "__main__":
    print("Starting Termux setup...")
    run_commands()
    print("Setup completed!")
