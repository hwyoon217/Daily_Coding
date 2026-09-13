# 신고 결과 받기 (프로그래머스 Lv.1, 해시)
# https://school.programmers.co.kr/learn/courses/30/lessons/92334
#
# 문제 요약:
# id_list: 유저 아이디 목록
# report: "신고자 피신고자" 형태의 신고 기록 목록 (같은 사람을 여러 번 신고해도 1회로 처리)
# k: 정지 기준 신고 횟수 (한 유저가 k명 이상에게 신고당하면 정지)
# 정지된 유저를 신고한 사람은 정지 처리 결과 메일을 1통 받음
# id_list 순서대로, 각 유저가 받는 메일 수를 배열로 return

from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report_dict = defaultdict(set)   # 피신고자 -> 신고자 집합 (정지 판정용)
    result_dict = defaultdict(list)  # 신고자 -> 신고한 대상 리스트 (최종 카운트용)

    for i in set(report):
        a, b = i.split()
        report_dict[b].add(a)
        result_dict[a].append(b)

    filtered_set = {b for b, reporters in report_dict.items() if len(reporters) >= k}

    for i, user in enumerate(id_list):
        answer[i] = sum(1 for t in result_dict[user] if t in filtered_set)

    return answer


if __name__ == "__main__":
    print(solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    ))  # [2, 1, 1, 0]
    print(solution(
        ["con", "ryan"],
        ["ryan con", "ryan con"],
        3,
    ))  # [0, 0]
