from direct.showbase.ShowBase import ShowBase
from mapmanager import *
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        self.hero = Hero((1, 1, 1), self.land)
        base.camLens.setFov(90)

game = Game()
game.run()  