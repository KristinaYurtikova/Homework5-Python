#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = str(input('Введите строку для кодирования: '))

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        print(encoding)
        return encoding

rle_encode(data)

data1 = str(input('Введите строку для декодирования: '))

def rle_decode(data1):
    decode = ''
    count = ''
    for char in data1:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    print(decode)
    return decode

rle_encode(data)
rle_decode(data1)


