from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)

from random import shuffle, randint
class Question():
    def __init__(self,question,right_answer,wrong_1,wrong_2,wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Английский', 'Итальянский'))
questions_list.append(Question('2+2*2', '6', '8', '0', '4'))
questions_list.append(Question('Кто изобрел лампочку', 'Эдисон', 'Испанский', 'Английский', 'Итальянский'))
app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    # установить в answers[0] текст правильного ответа right_answer
    answers[0].setText(q.right_answer)   
    # установить в answers[1] текст неправильного ответа wrong1
    answers[1].setText(q.wrong_1)
    # установить в answers[2] текст неправильного ответа wrong2
    answers[2].setText(q.wrong_2)
    # установить в answers[3] текст неправильного ответа wrong3
    answers[3].setText(q.wrong_3)
    # установить в lb_Question текст вопроса question
    lb_Question.setText(q.question)
    # установить в lb_Correct текст правильного ответа
    lb_Correct.setText(q.right_answer)
    # вызвать метод show_question для отображения панели с вопросом
    show_question()
def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    # установить в lb_Result текст, который записан в res
    lb_Result.setText(res)    
    # вызвать метод show_result для отображения панели с результатом
    show_result()
 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    # если выбран кнопка answers[0], то вызываем метод show_correct с параметром 'Правильно!'
    if answers[0].isChecked():
        show_correct('Угадал')
        window.score = window.score + 1
        print('Общее число вопросов =' + str(window.total) + 'Число правильных ответов = ' + str(window.score))
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Не правильно')
            print('Лузер')     
    # иначе, если выбрана кнопка answers[1] или answers[2] или answers[3], то вызываем функцию show_correct  с параметром 'Неверно!'
def next_question():
    i = randint(0,len(questions_list) - 1)
    window.total = window.total + 1
    q = questions_list[i]
    ask(q)
def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

window.score = 0
window.total = 0

next_question()


btn_OK.clicked.connect(click_ok) 
next_question() 
window.show()
app.exec()

