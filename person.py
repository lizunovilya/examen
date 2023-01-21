class Action:
    def __init__(self,name = 'Сходить в парк',money = 0, mood = 100, health = 100):
        self.money = money
        self.mood = mood
        self.name = 'Сходить в парк'
        self.health = health



class work(Exception):
    def __init__(self, massage='человек впал в депрессию'):
        Exception.__init__(self, massage)

class death(Exception):
    def __init__(self, massage='человек умер'):
        Exception.__init__(self, massage)

class bankruptcy(Exception):
    def __init__(self, massage='человек стал банкротом'):
        Exception.__init__(self, massage)

class Person:
    name = 'Человек'
    money = 0
    mood = 100
    health = 100

    def __init__(self, money = 0, mood = 100, name = 'Человек', health = 100):
        self.money = money
        self.mood = mood
        self.name = name
        self.health = health

    def __str__(self):
        return f'{self.name} (money:{self.money},' \
               f' mood:{self.mood},' \
               f' health: {self.health})'


    def do (self, money = 0, mood = 100, health = 100):

        if self.mood <= 0:
            raise work()
            pass

        else:
            pass

        if self.health <= 0:
            raise death()
            pass

        else:
            pass

        if self.money < 0:
            raise bankruptcy()
            pass

        else:
            pass
