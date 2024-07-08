# Day 1
## 문제
시간 제한: 1초
엘리스 토끼는 목표량을 정해 수학 문제를 열심히 풉니다. 목표량은 정수입니다.

내일 풀 수학 문제의 개수는 오늘 푼 문제 개수의 수와 숫자의 구성이 같으면서, 오늘 푼 문제 개수의 수보다 큰 수 중 가장 작은 수입니다.

예를 들어, 오늘 67문제를 풀었으면 다음 날 76문제를 풉니다.

오늘 푼 문제의 개수를 줬을 때 다음날 풀 문제의 개수를 출력하는 프로그램을 작성하세요.

## 풀이
```python
def next_problem_count(today_count):
    # 오늘 푼 문제의 개수를 문자열로 변환한 후 각 자리 숫자를 리스트로 변환
    digits = list(str(today_count))
    # 숫자 리스트의 길이를 구함
    n = len(digits)

    # 오른쪽에서부터 처음으로 감소하는 요소를 찾기 위해 i를 초기화
    i = n - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # 만약 감소하는 요소를 찾지 못했다면, 이는 숫자가 내림차순으로 정렬된 경우
    if i == -1:
        return -1

    # i 위치에서 찾은 요소보다 큰 요소를 찾기 위해 j를 초기화
    j = n - 1
    while digits[j] <= digits[i]:
        j -= 1

    # i와 j 위치의 요소를 교환
    digits[i], digits[j] = digits[j], digits[i]
    # i 위치 이후의 숫자들을 오름차순으로 정렬
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    # 숫자 리스트를 문자열로 결합한 후, 정수로 변환하여 반환
    return int(''.join(digits))

# 첫 번째 줄에 오늘 푼 문제의 개수인 자연수 N을 입력받음
N = int(input())

# next_problem_count 함수를 호출하여 내일 풀 문제의 개수를 계산하고 결과를 출력
print(next_problem_count(N))

```

