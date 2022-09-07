# https://app.codility.com/demo/results/training2MZ33J-G9M/

def solution(N: int):
    bits = []

    while N > 0:
        bits.append(N%2)
        N = N // 2

    bits.reverse()
    
    shouldCount = bool(False)
    maxValue = int(0)
    counter = int(0)

    for elem in bits:
        if not shouldCount:
            if elem:
                shouldCount = True
            continue

        if elem:
            maxValue = counter if counter > maxValue else maxValue
            counter = 0
        else:
            counter += 1
    
    return maxValue
