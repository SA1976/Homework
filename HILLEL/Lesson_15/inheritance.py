from abc import ABC, abstractmethod


class WaterBird(ABC):
    def __init__(self, name):
        self.name = name
        print('Bird is {}'.format(self.name))

    def where_is_life(self):
        print('On th Earth')

    def swim(self):
        print('Can swim')

    @abstractmethod
    def voice(self):
        pass


class Penguin(WaterBird):
    def __init__(self, name):
        WaterBird.__init__(self, name)
        print('Penguin was created')

    def where_is_life(self):
        WaterBird.where_is_life(self)
        print('South pole')

    def run(self):
        print('Can run')

    def voice(self):
        print('Pi-pi-pi')


class Duck(WaterBird):
    def __init__(self, name):
        super().__init__(name)
        print('Duck was created')

    def where_is_life(self):
        # super().where_is_life()
        print('Anywhere')

    def fly(self):
        print('Can fly')

    def voice(self):
        # print('Kra-kra-kra')
        pass


p = Penguin('Pink')
print(dir(p))
p.swim()
p.where_is_life()
p.voice()
p.run()

d = Duck('Donald Duck')
d.swim()
d.where_is_life()
d.voice()
d.fly()