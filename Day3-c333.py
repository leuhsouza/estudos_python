year = int(input('Digite um ano para verificar se é bissexto: '))

if year % 4 == 0:
    if year % 100 != 0:
        print('Leap year')
    else:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not leap year')
    print('Leap year')
else:
    print('Not leap year')