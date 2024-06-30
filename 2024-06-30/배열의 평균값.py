arr = [1,2,3,4,5,6,7,8,9,10]

def solution(arr):
    answer = 0
    
    for i in arr :
        answer += i
    return answer/len(arr)

print(solution(arr))