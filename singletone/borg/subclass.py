from borg import Borg 

class Child(Borg):
    pass

if __name__ == '__main__':
    borg = Borg()
    borg.only_one_var = 'only one var'
    child = Child()
    another_child = Child()

    print borg.only_one_var 
    print child.only_one_var 
    print another_child.only_one_var 
