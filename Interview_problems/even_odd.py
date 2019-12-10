def even_odd_constant_space(A) -> None:
    i, j = 0, len(A) - 1

    while i < j:
        if A[i] % 2 == 0:
            i += 1
        else:
            A[i], A[j] = A[j], A[i]
            j -= 1

    print(A)


test_nums = [1,2,5,3,4,5,7,8,9,2,3,4,3,3]
even_odd_constant_space(test_nums)