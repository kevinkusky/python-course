# Input Validation

age = 1
while age:
    age = input('What is your age? ')

    if age:
        try:
            age = int(float(age))
            if age > 0 and age < 120:
                print('Cool! You\'ve had %s birthdays' %age)
                break
            else:
                print('Are you he who remains? - Please try again')
        except:
            print('Please enter a number')
