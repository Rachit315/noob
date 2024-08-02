number=int(input('nummber: '))

if number==1:
    print('YOU WIN!')
else:
    while number< 1:
        number+=3
        print(number )
        print('YOU LOOSE')