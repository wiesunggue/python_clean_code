# ch17
# 파이썬다운 객체지향 프로그래밍

# 프로퍼티
# 기본적으로 파이썬에는 프라이빗 속성을 가지지 않는다.
# 이 때문에 비공개 속성은 _func, _var을 활용하지만 실제로는 접근할 수 있다.

# 하지만 프로퍼티를 활용하면 공식적으로 프라이빗 속성을 선언할 수 있다.
# 프로퍼티는 속성을 읽고, 바꾸고 삭제하는 방법을 조절할 수 있도록 개발된 것
# getter, setter, deleter 메소드를 가진 속성이다.

# 속성으로 프로퍼티 바꾸기
class ClassWithRegularAttributes:
    def __init__(self, someParemeter):
        self.someAttribute = someParemeter

obj = ClassWithRegularAttributes('some initial value')
print(obj.someAttribute)

obj.someAttribute = 'changed value'
print(obj.someAttribute)
del obj.someAttribute
# print(obj.someAttribute) 에러 발생 -> 접근 불가능

class ClassWithProperties:
    def __init__(self):
        self.someAttribute = 'some initial value'

    @property
    def someAttribute(self): # 이것은 getter 메소드다
        return self._someAttribute

    @someAttribute.setter
    def someAttribute(self,value): # 이것은 setter 메소드다
        self._someAttribute = value

    @someAttribute.deleter
    def someAttribute(self): # 이것은 deleter 메소드다
        del self._someAttribute

obj = ClassWithProperties()
print(obj.someAttribute)
obj.someAttribute = 'changed value'
print(obj.someAttribute)
del obj.someAttribute
# 위 코드는 기존 동작과 완전히 같다
# 하지만 해당 코드에서는 someAttribute에 접근할 수 없다.
# 외부의 접근은 _someAttribute로만 가능하다.
# 이런 특성 때문에 _someAttribute 속성은 지원 필드, 지원 변수라고 부른다.

# 데이터 검증을 위한 setter 사용
# 프로퍼티의 가장 일반적인 사용은 데이터의 유효성을 검증하는 것이다.

class WizCoinException(Exception):
    """wizcoin 모듈이 잘못 사용될 경우 이 예외를 발생시킨다."""
    pass

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """새로운 WizCoin 객체를 galleons, sickles, knuts로 생성한다."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # 주의: __init__() 메소드에는 절대 반환문이 없다.


    @property
    def galleons(self):
        """이 객체의 galleon 동전 숫자를 반환한다."""
        return self._galleons

    @galleons.setter
    def galleons(self,value):
        if not isinstance(value, int):
            raise WizCoinException('galleons attr must be set to an int, not a'+value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('galleons attr must be a positive int, not' + value.__class__.__qualname__) # 변슈.__class__.__qualname__은 변수의 타입을 가지고 있다.
        self._galleons = value

    @property
    def total(self):
        """이 WizCoin 객체에 속한 모든 동전의 가치 총합"""
        return (self.galleons * 17 * 29)+(self.sickles*29)+(self.knuts)

    # total에 setter와 deleter 메소드가 없음에 주목하자

# 읽기 전용 프로퍼티
# total 메소드

purse = WizCoin(2,5,10)
print(purse.total) # 읽기만 가능하여 purse.total=1000와 같은 대입 연산이 불가능하다.


# 프로퍼티를 사용하면 좋은 경우
# 1~2초 이상 걸리는 느린 작업, 예를 들어 파일을 다운로드 하거나 업로드 하는 경우
# 부수효과가 발생하는 작업, 이를테면 다른 속성이나 객체에 대한 변경이 발생하는 경우
# get 또는 set 작업에 추가 인수를 전달할 필요가 있는 작업

# 이중 밑줄 메소드

# __str__과 __repr__ 메소드
# __str__은 주로 사용자에게 제공할 정보를 위해서 사용
# __repr__은 주로 log파일과 같이 기술적인 맥락에서 사용
# repr문자에 의료정보, 개인정보 식별정보와 같은 민감한 정보가 포함된 경우에는 보안 문제가 발생할 여지가 존재함
class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'{self.__class__.__qualname__}({self.x}, {self.y})'

    def __str__(self):
        return f'self.x: {self.x}, self.y: {self.y}'

    def __add__(self,others):
        '''이러면 안된다'''
        if not isinstance(others, A):
            return NotImplemented
        self.x += others.x
        self.y += others.y
        return self # 앞의 a를 변경한다

    def __add__(self,others):
        if not isinstance(others, A):
            return NotImplemented

        return A(self.x+others.x,self.y+others.y) # 앞의 a를 변경하지 않고 새 클래스를 생성한다

    def __mul__(self,others):
        if not isinstance(others,int):
            return NotImplemented
        return A(self.x*others,self.y*others)

    def __rmul__(self,others):
        return self.__mul__(others)

a = A(1,'3')
print(a.__repr__())
print(a.__str__())

# 숫자 이중 밑줄 메소드
# +, *, -, /와 같은 연산을 가능하도록 한다.
print(a+a)

# 거울 숫자 이중밑줄 메소드
# a*10은 가능하지만 10*a는 불가능하다
# 이것을 해결하기 위해서 __rmul__을 이용한다
# rmul, radd, rsub, rmatmul, rtruediv 등등을 정의할 수 있다.
print(a*10)
print(10*a) # 거울 숫자 이중밑줄 메소드

# 제자리 바꿔치기 이중밑줄 메소드
# iadd, imul 등등이 있다
# +=, *= 와 같은 연산이 있음

# 비교 연산
# eq, gt, ge, lt, le
# ==, >, >=, <, <= 같은게 있음
