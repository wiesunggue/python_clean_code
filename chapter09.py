# ch09
# 파이썬의 기이한 특징들

# 1. 256 is 256은 참이지만 257 is 257은 참이 아닌 이유
# 파이썬은 실행할 때 자주 사용하는 -5에서 256까지 정수 객체를 미리 생성한다.
# 이런 정수를 미리 할당된 정수라고 부른다.
# 또, 미리 할당된 정수 객체는 선언하지 않고, 불러 오는 식으로 동작하기 때문에 시간과 메모리를 절약할 수 있다.

print(256 is 256)
print(1234 is 1234)
# 해당 문제는 수정된 듯?? -> 3.10에서는 정상 동작한다.

# 2. 문자열 인터닝
# 최적화의 일종으로 같은 문자가 있다면 객체를 재사용한다.
# 하지만 이에 의존하면 안된다. 다른 연산이 껴있는 경우 id가 달라진다
spam = 'cat'
eggs = 'cat'
print(spam is eggs)
print(id(spam), id(eggs))

# 3. 파이썬의 가짜 증감 연산자
spam = 42
sapm = --spam # 이는 증감 연산자가 아니라 음수를 2번 표기한 것으로 해석된다.
print(spam)

# 4. 아무것도 없으면 참인 all()
# all()은 리스트 등의 수열값이 모두 참이면 True를 반환하는 함수
# 하나만이라도 거짓이라면 False를 반환

print(all([]))
spam = []
print(all([i>42 for i in spam]))
print(all([i<42 for i in spam]))
print(all([i==42 for i in spam]))
# 정확히는 all은 거짓이 존재하지 않으면 참을 반환한다.

# 5. 부울값은 정수값이다.
# 부울값은 정수 0, 1과 같다
True == 1
False == 0

# bool은 정수 클래스의 하위 클래스로 bool형이라고도 할 수 있지만 int형이기도 하다

# 6. 다중 연산자 연달아 쓰기
print('6th ',False == False in [False]) # 출력하면 True가 나온다.
# 1==0==1 => 1==0 and 0==1 로 해석되는 원리
# 풀어쓰면 다음과 같다
(False == False) and (False in [False])
(True) and (False in [False])
(True) and (True)
True

# 흔한 예시
spam = 55
42 < spam < 99
(42 < spam) and (spam < 99)


# 7. 파이썬의 antigravity 기능
# import antigravity

# 해당 코드에서는 윈도우 기본 브라우저로 web페이지를 열어준다
# 이는 webbrowser의 기능이다.

import webbrowser
webbrowser.open('https://xkcd.com/353/')
# import antigravity와 같은 역할을 한다.
