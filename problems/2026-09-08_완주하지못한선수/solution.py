# 완주하지 못한 선수 (프로그래머스 Lv.1, 해시)
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
#
# 문제 요약:
# 마라톤 참가 선수 이름 목록 participant와 완주한 선수 이름 목록 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하기.
# - completion의 길이는 participant의 길이보다 1 작음 (완주 못한 선수는 항상 1명)
# - 동명이인이 있을 수 있음

from collections import Counter


# 1차 시도 (통과, 정렬 비교 방식)
def solution_v1(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


# 2차 시도 (Counter 사용)
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # leo
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
                    ["josipa", "filipa", "marina", "nikola"]))  # vinko
    print(solution(["mislav", "stanko", "mislav", "ana"],
                    ["stanko", "ana", "mislav"]))  # mislav (동명이인)
