# 제미나이를 활용한 GPT클론
from tkinter import * 
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter.font import *

import google.generativeai as genai

class py02(Tk):
    
    def __init__(self):
        super().__init__()
        self.settings()
        self.make_wiget()

    def settings(self):
        self.title('제미나이 챗봇')
        self.geometry('730x450')
        self.iconbitmap('./image/bot.ico')

    def make_wiget(self):
        self.myfont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)
        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)
        self.buttonSend = Button(self.inputFrame, text='전송', bg='green', fg='white', 
                    font=self.myfont,
                    command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT, padx=20, pady=5)
        self.textResult = ScrolledText(self, wrap=WORD, bg='#000000', fg='white', font=self.myfont) # bg='black' == bg='#000000'
        self.textResult.pack(fill=BOTH, expand=True)
        self.textMessage = Text(self.inputFrame, width=75, height=1, wrap=WORD, font=self.myfont)
        self.textMessage.bind('<Key>', self.keypress) 
        self.textMessage.pack(side=LEFT, padx=15)
        self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow')
        self.textResult.tag_configure('ai', font=self.myfont, foreground='limegreen') #89F336
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')
        self.textMessage.focus_set()

    def keypress(self,event):
        # print(repr(event.char)) # repr을 안쓰면 \r, \x80이 출력안됨
        # \r(캐리지 리턴), \n(뉴라인, 한줄 내려쓰기) 혼용해서 사용 \r\n, \n, \r
        if event.char == '\r':
            self.responseMessage()

    def responseMessage(self):
        genai.configure(api_key='') # 신청한 API키
        model = genai.GenerativeModel('gemini-1.5-flash') # 사전훈련된 AI 모델
        # showinfo('실행', 'API를 실행합니다!')
        inputText = self.textMessage.get('1.0', END).replace('\n', '').strip()
        print(inputText)
        self.textMessage.delete('1.0', END) # 입력창 글 지우기
        # showinfo('결과', inputText) # 다이얼로그, 모달(Modal)창

        if inputText:
            try:
                self.textResult.insert(END, '유저: ', BOLD)
                self.textResult.insert(END, f'{inputText}\n\n', 'user') # 'user' 텍스트 아규먼트

                ai_response = model.generate_content(inputText)
                response = ai_response.text

                self.textResult.insert(END, '챗봇: ', 'bold')
                self.textResult.insert(END, f'{response}\n', 'ai') # 'ai' 텍스트 아규먼트

            except Exception as e:
                self.textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
            finally:
                self.textResult.see(END) # 스크롤텍스트 마지막위치로 스크롤 다운


app = py02()
app.mainloop()