# 사용자로부터 두 정수 입력 받기
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

# 합과 차 계산
sum_result = num1 + num2
diff_result = num1 - num2

# 곱과 나눗셈 계산
mul_result = num1 * num2
div_result = num1 / num2

# 두수의 곱에 2 곱하기
mul2_result = num1 * num2 * 2

# 결과 출력
print("두 수의 합:", sum_result)
print("두 수의 차:", diff_result)
print("두 수의 곱:", mul_result)
print("두 수의 나눗셈:", div_result)
print("두 수의 곱 * 2:", mul2_result)