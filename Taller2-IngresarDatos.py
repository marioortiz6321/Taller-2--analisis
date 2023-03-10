def BiggestI_Difference(S):
    max_diff = float('-inf')
    pos = None
    for i in range(1, len(S)+1):
        left_sum = sumarSub(S[:i-1])
        right_sum = sumarSub(S[i:])
        if max_diff < (left_sum - right_sum):
            max_diff = left_sum - right_sum
            pos = i
    return (max_diff, pos)

def sumarSub(S):
    if len(S) == 0:
        return 0
    if len(S) == 1:
        return S[0]
    else:
        mid = len(S) // 2
        left_sum = sumarSub(S[:mid])
        right_sum = sumarSub(S[mid:])
        return left_sum + right_sum


n=int(input("Ingrese el numero de elementos de la secuencia: "))
S=[float(input("Ingrese un elemento de la secuencia: ")) for i in range(n)]
max,pos=BiggestI_Difference(S)
print("El pivote es el elemento numero:", pos, "de la secuencia")
print("La i-diferencia es:", max)