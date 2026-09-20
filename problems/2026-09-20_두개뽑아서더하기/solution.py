# 두 개 뽑아서 더하기 (프로그래머스 Lv.1, 해시/조합)
# https://school.programmers.co.kr/learn/courses/30/lessons/68644
#
# 문제 요약:
# numbers: 정수 배열
# 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 값을
# 중복 없이 오름차순으로 정렬해 return

from itertools import combinations


def solution(numbers):
    answer = set()
    for a, b in combinations(numbers, 2):
        answer.add(a + b)
    return sorted(answer)


# 참고용 한 줄 버전 (set comprehension)
# def solution(numbers):
#     return sorted({a + b for a, b in combinations(numbers, 2)})


# 참고용 최초 풀이 (이중 for문 + i == j 스킵)
# combinations를 쓰면 애초에 같은 인덱스 조합 자체를 만들지 않기 때문에
# i == j 체크가 필요 없어지고, (i, j)/(j, i) 중복 계산도 사라짐
#
# def solution(numbers):
#     answer = set()
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             if i == j:
#                 continue
#             answer.add(numbers[i] + numbers[j])
#     return sorted(answer)


if __name__ == "__main__":
    print(solution([2, 1, 3, 4, 1]))  # [2, 3, 4, 5, 6, 7]
    print(solution([5, 0, 2, 7]))     # [2, 5, 7, 9, 12]
