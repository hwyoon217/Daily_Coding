# 신고 결과 받기

- 플랫폼: 프로그래머스 (Lv.1, 해시)

## 접근

- `set(report)`로 중복 신고("같은 사람이 같은 대상을 여러 번 신고" 케이스) 제거 후 시작
- 두 개의 dict를 각각 다른 용도로 사용
  - `report_dict = defaultdict(set)`: 피신고자 -> 신고자 집합. 정지 여부(`len(reporters) >= k`) 판정용
  - `result_dict = defaultdict(list)`: 신고자 -> 신고한 대상 리스트. 최종 메일 수 계산용
- `filtered_set`: `report_dict`에서 신고자 수가 k 이상인 피신고자만 모은 set (정지된 유저 목록)
- `id_list`를 `enumerate`로 순회하면서, 각 유저가 신고한 대상(`result_dict[user]`) 중 `filtered_set`에 속한 개수를 세어 `answer[i]`에 반영

## 배운 점 / 실수

- 처음엔 `report_dict`(피신고자 -> 신고자 집합) 하나만 만들고, `answer[j] += 1`처럼 **키 이름(문자열)을 그대로 인덱스처럼 쓰려는 실수**를 함. dict 순회로 나오는 키는 인덱스가 아니라는 걸 헷갈림.
- 또한 애초에 "정지당한 사람"과 "메일을 받아야 할 신고자"를 같은 대상으로 착각해서, 카운트를 엉뚱한 쪽(정지당한 사람 본인)에 주려고 했던 논리 오류도 있었음.
- 해결: 판정용 dict(`report_dict`)와 결과 집계용 dict(`result_dict`)의 **역할을 분리**하고, `id_list.index()`(O(n), 검색할 때마다 리스트 전체 스캔) 대신 `enumerate(id_list)`로 인덱스를 직접 얻어 O(1)에 가깝게 처리.
- 다른 사람 풀이 중 `id_list.index(...)`를 반복 호출하는 버전은 전체 시간복잡도가 O(n×m)으로 느려짐 — 리스트 `.index()`를 반복문 안에서 쓰는 패턴은 피할 것 (지난 체육복 문제의 "set을 list로 되돌리는" 실수와 같은 계열의 시간복잡도 함정).
