# ch06
# 파이썬다운 코드를 작성하는 법

# 1. 파이썬의 선
# 파이썬 언어의 설계와 파이썬 프로그램을 위한 20가지 지침 모음

import this
# 해당 코드를 실행하면 20가지 지침이 출력된다.

# 2. 의미 있는 들여쓰기

# 3. 흔히 잘못 사용되는 구문
# 1) range() 보다는 enumerate()를 사용하자
animals = ['cat', 'dog','pig']
for i, animal in enumerate(animals):
    pass

# 2) open() close() 문보다는 with 문을 사용하자
# open() close()를 이용하면 try, except과정에서 파일이 계속 열린 상태가 되어 에러가 발생할 수 있다.
with open('spam.txt', 'w') as fileObj:
    fileObj.write('Hello World!')

# 3) == 대신 is를 써서 None과 비교하자
# ==는 두 객체의 값을 비교하지만 is는 두 객체의 아이디를 비교한다.
# 따라서 None비교는 is로 해야하고 bool값은 ==연산자를 써야 한다.

class SomeClass:
    def __eq__(self, other):
        if other is None:
            return True

spam = SomeClass()

print(spam==None)
print(spam is None)

# 4. 문자열 포메팅
# 문자열에 백슬래시가 많은 경우에는 원시 문자열을 사용하자
# 이스케이프 문자를 활용해서 문자열 리터러렝 포함되지 않는 텍스트를 삽입 할 수 있다.
# 이스케이프 문자를 많이 사용하는 대신 원시 문자열을 사용하자
bad_string = 'E:\\python_study\\python_clean_code\\chapter06.py'
good_string = r'E:\python_study\python_clean_code\chapter06.py' # 백슬래시가 중요한 상황에 사용할 수 있음
print(bad_string)
print(good_string)

# 5. f-문자열을 사용한 문자열 포메팅
# 문자열 포메팅은 총 4가지 방식이 존재한다
# .format을 활용한 방식, + 를 통한 방식, %를 활용한 방식, f-문자열 방식
# 파이썬 3.6 버전 이상에서 사용한다면 여기서 가장 가독성이 좋은 f-문자열 방식을 이용하자(그 전 버전도 이용하려면 format이나 %를 사용하자)

# 6. 리스트의 얕은 사본 만들기
# 복사를 위해서 [:] 대신 copy를 사용하자
import copy
spam = ['cat','dog','rat','eel']
eggs = copy.copy(spam)
print(spam is eggs) # 얕은 복사는 아이디가 다르다
eggs[1]='turkey'
print(spam) # 아이디가 달라서 turkey가 들어가지 않는다.
print(eggs)

# 7. 파이썬다운 딕셔너리 사용법
# 1) 딕셔너리에서 get()과 setdefault()를 이용하자
# get은 저장된게 없으면 defualt값 반환(딕셔너리에 저장을 하지는 않음), setdefault는 딕셔너리에 저장된 값이 없으면 default값 저장
numberOfPets = {'dogs':2}
print('I have',numberOfPets.get('cats',0), 'cats.')

numberOfPets = {'dogs':2}
numberOfPets.setdefault('cats', 0) # cats가 존재할 경우 아무것도 하지 않는다
numberOfPets['cats'] += 10
print(numberOfPets)

# 2) 기본값을 위해 collections.defaultdict를 사용하자
import collections
scores = collections.defaultdict(int) # 0을 기본 값으로 가진다
print(scores)
scores['A1']+=1
print(scores)
print(scores['Zophie'])
print(scores)

# 기본값으로 int형 대신 list를 이용할 수도 있다.
booksReadBy = collections.defaultdict(list)
booksReadBy['A1'].append('abc')
print(booksReadBy)

# 3) switch문 대신 딕셔너리를 사용하자
season = 'Winter'
if season == 'Winter':
    holiday = 'New Year\'s day'
elif season == 'Spring':
    holiday = 'May Day'
elif season == 'Summer':
    holiday = 'Juneteenth'
elif season == 'Fall':
    holiday = 'Halloween'
else:
    holiday = 'Personal day off'

# 해당 방식 대신 딕셔너리를 이용하여 깔끔하게 표현 가능하다.
holiday = {'Winter': 'New Year\'s Day',
           'Spring': 'May Day',
           'Summer': 'Juneteenth',
           'Fall': 'Halloween',
           }.get(season, 'Personal day off')


# 8. 조건식: 파이썬의 '보기 흉한' 3항 연산자
# 보기 흉하더라도 실횽적인 활용성 때문에 3항 연산자가 도입되었다.
# 3항 연산자를 중첩해서 사용하면 안된다.
# 되도록 3항 연산자 사용하는 대신, 조건문을 이용하자

# 9. 변수값 잡업
# 1) 체이닝 할당과 비교 연산자
spam = 50
if 42 < spam < 99: # 체이닝 할당 예제1
    pass

spam = eggs = bacon = 'string' # 체이닝 할당 예제2

# 2) 변수가 여러 값 중 하나인지 여부를 확인하자
spam = 'cat'
spam == 'cat' or spam == 'dog' or spam == 'moose' # 잘못된 예
spam in ('cat','dog','moose') # 파이썬 다운 예
# 심지어 아래 코드가 더 빠르다
