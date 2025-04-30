'''
404 - сайт недоступен
200 - Ок
500 - ошибка на сервере
'''

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import requests
from queue import Queue

class WebsiteCheckerApp:
    def __init__(self, window):
        self.window = window
        self.window.title('Проверка статуса сайтов')
        self.window.geometry('800x600')


window = tk.Tk()
w = WebsiteCheckerApp(window)
window.mainloop()