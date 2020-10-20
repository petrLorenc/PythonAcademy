class Engine:
    power = 1

    def start(self):
        print("Engine starting")

    def power_up(self, direction, position):
        position[0] += direction[0] * self.power
        position[1] += direction[1] * self.power


class SteeringWheel:
    def steer_left(self, direction):
        direction[0] -= 1


class Car:
    encapsulated_variable = "Animal"
    direction = [0., 0.]
    position = [0., 0.]

    def __init__(self, engine=Engine(), steeringWheel=SteeringWheel()):
        self.engine = engine
        self.wheel = steeringWheel

    def start(self):
        self.engine.start()

    def run(self):
        self.wheel.steer_left(self.direction)
        self.engine.power_up(self.direction, self.position)


car = Car()
car.start()
car.run()
print(car.position)

