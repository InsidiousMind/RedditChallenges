import curses


screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.addstr("Welcome to the Insidious' Calculator!")

screen.addstr("")


while True:
    event = screen.getch()
    if event == ord("q"): break
    elif event == curses.KEY_UP:
        screen.clear()
        screen.addstr(5, 0, "The User Pressed UP")
    elif event == curses.KEY_DOWN:
        screen.addstr(5, 0, "The User Pressed DOWN")


curses.endwin()

