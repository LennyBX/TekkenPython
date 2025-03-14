class Animal:
    def __init__(self, name, age, espece):
        self.name = name
        self.age = age
        self.espece = espece

    def tostring(self):
        if self.age < 2:
            print(f"Cet un animal s'appele {self.name}, c'est un jeune animal, c'est un {self.espece}")
        else:
            print(f"Cet un animal s'appele {self.name} il à {self.age} ans, c'est un {self.espece}")


class Poule(Animal):
    def tostring(self):
        if self.age < 2:
            print(f"Cet un animal s'appele {self.name}, c'est un poussin, c'est un {self.espece}")
        else:
            print(f"Cet un animal s'appele {self.name} il à {self.age} ans, c'est un {self.espece}")



chevre = Animal("chevre", 12, "animal")
mouton = Animal("mouton", 13, "animal")
poule = Animal("poule", 1, "animal")
poulenew = Poule("poulenew", 1, "animal")

chevre.tostring()
mouton.tostring()
poule.tostring()
poulenew.tostring()