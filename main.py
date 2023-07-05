from settings import *
import pygame as pg
import time
import sys


def Main():
    pg.init()
    from objects import Cube, SineMovement, Graphing

    # Window and canas setup
    window = pg.display.set_mode(WINDOW_SIZE)
    canvas = pg.Surface(WINDOW_SIZE)

    # Clock and Time
    clock = pg.time.Clock()
    prevTime = time.time()

    # Variables
    cube1 = Cube(25, 400, 16, 16, COLOR["blue"],
                 components=[
                     # Moves the cube in a wave like motion.
                     SineMovement(3, 3),  # (speed, waveRange)
                     Graphing(COLOR["blue"], 1)
                 ])

    cube2 = Cube(25, 150, 16, 16, COLOR["red"],
                 components=[
                     # Moves the cube in a wave like motion.
                     SineMovement(5, 5),  # (speed, waveRange)
                     Graphing(COLOR["red"], 1)
                 ])

    # Does everything related to time.
    def tickClock():
        # Guessing this ticks the clock. Who would've guessed!
        clock.tick(FPS)
        # Sets window caption to fps.
        pg.display.set_caption(f"{round(clock.get_fps())}")
        # Gets the current program time
        now = time.time()
        # Calulates delta time value
        dt = now - prevTime

        return now, dt

    # Handles what to do when certain events occur
    def eventHandler():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    # Draws and blits every element on screen.
    def refresh():
        # Refreshes the screen
        canvas.fill(COLOR["black"])

        # Draws game elements
        cube1.draw(canvas)
        cube2.draw(canvas)

        # Blit canvas to window and update the screen to reflect changes
        window.blit(canvas, (0, 0))
        pg.display.flip()

    # Main loop
    while True:
        # Runs the tickClock function while also getting current time and delta time
        curTime, deltaTime = tickClock()
        # Syncs prevTime with curTime
        prevTime = curTime
        # Handles events
        eventHandler()

        # Updates cube 1
        cube1.update()
        # Updates cube 2
        cube2.update()

        # draws the game and updates the screen
        refresh()


# This is the entry point! Run this first!
if __name__ == '__main__':
    Main()
