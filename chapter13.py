# ch13
# 빅오를 활용한 알고리즘 성능 분석과 개선

# 프로그램의 속도 측정하기 timeit과 cProfile 모듈
# 둘다 설치없이 사용가능

import timeit
# timeit은 평균적인 실행시간을 계산해준다.

a, b = 42, 101
print(a,b)

# a, b = b, a와 같은 동작
# 둘 중 무엇이 더 빠를까?
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

cal_time1 = timeit.timeit('a, b = 42, 101; a = a ^ b; b = a ^ b; a = a ^ b') # 이 방법이 제일 느리다.
cal_time2 = timeit.timeit('a, b = 42, 101; temp = a; a = b; b = temp')
cal_time3 = timeit.timeit('a, b = 42, 101; a, b = b, a')
# 실행시간 time1 = 0.13, time2 = 0.029, time3 = 0.032
print(cal_time1,cal_time2,cal_time3)

# 난수 1천만개를 추출하는데 5초 정도가 걸린다.
rand = timeit.timeit('random.randint(1,100)','import random',number=10000000)
print(rand)

# timeit을 활용한 변수는 다른 변수와 함수에 접근할 수 없다.
# globals 인스를 활용하면 해당 문제를 해결할 수 있다.
spam = 'hello'
try:
    timeit.timeit('print(spam)')
except:
    print('fail')

print(timeit.timeit('print(spam)',number = 1,globals = globals()))

# timeit은 작은 코드 조각에 대해서 유용하지만 cProfile은 전체 함수나 프로그램을 분석하는 용도로 유용하다.

import time, cProfile

def addUpNumbers():
    total = 0
    for i in range(1,100001):
        total += i

cProfile.run('addUpNumbers()')
# ncalls : 이 함수가 실행된 횟수
# tottime : 이 함수에서 호출한 다른 함수들의 시간을 제외하고 이 함수 자체에서 소비된 총 시간
# percall : 총 호출 시간을 누적 호출 횟수로 나눈 값
# cumtime : 이 함수와 이 함수가 호출한 모든 다른 함수들에 소비된 누적 시간
# percall : 누적 시간을 호출 횟수로 나눈 값
# filename:lineno : 함수가 들어 있는 파일과 행 번호

# 해당 파일은 다운받아야 사용할 수 있다.
# https://nostarch.com/download/CrackingCodesFiles.zip 여기서 다운받도록 하자
import CrackingCodesFiles.rsaCipher as rsaCipher
#rsaCipher.encryptAndWriteToFile('encrypted_file.txt', 'CrackingCodesFiles//al_sweigart_pubkey.txt','abc'*100000)
cProfile.run("rsaCipher.encryptAndWriteToFile('encrypted_file.txt', 'CrackingCodesFiles//al_sweigart_pubkey.txt','abc'*100000)")
# 해당 연산은 대부분 pow연산을 하는데 시간을 소모하고 있다는 것을 알 수 있음
# 이미 최적화된 코드라서 개선은 힘들지만, pow연산이 병목을 발생시킨다는 통찰은 얻을 수 있음.

# 빅-오 알고리즘 분석
# 빅오는 초나 CPU 사이클과 같은 단위를 사용하지 않음 -> 실행환경마다 차이가 존재하기 때문

# 빅 오메가 표기법 -> 최선의 경우
# 빅 세타 표기법 -> 최선과 최악의 차수가 동일한 경우 사용
