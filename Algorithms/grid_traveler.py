
def grid_traveler(s:int, d:int, memo:dict={}) -> int:
    
    if 0 in [s, d]: return 0
    elif 1 in [s, d]: return 1
    elif 2 in [s, d]: return max(s,d)

    if s*d in memo:
        return memo[s*d]
    
    memo[s*d] = grid_traveler(s-1, d, memo) + grid_traveler(s, d-1, memo)
    return memo[s*d]

if __name__ == '__main__':
    s = input('eter 2 values with space between: ')
    x,y = [int(i) for i in s.split()]
    print(grid_traveler(x,y))


