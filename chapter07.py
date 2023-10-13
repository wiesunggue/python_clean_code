# ch07
# 파이썬 세상의 프로그래밍 용어
import pandas as pd

# 1. 각종 용어의 정의
# 1) 프로그래밍 언어로서 파이썬 vs 인터프리터로서 파이썬

# 2) 가비지 컬렉션
# 메모리 누수 문제나 이중 할당 해제 버그 문제를 해결하기 위해 존재하는 것
# 메모리 할당과 해제하는 시점을 추적해 프로그래머의 부담을 덜어주는 자동화된 메모리 관리 기법
# 가비지 컬렉션은 새로운 데이터가 메모리를 사용 가능하게 만들 수 있으므로 메모리 재활용이라고도 한다.

# 3) 리터럴
# 사람이 직접 손으로 작성한 고정 값을 나타내는 소스 코드 상의 텍스트
age = 42 + len('Zophie')
# 42는 상수 리터럴, Zophie는 문자 리터럴
# age는 리터럴이 아니다.

# 4) 키워드
# 파이썬 고유 키워드가 존재한다.
# while, return, for, as, in, continue 등등이 키워드이다.

# 5) 객체, 값, 인스턴스, 아이디
# 객체는 데이터를 표현하는 것
# 모든 객체에는 값, 아이디, 데이터 타입이 존재한다.
spam = ['cat','dog','moose'] # 객체 선언하기
print(id(spam))

spam.append('snake')
print(id(spam)) # 같은 객체이므로 아이디는 변하지 않는다.

spam = [1,2,3]
print(id(spam)) # 객체가 바뀌어서 아이디가 바뀐다.

spam = {'name':'Zophie'}
print(id(spam))
eggs = spam
print(id(eggs)) # 같은 객체를 가르키므로 동일한 아이디를 가진다.
print(spam is eggs, spam==eggs)
spam['name']='A1'
print(eggs) #같은 객체를 가르키므로 eggs도 바뀐다.

# 즉, 데이터가 같은 것은 객체가 가진 '값'이 같은 것이고, 객체가 같은 것은 데이터의 아이디가 같다는 것이다.

# 6) 아이템
# 객체 안의 객체를 아이템 혹은 원소라고 부른다.

# 7) 가변 데이터 타입, 불변 데이터 타입
# 가변 데이터 타입의 종류 : 리스트, 딕셔너리, 집합, 바이트배열, 배열
# 정수, 부동소수점, 부울, 문자열, 고정집합(Frozen set), 바이트, 튜플
# 가변 객체는 업데이트가 가능하고, 불변 객체는 업데이트가 불가능
a=10
print(id(a))
a+=5
print(id(a)) # 불변 객체라서 업데이트 하면 아이디가 달라진다.

# 하지만 객체끼리 +연산을 하면 다른 객체가 생성된다.
spam = ['cat','dog']
print(id(spam))
spam.append('moose')
print(id(spam))
spam = spam + ['rat']
print(id(spam)) # 두 객체가 합쳐져서 아이디가 달라졌다.

# 8) 인덱스, 키, 해시
# 인덱스 연산자
# 파이썬은 0 기반 연산자를 활용한다.
# 음의 인덱스는 spam[-n] = spam[len(spam)-n]과 같다.
# 해시는 객체의 수명 주기동안 절대 변하지 않는 값.
# 객체의 값이 같다면 해시도 반드시 같아야 한다.
spam = {'name':'Zophie'}
# 'name'은 키이고, hash()함수는 해시 가능한 객체인 경우 해당 객체의 해시를 반환한다.
# 문자열, 정수, 부동소수, 튜플 같은 불변 객체는 해시가 가능하다.

spam[(1,2,3)]=3 # 불변 객체이기 때문에 해시 가능
print(spam)

# 해시는 아이디와 다르다. 값이 같다면 같은 해시를 가진다.

