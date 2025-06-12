import random

with open('numbers.txt','w', encoding='utf8') as file:
    for i in range(100):
        num = random.randint(1, 1000)
        file.write(str(num) + '\n')
even=[]
odd=[]
try:
    with open('numbers.txt','r', encoding='utf8') as file:
        value=file.readlines()
        print(value)
        for i in value:
            if int(i)%2==0:
                even.append(i) 
            else:
                odd.append(i)
        print(f'Количество чисел в файле numbers.txt: {len(value)}')
        integer1=[]
        for i in value:
            integer1.append(int(i))
        print(f'Сумма всех чисел:{sum(integer1)}')
        print(f'Среднее арифметическое:{sum(integer1)/len(integer1)}')

except FileNotFoundError:
        print('Файл с таким именем не найден')
with open('even.txt','w', encoding='utf8') as file:
    file.write(f'{even}')
    print(f'Количество чисел в файле even.txt: {len(even)}')
    integer2=[]
    for i in even:
        integer2.append(int(i))
    print(f'Сумма всех чисел:{sum(integer2)}')
    print(f'Среднее арифметическое:{sum(integer2)/len(integer2)}')
with open('odd.txt','w', encoding='utf8') as file:
    file.write(f'{odd}')
    print(f'Количество чисел в файле odd.txt: {len(odd)}')
    integer3=[]
    for i in odd:
        integer3.append(int(i))
    print(f'Сумма всех чисел:{sum(integer3)}')
    print(f'Среднее арифметическое:{sum(integer3)/len(integer3)}')
