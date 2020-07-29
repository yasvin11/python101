class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def make_noise(self):
        print('VRUUUUUUMMM')

    @property
    def number_of_wheels(self):
        return self.__number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.__number_of_wheels = number

tesla_model_s = Vehicle(4, 'electric', 5 ,250)
print(tesla_model_s.number_of_wheels)
print(tesla_model_s.type_of_tank)
print(tesla_model_s.seating_capacity)
print(tesla_model_s.maximum_velocity)

tesla_model_s.make_noise()

    
