from collections import deque

def solution(maps):
    # 시작점과 끝점 설정
    # 상, 하, 좌, 우 방향
    # 방문 기록
    # (x, y, 현재까지의 거리) 큐에 추가
    n, m = len(maps), len(maps[0])
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False] * m for _ in range(n)]
    q = deque([(0,0,1)])
    visited[0][0] = True

    while q:
        # 도착점에 도달하면 거리 반환
        r, c, d = q.popleft()
        if r == n-1 and c == m-1:
            return d

        # 상, 하, 좌, 우로 이동
        for dr, dc in direction:
            nr, nc = r+dr, c+dc
            if 0<= nr < n and 0<= nc < m and maps[nr][nc]==1 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr,nc,d+1))

    return -1  # 도달할 수 없으면 -1 반환
