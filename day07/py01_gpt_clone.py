# 제미나이를 활용한 GPT클론
# tkinter 모듈에 있는 모든 클래스, 함수, 변수등을 다 쓰겠다는 표시(*)
from tkinter import * 
from tkinter.messagebox import * # 모듈 및에 있는 모듈을 (from tkinter import *) 로 가져올 수 없음
from tkinter.scrolledtext import * # 모듈 및에 있는 모듈을 (from tkinter import *) 로 가져올 수 없음
from tkinter.font import *

# 제미나이를 위한 모듈
import google.generativeai as genai


# 6. 제미나이 API용 구성
genai.configure(api_key='AIzaSyAmkFtDDvdV0Qsm9A-i2UHCEadJALl3-XU') # 신청한 API키
model = genai.GenerativeModel('gemini-1.5-flash') # 사전훈련된 AI 모델

# 4. 전송버튼 이벤트, 제미나이 실행
def responseMessage():
    # showinfo('실행', 'API를 실행합니다!')
    inputText = textMessage.get('1.0', END).replace('\n', '').strip()
    print(inputText)
    textMessage.delete('1.0', END) # 입력창 글 지우기
    # showinfo('결과', inputText) # 다이얼로그, 모달(Modal)창

    if inputText:
        try:
            textResult.insert(END, '유저: ', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user') # 'user' 텍스트 아규먼트

            ai_response = model.generate_content(inputText)
            response = ai_response.text

            textResult.insert(END, '챗봇: ', 'bold')
            textResult.insert(END, f'{response}\n', 'ai') # 'ai' 텍스트 아규먼트

        except Exception as e:
            textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
        finally:
            textResult.see(END) # 스크롤텍스트 마지막위치로 스크롤 다운

# 8. textMessage 위젯에서 엔터를 치면 전송버튼이 작동
def keypress(event):
    # print(repr(event.char)) # repr을 안쓰면 \r, \x80이 출력안됨
    # \r(캐리지 리턴), \n(뉴라인, 한줄 내려쓰기) 혼용해서 사용 \r\n, \n, \r
    if event.char == '\r':
        responseMessage()

## 11. 종료시 이벤트처리 함수
def onClosing():
    if askyesno('종료확인', '종료하시겠습니까?'):
        root.destroy() # 완전 종료

# 1. 메인윈도우 생성
root = Tk()
root.title('제미나이 챗봇')
root.geometry('730x450')

# 7. 전체에서 사용할 폰트를 지정 -> 나눔고딕
myfont = Font(family='NanumGothic', size=10)
boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

# 2. UI화면 구성
inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF')
inputFrame.pack(side=BOTTOM, fill=BOTH)

# 3. inputFrame 들어갈 Entry와 Button 구성
textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myfont)

# 8. 입력창에서 엔터를 치면 keypress이벤트처리함수 발생
buttonSend = Button(inputFrame, text='전송', bg='green', fg='white', 
                    font=myfont,
                    command=responseMessage)
buttonSend.pack(side=RIGHT, padx=20, pady=5)
textMessage.bind('<Key>', keypress) 
textMessage.pack(side=LEFT, padx=15)
# 5. API호출 결과 메세지 출력될 스크롤기능 텍스트 위젯
textResult = ScrolledText(root, wrap=WORD, bg='#000000', fg='white', font=myfont) # bg='black' == bg='#000000'
textResult.pack(fill=BOTH, expand=True)

# 10. 스크롤텍스트에 나올 메시지 디자인
textResult.tag_configure('user', font=boldFont, foreground='yellow')
textResult.tag_configure('ai', font=myfont, foreground='limegreen') #89F336
textResult.tag_configure('error', font=boldFont, foreground='red')

# 9. 실행 후 바로 입력창에 포커스가 가도록
textMessage.focus_set()

# 11. 종료버튼(x)를 누르면 종료 메세지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing)

# 1. 종료시까지 계속 루프 실행
root.mainloop()