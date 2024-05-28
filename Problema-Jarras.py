from collections import deque
def solve_jug_problem():
    jug1_capacity = 3
    jug2_capacity = 5
    goal = 4
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        (jug1, jug2), path = queue.popleft()

        if jug2 == goal:
            path.append((jug1, jug2))
            return path
        next_states = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug2 + jug1)),
            (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1)))
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(jug1, jug2)]))
    return None
solution = solve_jug_problem()
if solution:
    for step in solution:
        print(step)
else:
    print("No hay solución.")
