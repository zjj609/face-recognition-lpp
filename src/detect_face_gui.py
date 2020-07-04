import tkinter as tk
import threading
from detect_webcam import *
import tkinter.font as tf


# 定义MainUI类表示应用/窗口，继承Frame类
class MainUI(tk.Frame):
    # Application构造函数，master为窗口的父控件
    def __init__(self, master = None):
        # 初始化Application的Frame部分 
        tk.Frame.__init__(self, master)
        # 显示窗口，并使用grid布局
        self.grid()
        self.detectFace = detect_face()
        self.ft = tf.Font(family='Times', size=15,weight=tf.BOLD,slant=tf.ITALIC)
        self.ft2 = tf.Font(family='Times', size=23,weight=tf.BOLD,slant=tf.ITALIC) #,underline=1
        # 创建控件
        self.createWidgets()


    # 创建线程执行程序
    def thread_it(self,func):		# 传入函数名和参数
        # 创建线程
        self.th = threading.Thread(target=func)
        # 守护线程
        self.th.setDaemon(True)
        # 启动
        self.th.start()

    def thread_stop(self,func):
        func()
        #self.th.join()
        
    def update_sec(self):
        self.variableText.set(self.detectFace.current_sec)
        self.after(500,self.update_sec)
        
    # 创建控件
    def createWidgets(self):
        # 创建一个按钮，用来触发start_detect方法
        self.clickButtonStart = tk.Button(self,text="开始",font=self.ft,command=lambda:self.thread_it(self.detectFace.start_detect))
        # 创建一个按钮，用来触发stop_detect方法
        self.clickButtonStop = tk.Button(self,text="结束",font=self.ft,command=lambda:self.thread_stop(self.detectFace.stop_detect))
        # 创建一个标签，输出要显示的内容
        self.showLabel = tk.Label(self,text="锁屏倒计时：",font=self.ft)
        # 创建一个标签，输出要显示的内容
        self.showLabelSec = tk.Label(self,text=" 秒",font=self.ft2)
        self.variableText = tk.StringVar()
        self.variableText.set(self.detectFace.current_sec)
        self.showLabelVar = tk.Label(self,textvariable=self.variableText,font=self.ft2)
        
        # 设定使用grid布局
        self.clickButtonStart.grid(row=1,column=0)
        self.clickButtonStop.grid(row=2,column=0)
        self.showLabel.grid(row=1,column=1)
        self.showLabelVar.grid(row=2,column=1)
        self.showLabelSec.grid(row=2,column=2)

        self.after(500,self.update_sec)
        

# 创建一个MainUI对象
app = MainUI()
# 设置窗口标题
app.master.title('自动锁屏系统')
# 设置窗体大小
app.master.geometry('280x83')
app.master.wm_attributes('-topmost',True)
# 主循环开始
app.mainloop()
