def BiggestI_Difference(S):
    max_diff = float('-inf')
    pos = None
    for i in range(1, len(S)+1):
        left_sum = sumarSub(S, 1, i-1)
        right_sum = sumarSub(S, i+1, len(S))
        if max_diff < (left_sum - right_sum):
            max_diff = left_sum - right_sum
            pos = i
    return (max_diff, pos)
def sumarSub(S, l, r):
    if l > r:
        return 0
    elif r - l + 1 <= 1000:
        return sum(S[l-1:r])
    else:
        q = (r - l) // 2
        left_sum = sumarSub(S, l, l+q)
        right_sum = sumarSub(S, l+q+1, r)
        return left_sum + right_sum

S = [1,2,3,4,5]
max,pos=BiggestI_Difference(S)
print("La diferencia maxima es: ",max," y se encuentra en la posicion: ",pos)