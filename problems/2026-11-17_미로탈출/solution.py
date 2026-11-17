from collections import deque


def solution(maps):
    answer = 0

    # [함수로 빼기] S→L, L→E 두 번 쓰니까 시작점/도착점만 받아서 거리 계산
    def bfs(start, end):
        sr, sc = start      # 튜플 언패킹 (.split()은 문자열용)
        er, ec = end
        n, m = len(maps), len(maps[0])
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        dist = [[-1] * m for _ in range(n)]
        dist[sr][sc] = 0    # 이동 시간을 세는 문제라 0부터
        q = deque([(sr,sc)])

        while q:
            r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                # [maps 조건] S, O, L, E 모두 지나갈 수 있음 → 못 가는 X만 뺀다
                # (== "O"로 쓰면 L, E 칸에 못 들어가서 항상 -1)
                if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] != "X" and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        # 갈 수 있는 칸 전부 거리를 적은 뒤, end 칸 값만 읽음 (못 가면 -1 그대로)
        return dist[er][ec]

    # [이중 for문] 'S'(지도 글자)를 찾아서 S(좌표 변수)에 (i, j) 저장
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)

    # [마지막] 둘 중 하나라도 못 가면 -1, 아니면 두 거리의 합
    if bfs(S,L) == -1 or bfs(L,E) == -1:
        answer = -1
    else:
        answer = bfs(S,L) + bfs(L,E)

    return answer


if __name__ == "__main__":
    print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))  # 16
    print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))  # -1
