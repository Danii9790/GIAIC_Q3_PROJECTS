"""
Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

"""
class Engine:
    def start(self):
        print("Engine Started...")
class Car:
    def __init__(self,engine):
        self.engine = engine

    def run(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.run()

        