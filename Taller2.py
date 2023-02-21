def BiggestI_Difference(S):
    n = len(S)
    max_diff = float('-inf')
    pos = None
    left_sums = [0] * (n+1)  # Almacena la suma acumulada de los elementos a la izquierda
    for i in range(1, n+1):
        left_sums[i] = left_sums[i-1] + S[i-1]
    right_sum = 0
    for i in range(n-1, 0, -1):
        right_sum += S[i]
        diff = left_sums[i] - right_sum
        if diff > max_diff:
            max_diff = diff
            pos = i
    return (max_diff, pos)

S = [10, 5, 3, 4, 2, 1,5]
max_diff, pos = BiggestI_Difference(S)
print("El mayor valor de la diferencia entre la suma de los elementos a la izquierda y a la derecha es: ", max_diff)
print("La posición del elemento que maximiza la diferencia es: ", pos)