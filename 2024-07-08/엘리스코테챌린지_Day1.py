def next_problem_count(today_count):
    digits = list(str(today_count))
    n = len(digits)

    i = n - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    if i == -1:
        return -1

    j = n - 1
    while digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    return int(''.join(digits))

N = int(input())

print(next_problem_count(N))
