N,M = map(int, input().split())
chess = [input() for _ in range(N)]
print(chess)

white_board = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBBBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
]

black_board = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBBBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]

def check(i, j): 
    result_w = 0
    result_b = 0
    for di in range(8):
        for dj in range(8): 
            Ni, Nj = i + di, i + dj 
            if chess[Ni][Nj] != white_board[di][dj]:
                result_w += 1
            if chess[Ni][Nj] != black_board[di][dj]:
                result_b += 1
    return min(result_w, result_b)

result = 10000000
for i in range(N - 7): 
    for j in range(M - 7): 
        result = min(result, check(i, j))

print(result)