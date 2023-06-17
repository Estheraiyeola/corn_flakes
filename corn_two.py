counter = 0
total = 0
required_class = 'SS3'
class_ = input('Enter the class of the students: ')
grade = int(input('Enter the grade except -25: '))

if class_ == required_class:
    while grade != -25:
        total += grade
        counter += 1

        grade = int(input('Enter another grade or enter -25 to end the program: '))
    average = float(total) / counter

    print('*' * 70)
    print('        Aso Rock Secondary School, Abuja Nigeria')
    print('*' * 70)
    print('Class: ', class_)
    print('Number of Students: ', counter)
    print('Total score: ', total)
    print('Average Score: ', average)