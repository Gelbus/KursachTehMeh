import math

"""
##############################################
Глава 1
##############################################
"""
print()
print('-----Глава 1')
N_inp: int = 10_000
N_out: int = 56
dn = 1.5

i_gen: float = round(N_inp / N_out, 4)
print(f'i общ = {i_gen}')

z1: int = 12
z5_: int = 12
z234_: int = 17
z2345_float: float = round(math.pow(i_gen * z1 * math.pow(z234_, 3), 1/4), 4)
z2345: int = round(z2345_float)
print(f'z2 = z3 = z4 = z5 = {z2345_float}')
print(f'z2 = z3 = z4 = z5 = {z2345}')


u12: float = round(z2345 / z1, 4)
u2_3: float = round(z2345 / z234_, 4)
u_gen: float = round(u12 * math.pow(u2_3, 3), 4)

print(f'u12 = {u12}')
print(f'u2_3 = {u2_3}')
print(f'u общ = {u_gen}')

n2 = round(N_inp / u12, 4)
n3 = round(n2 / u2_3, 4)
n4 = round(n3 / u2_3, 4)
n5 = round(N_inp / u_gen, 4)

print(f'n2 = {n2}')
print(f'n3 = {n3}')
print(f'n4 = {n4}')
print(f'n5 = {n5}')

delta_n = round(abs((N_out - n5)) / n5 * 100,4)
print(f'дельта n = {delta_n}')

"""
##############################################
Глава 2
##############################################
"""
print()
print('-----Глава 2')
m1: float = 0.3
m5_: float = 0.5
m2345: float = 0.3
m234_: float = 0.3
ksi: int = 8

print('Диаметр делительных окружностей:')
di1: float = round(m1 * z1, 4)
di2345: float = round(m2345 * z2345, 4)
di234_: float = round(m234_ * z234_, 4)
di5_: float = round(m5_ * z5_, 4)
print(f'di1 = {di1}')
print(f'di2 = di3 = di4 = di5 = {di2345}')
print(f'di2_ = di3_ = di4_ = {di234_}')
print(f'di5_ = {di5_}')

print('Диаметр делительных выступов:')
da1: float = round(m1 * (z1 + 2), 4)
da2345: float = round(m2345 * (z2345 + 2), 4)
da234_: float = round(m234_ * (z234_ + 2), 4)
da5_: float = round(m5_ * (z5_ + 2), 4)
print(f'da1 = {da1}')
print(f'da2 = da3 = da4 = da5 = {da2345}')
print(f'da2_ = da3_ = da4_ = {da234_}')
print(f'da5_ = {da5_}')

print('Диаметр делительных впадин:')
dfi1: float = round(m1 * (z1 - 3), 4)
dfi2345: float = round(m2345 * (z2345 - 3), 4)
dfi234_: float = round(m234_ * (z234_ - 3), 4)
dfi5_: float = round(m5_ * (z5_ - 3), 4)
print(f'dfi1 = {dfi1}')
print(f'dfi2 = dfi3 = dfi4 = dfi5 = {dfi2345}')
print(f'dfi2_ = dfi3_ = dfi4_ = {dfi234_}')
print(f'dfi5_ = {dfi5_}')

print('Ширина венца колеса:')
b1: float = round(3 * ksi * m1, 4)
b2345: float = round(3 * ksi * m2345, 4)
b234_: float = round(3 * ksi * m234_, 4)
b5_: float = round(12 * 0.5, 4)
print(f'b1 = {b1}')
print(f'b2 = b3 = b4 = b5 = {b2345}')
print(f'b2_ = b3_ = b4_ = {b234_}')
print(f'b5_ = {b5_}')

print('Межосевые расстояния:')
a12 = round((di1 + di2345) / 2, 4)
a2_3 = round((di234_ + di2345) / 2, 4)
print(f'a12 = {a12}')
print(f'a2_3 = {a2_3}')

"""
##############################################
Глава 3
##############################################
"""
print()
print('-----Глава 3')
eta: float = 0.95
Pv: float = 0.008
Ps: float = 0.03
k: int = 4
m: int = 1
n: int = 3
eta_gen: float = round(math.pow(eta, k) * math.pow(1 - Pv, m) * math.pow(1 - Ps, n), 4)
print(f'КПД общее = {eta_gen}')
