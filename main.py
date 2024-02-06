class Singleton:
    _instance = None

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Tato trieda je Singelton a uz bola Instancovana")
        else:
            self.meno = "Allan"
            Singleton._instance = self

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance


s1 = Singleton.getInstance()
print(s1.meno)
s2 = Singleton.getInstance()
s1.meno = "Milan"
print(s2.meno)
s3 = Singleton()
