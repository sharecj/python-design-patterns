
class Singletone(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance

if __name__ == '__main__':
    singletone = Singletone()
    another_singleton = Singletone()
    
    print singletone is another_singleton
