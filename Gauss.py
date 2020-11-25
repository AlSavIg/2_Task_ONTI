X = [2, 3, 1]
Y = [4, -8, 2]
i = int(0)
Plus_Part = float(0)
Minus_Part = float(0)
while 1:
    if i + 1 == len(Y):
        Plus_Part += float(X[i] * Y[0])
        break
    Plus_Part += float(X[i] * Y[i + 1])
    i += 1
i = int(0)
while 1:
    if i + 1 == len(X):
        Minus_Part += float(X[0] * Y[i])
        break
    Minus_Part += float(X[i + 1] * Y[i])
    i += 1
S = float(0.5 * abs(Plus_Part - Minus_Part))
print(S)
