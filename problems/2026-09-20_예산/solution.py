# 예산 (프로그래머스 Lv.1, 정렬)
# https://school.programmers.co.kr/learn/courses/30/lessons/64068
#
# 문제 요약:
# d: 각 부서가 신청한 예산 배열
# budget: 부서 지원에 사용할 수 있는 최대 예산
# 신청 금액이 적은 부서부터 지원해야 가장 많은 부서를 지원할 수 있음
# 최대 몇 개 부서까지 지원 가능한지 return


def solution(d, budget):
    d.sort()
    tot = 0
    for i, s in enumerate(d):
        tot += s
        if tot > budget:
            return i
    return len(d)


if __name__ == "__main__":
    print(solution([1, 3, 2, 5, 4], 9))   # 3
    print(solution([2, 2, 3, 3], 10))     # 4
