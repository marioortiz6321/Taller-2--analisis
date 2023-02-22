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

with open("test_cases.in", "r") as f:
  for line in f:
       line=line.strip()
       if line!="10000":
              S=[float(x) for x in line.split(" ")]
              max,pos=BiggestI_Difference(S) 
              with open("test_cases.out", "a") as f:
                f.write(str(pos)+" "+str(max)+"\n")


