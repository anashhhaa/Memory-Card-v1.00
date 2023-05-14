#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

#функции

class Question():
    def __init__(
        self, questioo, right_answer, wrong1, wrong2, wrong3
                ):
        self.questioo = questioo
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



def ask(LoQ: Question):
    #сначала все спрячем, пока творится ахалай-махалай
    RGB.hide()
    grup_ans.hide()
 
 #заполняем неотображаемые радиокнопки значениями
    rbut_1.setText(LoQ.right_answer)
    rbut_2.setText(LoQ.wrong1)
    rbut_3.setText(LoQ.wrong2)
    rbut_4.setText(LoQ.wrong3)
 
 
    shuffle(answers)                #перемешиваем значения
    layout_ver1.addWidget(answers[0]) 
    layout_ver1.addWidget(answers[1])
    layout_ver2.addWidget(answers[2]) 
    layout_ver2.addWidget(answers[3])

 
    RadioGroup.setExclusive(False)    #сброс флагов
    rbut_1.setChecked(False)
    rbut_2.setChecked(False)
    rbut_3.setChecked(False)
    rbut_4.setChecked(False)
    RadioGroup.setExclusive(True)
 

 
    
    question.setText(LoQ.questioo)
    answear.setText(LoQ.right_answer)
    RGB.show()
    ans_but.setText('Ответить')

def check_answer():    #функция проверки
    ans_correct = 'Верно!'
    ans_wrong = 'Ну ты  даееешь'
    ans_miss = 'ХА-ХА,  сначала вариант выбери, чудик'

    if rbut_1.isChecked():
        show_correct(ans_correct)
        main_win.score += 1
    elif rbut_2.isChecked() or rbut_3.isChecked() or rbut_4.isChecked():
        show_correct(ans_wrong)
    else:
        show_correct(ans_miss)


def show_correct(res):
    #сначала все спрячем, пока творится ахалай-махалай
    RGB.hide()
    grup_ans.hide()
    
    #заполняем переменные
    rez_ans.setText(res)
    answear = rbut_1.text
    
    #ахалай-махалай прошел - все проявляем
    grup_ans.show()
    ans_but.setText('Следующий вопрос')

      

def show_question():
    RGB.show()
    grup_ans.hide()
    question.setText('Какой национальности не существует?')
    ans_but.setText('Ответить')
    RadioGroup.setExclusive(False)    
    rbut_1.setChecked(False)
    rbut_2.setChecked(False)
    rbut_3.setChecked(False)
    rbut_4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    RGB.hide()
    grup_ans.show()
    question.setText('Самый слож вопрос')
    ans_but.setText('Следующий вопрос')



def start_test():
    if ans_but.text() == 'Ответить':
        show_result()
    else:
        show_question()


def next_question():
    print('Статистика')
    print('Всего вопросов:',main_win.total)
    print('Правильных ответов:', main_win.score)
    
    shuffle(questions_list)
    main_win.cur_question += 1
    main_win.total += 1
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0
        print('Рейтинг:', main_win.score/main_win.total*100,'%')
    LoQ = questions_list[main_win.cur_question]
    ask(LoQ)
    
    

def click_OK():
    if ans_but.text() == 'Ответить':
        check_answer()
    else:
        next_question()
#начало программы


app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Memory Card')

#Вопросы
quest1 = Question('сколько время?', 'не знаю', '10:30', '14:29','99:99')
quest2 = Question('Как звали 16 президента Америки?', 'Авраам Линкольн', "Владимир Путин", "Петр I", 'Энштейн')
quest3 = Question('Как называется данный химический элемент( Cl )? ', 'хлор', 'кальций', 'калий', 'гидраргиум')
quest4 = Question('Как на английском будет "Машина"?', 'car', 'mobil', 'avto', 'mashine')
quest5 = Question('Как сделать ТНТ в майнкрафте?', '4 песка, 5 пороха',"5 песка, 4 пороха", "2 песка, порох, нитка", "песок, порох, редстоун, нитка")


#Сюда суем вопросы

question = QLabel('Какой национальности не существует?')


RGB = QGroupBox('Варианты')  #группа
rbut_1 = QRadioButton('Энцы')
rbut_2 = QRadioButton('Смурфы')
rbut_3 = QRadioButton('Чулымцы')
rbut_4 = QRadioButton('Алеуты')
answers = [rbut_1, rbut_2, rbut_3, rbut_4]     #список с кнопками
layout_gor1 = QHBoxLayout()   
layout_ver1 = QVBoxLayout() 
layout_ver2 = QVBoxLayout()

RadioGroup = QButtonGroup() #групп по функц
RadioGroup.addButton(rbut_1)
RadioGroup.addButton(rbut_2)
RadioGroup.addButton(rbut_3)
RadioGroup.addButton(rbut_4)


layout_ver1.addWidget(rbut_1) 
layout_ver1.addWidget(rbut_2)
layout_ver2.addWidget(rbut_3) 
layout_ver2.addWidget(rbut_4)
layout_gor1.addLayout(layout_ver1)
layout_gor1.addLayout(layout_ver2)
layout_ver1.setSpacing(35)
layout_ver2.setSpacing(35)
layout_gor1.setSpacing(35)
RGB.setLayout(layout_gor1)

ans_but = QPushButton('Ответить')     #кнопка ответа
maim_lin_vert = QVBoxLayout()
maim_lin_gor1 = QHBoxLayout()
maim_lin_gor3 = QHBoxLayout()

maim_lin_gor1.addWidget(question, alignment=Qt.AlignHCenter)   #сбор виджетов и группы
maim_lin_gor3.addStretch(2)
maim_lin_gor3.addWidget(ans_but, stretch=5)
maim_lin_gor3.addStretch(2)
maim_lin_vert.addLayout(maim_lin_gor1)
maim_lin_vert.addWidget(RGB, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

#Счетчик верных и всего
main_win.score = 0
main_win.total = 0

#СЧЕТЧИК
main_win.cur_question = -1


#ФОРМА окна результата

grup_ans = QGroupBox('Результат ответа')
rez_ans = QLabel('Прав/неправ')
answear = QLabel('Правельный ответ')
boxline_vert = QVBoxLayout()

boxline_vert.addWidget(rez_ans)
boxline_vert.setSpacing(35)
boxline_vert.addWidget(answear, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

grup_ans.setLayout(boxline_vert)
maim_lin_vert.addWidget(grup_ans, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) #сбор виджетов и двух групп

maim_lin_vert.addLayout(maim_lin_gor3)  #сбор виджетов и двух групп
main_win.setLayout(maim_lin_vert)       #сбор виджетов и двух групп


questions_list = list()

questions_list.append(quest1)
questions_list.append(quest2)
questions_list.append(quest3)
questions_list.append(quest4)
questions_list.append(quest5)

ans_but.clicked.connect(click_OK)
next_question()


RGB.show()
grup_ans.hide()


main_win.show()
app.exec_()

