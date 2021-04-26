import pyttsx3
import os
import random
import webbrowser
import time
import speech_recognition as sr
import pandas as pd
from tkinter import *
from fuzzywuzzy import fuzz
from colorama import *

# раздел глобальных переменных

text = ''
r = sr.Recognizer()
engine = pyttsx3.init()
adress = ''
serch = ''
j = 0
task_number = 0

# name программы, который мы удаляем
ndel = [
    'вилена',
    'лена',
    'вильгельм',
    'виленка',
    'не могла бы ты',
    'пожалусйта'
]

# комманды на которые реагирует программа
commands = [
    'привет',
    'открой файл',
    'выключи комп',
    'выруби компьютер',
    'пока', 'покажи файл',
    'покажи список команд',
    'открой vk',
    'открой браузер',
    'включи vk',
    'открой интернет',
    'youtube',
    'включи музон',
    'вруби музыку',
    'очисти файл',
    'открой стату',
    'покажи cтатистику',
    'открой музыку',
    'переведи', 'планы',
    'на будущее',
    'что планируется',
    'векторы в pygame'
]


# раздел описания функций комманд

def pri_com():  # выводит на экран историю запросов
    z = {}
    mas = []
    mas2 = []
    mas3 = []
    mas4 = []
    file = open('old_commands.txt', 'r', encoding='UTF-8')
    k = file.readlines()
    for i in range(len(k)):
        line = str(k[i].replace('\n', '').strip())
        mas.append(line)
    file.close()
    for i in range(len(mas)):
        x = mas[i]
        if x in z:
            z[x] += 1
        if not (x in z):
            b = {x: 1}
            z.update(b)
        if not (x in mas2):
            mas2.append(x)
    for i in mas2:
        mas3.append(z[i])
    for i in range(1, len(mas3) + 1):
        mas4.append(str(i) + ') ')
    list = pd.DataFrame({
        'command': mas2,
        'count': mas3
    }, index=mas4)
    list.index.name = '№'
    print(list)


def comparison(x):  # осуществляет поиск самой подходящей под запрос функции
    global commands, j, add_file
    ans = ''
    for i in range(len(commands)):
        k = fuzz.ratio(x, commands[i])
        if (k > 50) & (k > j):
            ans = commands[i]
            j = k
    if (ans != 'пока') & (ans != 'привет'):
        add_file(ans)
    return (str(ans))


def plans():
    global engine
    plans = ''' 
	Пока нечего сказать.
	 '''
    engine.say(plans)


def clear_analis():  # очистка файла с историей запросов
    global engine
    file = open('old_commands.txt', 'w', encoding='UTF-8')
    file.close()
    engine.say('Файл аналитики очищен!')


def add_file(x):
    file = open('old_commands.txt', 'a', encoding='UTF-8')
    if x != '':
        file.write(x + '\n')
    file.close()


def web_search():  # осуществляет поиск в интернете по запросу (adress)
    global adress
    webbrowser.open('https://yandex.ru/yandsearch?clid=2028026&text={}&lr=11373'.format(adress))


def check_searching():  # проверяет нужно-ли искать в интернете
    global text, wifi_name, add_file
    global adress
    global web_search
    if 'найди' in text:
        add_file('найди')
        adress = text.replace('найди', '').strip()
        text = text.replace(adress, '').strip()
        web_search()
        text = ''
    elif 'найти' in text:
        add_file('найди')
        adress = text.replace('найти', '').strip()
        text = text.replace(adress, '').strip()
        web_search()
        text = ''
    adress = ''


def clear_task():  # удаляет ключевые слова
    global text, ndel
    for z in ndel:
        text = text.replace(z, '').strip()
        text = text.replace('  ', ' ').strip()


def hello():  # функция приветствия
    global engine
    z = ["Рада снова вас слышать!", 'Что вам угодно?', 'Привет. Чем-нибудь помочь?']
    x = random.choice(z)
    engine.say(x)


def quit():  # функция выхода из программы
    global engine
    x = ['надеюсь мы скоро увидемся!', 'рада была помочь', 'всегда к вашим услугам']
    engine.say(random.choice(x))
    engine.runAndWait()
    engine.stop()
    os.system('cls')
    exit(0)


def show_cmds():  # выводит на экран список доступных комманд
    my_com = ['привет', 'открой файл', 'выключи компьютер', 'пока', 'покажи список команд',
              'открой vk', 'открой интернет', 'открой в youtube', 'включи музыку', 'очисти файл', 'покажи cтатистику']
    for i in my_com:
        print(i)
    time.sleep(2)


def brows():  # открывает браузер
    webbrowser.open('https://google.ru')


def ovk():  # открывает вк
    webbrowser.open('https://vk.com/feed')


