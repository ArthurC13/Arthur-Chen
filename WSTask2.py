room_dimension = int(input('Please enter the dimensions of the room: '))
unpaintable = int(input('Please enter the total dimensions of the unpaintable areas: '))
coats = int(input('Please enter the number of coats of paint required: '))
paint = (room_dimension-unpaintable)*coats/11
print(paint,"litres of paint required")
