import numpy as np

def solve_cramer(A, B):
    n = A.shape[0]
    if A.shape[1] != n:
        raise ValueError("Матрица A должна быть квадратной")
    
    det_A = np.linalg.det(A)
    print("Детерминант матрицы A: ", round(det_A.real, 4) + round(det_A.imag, 4)*1j)
    
    if np.isclose(det_A, 0):
        raise ValueError("Детерминант матрицы A равен нулю, система не имеет уникального решения")
    
    # Решение методом Крамера
    x = np.zeros(n, dtype=complex) 
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = B
        
        det_A_i = np.linalg.det(A_i)
        print(f"Детерминант матрицы A_{i}: {round(det_A_i.real, 4) + round(det_A_i.imag, 4)*1j}")
        
        x[i] = det_A_i / det_A
    
    return x

# Пример системы линейных уравнений:
A = np.array([
        [3 - 1j, 4 - 2j],
        [4 + 2j, -(2 + 3j)]
    ], dtype=complex) # уравнения
B = np.array([2 + 6j, 5 + 4j], dtype=complex) # ответы

x = solve_cramer(A, B)
# Округление решения
x_rounded = np.round(x, 4)
print("Решение системы: ", x_rounded) # ниче не работает и я не знаю, почему. в теории, всё правильно :)
