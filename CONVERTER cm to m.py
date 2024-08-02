Length=int(input('Length: '))
ques=input('cm or inch: ')
if ques=='inch':
    value=(Length)*2.54
    print(f'{Length}inch is equal to {value}cm')
else:
    value=(Length)/2.54
    print(f'{Length}cm is equal to {value}inch')

    