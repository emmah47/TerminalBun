import time
import sys

basic_animation = [
    "  (\\(\\ \n  (o.o)\no(___)\n",
    "  (\\(\\ \n  (o.o)\no(___)\n",
    "  (\\(\\ \n  (o.o)\no(___)\n",
    "  (\\(\\ \n  (o.o)\no(___)\n",
    "   /)/) \n  (o.o)\no(___)\n",
    "   /)/) \n  (o.o)\no(___)\n",
    "   /)/) \n  (o.o)\no(___)\n",
    "  (\\(\\ \n  (o.o)\no(___)\n",
    "  (\\(\\ \n  (o.o)\no(___)\n",
    "  (\\(\\ \n  (o.o)\no(___)\n",
]

lie_down = [
    "\n   __(\\(\\ \no(___(-.-)\n",
    "\n   __(\\(\\ \no(___(-.-)\n",
    "\n   __(\\(\\ \no(___(-.-)\n",
    "\n   __(\\(\\ \no(___(-.-)\n",
    "\n   __(\\(\\ \no(___(-.-)\n",
    "\n   __(\\(\\ \no(___(-.-)\n",
    "\n   __(\\(\\ \no(___(o.o)\n",
    "\n   __(\\(\\ \no(___(-.-)\n",
    "\n   __(\\(\\ \no(___(o.o)\n",
    "\n   __(\\(\\ \no(___(o.o)\n",
    "\n   __(\\(\\ \no(___(o.o)\n",
]

welcomeMessage = "Welcome to the terminal~ Enjoy your stay! <3 "
messageLength = len(welcomeMessage)

def clear_screen():
    sys.stdout.write("\033[H\033[J")

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def set_cursor_position(row, col):
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()

def display_message():
    hide_cursor()
    for i in range(len(lie_down)):
        clear_screen()
        sys.stdout.write(lie_down[i % len(lie_down)])
        sys.stdout.flush()
        time.sleep(0.2)

    for i in range(len(basic_animation)):
        clear_screen()
        sys.stdout.write(basic_animation[i % len(basic_animation)])
        sys.stdout.flush()
        time.sleep(0.1)

    show_cursor()
    for i in range(messageLength):
        clear_screen()
        sys.stdout.write("  (\\(\\ \n")
        sys.stdout.write("  (>.o)" + "  " + welcomeMessage[0:i+1] + "\n")
        sys.stdout.write("o(___)\n")
        set_cursor_position(2, len("  (>.o)" + "  " + welcomeMessage[0:i+1]) + 1)
        sys.stdout.flush()
        if (i == messageLength - 1):
            # make cursor flash
            for j in range(3):
                hide_cursor()
                time.sleep(0.5)
                show_cursor()
                time.sleep(0.5)
            set_cursor_position(4, 0) # prevents bunny from being cleared once function ends
        else:
            time.sleep(0.05)

display_message()