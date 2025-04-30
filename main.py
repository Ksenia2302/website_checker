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


        self.queue = Queue()
        self.create_widgets()
        self.check_queue()


    def create_widgets(self):
        input_frame = ttk.Frame(self.window, padding='10')
        input_frame.pack(fill=tk.X)

        ttk.Label(input_frame, text='URL сайта: ').pack(side=tk.LEFT)
        self.url_entry = ttk.Entry(input_frame, width=50)
        self.url_entry.pack(side=tk.LEFT, padx=5)
        self.url_entry.bind('<Return>', lambda e: self.add_site())

        self.add_button = ttk.Button(input_frame, text='Добавить', command=self.add_site)
        self.add_button.pack(side=tk.LEFT)

        control_frame = ttk.Frame(self.window, padding='10')
        control_frame.pack(fill=tk.X)

        self.check_button = ttk.Button(control_frame, text='Проверить все', command=self.start_check_all)
        self.check_button.pack(side=tk.LEFT)
        self.clear_button = ttk.Button(control_frame, text='Очистить список', command=self.clear_list)
        self.clear_button.pack(side=tk.LEFT, padx=10)


        self.tree = ttk.Treeview(self.window, columns=('url', 'status', 'response_time'), show='headings')

        self.tree.heading('url', text='URL')
        self.tree.heading('status', text='Статус')
        self.tree.heading('response_time', text='Время ответа (мс)')


        self.tree.column('url', width=400)
        self.tree.column('status', width=150)
        self.tree.column('response_time', width=150)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.window,  textvariable=self.status_var, relief=tk.SUNKEN)
        self.status_bar.pack(fill=tk.X)





    def clear_list(self):
        pass
    def add_site(self):
        pass

    def check_queue(self):
        pass

    def start_check_all(self):
        pass





window = tk.Tk()
w = WebsiteCheckerApp(window)
window.mainloop()