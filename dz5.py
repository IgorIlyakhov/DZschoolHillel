A = [1, 2, 3, 4, 5, 6]
A1 = len(A) // 2
if A1 % 2:
    print([A[:A1], A[A1:len(A)]])
else:
    A1 += 1
    print([A[:A1], A[A1:len(A)]])
