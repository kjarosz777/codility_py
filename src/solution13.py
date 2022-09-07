# https://app.codility.com/demo/results/trainingABU5FR-AUD/

def solution(S: str, P: list[int], Q: list[int]) -> list[int]:
    aSums = [0] * (len(S) + 1)
    cSums = [0] * (len(S) + 1)
    gSums = [0] * (len(S) + 1)

    for i, elem in enumerate(S):
        aSums[i+1] = aSums[i]
        cSums[i+1] = cSums[i]
        gSums[i+1] = gSums[i]

        match elem:
            case "A":
               aSums[i+1] += 1
            case "C":
               cSums[i+1] += 1
            case "G":
               gSums[i+1] += 1
    
    result = []
    for i in range(0, len(P)):
        start = P[i]
        last = Q[i]

        if aSums[last+1] - aSums[start] > 0:
            result.append(1)
        elif cSums[last+1] - cSums[start] > 0:
            result.append(2)
        elif gSums[last+1] - gSums[start] > 0:
            result.append(3)
        else:
            result.append(4)


    return result
