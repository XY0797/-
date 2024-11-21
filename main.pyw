import time
import threading

import tkinter as tk
from tkinter import scrolledtext, ttk

import pyautogui
from SendInput import Keyboard


def input_one_char(char_str):
    if char_str=='\n':
        Keyboard.press(0x0D) # ENTER键
        Keyboard.release(0x0D)
    else:
        Keyboard.pressByUnicode(char_str)
        Keyboard.releaseByUnicode(char_str)


def simulate_input_st():
    # 按钮切换为禁止状态
    start_button.config(state=tk.DISABLED)
    # 启动线程，避免卡UI
    t = threading.Thread(target=simulate_input)
    t.start()


def simulate_input():
    # 获取文本框中的文本
    text_to_type = text_area.get("0.0", "end-1c")
    # 统一换行符
    text_to_type = text_to_type.replace('\r\n', '\n')
    text_to_type = text_to_type.replace('\r', '\n')

    # 延时3秒，修改按钮显示的文本
    for i in range(3):
        start_button.config(text=f"{3-i}秒后开始输入")
        time.sleep(1)

    # 模拟输入文本
    # 判断选中的方式
    opt_choice_index = option_menu.current()
    if opt_choice_index == 0:
        # 模拟输入unicode字符
        for char in text_to_type:
            input_one_char(char)
    elif opt_choice_index == 1:
        # 模拟键盘按下
        pyautogui.write(text_to_type)

    # 恢复按钮显示
    start_button.config(text="开始输入")
    start_button.config(state=tk.NORMAL)


# 创建主窗口（置顶）
root = tk.Tk()
root.title("模拟输入内容")
root.attributes("-topmost", True)

# 添加文本框
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_area.pack(padx=10, pady=10)

# 添加选择框
container = tk.Frame(root)
container.pack(pady=10)
label = ttk.Label(container, text="模拟输入：")
label.pack(side=tk.LEFT, padx=5)
var = tk.StringVar()
var.set("模拟输入unicode字符")
options = ["模拟输入unicode字符", "模拟键盘按下(仅支持键盘上有的字符)"]
option_menu = ttk.Combobox(
    container, textvariable=var, values=options, state="readonly", width=30
)
option_menu.pack(side=tk.LEFT, padx=5)

# 添加开始按钮
start_button = ttk.Button(root, text="开始输入", command=simulate_input_st, padding=5)
start_button.pack(pady=20)

# 运行主循环
root.mainloop()
