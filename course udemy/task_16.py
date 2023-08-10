def cat_voice():
    print('Meow!')


def dog_voice():
    print('Woof!')


cat_voice()
dog_voice()

def cat_voice():
    return 'Meow!'


def dog_voice():
    return 'Woof!'


print(cat_voice()*2)
print(dog_voice()*2)

def get_voice(text = 'Empty param'):
    print(text + '!')

def odd_num(a=0,b=0):
    '''
    Функция генерирует последовательность нечетных чисел в диапазоне от a до b
    включительно, передаются вараметры a и b, возвращает  лист A.
    '''
    A=[]
    for i in range (a, b+1, 1):
        if i % 2 != 0:
            A.append(i)
        return A


def odd_num_c(a=0,b=0):
    '''
    Функция генерирует последовательность нечетных чисел в диапазоне от a до b
    включительно, передаются вараметры a и b, возвращает  лист A.
    '''
    A=[i for i in range(a, b+1, 1) if i % 2 != 0]
    return A
