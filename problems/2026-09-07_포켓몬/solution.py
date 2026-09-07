# 1차 시도 (통과, 프로그래머스 제출본)
def solution_v1(nums):
    answer = []
    ans = 0

    for i in range(len(nums)):
        if nums[i] not in answer:
            answer.append(nums[i])

    if len(answer) >= len(nums)/2:
        ans = len(nums)/2
    else:
        ans = len(answer)

    return ans


# 개선 (set 사용, O(n))
def solution(nums):
    return min(len(set(nums)), len(nums) // 2)
