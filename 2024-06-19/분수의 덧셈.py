from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):

    fraction1 = Fraction(numer1, denom1)
    fraction2 = Fraction(numer2, denom2)

    result = fraction1 + fraction2

    answer = [result.numerator, result.denominator]
    
    return answer

numer1, denom1, numer2, denom2 = 1, 2, 3, 4
result = solution(numer1, denom1, numer2, denom2)

print(f"분수 계산 결과: {result[0]}/{result[1]}")
