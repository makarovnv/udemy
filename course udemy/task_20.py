class GameCharacter:

    def __init__(self, name, health,
                 level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is ' + self.name)


class Villain(GameCharacter):

    def __init__(self, name, health,
                 level):
        GameCharacter.__init__(self, name, health,
                               level)

    def speak(self):
        print('Hi, my name is ' + self.name + ' and I will kill you')

    def kill(self, other):
        other.health = 0
        print('Bang-bang, now you\'re dead')


james = GameCharacter('James', 100, 1)
jim = Villain('Jim', 100, 2)

james.speak()
jim.speak()
print(james.health)
jim.kill(james)
print(james.health)
