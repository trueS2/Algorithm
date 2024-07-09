# Day 2
## 문제
시간 제한: 1초
정리 정돈을 좋아하는 k씨의 본명은 아무도 모릅니다. 사람들은 k씨의 특이한 행동 2가지 때문에 그를 '정리 정돈을 좋아하는 k씨'라고 부릅니다. 그 두 가지 행동은 그가 숫자를 정리하는 일을 하면 아무 규칙없이 나열되어 있는 숫자중 범위를 정한 후 무조건 오름차순으로 정리한다는 것, 그리고 오름차순으로 정리된 숫자 중 k번째 숫자를 선택한다는 것입니다

## 풀이
```python
# 입력 받기
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 결과를 저장할 리스트
results = []

# 각 작업에 대해 처리
for _ in range(m):
    i, j, k = map(int, input().split())
    # 범위 설정 및 정렬
    sub_array = sorted(array[i-1:j])
    # k번째 숫자 선택
    results.append(sub_array[k-1])

# 최종 결과 출력
for result in results:
    print(result)

```