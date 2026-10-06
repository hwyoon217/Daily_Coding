def solution(k, dungeons):
    answer = 0
    visited = [0] * len(dungeons)

    def dfs(hp, count):
        nonlocal answer
        answer = max(answer, count)

        for idx, (need, cost) in enumerate(dungeons):
            if not visited[idx] and hp >= need:
                visited[idx] = 1
                dfs(hp-cost, count+1)
                visited[idx] = 0
    dfs(k,0)
    return answer
