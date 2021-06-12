# game parameters:
end = 59  # for end==x, game with (a, b) ends if a+b>=x
start_cnt = 5  # start position is (5, S)


# possible moves:
def f1(a, b):
    return a, b + 2


def f2(a, b):
    return a, b * 2


def f3(a, b):
    return a + 2, b


def f4(a, b):
    return a * 2, b


poss_moves = [f1, f2, f3, f4]  # possible moves in list:
dp = [[None] * end for i2 in range(end)]


# if dp[a][b] > 0, first wins, if dp[a][b] < 0, second wins.
# abs(dp[a][b]) - maximal number of moves of winner


def calc(a, b):  # recursive function to calculate dp and return dp[a][b]:
    if a + b >= end:  # already lose
        if a < end and b < end:
            dp[a][b] = 0
        return 0
    if dp[a][b] is not None:  # if dp[a][b] is already computed
        return dp[a][b]
    max_good = -10 ** 9
    max_win = -1
    for f in poss_moves:  # try all moves
        a1, b1 = f(a, b)
        res = calc(a1, b1)
        if res <= 0:
            max_good = max(max_good, res)
        else:
            max_win = max(max_win, res)
    if max_good > -10 ** 9: # if we win
        dp[a][b] = -max_good + 1
    else: # if we lose
        dp[a][b] = -max_win
    return dp[a][b]

for a in range(1, end):
    for b in range(1, end):
        calc(a, b)

# how to solve tasks:
# 19 - manually
# 20:
#