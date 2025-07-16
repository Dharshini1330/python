class Parent:
    def code(self):
        print("good coder")

class Child(Parent):
    def develop(self):
        print("good developer")

c = Child()
c.develop()
c.code()
print(".....................")

class Parent1:
    def code(self):
        print("good coder")

class Parent2:
    def chef(self):
        print("good chef")

class Child(Parent1, Parent2):
    def develop(self):
        print("good developer")

multi = Child()
multi.develop()
multi.code()
multi.chef()
print(".....................")

class Grandparent:
    def code(self):
        print("good coder")

class Parent(Grandparent):
    def chef(self):
        print("good chef")

class Child(Parent):
    def develop(self):
        print("good developer")

m = Child()
m.develop()
m.code()
m.chef()
print(".....................")

class Parent:
    def house(self):
        print("has an apartment")

class Child1(Parent):
    def chef(self):
        print("good chef")

class Child2(Parent):
    def develop(self):
        print("good developer")

h1 = Child2()
h1.develop()
h1.house()

h2 = Child1()
h2.chef()
h2.house()
print(".....................")

class Grandparent:
    def home(self):
        print("has an apartment")

class Parent1(Grandparent):
    def doctor(self):
        print("was a doctor")

class Parent2(Grandparent):
    def professor(self):
        print("was a professor")

class Child(Parent1, Parent2):
    def develop(self):
        print("good developer")        

h = Child()
h.develop()
h.professor()
h.doctor()
h.home()
