import numpy as np


# 默认 z0 = 1

def abcd_to_z(a, b, c, d):
    z11 = a / c
    z12 = (a * d - b * c) / c
    z21 = 1 / c
    z22 = d / c
    matrix_z = np.mat([[z11, z12], [z21, z22]])
    print(matrix_z)
    return matrix_z


def abcd_to_y(a, b, c, d):
    y11 = d / b
    y12 = (b * c - a * d) / b
    y21 = 1 / b
    y22 = a / b
    matrix_y = np.mat([[y11, y12], [y21, y22]])
    print(matrix_y)
    return matrix_y


def abcd_to_s(a, b, c, d):
    s11_ = a + b - c - d
    s12_ = 2 * (a * b - b * c)
    s21_ = 2
    s22_ = (-a + b - c + d)
    coefficient = 1 / (a + b + c + d)
    matrix_s = coefficient * np.mat([[s11_, s12_], [s21_, s22_]])
    print(matrix_s)
    return matrix_s


def z_to_abcd(z1, z2, z3, z4):
    a_ = z1
    b_ = z1 * z4 - z2 * z3
    c_ = 1
    d_ = z4
    coefficient = 1 / z3
    matrix_abcd = coefficient * np.mat([[a_, b_], [c_, d_]])
    print(matrix_abcd)
    return matrix_abcd


def y_to_abcd(y1, y2, y3, y4):
    a_ = -y4
    b_ = -1
    c_ = y2 * y3 - y1 * y4
    d_ = -y1
    coefficient = 1 / y3
    matrix_abcd = coefficient * np.mat([[a_, b_], [c_, d_]])
    print(matrix_abcd)
    return matrix_abcd


def s_to_abcd(s1, s2, s3, s4):
    a_ = (1 + s1) * (1 - s4) + s2 * s3
    b_ = (1 + s1) * (1 + s4) - s2 * s3
    c_ = (1 - s1) * (1 - s4) - s2 * s3
    d_ = (1 - s1) * (1 + s4) + s2 * s3
    coefficient = 1 / (2 * s3)
    matrix_abcd = coefficient * np.mat([[a_, b_], [c_, d_]])
    print(matrix_abcd)
    return matrix_abcd


def z_to_y(z1, z2, z3, z4):
    y11_ = z4
    y12_ = -z2
    y21_ = -z3
    y22_ = z1
    coef = 1 / ((z1 * z4) - (z2 * z3))
    matrix_y = coef * np.mat([[y11_, y12_], [y21_, y22_]])
    print(matrix_y)
    return matrix_y


def z_to_s(z1, z2, z3, z4):
    s11_ = z1
    s12_ = z1 * z4 - z2 * z3
    s21_ = 1
    s22_ = z4
    coef = 1 / z3
    matrix_s = coef * np.mat([[s11_, s12_], [s21_, s22_]])
    print(matrix_s)
    return matrix_s


def y_to_z(y1, y2, y3, y4):
    z11_ = y4
    z12_ = -y2
    z21_ = -y3
    z22_ = y1
    coef = 1 / (y1 * y4 - y2 * y3)
    matrix_z = coef * np.mat([[z11_, z12_], [z21_, z22_]])
    print(matrix_z)
    return matrix_z


def y_to_s(y1, y2, y3, y4):
    s11_ = (1 - y1) * (1 + y4) + y2 * y3
    s12_ = -2 * y2
    s21_ = -2 * y3
    s22_ = (1 + y1) * (1 - y4) + y2 * y3
    coef = 1 / ((1 + y1) * (1 + y4) - y2 * y3)
    matrix_s = coef * np.mat([[s11_, s12_], [s21_, s22_]])
    print(matrix_s)
    return matrix_s


def s_to_z(s1, s2, s3, s4):
    z11_ = (1 + s1) * (1 - s4) + s2 * s3
    z12_ = 2 * s2
    z21_ = 2 * s3
    z22_ = (1 - s1) * (1 + s4) + s2 * s3
    coef = 1 / ((1 - s1) * (1 - s4) - s2 * s3)
    matrix_z = coef * np.mat([[z11_, z12_], [z21_, z22_]])
    print(matrix_z)
    return matrix_z

def s_to_y(s1, s2, s3, s4):
    y11_ = (1 - s1) * (1 + s4) + s2 * s3
    y12_ = -2 * s2
    y21_ = -2 * s3
    y22_ = (1 + s1) * (1 - s4) + s2 * s3
    coef = 1 / ((1 + s1) * (1 + s4) - s2 * s3)
    matrix_y = coef * np.mat([[y11_, y12_], [y21_, y22_]])
    print(matrix_y)
    return matrix_y
