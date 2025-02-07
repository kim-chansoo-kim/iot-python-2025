# 나의 영화 리스트 콘솔앱
import os # 운영체제 모듈
from Movie import Movie 

VERSION = 0.5

def clearScreen(): # os에 특화된 팁.
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# 메인에서 제일 처음 실행되는 함수
def run():
    # movie = Movie('어벤저스: 인피니티 워', 2018, '디즈니', 8.6)
    # print(movie)
    # set_movie()
    clearScreen() # 최초의 화면 클리어
    lst_movie = [] # 영화리스트를 담는 변수 type: list
    load_movie(lst_movie)

    while True:
        sel_menu = set_menu()
        if sel_menu == 1:
            # print('영화 입력') # 밑에 한번더 출력 되는친구
            movie = set_movie()
            lst_movie.append(movie)

        elif sel_menu == 2:
            print('영화 출력')
            get_movie(lst_movie)

        elif sel_menu == 3:
            print('영화 검색')
            title = input('검색할 영화명 입력 -> ')
            serch_movie(lst_movie, title)

        elif sel_menu == 4:
            print('영화 삭제')
            title = input('삭제할 영화명 입력 -> ')
            del_movie(lst_movie, title)

        elif sel_menu == 5:
            # print('앱 종료')
            # 종료직전 DB파일생성 완료
            save_movie(lst_movie)
            break # 반복문 탈출
        
        else:
            pass # 아무 것도 하지 않음
        input() # 입력대기 : 엔터치면 화면 넘어감
        clearScreen() # 메뉴 기능이 완료되면 화면 클리어


# 영화검색 함수
def serch_movie(items: list, title: str):
    for item in items: # item이 Movie 클래스인지 알 수 없음
        if item.isNameContain(title): # 오타발생 위험!
            print(item)

# 영화삭제 함수
def del_movie(items: list, title: str):
    for i, item in enumerate(items):
        if item.isNameExist(title):
            del items[i] # 인덱스로 리스트에 요소하나를 삭제

# 폴더에 파일로 영화리스트 저장
def save_movie(items: list):
    f = open('movie_db.txt', encoding ='utf-8', mode ='w') # 파일쓰기 오픈
    for item in items:
        f.write(f'{item.getTitle()}|')
        f.write(f'{item.getYear()}|')
        f.write(f'{item.getCompany()}|')
        f.write(f'{item.getRate()}\n')

    f.close()

def load_movie(items: list):
    f = open('movie_db.txt', encoding ='utf-8', mode ='r')
    while True:
        line = f.readline().replace('\n', '')
        if not line: break # 무한루프 빠져나가는 조건

        lines = line.split('|') # 구분자로 잘라서 네개요소의 리스트 생성
        title = lines[0]
        year = int(lines[1])
        company = lines[2]
        rate = float(lines[3]) # 평점\n들어감

        movie = Movie(title, year, company, rate)
        items.append(movie)
    f.close()

# 영화입력 함수
def set_movie():
    title, year, company, rate = input('영화입력[제목|개봉년|제작사|평점] > ').split('|') # 입력 중 예외발생
    year = int(year) # 년도는 정수로
    rate = float(rate) # 평점은 실수로
    # print(title, year, company, rate)
    # movie = Movie(title, year, company, rate) 아래와 같은 뜻
    movie = Movie(title= title, year=year, company=company, rate=rate) # 데이터형 예외발생
    return movie

# lst변수는 list타입이라고 지정
def get_movie(items: list):
    for item in items:
        print(item) # item: Movie 객체

def set_menu():
    str_menu = (f'내 영화 앱 v{VERSION}\n'
                '1. 영화 입력\n'
                '2. 영화 출력\n'
                '3. 영화 검색\n'
                '4. 영화 삭제\n'
                '5. 앱 종료\n')
    print(str_menu)
    try:
        sel_menu = int(input('메뉴번호 입력: ')) # 예외있음(ValueError)
    except Exception as e:
        sel_menu = 0
    return sel_menu

if __name__ == '__main__':
    # print('내영화 앱 시작')
    run()

print('프로그램 종료')