# ch16
# 코드 복제는 이제 그만! 상속으로 해결하기
import copy


class ParentClass:
    def printHello(self):
        print("Hello, world!")

class ChildClass(ParentClass):
    def someNewMehtod(self):
        print("ParentClass objects don't have this method.")

class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print('Only GrandchildClass objects have this method.')

print("Create ParentClass object and call its methods:")
parent = ParentClass()
parent.printHello()

print('Create ChildClass object and call its methods:')
child = ChildClass()
child.printHello()
child.someNewMehtod()

print('Create GrandchildClass object and call its methods:')
grandchild = GrandchildClass()
grandchild.printHello()
grandchild.someNewMehtod()
grandchild.anotherNewMethod()

print('An error:')
#parent.someNewMehtod()

# 상속은 코드 수정 시 압도적인 유리함을 가지고 있다.
# 부모 클래스는 상위 클레스 혹은 기반 클래스라고 부르고
# 자식 클래스는 하위 클래스 혹은 파생 클래스라고 한다

# 메소드 오버라이드
# 자식 클래스는 부모 클래스의 모든 메소드를 상속받음
# 하지만 자식 클래스의 자체 코드를 통해서 상속된 메소드를 오버라이드 할 수 있음

from chapter15_3 import TTTBoard
#
class MiniBoard(TTTBoard):
    def getBoardStr(self): # 오버라이딩
        """말판의 텍스트 표현을 작게 하는 문자열을 반환한다."""
        # 공백 한칸을 '.'으로 치환한다.
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                self._spaces[space] = '.'

        return f'''
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9'''

        # 공백 한칸을 BLANK으로 치환한다.
        for space in ALL_SPACES:
            if self._spaces[space] == '.':
                self._spaces[space] = BLANK

# super() 함수
# super함수는 오버라이딩시 중복되는 부분을 줄여준다.
# 해당 함수는 super()을 통해서 기존 함수를 불러올 수 있고, 혹은 함수 내부에서 함수처럼 사용할 수 있다.

class HintBoard(TTTBoard):
    def getBoardStr(self):
        """힌트가 포함된 말판을 텍스트로 표현하는 문자열을 반환한다."""
        boardStr = super().getBoardStr() # TTTBoard에 있는 getBoardStr()을 호출한다.

        xCanWin = False
        oCanWin = False
        originalSpaces = self._spaces # _spaces를 백업한다.
        for space in ALL_SPACES: # 모든 칸을 확인한다.
            # 이 칸에서 X이동을 시뮬레이션한다.
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.isWinner(X):
                xCanWin = True
            # 이 칸에서 O 이동을 시뮬레이션 한다.
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.isWinner(O):
                oCanWin = True
        if xCanWin:
            boardStr += '\nX는 한 번만 더 이동하면 승리할 수 있습니다.'
        if oCanWin:
            boardStr += '\nO는 한 번만 더 이동하면 승리할 수 있습니다.'
        self._spaces = originalSpaces
        return boardStr

