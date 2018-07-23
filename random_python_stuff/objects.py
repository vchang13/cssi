victoria = {'name': 'Victoria',
            'age' : 18,
            'anime': True,
            'hair_color': 'black'}

print(victoria)

class Person(object): #classes are upper case (camelcase??)
    def __init__(
            self, name, age, anime, hair_color=None,
            works_at_google=False,
            ):
        self.name = name
        self.age = age
        self.anime = anime
        self.hair_color = hair_color
        self.googler = works_at_google
        self.hungry = True
        # self.kids = []
        # self.bored = True

    def eat(self, food):
        print('im eating {food}'.format(food=food))
        self.hungry = False

    # def __str__(self):
    #     victoria_string = 'Name: {n}, Age: {a}, Anime: {an}'.format(n=self.name, a=self.age, an=self.anime)
    #     return victoria_string
    # def entertain(self, do):
    #     print('i am going to {do}'.format(do=do))
    #     self.bored = False

    # def give_birth(self, new_person):
    #     self.kids.append(new_person)


victoria = Person(
        name='Victoria',
        age=18,
        anime=True,
        hair_color='black'
        # bored=True
        )

brooke = Person(
        name='Brooke',
        age=18,
        anime=False,
        hair_color='brown')

print(victoria.name)
print('Victoria is hungry: {h}'.format(h=victoria.hungry))
# print('Victoria is bored: {b}'.format(b=victoria.bored))
# victoria.hungry = False
victoria.eat('ramen')
# victoria.entertain('yeet')
print('Victoria is hungry: {h}'.format(h=victoria.hungry))
# print('Is Victoria bored? {b}'.format(b=victoria.bored))
print(brooke.name)
print('Brooke is hungry: {h}'.format(h=brooke.hungry))