# 9) 컨테이너, 시퀀스, 매핑, 집합 타입
# 컨테이너는 여러 종류의 객체를 포함할 수 있는, 어떤 데이터 타입이든 가능한 객체
# 리스트, 딕셔너리, 집합은 컨테이너이다.

# 시퀀스는 정수 인덱스를 통해 접근 가능한, 순서 있는 값을 가진 컨테이너 데이터 타입.
# 문자열, 튜플, 리스트, 바이트 객체가 시퀀스 데이터 타입

# 매핑은 인덱스 대신 키를 사용하는 컨테이너 데이터 타입의 객체
# 매핑은 정렬 여부는 상관 없음

# 10) 이중밑줄 메소드, 매직 메소드
# 17장에서 설명

# 11) 모듈, 패키지
# 모듈은 import spam으로 사용할 수 있는 것
# 패키지는 __init__.py라는 이름의 파일을 폴더 안에 넣어서 생성하는 모듈들의 집합

# 12) 호출가능 객체, 일급 객체
# 함수에서 호출 연산으로 ()라는 연산이 존재한다.
# 함수는 일급 객체로 분류된다.
# 일급 객체는 인수 전달, 호출 결과 반환 등 객체로 가능한 모든 연산을 할 수 있다.
# 함수는 객체이므로 별칭을 가질 수 있다.
def spam():
    print('spam!!')
eggs = spam
eggs() # spam을 호출한다.

# 일급 함수는 함수의 인수로 함수를 받는다.
def callTwice(func):
    func()
    func()
callTwice(spam)

# 2. 흔히 혼동되어 사용되는 용어

# 1) 문(statement) vs 표현식(expression)

# 표현식은 단일 값으로 평가되는 값과 연산자로 이루어진 명령어
# 값은 함수 호출, 변수 값 두가지가 있다.
# 2+2, len(myName) > 4 와 같은 것들이 표현식이다

# 문은 값으로 표현되지 않는 모든 명령
# if 문 for 문 def 문 return 문 등등이 존재

# 2) 블록, 절, 바디

# 블록은 들여쓰기로 시작하여 해당 들여쓰기 수준이 이전 들여쓰기 수준으로 돌아오면 종료
# if, else, for, while, def, class와 같은 것들 뒤에 오는 것이 블록이다.
# :를 통해서 한줄 블록을 구성할 수 있다.

# 절은 블록+헤더
# 블록 부분은 바디라고도 한다.

# 3) 변수 vs 속성
# 변수는 객체의 이름을 표현한다.
# 속성은 '점 다음에 나오는 모든 이름'
import datetime
spam = datetime.datetime.now() # spam은 객체
print(spam.year) # spam의 속성
print(spam.month) # spam의 속성

# 4) 함수 vs 메소드
# 함수는 자신이 호출될 때 실행되는 코드의 모음
# 메소드는 클래스와 연관된 일종의 함수
len('Hello') # 함수
'Hello'.upper() # string 클래스의 함수 -> 메소드

# 5) 반복가능 객체 vs 반복자
# 반복 가능 객체는 for 루프문에서 사용 가능한 객체
# 범위, 리스트, 튜플, 문자열과 같은 모든 시퀀스 유형이 가능하고
# 객체와 딕셔너리 집합, 파일 객체 같은 일부 컨테이너 객체가 포함됨
# for문의 동작 방식은 iter()과 next()를 이용해서 동작함
iterableObj = range(3)
print(iterableObj)
iterableObj = iter(iterableObj)
i = next(iterableObj)
print(i)

i = next(iterableObj)
print(i)

i = next(iterableObj)
print(i)

#i = next(iterableObj) # 해당 부분에서 StopIteration 에러가 난다. -> for문은 에러를 만날 때 까지 실행하고 정지

# 반복자는 반복가능 객체에서 아이템을 한 차례만 반복할 수 있다.
# 이미 읽은 내용을 다시 읽을 수는 없다.
# 다시 읽기 위해서는 iter()를 다시 호출하여 읽어야 한다.

