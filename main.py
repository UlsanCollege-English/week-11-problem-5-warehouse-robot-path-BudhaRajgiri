from collections import deque

def parse_grid(lines):
    graph = {}
    start = None
    target = None

    rows = len(lines)
    cols = len(lines[0])

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] != '#':
                key = f"{r},{c}"
                graph[key] = []
                if lines[r][c] == 'S':
                    start = key
                if lines[r][c] == 'T':
                    target = key

    # build edges
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == '#':
                continue
            key = f"{r},{c}"
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] != '#':
                    graph[key].append(f"{nr},{nc}")

    return graph, start, target


def grid_shortest_path(lines):
    graph, start, target = parse_grid(lines)

    # >>> FIX HERE <<<
    if start == target:
        return [start]

    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == target:
            return path

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(path + [nei])

    return None
