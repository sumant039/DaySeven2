# DaySeven2


#A method in the derived calls is always called before the method of the base class.

#In our example, Dog class is called before NonMarineMammal or NoneWingedMammal. These two classes are called before Mammal which is called before Animal, and Animal class is called before object.

#If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal), method of NonMarineMammal is invoked first because it appears first.


