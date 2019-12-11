# Chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""

int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

"""

# 데이터 타입
str1 = "python"
bool1 = False
str2 = 'Anaconda'
float_v = 10.0
int_v = 3
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "Version": 2.0
}
tuple = (7, 8, 9)
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool1))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))
print()
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) x**y -> 2**3 2^3

"""

# 정수 선언
i = 77
i2 = -14
big_int = 777777777777777777788888888888888888
print(i)
print(i2)
print(big_int)
print()
# 실수 출력
f = 0.99999
f2 = 3.1415925
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 9393
big_int1 = 39482034829348249823943
big_int2 = 2943809248924094893483948
f1 = 1.4242
f2 = 3.3943

# +
print(">>>>+")
print("i1 + i2 : ", i1 + i2 )
print("f1 + f2 : ", f1 + f2 )
print("big_int1 + big_int2 : ", big_int1 + big_int2 )
print()

# *
print(">>>>*")
print("i1 * i2 : ", i1 * i2 )
print("f1 * f2 : ", f1 * f2 )
print("big_int1 * big_int2 : ", big_int1 * big_int2 )
print()
# 형 변환 실습

a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(a))
print(int(d))
print(int(True)) # True : 1, False : 0
print(float(False))
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False))
print(int('3'))
print()
# 수치 연산 함수
print(abs(-7))

x, y = divmod(100, 8)
print(x,y)
print(pow(5,3), 5 ** 3)
print()
# 외부모듈
import math

print(math.pi)
