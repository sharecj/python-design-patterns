from singletone import Singletone

class Child(Singletone):
    pass

if __name__ == '__main__':
    child = Child()
    another_child = Child()
    print child is another_child
