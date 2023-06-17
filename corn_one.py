counter = 0
total = 0
required_class = 'SS3'
class_ = input('Enter the class of the student: ')

if class_ == required_class:
    while counter < 20:
        grade = int(input('Enter the grade of the student: '))
        total += grade
        counter += 1

    average_no = float(total) / counter

    print('*' * 70)
    print('      Aso Rock Secondary School, Abuja Nigeria      ')
    print('*' * 70)
    print('Class: SS3')
    print('Number of Students: ', counter)
    print('Total score: ', total)
    print('Average score: ', average_no)