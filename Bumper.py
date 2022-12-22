from Object import Object

class Bumper(Object):
    def __init__(self, parent, position, size, dy, color, group):
        super().__init__(position, size, color, group)

        self.parent = parent
        self.position, self.x, self.y = position, position[0], position[1]
        self.width, self.height = size[0], size[1]
        self.dy = dy

    def move(self, direction):
        match direction:
            case "up":
                self.y -= self.dy
            case "down":
                self.y += self.dy

        self.check_boundaries()
        self.position = (self.x, self.y)

    def check_boundaries(self):
        # Revert movement if outside screen
        if self.y < 0:
            self.y = 0
        elif self.y > self.parent.height - self.height:
            self.y = self.parent.height - self.height

    def update(self):
        self.set_image()
