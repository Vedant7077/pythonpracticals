class Engine:
    def start(self):
        print("Engine started..")
    def stop(self):
        print("Engine stopped...")
class Car(Engine):
    def __init__(self):
        self.engine = Engine()
    def start(self):
        print("Car is starting...")
        self.engine.start()
    def stop(self):
        print("Car is stopping...")
        self.engine.stop()
car = Car()        
car.start()
car.stop()

        