# 두 개 뽑아서 더하기

- 플랫폼: 프로그래머스 (Lv.1, 해시/조합)

## 접근

- 최초 풀이: 이중 for문으로 모든 `(i, j)` 순서쌍을 돌면서 `i == j`만 스킵하고 `set`에 합을 누적
  - `i == j` 체크는 단순 최적화가 아니라 **정답 정확성에 필수**: 이걸 빼면 `numbers[i] + numbers[i]`(같은 원소를 두 번 뽑은 값)까지 포함돼서 오답이 됨. `set`은 "중복 제거"만 해줄 뿐, "애초에 포함되면 안 되는 값"까지 걸러주진 않음.
  - 다만 `(i, j)`와 `(j, i)`를 둘 다 도는 건 같은 합을 두 번 계산하는 중복 작업
- 개선: `itertools.combinations(numbers, 2)`로 교체
  - 서로 다른 인덱스 조합을 순서 없이 한 번씩만 생성하므로 `i == j` 체크 자체가 불필요해짐 (제거된 게 아니라 `combinations`가 대신 처리)
  - `(i, j)`/`(j, i)` 중복 계산도 사라짐

```python
from itertools import combinations

def solution(numbers):
    answer = set()
    for a, b in combinations(numbers, 2):
        answer.add(a + b)
    return sorted(answer)
```

- 참고용 한 줄 버전: `return sorted({a + b for a, b in combinations(numbers, 2)})`
  - set comprehension으로 `set() + for + add()` 3줄을 한 줄로 압축한 것뿐, 동작은 동일

## 배운 점 / 실수

- `sorted(list(answer))`처럼 정렬 전에 굳이 `list()`로 먼저 변환하는 습관이 있었음. `sorted()`는 어떤 이터러블이든 받아서 리스트로 반환하므로 `list()` 래핑은 불필요한 중간 객체만 만듦. `sorted(answer)`로 충분.

