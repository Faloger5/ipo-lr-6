import string

stroki = int(input('Введите кол-во строк: '))
if stroki <= 0:
    print('Вы ввели некорректное значение')
else:
    texts = []
    for i in range(stroki):
        user_input = input(f'Введите {i+1}-ю строку: ')
        texts.append(user_input)

    total_words = 0
    for line in texts:
        words = line.split()  # разбиваем строку на слова
        total_words += len(words)

    print('Кол-во слов в тексте:', total_words)
