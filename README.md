# 模拟输入内容

解决学习通等平台不让粘贴的问题，适用于Windows平台。

## 介绍

一个简单的 python 程序，适用于Windows平台，利用Windows SendInput API，可以模拟输入内容到用户选中的页面。

使用 pyinstaller 打包脚本为独立的 exe 文件发行。

## 使用

1. 下载 Realses 中的 exe 文件
2. 双击运行
3. 切到要输入的页面
4. 粘贴你需要模拟输入的内容到程序的输入框中
5. 点击`开始输入`按钮
6. 程序会等待 3 秒后开始模拟输入，请尽快切换到目标页面，点击想要输入内容的输入框，倒计时结束后程序会以非常快的速度模拟输入文本，**支持中文和emoji**。

## 缺点

点击`开始输入`按钮后，程序会固定等待 3 秒，然后才会开始输入。程序并不能自动识别你是否准备好，只会在固定的时间后开始。

## 开发

### 配置依赖

（推荐在.venv 环境或 conda 环境下进行开发，避免污染你的主环境）

安装 pyautogui 库

```sh
pip install pyautogui
```

安装 pyinstaller 库用于打包

```sh
pip install pyinstaller
```

### 打包

```sh
pyinstaller -w -F -i icon.ico main.pyw
```

`-w`：使打包成品运行后无终端窗口

`-F`：一份可执行文件

`-i`：图标

打包后的产物会在 dist 文件夹下。
