# 의상 (프로그래머스 Lv.2, 해시)
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
#
# 문제 요약:
# clothes: [의상 이름, 의상 종류] 목록
# 하루에 종류별로 최대 1개씩 입을 수 있고, 최소 1개는 입어야 함
# 서로 다른 옷 조합의 수를 return

from collections import defaultdict


def solution(clothes):
    # 1단계: 종류별로 옷이 몇 개인지 세기 (예: {"headgear": 2, "eyewear": 1})
    c_map = defaultdict(int)
    for name, cat in clothes:
        c_map[cat] += 1

    # 2단계: 종류마다 "그 중 하나 입기 + 안 입기" → (개수 + 1)가지, 전부 곱하기
    answer = 1
    for c in c_map.values():
        answer *= (c + 1)

    # 3단계: 모든 종류를 다 안 입은 경우 1가지는 빼기 (최소 한 개는 입어야 함)
    return answer - 1


if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))  # 3
