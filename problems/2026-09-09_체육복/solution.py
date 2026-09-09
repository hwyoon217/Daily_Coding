# 체육복 (프로그래머스 Lv.1, 그리디/set)
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
#
# 문제 요약:
# 학생 n명(번호 1~n), 여벌 체육복 있는 학생 번호 목록 reserve,
# 체육복 잃어버린 학생 번호 목록 lost가 주어짐.
# 바로 옆번호(자신 번호 -1 또는 +1) 학생에게만 빌려줄 수 있음.
# 여벌이 있으면서 잃어버리기도 한 학생은 자기 것부터 챙긴다고 가정.
# 체육수업을 들을 수 있는 학생 수의 최댓값을 return 하기.

def solution(n, lost, reserve):
    u_lost = set(lost) - set(reserve)
    u_reserve = set(reserve) - set(lost)

    for i in u_lost:
        if i - 1 in u_reserve:
            u_reserve.remove(i - 1)
        elif i + 1 in u_reserve:
            u_reserve.remove(i + 1)
        else:
            n -= 1

    return n


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))  # 5
    print(solution(5, [2, 4], [3]))        # 4
    print(solution(3, [3], [1]))           # 2
