class Hero:
    def __init__(self,name='player1',hp=100,act=10):
        self.name = name
        self.hp = hp
        self.act = act
        print('奥特鳗%s来啦！'% self.name)
    def hit(self,name):
        name.hp = name.hp - self.act
class Element:
    def __init__(self,name='boss',hp=1000,act=100):
        self.name = name
        self.hp = hp
        self.act = act
        print('小怪兽 %s 来啦' % self.name)

milo = Hero('milo')
boss = Element('wuyaowang')
haishan1 = Element('wuyao')
milo.hit(boss)
print(boss.hp)
milo.hit(haishan1)
print(haishan1.hp)