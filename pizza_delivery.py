import os
import sys
import time


# ============================================================
#                    PROJECT CONFIGURATION
# ============================================================

PROJECT_NAME = "Welcome to pizza delivery"
PROJECT_VERSION = "v1.0.0"
DEVELOPER = "Ritu Raj"
ROLE = "Data Science & AI Developer"


# ============================================================
#                         COLORS
# ============================================================

RESET = "\033[0m"
BOLD = "\033[1m"

CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
WHITE = "\033[97m"
GRAY = "\033[90m"


# ============================================================
#                       UTILITIES
# ============================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def type_text(text, speed=0.015):
    """Print text with typing animation."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()


def slow_text(text, speed=0.03):
    """Slower typing animation."""
    type_text(text, speed)


def loading_bar(width=42, delay=0.025):
    """Display a smooth loading bar."""
    for i in range(width + 1):
        percent = int((i / width) * 100)

        filled = "█" * i
        empty = "░" * (width - i)

        print(
            f"\r{CYAN}[{filled}{empty}]{RESET} "
            f"{WHITE}{percent:3d}%{RESET}",
            end="",
            flush=True
        )

        time.sleep(delay)

    print()


def divider():
    print(f"{GRAY}╞{'═' * 66}╡{RESET}")


def status_ok(message):
    print(
        f"  {GREEN}✓{RESET} "
        f"{WHITE}{message:<52}{RESET}"
        f"{GREEN}[ OK ]{RESET}"
    )


def status_loading(message):
    print(
        f"  {YELLOW}›{RESET} "
        f"{WHITE}{message}{RESET}"
    )


# ============================================================
#                      START PROJECT
# ============================================================

clear_screen()

print()

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

print(f"{CYAN}╔{'═' * 66}╗{RESET}")
print(f"{CYAN}║{RESET}                                                                  {CYAN}║{RESET}")
print(
    f"{CYAN}║{RESET}"
    f"          {BOLD}{WHITE}R I T U   R A J{RESET}"
    f"                                  {CYAN}║{RESET}"
)
print(
    f"{CYAN}║{RESET}"
    f"          {GRAY}{ROLE}{RESET}"
    f"                        {CYAN}║{RESET}"
)
print(f"{CYAN}║{RESET}                                                                  {CYAN}║{RESET}")
print(f"{CYAN}╚{'═' * 66}╝{RESET}")

time.sleep(0.4)

print()

# ------------------------------------------------------------
# PROJECT TITLE
# ------------------------------------------------------------

print(f"{MAGENTA}┌{'─' * 66}┐{RESET}")

slow_text(
    f"{MAGENTA}│{RESET}  🚀  {BOLD}{CYAN}{PROJECT_NAME}{RESET}",
    0.018
)

print(
    f"{MAGENTA}│{RESET}"
    f"  {GRAY}Version: {PROJECT_VERSION}{RESET}"
)

print(f"{MAGENTA}└{'─' * 66}┘{RESET}")

time.sleep(0.4)

# ------------------------------------------------------------
# WELCOME MESSAGE
# ------------------------------------------------------------

print()

slow_text(
    f"{YELLOW}  WELCOME DEVELOPER 👨‍💻{RESET}",
    0.03
)

slow_text(
    f"{WHITE}  Welcome to another step of the coding journey.{RESET}",
    0.018
)

slow_text(
    f"{GRAY}  Code • Learn • Build • Improve • Repeat{RESET}",
    0.018
)

print()

# ------------------------------------------------------------
# INITIALIZATION
# ------------------------------------------------------------

divider()

print()
slow_text(
    f"{BLUE}{BOLD}  INITIALIZING PROJECT ENVIRONMENT...{RESET}",
    0.02
)

print()

status_loading("Starting Python runtime...")
time.sleep(0.25)
status_ok("Python runtime")

status_loading("Loading data processing modules...")
time.sleep(0.25)
status_ok("Data processing")

status_loading("Preparing machine learning environment...")
time.sleep(0.25)
status_ok("Machine learning")

status_loading("Initializing AI components...")
time.sleep(0.25)
status_ok("Artificial intelligence")

status_loading("Checking project configuration...")
time.sleep(0.25)
status_ok("Project configuration")

print()

# ------------------------------------------------------------
# LOADING BAR
# ------------------------------------------------------------

slow_text(
    f"{CYAN}  BUILDING PROJECT ENVIRONMENT{RESET}",
    0.02
)

loading_bar()

time.sleep(0.3)

# ------------------------------------------------------------
# SYSTEM STATUS
# ------------------------------------------------------------

print()

divider()

print()

print(
    f"  {GREEN}●{RESET} "
    f"{WHITE}SYSTEM STATUS{RESET}"
    f"                    {GREEN}ONLINE{RESET}"
)

print(
    f"  {BLUE}●{RESET} "
    f"{WHITE}PROJECT STATUS{RESET}"
    f"                  {GREEN}READY{RESET}"
)

print(
    f"  {MAGENTA}●{RESET} "
    f"{WHITE}DEVELOPER{RESET}"
    f"                      {CYAN}{DEVELOPER}{RESET}"
)

print(
    f"  {YELLOW}●{RESET} "
    f"{WHITE}MISSION{RESET}"
    f"                        {YELLOW}BUILD SOMETHING GREAT{RESET}"
)

print()

divider()

# ------------------------------------------------------------
# CODING JOURNEY
# ------------------------------------------------------------

print()

slow_text(
    f"{WHITE}        CODE  →  LEARN  →  BUILD  →  TEST{RESET}",
    0.025
)

slow_text(
    f"{WHITE}             →  IMPROVE  →  DEPLOY{RESET}",
    0.025
)

slow_text(
    f"{CYAN}                    →  MASTER 🚀{RESET}",
    0.025
)

print()

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

print(f"{GRAY}{'─' * 68}{RESET}")

slow_text(
    f"{MAGENTA}        R I T U   R A J   •   D A T A   •   A I{RESET}",
    0.025
)

slow_text(
    f"{GRAY}             Turning ideas into working projects.{RESET}",
    0.02
)

print()

print(f"{GRAY}{'─' * 68}{RESET}")

print()

slow_text(
    f"{GREEN}  ✓ PROJECT INITIALIZATION COMPLETE{RESET}",
    0.025
)

slow_text(
    f"{CYAN}  🚀 Let's build something amazing!{RESET}",
    0.025
)

print()
time.sleep(0.5)




print("--------Welcome to pizza delivery--------")
print(" \n")
# print("")
print("Prise based on Size of pizza :-  ")
print("")
print("$8  for Small (S) ")
print("$10  for medium (M) ")
print("$12  for Large (L) ")
print(" \n")
# print("")
size = input("Enter size of pizza. S / M / L  :  ")
print("")
papperoni = input("Do you want papperoni on your pizza ? Y or N  :  ")
print("")
extra_chease = input("Do you wnat extra chease ? y or N  : ")
print("")

size = size.capitalize()
papperoni = papperoni.capitalize()
extra_chease = (extra_chease).capitalize()
price = 0

if size == "S" :
    price += 8
    if papperoni == "Y":
        price +=2
        if extra_chease == "Y":
            price += 1
        else:
            pass
    elif papperoni == "N":
            if extra_chease == "Y":
                price += 1
            else:
                pass
    else:
            pass
elif size == "M" :
    price += 20
    if papperoni == "Y":
        price +=2
        if extra_chease == "Y":
            price += 1
        else:
            pass
    elif papperoni == "N":
            if extra_chease == "Y":
                price += 1
            else:
                pass
    else:
            pass
elif size == "L" :
    price += 25
    if papperoni == "Y":
        price +=2
        if extra_chease == "Y":
            price += 1
        else:
            pass
    elif papperoni == "N":
            if extra_chease == "Y":
                price += 1
            else:
                pass
    else:
            pass
else :
    pass

print(f"Your total bill is = ${price} ")
