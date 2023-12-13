# ch02
# 환경 설정과 명령행 사용 방법

# 파이썬의 경로
# 윈도우에서는 폴더와 파일명을 \로 분리하지만 맥OS와 리눅스에서는 /로 구분한다.
# 파이썬 스크립트의 호환 가능성을 보장하려면 /나 \를 이용하는 대신 pathlib 모듈과 연산자를 활용해야 한다.

import os
from pathlib import Path
print(Path('E:')/'python_study'/'python_clean_code')

# 홈 디렉토리
# Path.home()을 이용하면 시스템마다의 홈 디렉토리를 얻을 수 있다.
print('home: ',Path.home())

# 현재 작업 디렉터리(current working directory, cwd)
print('cwd',Path.cwd())

# 현재 작업 디렉토리를 홈 공간으로 변경하기
os.chdir(Path.home())
print(Path.cwd())

# 절대 경로와 상대 경로
# ../ 는 cwd에서 상위 폴더로의 접근을 의미한다

# 프로그램과 프로세스
# 프로그램은 실행할 수 있는 모든 소프트웨어 응용프로그램을 의미
# 프로세스는 프로그램의 실행 인스턴스
# ex)계산기를 5개를 켠다면 계산기 프로그램은 1개이지만 프로세스는 5개가 실행 중인 상태

# 명령행
# 명령행은 텍스트 기반 프로그램으로 명령어를 입력해서 운영체제와 상호작용을 하고 프로그램을 실행하는 역할
# 명령행 인터페이스(comand line interface, CLI) 명령 프롬프트, 터미널, 쉘, 콘솔이라고 부른다

# 명령행에서 프로그램을 실행하는 방법
# * 윈도우, 맥OS에서는 대소문자를 구분하지 않는다.
# 리눅스에서는 대소문자를 구분한다.

# 계산기 실행하기
# cwd내에서 실행가능하므로 calc.exe만 입력하면 된다.
# 만약 다른 곳의 파일을 실행하고 싶다면 해당 디렉토리로 cwd를 이동하여 실행 명령을 입력하면 된다.

# 명령행 인수
# 명령행 인수: 명령어 뒤에 입력하는 텍스트 조각
# 명령행 옵션: 단일 문자 또는 짧은 단어로 이루어진 명령행 인수
# 띄어쓰기가 있다면 명령행 인수로 처리하기 때문에 하나의 파일에 공백이 존재한다면 ""로 묶어주어야 한다.
# ex) cd "python study"

# 명령행에서 -c옵션으로 파이썬 코드를 실행하는 방법
# python -c "print('Hello, World!')"
# python -c "help(len)"

# 명령행에서 파이썬 프로그램 실행
# python 파일.py를 활용하면 된다.
# 여기서 추가 인자를 공백으로 구분하여 입력하게 되면 python파일 내에서 sys.argv 변수가 입력받는다.

# py.exe 프로그램 실행하기
# py -3.10 -c "import sys; print(*sys.argv[1:])" what is your name
# 해당 코드를 실행하면 what is your name이 출력된다.

# 파이썬 프로그램에서 명령어 실행하기
import subprocess, locale
# subprocess.run()은 파이썬 프로그램에서 셸 명령을 실행하기
procObj = subprocess.run(['python', '-c', 'help(len)'], stdout=subprocess.PIPE)
outputStr = procObj.stdout.decode(locale.getdefaultlocale()[1]) # 셀의 실행 결과를 반환한다
print('outputStr',outputStr)

# 타이핑을 최소화하는 탭 완성 기능
# 명령어를 실행하는 중간에 tab을 누르면 자동완성이 실행된다.
# cd c:\u에서 탭을 누르면 u로 시작하는 파일을 알아서 채워준다
# 여러번 누르면 u로 시작하는 파일을 순차적으로 보여준다

# 명령어 이력 보기
# 위쪽 화살표를 통해 접근 가능하다.

# 필수 명령어 모음
# 와일드카드 패턴
# *와 ?를 이용하여 접근 가능하며 *는 문자의 길이를 모를 때, ?는 문자의 길이를 알 때 사용 가능하다.
# 모르는 부분을 *와 ?로 채우고 입력하면 파일 탐색이 가능하다.
# dir *.py를 입력하면 해당 경로 안에서 .py로 끝나는 모든 파일을 전부 탐색한다.(하위 경로는 미탐색)

# cd를 이용한 디렉터리 변경
# 잘 아니까 패스

# 하위 경로까지 포함시키기
# dir /s *.py 처럼 이용하면 된다
# 맥과 리눅스에서는 find 명령어를 이용해야 한다.

# copy와 cp를 이용한 폴더 복사
# copy [원본 파일 또는 폴더] [대상 폴더] 혹은 cp [원본 파일 또는 폴더] [대상 폴더]를 이용한다.
# 만약 같은 폴더 내에 저장하고 싶다면 cp [원본 파일 또는 폴더] [파일 이름] 을 입력한다.

# move와 mv를 이용한 파일 이동
# move [원본 파일 또는 폴더] [대상 폴더] 혹은 mv [원본 파일 또는 폴더] [대상 폴더]을 활용한다.

# ren과 mv을 이용한 파일과 폴더 이름 변경
# ren [파일 또는 폴더] [새이름] 혹은 mv [파일 또는 폴더] [새이름] 을 활용한다

# del과 rm을 활용한 파일과 폴더 삭제
# del은 하위 폴더와 하위 폴더내의 파일은 남겨두고, 오직 해당 폴더 내의 파일만 삭제한다.
# del [파일 또는 폴더]로 실행하면 된다.
# 만약 하위 폴더만 남기고 모든 파일을 삭제하고 싶다면 del /s /q [폴더] 를 실행하면된다.
# 하위 폴더까지 삭제하려면 rd /s /q [폴더]를 입력하면 된다.(원본 폴더 포함)

# md와 mkdir을 이용한 폴더 생성
# md [폴더 명] 혹은 mkdir [폴더 명] 을 이용하면 폴더가 생성된다.

# where과 which를 이용한 프로그램 위치 검색
# 윈도우는 where, 맥, 리눅스는 which를 통해 프로그램의 위치를 탐색할 수 있다.
# where [프로그램] 혹은 which [프로그램]을 입력하면 된다.

# cls와 clear을 통해 터미널의 모든 입력을 삭제할 수 있다.

# 환경 변수와 PATH
# set 변수를 이용하여 터미널 창에 떠 있는 셀의 환경 변수 목록을 출력 가능
# 환경 변수에 있다면 긴 경로를 입력하지 않고 프로그램을 바로 실행할 수 있다.
# 원래도 파이썬을 실행하려면 C:....~~/python.exe를 실행해야 하지만 환경 변수에 있기 때문에 python.exe만 입력해도 실행 가능하다.


# 환경 변수 수정하기는 패스
