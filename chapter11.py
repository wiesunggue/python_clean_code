# ch11
# 주석과 타입 힌트

# 독스트링 : 함수, 메소드, 모듈에 대한 파이썬 문서 형식
# 타입 힌트 : 파이썬 소스코드에 추가할 수 있는 지시자

# 1. 주석 #을 이용한 주석과 """"""를 이용한 주석 2가지가 있다
# 여러 행을 걸쳐서 주석을 입력해야 하는 경우 """"""을 이용해라
def someCode():
    pass

# 아래 줄 코드에 대한 주석부는 여기에 넣는다.
someCode()

# 1) 주석 스타일
# 이 부분을 여러 개의 단일 행 주석을
# 기호를 이용해 연속으로 배치해 여러 행에 길게 걸치게 만든 블록 주석이다.
# 이런 형태를 블록 주석이라 부른다.

if True:
    # 다른 코드에 대한 주석부는 여기에 넣는다.
    someCode() # 이 형태는 인라인 주석이다.

# 2) 인라인 주석
while True: # 인라인 주석
    break

a = 5 # 인라인 주석

# 3) 설명 주석
currentWeekWages = 100

# 나쁜 설명
currentWeekWages *= 1.5 # 현재 주급의 1.5배

# 올바른 설명
currentWeekWages *= 1.5 # 초과 근무 반영

# 4) 요약 주석
# 한줄한줄 설명하는 것 보다 요약해서 설명하는게 좋은 경우도 있음
PLAYER_X=1
PLAYER_O=0
playerTurn = 1

# 다른 플레이어에게 차례를 넘김
if playerTurn == PLAYER_X:
    playerTurn = PLAYER_O
elif playerTurn == PLAYER_O:
    playerTurn = PLAYER_X

# 5) 경험 지식을 담은 주석
# 경험적인 설명이라고 해서 적는걸 두려워 하지 마라
# 유지보수 하는 입장에서는 아주 중요하다

# 6) 법무 정보를 담은 주석
# 일부 소프트웨어 회사나 오픈 소스 프로젝트는 법적인 이유로 각 소스 코드 파일 상단의 주석에 판권, 소프트웨어 라이선스, 저작권 정보를 넣어야 한다는 정책이 있다.
"""Cat Herder 3.0 Copyright (C) 2021 AI Sweigart. All rights reserved. See license.txt for the full txt"""
# 이런 식으로 적어야 한다.

# 7) 전문적인 주석
# 소스코드를 간혹 고객들에게 공개해야 하는 경우도 있으니 전문적인 어조로 작성해야 한다.
# WTF같은걸 적으면 큰일난다.
# 농담 말장난 같은걸 적으면 안된다.

# 8) 코드태그와 TODO주석
# 주석 앞에 TODO를 붙혀서 메모를 하자
# TODO : 왜 매주 화요일이면 장애가 생기는지 알아보기
# 이외의 코드 태그들
# FIXME : 전혀 동작하지 않으므로 문제가 있음
# HACK : 추후 개선해야 함
# XXX : 심각도가 높아지는 일반적인 경고를 담아두어야 하는 경우

# 9) 매직 주석과 소스 파일
# 주석에도 매직 주석이 있다.
#!/usr/bin/env python3
# -*- coding: utf:8
# 이는 코딩 정보와 파일의 명령어를 실행하기 위해 운영체제에 전달된다.

# 2. 독스트링
# class나 함수 정의 앞부분에 존재하는 것으로 """"""로 표시되는 다중행 주석
def get():
    r"""Sends a GET request. Returns :class:'Response' object
    :param url : URL for the new : class :'Request' object"""
    pass
from chapter10 import ch11
print(ch11.__doc__) # 주석을 출력할 수 있다.

# 3. 타입 힌트
def describeNumber(number: int) -> str:
    pass
number : int = 42

# 이렇게 타입 힌트를 줄 수 있다.

# 1) 정적 분석 도구 사용
# 정적 분석은 코드 실행 없이 코드를 검사하는 것
# mypy를 활용하면 타입 검사를 할 수 있다.


# 2) 타입 힌트를 다중 타입으로 설정하기
# 복수의 타입을 가지는 경우는 어떻게 처리할까??
from typing import Union, Optional, Any

# Union을 활용하기
def describeNumber(number : Union[int,float]) -> str:
    pass
# Optional을 활용하기
# Optional은 Union[str, None]과 같은 의미이다.
lastName : Optional[str] = None
lastName = 'Sweigart'
# Any를 활용하기
# 모든 타입이 가능하다는 뜻
data : Any =50

# 3) 리스트, 딕셔너리 등을 위한 타입 힌트 설정
from typing import List

catNames :List[str] = ['cat','pig']
numbers :List[Union[int, float]] = [1, 1.11, 3.14, 10]

# 같은 방법으로 튜플, 딕셔너리, 집합, 등등의 데이터 타입도 가능하다.

# 4) 주석을 활용한 타입 힌트 백포팅
spam = 42 # type : int
# 이렇게 타입 힌트를 제공할 수 있다.
