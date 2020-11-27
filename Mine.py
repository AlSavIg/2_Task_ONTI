from math import*


def conversion_to_egrees(mas):
    res = float((mas[2] / 3600) + (mas[1] / 60) + mas[0])
    return res


def area(X_list, Y_list):
    i = int(0)
    Plus_Part = float(0)
    Minus_Part = float(0)
    while 1:
        if i + 1 == len(Y_list):
            Plus_Part += float(X_list[i] * Y_list[0])
            break
        Plus_Part += float(X_list[i] * Y_list[i + 1])
        i += 1
    i = int(0)
    while 1:
        if i + 1 == len(X_list):
            Minus_Part += float(X_list[0] * Y_list[i])
            break
        Minus_Part += float(X_list[i + 1] * Y_list[i])
        i += 1
    S = round(float(0.5 * abs(Plus_Part - Minus_Part)), 1)
    return S


def taking_coordinates_lon(latitude):
    res = 2 * pi_c * RE / 360 * (latitude - average_latitude)
    return res


def taking_coordinates_lat(longit):
    koef = cos(radians(average_latitude))
    res = float((longit - average_longit)
                   * koef * (2*pi_c * RE) / 360)
    return res


def fill_nulls(number):
    number = str(number)
    if len(number) == 3:
        number = "000" + number
    if len(number) == 4:
        number = "00" + number
    if len(number) == 5:
        number = "0" + number
    return number


# Constant
pi_c = 3.1415926
RE = 6371000
list_final = []
egrees_list = []
X_list = []
Y_list = []

for i in input().split(' '):
    list_final.append((list(map(float, i.split(":")))))

for i in range(len(list_final)):
    egrees_list.append(conversion_to_egrees(list_final[i]))

count = sum = 0
for i in range(1, len(egrees_list), 2):
    count += 1
    sum += egrees_list[i]
average_longit = float(sum / count)

count = sum = 0
for i in range(0, len(egrees_list), 2):
    count += 1
    sum += egrees_list[i]
average_latitude = float(sum / count)

for i in range(0, len(egrees_list), 2):
    X_list.append(taking_coordinates_lat(egrees_list[i]))
for i in range(1, len(egrees_list), 2):
    Y_list.append(taking_coordinates_lon(egrees_list[i]))

print(fill_nulls(area(X_list, Y_list)))
