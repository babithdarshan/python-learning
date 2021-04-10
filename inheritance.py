class baseclass:
    a=10
    b=200
    def display(self):
        print("base class")
class derivedclass(baseclass):
    c=20
    d=200
    def show(self):
        print("derived class")
dobject=derivedclass()
print(dobject.c,dobject.d)
dobject.show()
print(dobject.a,dobject.b)
dobject.display()
