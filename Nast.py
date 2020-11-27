def conv_egrees(massive):
    res = float((massive[2] / 3600) + (massive[1] / 60) + massive[0])
    return res


def lon_coord(latitude):
    res = 2 * pi_const * RE / 360 * (latitude - AV_lat)
    return res


def lat_coord(longit):
    coef = cos(radians(AV_lat))
    res = float((longit - AV_long)
                   * coef * (2*pi_const * RE) / 360)
    return res


from math import*
# Constant
pi_const = 3.1415926
RE = 6371000
list_final = []
for i in input().split(' '):
    list_final.append((list(map(float, i.split(":")))))
egrees = []
for i in range(len(list_final)):
    egrees.append(conv_egrees(list_final[i]))
quality = summa = 0
for i in range(1, len(egrees), 2):
    summa += egrees[i]
    quality += 1
AV_long = float(summa / quality)
quality = summa = 0
for i in range(0, len(egrees), 2):
    summa += egrees[i]
    quality += 1
AV_lat = float(summa / quality)
X = []
Y = []
for i in range(0, len(egrees), 2):
    X.append(lat_coord(egrees[i]))
for i in range(1, len(egrees), 2):
    Y.append(lon_coord(egrees[i]))

i = int(0)
positive = float(0)
negative = float(0)
while 1:
    if i + 1 == len(Y):
        positive += float(X[i] * Y[0])
        break
    positive += float(X[i] * Y[i + 1])
    i += 1
i = int(0)
while 1:
    if i + 1 == len(X):
        negative += float(X[0] * Y[i])
        break
    negative += float(X[i + 1] * Y[i])
    i += 1
area = str(round(float(0.5 * abs(positive - negative)), 1))

if len(area) == 3:
    area = "0" + "0" + "0" + area
if len(area) == 4:
    area = "0" + "0" + area
if len(area) == 5:
    area = "0" + area

print(area)
