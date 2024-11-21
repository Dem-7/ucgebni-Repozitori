class Dvigatel ():
    def start (self):
        print("Двигатель запущен")
    def stop(self):
        print("Двигатель заглушен")
class Avto():
    def __init__ (self):
        self.dvigatel = Dvigatel
    def start(self):
        self.dvigatel.start(self)
    def stop (self):
        self.dvigatel.stop(self)
avto = Avto()
avto.start()
avto.stop()