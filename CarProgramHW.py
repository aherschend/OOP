import CarClass as c

def main():

    

    model = input('What year is your car model?  ')
    make = input('What is the make of your car?  ')
    speed = print('Current Speed:  0')

    my_car = c.Car(model, make, speed)

    print()
    print('Accelerating...')
    print()

    #1 accelerate
    my_car.accelerate()
    print('Current Speed: ', my_car.get_speed())
    #2 accelerate
    my_car.accelerate()
    print('Current Speed: ', my_car.get_speed())
    #3 accelerate
    my_car.accelerate()
    print('Current Speed: ', my_car.get_speed())
    #4 accelerate
    my_car.accelerate()
    print('Current Speed: ', my_car.get_speed())
    #5 accelerate
    my_car.accelerate()
    print('Current Speed: ', my_car.get_speed())

    print()
    print('Braking...')
    print()

    #1 brake
    my_car.brake()
    print('Current Speed: ', my_car.get_speed())
    #2 brake
    my_car.brake()
    print('Current Speed: ', my_car.get_speed())
    #3 brake
    my_car.brake()
    print('Current Speed: ', my_car.get_speed())
    #4 brake
    my_car.brake()
    print('Current Speed: ', my_car.get_speed())
    #5 brake
    my_car.brake()
    print('Current Speed: ', my_car.get_speed())

main()

