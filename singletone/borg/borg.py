
class Borg(object):
    _shared_state = {}

    def __new__(cls):
        obj = super(Borg, cls).__new__(cls)
        obj.__dict__ = cls._shared_state
        return obj 

if __name__ == '__main__':
    borg = Borg()
    another_borg = Borg()
    
    print borg is Borg 
