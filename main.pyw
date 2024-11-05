import pyautogui
import time
import tkinter as tk
from tkinter import scrolledtext


def simulate_input():
    # 获取文本框中的文本
    text_to_type = text_area.get("1.0", tk.END)

    # 延时3秒
    time.sleep(3)

    # 模拟输入文本
    pyautogui.write(text_to_type)


# 创建主窗口
root = tk.Tk()
root.title("模拟输入内容")

# 添加文本框
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_area.pack(padx=10, pady=10)

# 添加开始按钮
start_button = tk.Button(root, text="开始输入", command=simulate_input)
start_button.pack(pady=5)

# 运行主循环
root.mainloop()
