# iot-python-2025
IoT 개발자 기초 프로그래밍 언어 리포지토리

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
    - 변수
        - `데이터`를 담아서 다른데서 쓰기위해 사용
    - 자료형
        - None, int, float, string, bool, list, tuple, dict, set, ...
        - type() 함수로 <class 'str'> 확인가능
    - 화면입출력 - 콘솔에서 입력하고 결과를 출력
        - input(), print()
    - 문자열 포맷팅
        - 문자열을 조금 더 깔끔하게 표현하기 위해서
        - %s, %d, %f, ...
        - {0}, {1}, {2}, ...
        - f'{name, ..., {age}}'
    - 연산자
        - 사칙연산 : +, -, *, /, //, %, **, (, )
        - 리스트연산 : list[0], list[0:3 + 1]
        - 문자열연산 : .split(), .replce(), strip(), find(), ...

- 깃허브[데스크탑]
    1. **fetch origin** : 리모트 최신변경사항 확인(중요!)
    2. pull : 리모트에 변경사항을 로컬로 내려받기
    3. commit : 로컬, 리미트에 변경사항을 확정
    4. push : 로컬의 변경사항을 리모트로 올리기
    
## 3일차
- 파이썬 기초
    - 흐름제어
        - if - 참을 기준으로 분기
        - for - 일반적인 반복문
        - while - 참인 조건일 동안 무한 반복
    - 파일입출력
        - open(경로, mode='r|w|a', encoding='utf-8')
        - write(), readline()
        - close()
    - 함수
        - f(x) = y
        - 자주 사용할 로직을 묶어놓은 덩어리
        - 함수 호출
        ```python
        def funcName(param):
            # 로직
        ```
    - 객체지향
        - 현실세계와 동일하게 프로그래밍을 하겠다는 설계방식
        - 객체의 틀이되는 클래스 선언
        - 클래스 : 명사와 동사의 집합
            - 명사 : 멤버변수(속성)
            - 동사 : 멤버함수(메서드)

        ```python
        class ClassName:
            # 멤버변수
            
            def 멤버함수(self, param):
                #로직
        ```

## 4일차
- 파이썬 기초
    - 리스트연산 추가
        - append(), insert(index, value), del(list[index]), pop(), sort(), ...

    - 객체지향 다시
        - 모든 클래스의 조상은 `object` 클래스!
        - 클래스 작성방법
        - 속성(멤버변수)
        - 메서드(멤버함수)
        - 캡슐화(멤버변수를 폐쇄화), __멤버변수
        - 상속 - 상위클래스를 가지고 자식클래스를 만드는 것
        - **추상화**
        - **인터페이스**
        - **다형성**
        - **SOLID 원칙**

    - 모듈, 패키지
        - 함수나 클래스 등 자주 사용할 파이썬 파일로 만든것
        - 패키지(라이브러리) : 모듈을 모아둔 폴더
        - pip : 외부모듈을 다운로드 후 설치하는 명령어 (https://pypi.org에서 설치할 패키지 검색)

    - 예외처리
        - 예외 : 실행 중 프로그램 비정상 종료되는 Error
## 5일차
- 파이썬 기초
    - 예외처리
        - 프로그래밍에서 가장 중요!
        - 실행 중 발생, 프로그램을 비정상 종료시키는 것
    - 디버깅
        - 버그를 잡을때 가장 유용
        - F9, F5, F10, F11, Shift + F5, 변수탭, 조사식탭
        - 소스코드를 분석할 때 

- 파이썬 응용
    - 토이프로젝트
        - 콘솔앱 : My Movie List

## 6일차
- 파이썬 응용
    - 토이프로젝트
        - 내 영화 앱 수정, 마무리
        - 챗GPT 윈도우앱(tkinter) 만들기

    - 주피터 노트북 학습
    - PyQt 학습
    
    - 토이프로젝트
        - 윈도우앱(PyQt)



```python
파이썬 유용한 단축키
- 편리성 단축기
    - (shift + Del)한줄 삭제(매우 효율!)
    - (Ctrl + F5) 는 디버깅없이 실행
    - (Ctrl + /) 주석생성
    - (shift + 소괄호) 문장 선택후 문장 괄호치기
    - (Alt + 방향키) 한줄을 위아래로
- 디버그 단축기
    - (F5) 디버깅 시작, 중단점까지 실행
    - (F9) 중단점(Break Point) 표시/해체 기능
    - (F10) 한 줄 실행, 함수가 있어도 함수를 실행하고 넘어감
    - (F11) 한 줄 실행, 함수가 있으면 함수 안으로 진입
    - (Shilft + F5) 디버깅 종료
```