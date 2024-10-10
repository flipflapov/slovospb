txt = input('Введите ваш текст: ')
txt = txt.split('.')

lo = [
    word for line in txt for word in line.split(' ')
]

print(lo)