def youtube():  # открывает ютюб
    global check_searching_youtube
    global serch
    x = ['Через сколько мне вас искать?', 'Опять за свои гаджеты!!!', 'Ютуб - наверное ваше будущее!!!',
         'Работайте, работайте!!!']
    engine.say(random.choice(x))
    webbrowser.open('http://www.youtube.com/watch?v='.format(serch))


def check_searching_youtube():  # проверяет нужно-ли искать в youtube
    global text, wifi_name, add_file
    global serch
    global youtube
    if 'youtube' in text:
        add_file('youtube')
        serch = text.replace('youtube', '').strip()
        text = text.replace(serch, '').strip()
        youtube()
        text = ''
    elif 'youtube' in text:
        add_file('youtube')
        serch = text.replace('youtube', '').strip()
        text = text.replace(serch, '').strip()
        youtube()
        text = ''
    serch = ''


def shut():  # ыключает компьютер
    global quit
    os.system('shutdown /s /f /t 10')
    quit()


def musik():  # включает музыку
    webbrowser.open('https://vk.com/')


def check_translate():
    global text, tr
    tr = 0
    variants = ['переведи', 'перевести', 'переводить', 'перевод']
    for i in variants:
        if (i in text) & (tr == 0):
            word = text
            word = word.replace('переведи', '').strip()
            word = word.replace('перевести', '').strip()
            word = word.replace('переводить', '').strip()
            word = word.replace('перевод', '').strip()
            word = word.replace('слово', '').strip()
            word = word.replace('слова', '').strip()
            webbrowser.open('https://translate.google.ru/#view=home&op=translate&sl=auto&tl=ru&text=привет'.format(word))
            tr = 1
            text = ''


def vectors():
    global engine
    vectors = ''' 
	Вектор - это одномерный массив: он содержит компоненты
	доступ к которым можно получить с помощью интегрального индекса.
	 '''
    engine.say(vectors)


cmds = {
    'привет': hello,
    'выруби компьютер': shut,
    'выключи комп': shut,
    'пока': quit,
    'покажи  cтатистику': pri_com,
    'покажи список команд': show_cmds,
    'открой браузер': brows,
    'включи vk': ovk,
    'открой интернет': brows,
    'youtube': youtube,
    'вруби музыку': musik,
    'открой vk': ovk,
    'открой  стату': pri_com,
    'включи музон': musik,
    'очисти файл': clear_analis,
    'покажи файл': pri_com,
    'открой файл': pri_com,
    'открой музыку': musik,
    'планы': plans,
    'на будущее': plans,
    'что планируется': plans,
    'переведи': check_translate,
    'векторы в pygame': vectors
}


# распознавание

def talk():
    global text, clear_task
    text = ''
    with sr.Microphone() as sourse:
        print('Я вас слушаю: ')
        r.adjust_for_ambient_noise(sourse)
        audio = r.listen(sourse)
        try:
            text = (r.recognize_google(audio, language="ru-RU")).lower()
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
        os.system('cls')
        lb['text'] = text
        clear_task()


# выполнение команд

def cmd_exe():
    global cmds, engine, comparison, check_searching, task_number, text, lb
    check_translate()
    text = comparison(text)
    print(text)
    check_searching()
    if (text in cmds):
        if (text != 'привет') & (text != 'пока') & (text != 'покажи список команд'):
            k = ['Секундочку', 'Пару минут']
            engine.say(random.choice(k))
        cmds[text]()
    elif text == '':
        pass
    else:
        print('Команда не найдена!')
        engine.say('Сам такой!!! Меня такому не учили!')
    task_number += 1
    if (task_number % 10 == 0):
        engine.say('Сам такой!!! Меня такому не учили!')
    engine.runAndWait()
    engine.stop()


# исправляет цвет

print(Fore.YELLOW + '', end='')
os.system('cls')


# основной бесконечный цикл

def main():
    global text, talk, cmd_exe, j
    try:
        talk()
        if text != '':
            cmd_exe()
            j = 0
    except(UnboundLocalError):
        pass
    except(TypeError):
        pass


# раздел создания интерфейса

root = Tk()
root.geometry('250x350')
root.configure(bg='gray22')
root.title('V.I.L.E.N.A.')
root.resizable(False, False)

lb = Label(root, text=text)
lb.configure(bg='gray')
lb.place(x=25, y=25, height=25, width=200)

but1 = Button(root, text='Add', command=main)
but1.configure(bd=1, font=('Castellar', 25), bg='gray')
but1.place(x=50, y=160, height=50, width=150)

but2 = Button(root, text='Exit', command=quit)
but2.configure(bd=1, font=('Castellar', 25), bg='gray')
but2.place(x=50, y=220, height=50, width=150)

root.mainloop()

while True:
    main()