file = open('chengfabiao.txt', 'w', encoding='utf-8')
for i in range(1, 10):
    for j in range(1, i+1):
        my_str = str(j) + '*' + str(i) + '=' + str(i*j)
        print(my_str.center(8, ' '), end="   ")
        file.write(my_str.center(8, ' '))
    print("")
    file.write('\n')
