# ch08
# 파이썬에서 빠지기 쉬운 함정들

# 1. 루프문 진행 중에는 리스트에서 아이템을 추가/삭제하지 말자
# 루프문 내에서의 변형은 많은 버그 가능성을 내포한다.

# 메모리 사용과 리스트 -> 새로운 리스트의 형성은 참조하는데 있다.
# 리스트를 수정해야 한다면 가장 마지막 부터 시작하는 것도 하나의 방법이다
# 나쁜 예시(에러)
someInts = [1,7,4,5]
'''
for i in range(len(someInts)):
    if someInts[i]%2==0:
        del someInts[i]
'''
# 좋은 예시
for i in range(len(someInts)-1,-1,-1):
    if someInts[i]%2==0:
        del someInts[i]

# 새 값을 추가할 때도 이는 좋은 방법이다.

# 2. copy.copy()나 copy.deepcopy()없이 가변 값을 복사하지 말자
# 변수는 객체를 참조하는 레이블 또는 이름 태그로 생각하는 편이 좋다.
# 즉, 복사를 하게 되면 주소만 복사하는 것이기 때문에 하나의 값을 변경하면 다른 값도 바뀌게 된다.
# 이를 방지하기 위해 copy를 사용해야 한다.

# 3. 기본 인수에 가변 객체는 사용하지 말자
# 함수의 인수로 가변 객체를 넣어준다면 가변 객체는 같은 주소에 대해서 재사용 하는 것 이기 때문에 반복 사용 시 문제가 발생한다.

def func(x,arr=[3,5]):
    arr.append(x)
    print(arr)

func(1)
func(2) # 반복 사용 시 arr이 [3,5,1]이 저장되어 있다.


# 4. 문자열을 문자열 연결로 생성하지 말자
# 문자열은 불변 객체이다.
# 문자열 수정은 새 객체를 생성하는 것
spam = 'Hello'
spam = spam + ' World!' # 이러지 말자

# 이는 f-string, format, 문자열 메소드 또는 %s 형식지정자 모두 마찬가지이다.
spam = ''
# 나쁜 방식
for i in range(100):
    spam += 'spam '

# 좋은 방식
arr = []
for i in range(100):
    arr.append('spam ')
finalString = ''.join(arr)
# 아래 방식으로 생성한 문자열이 훨씬 더 빠르다

print(spam)
print(finalString)

# 5. sort가 알파벳 순으로 정렬하리라 기대하지는 말자
# 소문자와 대문자가 섞인 경우에는 대문자 -> 소문자 순으로 정렬된다.(정확히는 아스키 코드순으로 정렬)
# 참고로 파이썬의 정렬은 Timsort로 병합 정렬과 삽입 정렬의 혼합 버전이다.

# 6. 부동 소수가 완벽히 정확할 거라고 가정하지 말자.
print(0.1+0.1+0.1)
print(0.3 == 0.1+0.1+0.1)
# float에서 2**53을 넘어가는 숫자는 표현할 수 없다
print('2**53 넘어가는 수',float(2**53) == float(2**53))
print(float(2**53+1))
print(float(2**53))

# 필요하다면 Decimal을 이용하라 부동 소수의 부정확함 없이 사용 가능하다.

# 6. 부등 연산자 != 를 연달아 쓰지 말자

# 7. 단일 아이템 튜플에서는 쉼표를 잊지 말자
spam = ('cat') # 문자열
spam2 = ('cat',) # 튜플

print(spam[0],spam2[0])
