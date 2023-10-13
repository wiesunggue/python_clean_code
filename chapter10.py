# ch10
# 파이썬 다운 함수 만들기

# 1. 함수명
# 일반적인 식별자의 규칙을 따라야 한다.
# 내장 함수를 함수명으로 선언하면 안된다.
# 실용적인 이름을 선언해야 한다.

# 2. 함수 크기의 트레이드오프
# 함수의 길이가 길어지면 이해하기 어려워지고, 함수의 길이가 짧아지면 이해하기 쉬워진다.

# 짧은 길이 함수의 장점
# 1) 함수 코드를 이해하기가 더 쉽다
# 2) 필요한 파라미터가 더 적다
# 3) 230페이지의 함수형 프로그래밍 절에서 설명한 내용처럼 부수 효과를 일으킬 가능성이 적다.
# 4) 테스트와 디버그가 더 쉽다
# 5) 예외가 더 적게 발생한다

# 짧은 길이 함수의 단점
# 1) 함수를 짧게 작성하면 프로그램에서 필요한 함수 개수가 늘어나기 쉽다
# 2) 함수가 더 많다는 것은 프로그램이 더 복잡해짐을 의미한다
# 3) 각 함수별로 설명적이면서 정확한 이름을 붙여야 하는데, 함수 개수가 늘어나면 이것이 쉽지 않다
# 4) 함수를 많이 사용할수록 작성할 문서도 많아진다
# 5) 함수 간의 관계가 더욱 복잡해진다

# 저자가 주장하는 이상적인 함수의 길이는 30행 이하여야 하며 결코 200줄을 넘기면 안된다.

# 3. 함수 파라미터와 인수
# 함수의 인수가 5~6개라면 너무 많다.
# 함수를 쪼개서 인수를 3개 이하로 줄여야 한다.

# 1) 기본 인수
# 복잡도를 줄이기 위해서 default argument를 이용하자
# default argument로 가변 객체를 이용하면 안된다.
# *와 **를 사용해 함수에 인수 전달하기
# *를 이용하면 반복가능 객체의 아이템을 전달할 수 있다.
# **를 이용하면 키-값의 쌍을 인수로 전달할 수 있다.

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

# min 처럼 min([1,2,3,4]), min(1,2) 둘다 받는 함수 만들기
def myMinFunction(*args):
    print('start function',args,len(args))
    if len(args) == 1: # 하나의 튜플 입력을 받는 경우(하나의 변수로 입력을 받음)
        values = args[0]
    else: # 복수의 입력을 받는 경우(입력은 튜플로 변환되어 받아짐)
        values = args

    if len(args) == 0:
        raise ValueError('myMinFunction() args is an empty sequence')

    for i, value in enumerate(values):
        if i==0 or value < smallestValue:
            smallestValue = value

    return smallestValue

print(myMinFunction(1,2,3))
print(myMinFunction([1,2,3]))
print(myMinFunction([1]))

# **를 사용해 가변인수 함수 만들기
def forMolecules(**kwargs):
    if len(kwargs) == 2 and kwargs['hydrogen'] == 2 and kwargs['oxygen'] == 1:
        return 'water'

# *와 **로 래퍼 함수 만들기
# 래퍼는 함수의 인수를 다른 함수로 전달하고, 함수의 반환값을 전달하는 함수
def printLower(*args, **kwargs):
    args = list(args)
    for i, value in enumerate(args):
        args[i] = str(value).lower()
    return print(*args, **kwargs)

printLower('123','455',sep=', ')
# args로 ('123', '455')가 들어가고, kwargs로 {'sep'=', '}가 들어간다.

# 4. 함수형 프로그래밍
# 함수형 프로그래밍은 전역 변수나 어떠한 외부 상태도 수정하지 않고, 계산 수행 목적의 함수 작성을 강조하는 프로그래밍 패러다임

# 1) 부수 효과
# 부수효과는 함수 바깥에 존재하는 프로그램의 각 부분에 가하는 모든 변화를 말한다.

# 부수효과가 없는 함수
def substract(number1, number2):
    return number1 - number2

TOTAL = 0
def addToTotal(amount):
    global TOTAL
    TOTAL += amount
    return TOTAL

def removeLastCatFromList(petSpecies):
    if len(petSpecies) > 0 and petSpecies[-1] =='cat':
        petSpecies.pop()

myPets = ['dog','cat','bird','cat']
removeLastCatFromList(myPets)
print(myPets)

# 결정론적 함수(deterministic function)
# 같은 인풋을 받으면 항상 같은 결과를 반환하는 함수

# 비결정론적 함수(nondeterministic function)
# 같은 인풋을 받아도 다른 결과를 반환하는 함수

# 2) 고차원적 함수
# 함수를 인수로 받는 함수

# 3) 람다 함수
# pass

# 4) 리스트 컴프리헨션을 이용한 매핑과 필터링
# map() 함수와 filter()함수

# 리스트의 원소에 특정 연산하기
mapObj = map(lambda n : str(n), [8, 16, 18, 19, 12, 1, 6, 7])
print(list(mapObj))

# 리스트에서 포함-제외 판별하기
filterObj = filter(lambda n: n%2==0, [8, 16, 18, 19, 12, 1, 6, 7])
print(list(filterObj))

# 5. 결과값은 항상 동일한 데이터 타입이어야 한다.
# 되도록 노력하자
# 또한, 함수의 반환값으로 None을 반환하지 않도록 해야한다.
# None 타입이 오류 역추적의 많은 위험을 수반한다.
# 대신, 직접 에러의 원인을 알려줄 수 있도록 raise를 이용하자

# 6. 예외 발생시키기 vs 에러 코드 반환하기
# index는 에러 코드를 내지만 find는 없을 경우 예외로 -1을 반환한다.
# (둘 다 반환 타입은 항상 같다)

def ch11():
    r"""Sends a GET request. Returns :class:'Response' object
    :param url : URL for the new : class :'Request' object"""
    pass