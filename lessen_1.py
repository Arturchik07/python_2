class Car:
    def __init__(self, model, year, color, penalties=0):
        self.model = model
        self.year = year
        self.color = color
        self.penalties = penalties

number = 3
bmw_car = Car( 'BMW E30', 1992, 'black')
print(number)
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color}'
      f'PENALTIES: {bmw_car.penalties} ')
bmw_car.color = 'red'
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} NEW COLOR: {bmw_car.color}'
      f'PENALTIES: {bmw_car.penalties} ')

mers_car = Car( 'Mercedes-Benz C-Class', 1990, 'silver')
print(f'MODEL: {mers_car.model} YEAR: {mers_car.year} COLOR: {mers_car.color}'
      f'PENALTIES: {mers_car.penalties} ')

print('end of program ')