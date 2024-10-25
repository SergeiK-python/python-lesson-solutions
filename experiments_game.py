import arcade


# Some problems with Pyton version after 3.11 with:  pip install arcade
# use https://github.com/pythonarcade/arcade/archive/master.zip and then: pip install -e .
# or: pip install -e .[dev] to install with additional documentation and development requirements (it does not work)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pong Game"


class Bar(arcade.Sprite):
    INITIAL_SPEED_X = 10
    INITIAL_WIDTH_X = 0
    INITIAL_OFFSET_Y = 0

    def __init__(self):
        super().__init__('./resources/bar.png', 0.4)
        Bar.INITIAL_WIDTH_X = self.width * 0.6
        Bar.INITIAL_OFFSET_Y = self.center_y - self.height / 2
        self.moving = False
        self.change_x = 0
        self.change_y = 0

    def update(self):
        if self.moving:
            if self.change_x > 0:
                if self.center_x + self.change_x > SCREEN_WIDTH - Bar.INITIAL_WIDTH_X / 2:
                    self.center_x = SCREEN_WIDTH - Bar.INITIAL_WIDTH_X / 2
                    self.moving = False
                else:
                    self.center_x += self.change_x
            else:
                if self.center_x + self.change_x <Bar.INITIAL_WIDTH_X / 2:
                    self.center_x = Bar.INITIAL_WIDTH_X / 2
                    self.moving = False
                else:
                    self.center_x += self.change_x

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.change_x = -Bar.INITIAL_SPEED_X
            self.moving = True
        elif key == arcade.key.RIGHT:
            self.change_x = Bar.INITIAL_SPEED_X
            self.moving = True

    def get_boarder(self):
        return self.center_x - Bar.INITIAL_WIDTH_X / 2, self.center_x + Bar.INITIAL_WIDTH_X / 2

class Ball(arcade.Sprite):
    INITIAL_SPEED_X = 5
    INITIAL_SPEED_Y = 5

    def __init__(self, bar: Bar):
        super().__init__('./resources/ball.png', 0.05)
        Ball.INITIAL_SPEED_X = self.width / 4
        Ball.INITIAL_SPEED_Y = - self.height / 4
        self.change_x = Ball.INITIAL_SPEED_X
        self.change_y = Ball.INITIAL_SPEED_Y
        self.bar = bar

    def update(self):
        bar_boarder = self.bar.get_boarder()
        if self.change_x > 0:
            if self.center_x + self.change_x > SCREEN_WIDTH - self.width / 2:
                self.center_x = SCREEN_WIDTH - self.width / 2
                self.change_x = - Ball.INITIAL_SPEED_X
            else:
                self.center_x += self.change_x
        else:
            if self.center_x + self.change_x < self.width / 2:
                self.center_x = self.width / 2
                self.change_x = Ball.INITIAL_SPEED_X
            else:
                self.center_x += self.change_x

        if self.change_y > 0:
            if self.center_y + self.change_y > SCREEN_HEIGHT - self.height / 2:
                self.center_y = SCREEN_HEIGHT - self.height / 2
                self.change_y = Ball.INITIAL_SPEED_Y
            else:
                self.center_y += self.change_y
        else:
            if self.center_y + self.change_y < self.height / 2:
                self.center_y = self.height / 2
                self.change_y = - Ball.INITIAL_SPEED_Y
            elif self.check_conflict():
                pass
            else:
                self.center_y += self.change_y

    def check_conflict(self):
        if self.change_y >= 0:
            return False
        elif self.center_y + self.change_y < Bar.INITIAL_OFFSET_Y - self.height / 2:
            return False
        elif self.center_y >= Bar.INITIAL_OFFSET_Y - self.height / 2:
            return False

        boarder = self.bar.get_boarder()
        if self.change_x > 0:
            if boarder.index(0) - self.height / 2 > self.center_x + self.change_x:
                return False
            if boarder.index(0) - self.height / 2 <= self.center_x + self.change_x <= boarder.index(0):
                self.center_x = boarder.index(0) - self.height / 2
                self.change_x = - Ball.INITIAL_SPEED_X
                return True
            elif self.center_x + self.change_x <= boarder.index(1):
                self.center_y = Bar.INITIAL_OFFSET_Y - self.height / 2
                self.change_y = - Ball.INITIAL_SPEED_Y
                return True
        else:
            if boarder.index(1) + self.height / 2 < self.center_x + self.change_x:
                return False
            if boarder.index(1) + self.height / 2 <= self.center_x + self.change_x <= boarder.index(1):
                self.center_x = boarder.index(1) + self.height / 2
                self.change_x = Ball.INITIAL_SPEED_X
                return True
            elif self.center_x + self.change_x >= boarder.index(0):
                self.center_y = Bar.INITIAL_OFFSET_Y - self.height / 2
                self.change_y = - Ball.INITIAL_SPEED_Y
                return True

        return False

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball(self.bar)
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT * 4 / 5
        Bar.INITIAL_OFFSET_Y += self.bar.center_y

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta_time: float):
        self.bar.update()
        self.ball.update()

    def on_key_press(self, symbol: int, modifiers: int):
        self.bar.on_key_press(symbol, modifiers)


if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
