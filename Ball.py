from Object import Object

import math

class Ball(Object):
    def __init__(self, parent, position, size, dx, dy, color, group, collision_group):
        super().__init__(position, size, color, group)

        self.parent = parent
        self.position, self.x, self.y = position, position[0], position[1]
        self.width, self.height = size[0], size[1]
        self.dx, self.dy = dx, dy
        self.collision_group = collision_group

    def move(self):
        pass # TODO calculate position change from angle

        self.check_boundaries()
        self.check_collision()
        self.position = (self.x, self.y)

    def check_boundaries(self):
        # Revert movement if outside screen
        if self.y < 0:
            self.y = 0
        elif self.y > self.parent.height - self.height:
            self.y = self.parent.height - self.height
        if self.x < 0:
            self.x = 0
        elif self.x > self.parent.width - self.width:
            self.x = self.parent.width - self.width

    def check_collision(self):
        pass #TODO

    def update(self):
        self.move()
        self.set_image()