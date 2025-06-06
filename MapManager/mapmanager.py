import pickle
class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0, 0, 1, 1)
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def saveMap(self):
        blocks = self.land.getChildren()
        with open('my_map.dat', 'wb') as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)

    def loadMap(self):
        self.clear()
        with open('my_map.dat', 'rb') as fin:
            length = pickle.load(fin)
            for i in range(length):
                pos = pickle.load(fin)
                self.addBlock(pos)

    def addBlock(self, position):
        block = loader.loadModel(self.model)
        block.setTexture(loader.loadTexture(self.texture))
        block.setColor(self.color)
        block.setPos(position)
        block.reparentTo(self.land)
        block.setTag('at', str(position))
    
    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def buildBlock(self, pos):
        x, y, z = pos 
        new = self.findHigestEmpty(pos)
        if new[2] <=z + 1:
            self.addBlock(new)
    
    def delBlockFrom(self, position):
        x, y, z = self.findHigestEmpty(position)
        pos = x, y, z - 1
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def findBlocks(self,pos):
        return self.land.findAllMatches('=at=' + str(pos))
    
    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
        
    def findHigestEmpty(self,pos):
        x, y, z, = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = list(map(int, line.split()))
                for symbol in line:
                    for z in range(0, symbol+1):
                        self.addBlock((x, y, z))
                    x += 1
                y += 1

    def clear(self):
        self.land.removeNode()
        self.startNew()