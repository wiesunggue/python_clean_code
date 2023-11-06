# ch15
# 틱택토 게임으로 배우는 객체지향 프로그래밍과 클래스

# 관례적으로 모듈 이름은 소문자로 시작하고, 클래스 이름은 대문자로 시작한다.

# 객체 생성하기 예제
import datetime
birthday = datetime.date(1998,3,11) # 연월일을 전달
print(birthday)
print(birthday.year)
print(birthday.weekday()) # 이것은 메소드이다 # 요일을 계산하여 출력한다.

# WizCoin이라는 간단한 클래스 생성하기

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """galleons, sickless, knuts로 새로운 WizCoin 객체를 생성한다."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # 참고 __init__() 메소드에는 return문이 존재해서는 안된다.

    def value(self):
        """이 WizCoin 객체에 포함된 모든 동전의 가치(크넛 단위)"""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """그램 단위로 동전의 무게를 반환한다."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

purse = WizCoin(2,5,99)
print(purse)
print('G:',purse.galleons,'S:',purse.sickles,'K:',purse.knuts)
print('total value:', purse.value())
print('Weight:',purse.weightInGrams())

# 속성(attribute)
# 속성은 .뒤에 오는 모든 이름이라고 정의한다.
# ex) birthday.year, purse.sickles와 같은 것을 속성이라고 함

# 프라이빗 속성과 프라이빗 메소드
# 모든 속성과 메소드는 퍼블릭 접근을 허용함
# 하지만 비공개 접근을 위해서는 _로 이루어진 이름을 활용해야 한다.


# private 예제
class BankAccount:
    def __init__(self, accountHolder):
        # self._balance에 BankAccount 메소드는 접근할 수 있지만
        # 이 클래스 외부의 코드는 접근하면 안된다.
        self._balance = 0
        self._name = accountHolder

        with open(self._name+"Ledger.txt",'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self,amount):
        if amount <= 0:
            return # 음수 잔고를 허용하지 않는다
        self._balance += amount
        with open(self._name+'Ledger.txt','a') as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return # 잔고가 충분하지 않거나 인출 금액이 음수다
        self._balance -= amount
        with open(self._name + 'Ledger.txt','a') as ledgerFile:
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

acct = BankAccount('Alice')
acct.deposit(120)
acct.withdraw(40)

# BankAccount 외부에서 _name이나 _balance를 변경하는 것은 관례에서 벗어나지만 허용된다.
acct._balance = 1e10
acct.withdraw(1000)

acct._name = 'Bob'
acct.withdraw(1000)

# type() 함수와 __qualname__ 속성
# 파이썬은 타입과 데이터 타입과 클래스의 의미가 모두 같다.

print(type(42)) # 객체 42는 int 타입이다
print(int)  # int는 정수 데이터 타입을 위한 객체이다
print(type(42) == int) # 42가 int인지 type로 확인한다.

print(type('Hello') == int)
print(type(42))
print(type(42).__qualname__) # 더 깔끔한 문자열을 반환한다.
# __qualname__ 속성은 좀 더 깔끔한 문자열을 반환한다.

# 객체지향 vs 비 객체지향 방식의 프로그램 비교: 틱택토 게임
