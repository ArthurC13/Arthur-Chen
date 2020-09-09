last_fill = int(input('Please enter the car mileage the last time the car was filled: '))   #int
now = int(input('Please enter the car mileage now: '))                                      #int
tank = int(input('Please enter the total number of litres taken to fill the tank: '))       #int
gallons_to_litre = 0.22                                                                     #constant
litre_to_gallons = 4.546                                                                    #constant
miles_per_gallon = (now-last_fill)/tank*getattr                                             #real
print('The number of miles per gallon the car is doing:',miles_per_gallon)
