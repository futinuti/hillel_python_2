def max_letters(stroka):
    stroka = stroka.lower()
    stroka = stroka.split(" ")
    str_schet = []
    for i in stroka:
        schet = 0
        for j in stroka:
            if i == j:
                schet += 1
        str_schet.append(schet)
    di = dict(zip(stroka, str_schet))
    maks = 0
    max_i = []
    for i in di.items():
        if i[1] > maks:
            maks = i[1]
            max_i = i
    return print(f'Максимально встречающееся слово "{max_i[0]}" кол-во {max_i[1]} раз')


with open('stroka_5.txt', 'r') as file:
    a = file.readline()
    max_letters(a)
