room_dimension = int(input('Please enter the dimensions of the room: '))
unpaintable = int(input('Please enter the total dimensions of the unpaintable areas: '))
coats = int(input('Please enter the number of coats of paint required: '))
## ACS - Why are you dividing by 11?
paint = (room_dimension-unpaintable)*coats/11
print(paint,"litres of paint required")

## ACS - You need some comments in the code
## ACS- deminsions of the room need two inputs wdith and height?
