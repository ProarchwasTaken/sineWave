from main import *
import math
import numpy as np


# Basic cube Class
class Cube:
    # Runs at instance initialization
    def __init__(self, x, y, width, height, color, components=list()):
        # Basic rect setup
        self.rect = pg.Rect(x, y, width, height)
        self.color = color

        # Gives the ability to add extensions to the instance
        self.component = np.array(components)

    # Runs once per frame
    def update(self):
        # Updates each component if there is any.
        for component in self.component:
            component.update(self)

    # Draws the object and it's component
    def draw(self, surface):
        # Draws the instance.
        pg.draw.rect(surface, self.color, self.rect)

        # Draws each component if it has a draw function.
        for component in self.component:
            try:
                component.draw(surface)
            except AttributeError:
                pass


# Component class. When added to a class instance. It will cause it to move in a sine wave function
class SineMovement:
    # Runs on component initialization
    def __init__(self, speed, waveRange):
        self.speed = speed
        self.waveRange = waveRange

    # Runs once per frame
    def update(self, parent):
        # Moves the parent instance up and down based on sine
        parent.rect.y += round(math.sin(time.time() * self.speed) * self.waveRange)


# Component. When assigned to a class instance, it will graph its movement on the Y axis
class Graphing:
    # Runs on component initialization
    def __init__(self, color, pointSpeed):
        # The color on all points
        self.pointColor = color

        # How fast each point will move.
        self.pointSpeed = pointSpeed

        # Saves a list of all point rects
        self.pointList = list()

    # Runs once per frame
    def update(self, parent):
        # Gets center position of parent
        centerX, centerY = parent.rect.centerx, parent.rect.centery

        # Creates a new point and add it to the list.
        self.pointList.append(pg.Rect(centerX, centerY, 4, 4))

        for point in self.pointList:
            point.x += self.pointSpeed

            # Check if the point is outside the screen, if so, then it will delete itself.
            if point.left > WIDTH:
                self.pointList.remove(point)

    # Draws every point.
    def draw(self, surface):
        for point in self.pointList:
            pg.draw.rect(surface, self.pointColor, point)

