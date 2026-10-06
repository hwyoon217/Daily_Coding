def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    visited = [0] * len(numbers)
    nums = set()

    def dfs(s):
        if s:
            nums.add(int(s))
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = 1
                dfs(s + numbers[i])
                visited[i] = 0


    dfs("")


    return sum(is_prime(n) for n in nums)
