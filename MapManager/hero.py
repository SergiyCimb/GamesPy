class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.mode = True

    def accept_events(self):
        base.accept('z', self.land.saveMap)
        base.accept('x', self.land.loadMap)
        base.accept('b', self.build)
        base.accept('n', self.destroy)
        base.accept('i', self.changeMode)
        base.accept('u', self.changeView)
        base.accept('q', self.turn_left)
        base.accept('q'+'-repeat', self.turn_left)
        base.accept('e', self.turn_right)
        base.accept('e'+'-repeat', self.turn_right)
        base.accept('space', self.up)
        base.accept('space'+'-repeat', self.up)
        base.accept('alt', self.down)
        base.accept('alt'+'-repeat', self.down)
        base.accept('w', self.forward)
        base.accept('w'+'-repeat', self.forward)
        base.accept('s', self.back)
        base.accept('s'+'-repeat', self.back)
        base.accept('a', self.left)
        base.accept('a'+'-repeat', self.left)
        base.accept('d', self.right)
        base.accept('d'+'-repeat', self.right)

    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def up(self):
        self.hero.setZ(self.hero.getZ()+1)
        
    def down(self):
        self.hero.setZ(self.hero.getZ()-1)

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def move_to(self, angle):
        if self.mode == True:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHigestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx, from_y + dy, from_z
    
    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return 0, -1
        elif angle >= 20 and angle <= 65:
            return 1, -1
        elif angle >= 65 and angle <= 110:
            return 1, 0
        elif angle >= 110 and angle <= 155:
            return 1, 1
        elif angle >= 155 and angle <= 200:
            return 0, 1
        elif angle >= 200 and angle <= 245:
            return -1, 1
        elif angle >= 245 and angle <= 290:
            return -1, 0
        else: 
            return -1, -1

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)

    def forward(self):
        angle = (self.hero.getH()+0) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
    
    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else: 
            self.land.buildBlock(pos)
    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else: 
            self.land.delBlockFrom(pos)