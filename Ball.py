from Object import Object

import math

class Ball(Object):
    def __init__(self, parent, position, radius, dx, dy, color, group):
        super().__init__(position, (radius, radius), color, group)

        self.parent = parent
        self.position, self.x, self.y = position, position[0], position[1]
        self.radius = radius
        self.dx, self.dy = dx, dy

    def move(self):
        self.y += self.dy
        self.x += self.dx

        # Check anything that would cause abnormal movement
        self.check_boundaries()
        self.check_collision()
        self.position = (self.x, self.y)

    def check_boundaries(self):
        # Reverse y movement if hits top or bottom
        if self.y < 0:
            self.y = 0
            self.dy *= -1
        elif self.y > self.parent.height - self.radius:
            self.y = self.parent.height - self.radius
            self.dy *= -1

        # # Handle score if past side of screen, reset the ball if someone scored
        # if (self.x < 0) and not (self.parent.p1.y < self.y < self.parent.p1.y + self.parent.bumper_height):
        #     self.parent.score[1] += 1

        #     self.position = (self.parent.width + self.radius) / 2, (self.parent.height + self.radius) / 2
        #     self.dx, self.dy = self.parent.initial_ball_speed_x, self.parent.initial_ball_speed_y
        # elif self.x > self.parent.width - self.radius:
        #     self.parent.score[0] += 1

        #     self.position = (self.parent.width + self.radius) / 2, (self.parent.height + self.radius) / 2
        #     self.dx, self.dy = self.parent.initial_ball_speed_x, self.parent.initial_ball_speed_y

    def check_collision(self):
        # If ball is touching inside edge of bumper, or phased through bumper when it should have hit
        if (self.x <= self.parent.bumper_width) and (self.parent.p1.y < self.y < self.parent.p1.y + self.parent.bumper_height):
            # Then set ball to be at edge of bumper,
            self.x = self.parent.bumper_width

            # Calculate the centers of the ball and bumper,
            ball_center = (self.x + self.radius/2, self.y + self.radius/2)
            bumper_center = (self.parent.p1.x + self.parent.bumper_width/2, self.parent.p1.y + self.parent.bumper_height/2)

            # Find the distance in each dimension,
            distance_x = ball_center[0] - bumper_center[1]
            distance_y = ball_center[1] - bumper_center[1]

            # Calculate the collision angle using trig, *1.2 to make it more extreme
            collision_angle = math.atan2(distance_y, distance_x)

            # Increase the speed of the ball so game gets harder the longer it is played
            # And recalculate the velocity components using the collision angle
            speed = math.sqrt(math.pow(self.dx, 2) + math.pow(self.dy, 2)) + 0.5
            self.dy = math.sin(collision_angle) * speed
            self.dx = math.cos(collision_angle) * speed * -1
        # Same implementation as above but used for Player 2's bumper
        elif (self.x >= self.parent.width - (self.parent.bumper_width + self.radius)) and (self.parent.p2.y < self.y < self.parent.p2.y + self.parent.bumper_height):
            self.x = self.parent.width - (self.parent.bumper_width + self.radius)

            ball_center = (self.x + self.radius/2, self.y + self.radius/2)
            bumper_center = (self.parent.p2.x + self.parent.bumper_width/2, self.parent.p2.y + self.parent.bumper_height/2)

            distance_x = ball_center[0] - bumper_center[1]
            distance_y = ball_center[1] - bumper_center[1]

            collision_angle = math.atan2(distance_y, distance_x)

            speed = math.sqrt(math.pow(self.dx, 2) + math.pow(self.dy, 2)) + 0.5
            self.dy = math.sin(collision_angle) * speed
            self.dx = math.cos(collision_angle) * speed * -1

    def update(self):
        self.move()
        self.set_image()