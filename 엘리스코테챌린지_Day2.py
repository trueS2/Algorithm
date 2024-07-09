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
