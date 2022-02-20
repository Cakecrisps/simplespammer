import time

import pyautogui
def spam(times = 5,word = 'Hello World',thred = 10):
    time.sleep(times)
    for i in range(thred):

        pyautogui.typewrite(word)
        pyautogui.press('Enter')
def main():
    while True:
        print('Введите текст на английском -->')
        word = input()
        try:
            print('Введите задержку -->')
            timesl = abs(int(input()))
            print('Введите количевство повторений')
            count = abs(int(input()))
        except:
            print('Некоректное значение')
            continue
        spam(word = word,times=timesl,thred=count)

if __name__ == '__main__':
    main()
