D1_lat, m1_lat, s1_lat = map(float, input().split(':'))
D1_lon, m1_lon, s1_lon = map(float, input().split(':'))
P1_lat = (s1_lat / 3600) + (m1_lat / 60) + d1_lat
P1_lon = (s1_lon / 3600) + (m1_lon / 60) + d1_lon

From math import*
Def truncate(f, n):
    S = '%.19f' % f
    I, p, d = s.partition('.')
    Return '.'.join([i, (d+'0'*n)[:n]])

Def dms(dd1, dd2):
    Mnt1, sec1 = divmod(dd1*3600, 60)
    Deg1, mnt1 = divmod(mnt1, 60)
    Mnt2, sec2 = divmod(dd2*3600, 60)
    Deg2, mnt2 = divmod(mnt2, 60)
    Print(int(deg1), int(mnt1), truncate(sec1, 12), int(deg2), int(mnt2), truncate(sec2, 12))

RE = 6371000
R = float(input())  # это радиус Земли
# R = R/(2*pi*RE)*360
D1_lat, m1_lat, s1_lat, d1_lon, m1_lon, s1_lon = map(float, input().split(' '))
D2_lat, m2_lat, s2_lat, d2_lon, m2_lon, s2_lon = map(float, input().split(' '))
D3_lat, m3_lat, s3_lat, d3_lon, m3_lon, s3_lon = map(float, input().split(' '))

P1_lat = (s1_lat/3600) + (m1_lat/60) + d1_lat
P1_lon = (s1_lon/3600) + (m1_lon/60) + d1_lon
P2_lat = (s2_lat/3600) + (m2_lat/60) + d2_lat
P2_lon = (s2_lon/3600) + (m2_lon/60) + d2_lon
P3_lat = (s3_lat/3600) + (m3_lat/60) + d3_lat
P3_lon = (s3_lon/3600) + (m3_lon/60) + d3_lon

K = cos(radians(p2_lon))
# вот это тот самый коэффициент пересчета, в вашем случае чтобы пересчитать
# относительно точки центра просто в аргумент пишите lon среднее от точек
Pi1 = pi
X1 = p1_lon*(2*pi1*RE)/360  # получение координат на плоскости
Y1 = p1_lat*k*(2*pi1*RE)/360
X2 = p2_lon*(2*pi1*RE)/360
Y2 = p2_lat*k*(2*pi1*RE)/360
X3 = p3_lon*(2*pi1*RE)/360
Y3 = p3_lat*k*(2*pi1*RE)/360
