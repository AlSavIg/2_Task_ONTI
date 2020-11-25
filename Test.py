from math import*


def conversion_to_egrees(mas):
    result = float((mas[2] / 3600) + (mas[1] / 60) + mas[0])
    return result


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
    S = float(0.5 * abs(Plus_Part - Minus_Part))
    print(S)


def taking_coordinates_lon(latitude, longitude):
    # result = float(latitude*(2*pi_c * RE) / 360)
    result = RE * cos(radians(latitude*2*pi_c / 360))*cos(radians(longitude * 2 * pi_c / 360))
    return result


def taking_coordinates_lat(longitude):
    # result = float(longitude * koef * (2*pi_c * RE) / 360)
    return result


# Constant
pi_c = 3.1415926
RE = 6371000
list_final = []
egrees_list = []
X_list = []
Y_list = []

for i in input().split(' '):
    list_final.append((list(map(float, i.split(":")))))
print(list_final)

for i in range(len(list_final)):
    egrees_list.append(conversion_to_egrees(list_final[i]))
print(egrees_list)
count = sum = 0
for i in range(1, len(egrees_list), 2):
    count += 1
    sum += egrees_list[i]

average_longitude = float(sum / count)
koef = cos(radians(average_longitude))


x = taking_coordinates_lon(egrees_list[0], egrees_list[1])
print(x)


for i in range(0, len(egrees_list), 2):
    X_list.append(taking_coordinates_lat(egrees_list[i]))
for i in range(1, len(egrees_list), 2):
    Y_list.append(taking_coordinates_lon(egrees_list[i]))

print(X_list, Y_list)
area(X_list, Y_list)
