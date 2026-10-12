from collections import deque

def solve(start, goal):
    q = deque([(start, [])])
    visited = {tuple(start)}

    while q:
        state, path = q.popleft()

        if state == goal:
            return path + [state]

        i = state.index(0)
        for j in [i-3, i+3, i-1, i+1]:
            if 0 <= j < 9 and abs(i//3 - j//3) + abs(i%3 - j%3) == 1:
                new = state[:]
                new[i], new[j] = new[j], new[i]
                t = tuple(new)

                if t not in visited:
                    visited.add(t)
                    q.append((new, path + [state]))

    return None

start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

result = solve(start, goal)

if result:
    for s in result:
        print(s[:3])
        print(s[3:6])
        print(s[6:])
        print()
else:
    print("No solution")