iterableObj = list('cat')
iterableObj1 = iter(iterableObj)
iterableObj2 = iter(iterableObj) # 여러 가지의 iter 객체

print(next(iterableObj1))
print(next(iterableObj1))
print(next(iterableObj2))

# 반복 가능 객체는 iter 함수에 인수로 전달되는 반면 iter 호출에서 반환되는 객체는 반복자 객체이다.
# iterableObj = 반복 가능 객체
# iterableObj1, iterableObj2 = 반복자 객체

# 6) 구문 에러 vs 런타임 에러 vs 의미 에러

# 구문 에러는 유효한 명령어에 대한 규칙 집합.
# 괄호 누락, 쉼표 대신 마침표 표시 등등이 나타나면 즉시 SyntaxError를 생성

# 런타임 에러는 실행 중인 프로그램에 존재하지 않는 파일을 열려고 하거나 숫자를 0으로 나누는 것과 같은 몇가지 작업을 수행하지 못하는 경우 발생
# 런타임 에러는 프로그램이 실행되기 전에 찾아낼 수 없다.

# 의미 에러는 에러 메시지를 발생하지는 않지만 프로그래머가 의도하지 않은 방식으로 코드를 수행하는 것

# 7) 파라미터 vs 인수

# 파라메터는 함수에서 괄호 사이의 변수 이름
# 인수는 함수 호출에서 전달된 값으로 파라메터에 지정되는 값
def  greeting(name, species):
    print(name + 'is a' + species)
greeting('Zophie','cat')
# 여기서 파라메터는 name, species가 있고
# 인수는 'Zophie', 'cat'이다

# 8) 타입 강제변환 vs 타입 캐스팅

# 타입 캐스팅은 명시적으로 지정한 타입으로 변환 되는 것
int('42') # 타입 캐스팅

# 타입 강제 변환은 묵시적으로 타입이 변환되는 것
3+4.0 # 타입 강제 변환
True+False+True # 타입 강제 변환

# 9) 프로퍼티 vs 속성


# 10) 바이트코드 vs 기계어 코드
# 11) 스크립트 vs 프로그램, 스크립트 언어 vs 프로그래밍 언어
# 12) 라이브러리 vs 프레임워크 vs SDK vs 엔진 vs API

import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy
import scipy.stats
size=10000
arr=[0]*size
print(np.random.standard_normal()*np.random.random()) # 베이지안 난수 모수=평균
for i in range(size):
    arr[i]=np.random.standard_normal()*np.random.random()
data = arr
dist_names = ["norm", "gamma", "beta", "expon", "t", "chi2"]
dist_results = []
params = {}
for dist_name in dist_names:
    dist = getattr(scipy.stats, dist_name)  # 분포의 특징을 가져와서
    param = dist.fit(data)  # 관측값을 이용하여 가정한 분포의 모수를 추정
    params[dist_name] = param  # 추정한 모수를 Dictionary에 넣고
    Stat, p = stats.kstest(data, dist_name, param)  # Kolmogorov-Smirnov 검정을 합니다.
    dist_results.append((dist_name, p))  # 결과를 list에 넣고요,

print(dist_results)  # 각 분포의 p value를 한 번 보고요.
best_dist, best_p = (max(dist_results, key=lambda item: item[1]))  # 그중에 제일 p값이 큰 것을 찾고요
print("제일 비슷한 분포: %s" % (best_dist))
print("그 분포의 p_value: %f" % (best_p))

arr.sort()
plt.hist(arr,bins=50)
plt.show()

data2 = [0]*size
for i in range(size):
    m = np.random.beta(1,1)
    data2[i] = np.random.binomial(n=10, p=m)
data2 = pd.DataFrame(data2)
print(data2.describe())
plt.hist(data2,bins=50)
plt.show()

# E(x) = (x+1)/(10+1+1)