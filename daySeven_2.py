class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super().__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super().__init__(NonMarineMammalName)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')

#Method Resolution Order (MRO)
print Dog.__mro__

#A method in the derived calls is always called before the method of the base class.
#In our example, Dog class is called before NonMarineMammal or NoneWingedMammal. These two classes are called before Mammal which is called before Animal, and Animal class is called before object.
#If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal), method of NonMarineMammal is invoked first because it appears first.
