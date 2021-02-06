#Yeşim Ece Ersoy Homework Day 3


class Animal:
  def __init__(self, dog, cat):
    self.dogs = dog
    self.cats = cat
x = Animal("dog", "cat")
#DOG
class Dogs:
  def __init__(self, color, racename):
    self.color = color
    self.racename = racename
y = Dogs("chocolate", "bulldog")

#CATS
class Cats:
  def __init__(self, color, racename):
    self.color = color
    self.racename = racename
z = Cats("bluesilver", "Persian Cat")

#OUTPUTS
print(x.dogs)
print(x.cats)
print(y.color, y.racename)
print(z.color,z.racename)
