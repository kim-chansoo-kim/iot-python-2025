# iot-python-2025
IoT 개발자 기초 프로그래밍 언어 리포지토리

## 파이썬 유용한 단축키
- 편리성 단축기
    - (shift + Del)한줄 삭제(매우 효율!)
    - (Ctrl + F5) 는 디버깅없이 실행
    - (Ctrl + /) 주석생성
    - (shift + 소괄호) 문장 괄호치기

## 1일차
- 개발환경 설정
    - 압축, 폰트, 개발용 에디터 설치
        - 압축 - 반디집 설치(교육, 회사 모두 무료)
        - 폰트 - 나눔글꼴 중 D2Coding. 추후 나눔고딕코딩 필요(https://hangeul.naver.com/font)
        - NotePad++ 설치(메모장(https://notepad-plus-plus.org/downloads/))
        - 깃(https://git-scm.com/)
        - 깃허브 데스크탑(https://docs.github.com/ko/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop)
    - Visual Studio Code 설치(https://code.visualstudio.com/)
        - 확장 korean 설치
        - Font Family D2coding 추가, Mouse wheel zoom 설정

- 프로그래밍 언어 종류
    - 컴파일러(실행파일 생성)
        - C, C#, C++, Java, ...
    - 인터프리터(소스코드를 바로 실행, 실행파일 없음)
        - 파이썬, Javascript, ...
    
- 파이썬(Python)
    - 1990년에 개발한 인터 프리터 언어
    - 네덜란드 개발자 귀도 반 로섬이 개발
    - 객체지향 프로그래밍 언어(Object Oriented Program)
    - 아주 쉽게 학습할 수 있는 언어
    - 다운로드(https://www.python.org/)

- 파이썬 개발환경(Pyenv)
    - 파이썬 버전을 손쉽게 변경할 수 있는 툴
    - 파워셀 관리자모드 오픈, 아래의 명령어 실행
        ```shell
        > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
        ```
    - 사이트의(https://pyenv-win.github.io/pyenv-win/) Quick Start 1번실행(Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1")
    - pyenv로 파이썬 버전 설치 및 전역설정

- Visual Studio Code
    - 확장에서 Python 확장 설치
    - *.py 파일 생성 후 코딩
    - Ctrl + F5로 실행

## 2일차
- 파이썬 기초
    - 변수와 자료형
    - 입출력 
        - 화면입출력
        - 문자열 포맷팅
    - 연산자
    - 흐름제어
    - 파일입출력
    - 함수
    - 객체지향
    - 모듈, 패키지
    - 예외처리
    - 디버깅

