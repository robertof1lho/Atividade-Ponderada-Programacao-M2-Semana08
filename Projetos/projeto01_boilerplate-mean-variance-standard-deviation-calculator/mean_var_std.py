import numpy as np

def calculate(list):
    # Verificar se a matriz é 3x3
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    matriz = np.array(list).reshape(3,3)

    # Calcular média
    mean = np.mean(matriz)
    mean_axis1 = np.mean(matriz, axis=0)
    mean_axis2 = np.mean(matriz, axis=1)

    # Calcular variância
    variance = np.var(matriz)
    variance_axis1 = np.var(matriz, axis=0)
    variance_axis2 = np.var(matriz, axis=1)

    # Calcular desvio padrão
    std = np.std(matriz)
    std_axis1 = np.std(matriz, axis=0)
    std_axis2 = np.std(matriz, axis=1)

    # Calcular máximo
    max_value = np.max(matriz)
    max_axis1 = np.max(matriz, axis=0)
    max_axis2 = np.max(matriz, axis=1)

    # Calcular mínimo
    min_value = np.min(matriz)
    min_axis1 = np.min(matriz, axis=0)
    min_axis2 = np.min(matriz, axis=1)

    # Calcular soma
    sum_value = np.sum(matriz)
    sum_axis1 = np.sum(matriz, axis=0)
    sum_axis2 = np.sum(matriz, axis=1)

    return {
        'mean': [mean_axis1.tolist(), mean_axis2.tolist(), mean],
        'variance': [variance_axis1.tolist(), variance_axis2.tolist(), variance],
        'standard deviation': [std_axis1.tolist(), std_axis2.tolist(), std],
        'max': [max_axis1.tolist(), max_axis2.tolist(), max_value],
        'min': [min_axis1.tolist(), min_axis2.tolist(), min_value],
        'sum': [sum_axis1.tolist(), sum_axis2.tolist(), sum_value]
    }

result = calculate([4, 4, 7, 9, 56, 3, 1, 6, 3])
print(result)
