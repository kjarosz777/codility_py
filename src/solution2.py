# https://app.codility.com/demo/results/trainingC9XV8E-4G8/

def solution(A: list[int], K: int):
    
    if len(A) < 2:
        return A

    result = [0] * len(A)
    for i, elem in enumerate(A):
        newPos = (i + K)%len(A)
        result[newPos] = elem

    return result
