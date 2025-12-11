from collections import deque
import re
    
def min_presses_bfs(target, buttons):
    n_lights = len(target)
    start = (0,) * n_lights
    
    # Already at target
    if start == target:
        return 0
    
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        state, presses = queue.popleft()
        
        # Try each button
        for button in buttons:
            # Apply button (toggle affected lights)
            new_state = list(state)
            for light_idx in button:
                new_state[light_idx] ^= 1
            new_state = tuple(new_state)
            
            # Check if we reached target
            if new_state == target:
                return presses + 1
            
            # Add to queue if not visited
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))
    
    return -1  # No solution found

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
total = 0
for line in lines:
    target = tuple(0 if x == "." else 1 for x in line.split("]")[0].split("[")[1])
    buttons_str = line.split("]")[1].split("{")[0]
    buttons = [tuple(int(x) for x in re.findall(r'\d+', button)) for button in re.findall(r'\([^)]+\)', buttons_str)]
    total += min_presses_bfs(target, buttons)
print(total)