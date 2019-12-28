cal_1 = 0.0
cal_2 = 0.0

while True:
    result = 0
    calculation = input('>')
    if '+' in calculation:
        index_of_operator = calculation.index('+')
        cal_1 = calculation[0:index_of_operator]
        cal_2 = calculation[index_of_operator + 1:]
        result = float(cal_1) + float(cal_2)
    elif '-' in calculation:
        index_of_operator = calculation.index('-')
        cal_1 = calculation[0:index_of_operator]
        cal_2 = calculation[index_of_operator + 1:]
        result = float(cal_1) - float(cal_2)
    elif '*' in calculation:
        index_of_operator = calculation.index('*')
        cal_1 = calculation[0:index_of_operator]
        cal_2 = calculation[index_of_operator + 1:]
        result = float(cal_1) * float(cal_2)
    elif '/' in calculation:
        index_of_operator = calculation.index('/')
        cal_1 = calculation[0:index_of_operator]
        cal_2 = calculation[index_of_operator + 1:]
        result = float(cal_1) / float(cal_2)
    elif calculation == 'exit':
        print('exit')
        break
    else:
        print('erro')
    print('>' + str(result))
