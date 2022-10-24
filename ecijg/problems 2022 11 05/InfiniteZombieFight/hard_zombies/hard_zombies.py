import sys
import time 
from collections import deque

def LS(): return sys.stdin.readline().strip().split()
def I(): return int(sys.stdin.readline().strip())

def solve():
    n = I()
    f = deque(LS())
    m = I()
    for i in range(m):
        fight = LS()
        side = fight[0]
        fighter = fight[1]

        if fighter != 'D':
            if side == 'L':
                f.appendleft(fighter)
            else:
                f.append(fighter)
            continue

        if len(f) == 0:
            continue

        if side == 'L':
            f.popleft()
        else:
            f.pop()

    return f

def main():
    
    start_time = time.time()

    tests = I()
    for i in range(tests):
        ans = solve()
        print(f"Scenario {i+1}")
        print(f"{len(ans)} survivors")
        for i in range(len(ans)):
            if i > 0:
                print(" ",end="")
            print(ans[i], end="")
        print()
    
    
    #print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

