#Q4
students = int(input('Please enter the number of students: '))
books = int(input('Please enter the number of books: '))
receive = books//students
left_over = books%students
print('Each student will receive',receive,'books with',left_over,'books left over')

#Q5
name = input('Please enter a name: ')
length = len(name)
print('This name is',length,'characters long')
