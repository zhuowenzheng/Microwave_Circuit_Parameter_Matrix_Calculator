import numpy as np
import microwave

def z_transition_function(a, b, c, d):
    z11 = a / c
    z12 = (a * d - b * c) / c
    z21 = 1 / c
    z22 = d / c
    matrix_z = np.mat([[z11, z12], [z21, z22]])
    print(matrix_z)
    return matrix_z


def y_transition_function(a, b, c, d):
    y11 = d / b
    y12 = (b * c - a * d) / b
    y21 = 1 / b
    y22 = a / b
    matrix_y = np.mat([[y11, y12], [y21, y22]])
    print(matrix_y)
    return matrix_y


def s_transition_function(a, b, c, d):
    s11_ = a + b - c - d
    s12_ = 2 * (a * b - b * c)
    s21_ = 2
    s22_ = (-a + b - c + d)
    coefficient = 1 / (a + b + c + d)
    matrix_s = coefficient * np.mat([[s11_, s12_], [s21_, s22_]])
    print(matrix_s)
    return matrix_s
