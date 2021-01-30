# Programming assignment 5
# button.py
# partial code from Zelle chapter 10 (pp. 324)


from graphics import *

# define button class


class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        # as you read through this, ask yourself:  what are the instance variables here?
        # it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        # you should comment these variables...
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        # this variable keeps track of whether or not the button is currently "active"
        self.active = True

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')  # color the text "black"
        self.rect.setWidth(2)  # set the outline to look bolder
        self.active = True  # set the boolean variable that tracks "active"-ness to True

    def deactivate(self):
        "Sets this button to 'inactive'."
        # color the text "darkgray"
        # set the outline to look finer/thinner
        # set the boolean variable that tracks "active"-ness to False
        self.label.setFill("grey")
        self.rect.setWidth(1/2)
        self.activate = False

    "Returns true if button active and Point p is inside"

    def clicked(self, pt):
        x = pt.getX()
        y = pt.getY()
        if self.xmin < x and self.xmax > x and self.ymin < y and self.ymax > y:
            return True
        else:
            return False


def main():
    print()


main()
if __name__ == '__main__':
    main()