import copy
ALL_SPACES = list('123456789') # 틱택토 말판 딕셔너리를 위한 키
X, O, BLANK = 'X', 'O', ' ' # 문자열 값을 위한 상수
def main():
    """틱택토 게임을 실행한다."""
    print('틱택토 게임에 오신 당신을 환영합니다')
    gameBoard = HintBoard() # TTTBoard 객체를 생성한다.
    currentPlayer, nextPlayer = X, O # X가 선공, O가 후공

    while True:
        print(gameBoard.getBoardStr()) # 화면에 말판을 표시한다.

        # 플레이어가 1-9사이의 숫자를 입력할 때까지 계속해서 요청한다.
        move = 0
        while not gameBoard.isValidSpace(move):
            print(f'{currentPlayer}의 움직임은?(1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer) #움직임을 만든다.

        # 게임이 끝났는지 확인한다.
        if gameBoard.isWinner(currentPlayer):
            print(gameBoard.getBoardStr())
            print(currentPlayer + '가 승리했습니다')
            break
        # 다음으로 무승부인지 확인한다.
        elif gameBoard.isBoardFull():
            print(gameBoard.getBoardStr())
            print('무승부 게임입니다!')
            break

        currentPlayer, nextPlayer = nextPlayer, currentPlayer # 턴을 바꾼다.
    print('즐겁게 퍼즐을 풀어주셔서 감사합니다.')

#if __name__ == '__main__':
#    main() # 임포트하지 않고, 이 모듈이 실행되면 main()을 호출한다.


# 상속 보다는 합성을 활용하자
# 합성은 상속 대신에 클래스 내부에서 클래스를 선언하는 형식으로 접근하는 것을 의미한다.

# isinstance()와 issubclass()함수
# isinstance는 is a관계인지 살펴보는 것
# A가 부모, B가 자식 클래스라면 B는 A에 포함되어 있다 -> B is a A관계

# issubclass는 클래스의 하위 객체인지 판단하는 함수이다.
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

parent = ParentClass()
child = ChildClass()
print(isinstance(parent, ParentClass)) # True 반환
print(isinstance(parent, ChildClass)) # False 반환
print(isinstance(child, ParentClass)) # True 반환 -> 부모클래스가 Parent로 상속되어서 True반환됨
print(isinstance(child, ChildClass)) # True 반환

print(isinstance(42,(int, str, bool))) # 42가 int str bool 3개중 하나인지 살펴보는 함수

print(issubclass(ChildClass, ParentClass)) # True 반환
print(issubclass(ChildClass,str)) # False 반환
print(issubclass(ChildClass,ChildClass)) # True 반환 -> 자기자신도 포함

# 클래스 메소드
class ExampleClass:
    def exampleRegularMethod(self):
        print('이것은 정규 메소드입니다.')

    @classmethod
    def exampleClassMethod(cls):
        print('이것은 클래스 메소드입니다.')

# 객체를 인스턴스화하지 않은 상태로 클래스 메소드를 호출한다.
ExampleClass.exampleClassMethod()
#ExampleClass.exampleRegularMethod() # 에러가 난다
obj = ExampleClass()

# 위에서 호출한 행과 아래 두 행은 동일하다.
obj.exampleClassMethod()
obj.__class__.exampleClassMethod()

# cls파라메터는 self와 유사하지만, self는 객체를 참조하고, cls는 파라미터 객체의 클래스를 참조한다.
# 즉 self가 있다면 한번 반드시 인스턴스화 시킨 후에 사용가능하지만, cls를 참조하는 경우 인스턴스화 시키지 않고 사용이 가능하다.

# 클래스 속성
# 클래스 속성은 객체보다는 클래스에 속하는 변수이다
# 이것을 활용하면 클래스를 사용한 횟수를 계산할 수 있다.
class CreateCounter:
    count = 0
    def __init__(self):
        CreateCounter.count += 1

a = CreateCounter() # 0로 초기화
b = CreateCounter() # 1로 초기화
c = CreateCounter() # 2로 초기화
print('생성된 객체',CreateCounter.count)

# 정적 메소드
# cls나 self에 접근할 수 없는 클래스
# 일반적인 함수와 같다
class ExampleClassWithStaticMethod:
    @staticmethod
    def sayHello():
        print("Hello")

# 클래스와 정적 객체지향 기능을 사용가능할 때

# 객체지향과 관련된 전문 용어들
# 캡슐화
# 연관된 데이터와 코드를 하나의 단위로 묶는 것
# 복잡한 구현 세붛사항을 감추는 정보 은닉 기술

# 다형성
# 어떤 타입의 객체를 다른 타입의 객체로 취급할 수 있는것을 말함
# len함수는 리스트의 길이, 딕셔너리의 길이, 문자열의 길이에 전부 사용이 가능하다.
# 이것과 같이 복수의 타입에 대한 입력에 잘 작동가능하도록 만드는 것을 의미함

# 상속을 사용하지 않아야 하는 경우
# self또는 cls 파라미터를 전혀 사용하지 않는 메소드로 구성된 경우, 메소드 대신 함수를 사용한다
# 자식 클래스가 하나 뿐인 부모 클래스를 만들었지만, 그 부모의 객체를 전혀 만들지 않은 경우 이럴때는 부모와 자식을 합쳐서 단일 클래스로 만들 수 있다.
# 3~4단계 이상의 하위 클래스를 생성한 경우 불필요하게 상속하고 있을 가능성이 높다. 하위 클래스를 통합하여 수를 줄인다.

# 다중 상속
# 여러개의 클래스를 동시에 상속받을 수 있다.
class HybridBoard(HintBoard, MiniBoard):
    pass
# 이 클래스는 힌트도 제공하면서 Board의 사이즈를 작게도 할 수 있다.
# 하지만 메소드 결정 순서때문에 신중해야 한다.
# 만약 class HybridBoard(MiniBoard, HintBoard):가 되면 오버라이딩 순서 때문에 Hint가 사라지게 된다.
# 이것은 class의 mro를 통해서 알 수 있다.
print(HybridBoard.mro())

# 클래스
# HybridBoard -> HintBoard(getBoardStr오버라이드됨,super) -> TTTBoard
# HybridBoard -> MiniBoard(getBoardStr오버라이드됨) -> TTTBoard

# C3 알고리즘에 의해 결정됨
# 파이썬은 부모 클래스에 앞서 자식 클래스를 먼저 확인한다.
# 파이썬은 class문의 왼쪽에서 오른쪽 순서로 상속된 클래스를 확인한다.
# 자세한 내용은 다루지 않음
# 프로그램의 수준의 월등히 높아지긴 하지만 상당히 헷갈리므로 사용하지 않는 편이 좋다.
