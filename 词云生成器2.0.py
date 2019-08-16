from wordcloud import WordCloud, ImageColorGenerator
import imageio
import jieba


class CiYu:
    def __init__(self, txt_p, png_p, jpg_p,
                 width, height, bgcolor, num,
                 font_p, maxw
                 ):
        self.txt_p = txt_p
        self.png_p = png_p
        self.jpg_p = jpg_p
        self.width = width
        self.height = height
        self.bgcolor = bgcolor
        self.font_p = font_p
        self.scale = "5"
        self.rs = "0.01"
        self.maxw = maxw
#        self.maxfs = 20000
        self.repeat = 1
        self.num = num

    def txt_path(self):
        txt_p = self.txt_p
        with open(txt_p, encoding='utf-8') as f:
            txt_ys = f.read()
            txt_cut = jieba.lcut(txt_ys)
            txt_cut = " ".join(txt_cut)
            print(txt_cut)

        # def wcloud(self):
        if self.png_p:
            mask = imageio.imread(self.png_p)
            mc = ImageColorGenerator(mask)
        else:
            mask = None
            mc = None

        # w = WordCloud(mask=mk)

        w = WordCloud(width=int(self.width),
                      height=int(self.height),
                      background_color=str(self.bgcolor),
                      font_path=self.font_p,
                      scale=int(self.scale),
                      relative_scaling=float(self.rs),  # 值越小越频密，需配合max_word才有好效果
                      max_words=self.maxw,  # 值越大越频密
#                      max_font_size=int(self.maxfs),
                      max_font_size=300,
                      repeat=bool(self.repeat),
                      mask=mask)

        # wg = w.generate(self.txt_cut)
        for i in range(int(self.num)):
            global files
            wg = w.generate(txt_cut).recolor(color_func=mc)
            files = self.jpg_p + "\\" + str(i) + ".jpg"
            wg.to_file(files)
            print("生成{}成功!".format(files))
            

import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
# Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
from tkinter.messagebox import *


# Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
import tkinter.filedialog as tkFileDialog
# import tkinter.simpledialog as tkSimpleDialog  #askstring()

class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('词云生成器V2.0')
        self.master.geometry('386x469')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.颜色Var = StringVar(value='white')
        self.颜色 = Entry(self.top, textvariable=self.颜色Var, font=(u'微软雅黑', 10))
        self.颜色.setText = lambda x: self.颜色Var.set(x)
        self.颜色.text = lambda: self.颜色Var.get()
        self.颜色.place(relx=0.373, rely=0.648, relwidth=0.148, relheight=0.053)

        self.Command6Var = StringVar(value='GO！')
        self.style.configure('TCommand6.TButton', font=(u'微软雅黑', 29))
        self.Command6 = Button(self.top, text='Command6', textvariable=self.Command6Var, command=self.Command6_Cmd,
                               style='TCommand6.TButton')
        self.Command6.setText = lambda x: self.Command6Var.set(x)
        self.Command6.text = lambda: self.Command6Var.get()
        self.Command6.place(relx=0.601, rely=0.648, relwidth=0.334, relheight=0.292)

        self.密度Var = StringVar(value='1000')
        self.密度 = Entry(self.top, textvariable=self.密度Var, font=(u'宋体', 12))
        self.密度.setText = lambda x: self.密度Var.set(x)
        self.密度.text = lambda: self.密度Var.get()
        self.密度.place(relx=0.373, rely=0.887, relwidth=0.127, relheight=0.053)

        self.次数Var = StringVar(value='1')
        self.次数 = Entry(self.top, textvariable=self.次数Var, font=(u'宋体', 12))
        self.次数.setText = lambda x: self.次数Var.set(x)
        self.次数.text = lambda: self.次数Var.get()
        self.次数.place(relx=0.373, rely=0.768, relwidth=0.065, relheight=0.053)

        self.宽Var = StringVar(value='500')
        self.宽 = Entry(self.top, textvariable=self.宽Var, font=(u'宋体', 12))
        self.宽.setText = lambda x: self.宽Var.set(x)
        self.宽.text = lambda: self.宽Var.get()
        self.宽.place(relx=0.705, rely=0.529, relwidth=0.231, relheight=0.053)

        self.长Var = StringVar(value='1000')
        self.长 = Entry(self.top, textvariable=self.长Var, font=(u'宋体', 12))
        self.长.setText = lambda x: self.长Var.set(x)
        self.长.text = lambda: self.长Var.get()
        self.长.place(relx=0.373, rely=0.529, relwidth=0.231, relheight=0.053)

        self.字体路径Var = StringVar(value='*.ttf')
        self.字体路径 = Entry(self.top, textvariable=self.字体路径Var, font=(u'宋体', 9))
        self.字体路径.setText = lambda x: self.字体路径Var.set(x)
        self.字体路径.text = lambda: self.字体路径Var.get()
        self.字体路径.place(relx=0.373, rely=0.29, relwidth=0.562, relheight=0.053)

        self.选择字体Var = StringVar(value='请选择字体')
        self.style.configure('T选择字体.TButton', font=(u'宋体', 9))
        self.选择字体 = Button(self.top, text='请选择字体', textvariable=self.选择字体Var, command=self.选择字体_Cmd,
                           style='T选择字体.TButton')
        self.选择字体.setText = lambda x: self.选择字体Var.set(x)
        self.选择字体.text = lambda: self.选择字体Var.get()
        self.选择字体.place(relx=0.062, rely=0.29, relwidth=0.231, relheight=0.053)

        self.保存路径Var = StringVar(value='C:\\')
        self.保存路径 = Entry(self.top, textvariable=self.保存路径Var, font=(u'宋体', 9))
        self.保存路径.setText = lambda x: self.保存路径Var.set(x)
        self.保存路径.text = lambda: self.保存路径Var.get()
        self.保存路径.place(relx=0.373, rely=0.409, relwidth=0.562, relheight=0.053)

        self.选择目录Var = StringVar(value='保存到目录')
        self.style.configure('T选择目录.TButton', font=(u'宋体', 9))
        self.选择目录 = Button(self.top, text='保存到目录', textvariable=self.选择目录Var, command=self.选择目录_Cmd,
                           style='T选择目录.TButton')
        self.选择目录.setText = lambda x: self.选择目录Var.set(x)
        self.选择目录.text = lambda: self.选择目录Var.get()
        self.选择目录.place(relx=0.062, rely=0.409, relwidth=0.231, relheight=0.053)

        self.边界路径Var = StringVar(value='')
        self.边界路径 = Entry(self.top, textvariable=self.边界路径Var, font=(u'宋体', 9))
        self.边界路径.setText = lambda x: self.边界路径Var.set(x)
        self.边界路径.text = lambda: self.边界路径Var.get()
        self.边界路径.place(relx=0.373, rely=0.171, relwidth=0.562, relheight=0.053)

        self.选择边界Var = StringVar(value='请选择边界图')
        self.style.configure('T选择边界.TButton', font=(u'宋体', 9))
        self.选择边界 = Button(self.top, text='请选择边界图', textvariable=self.选择边界Var, command=self.选择边界_Cmd,
                           style='T选择边界.TButton')
        self.选择边界.setText = lambda x: self.选择边界Var.set(x)
        self.选择边界.text = lambda: self.选择边界Var.get()
        self.选择边界.place(relx=0.062, rely=0.171, relwidth=0.231, relheight=0.053)

        self.文本路径Var = StringVar(value='*.txt')
        self.文本路径 = Entry(self.top, textvariable=self.文本路径Var, font=(u'宋体', 9))
        self.文本路径.setText = lambda x: self.文本路径Var.set(x)
        self.文本路径.text = lambda: self.文本路径Var.get()
        self.文本路径.place(relx=0.373, rely=0.051, relwidth=0.562, relheight=0.053)

        self.选择文本Var = StringVar(value='请选择文本')
        self.style.configure('T选择文本.TButton', font=(u'宋体', 9))
        self.选择文本 = Button(self.top, text='请选择文本', textvariable=self.选择文本Var, command=self.选择文本_Cmd,
                           style='T选择文本.TButton')
        self.选择文本.setText = lambda x: self.选择文本Var.set(x)
        self.选择文本.text = lambda: self.选择文本Var.get()
        self.选择文本.place(relx=0.062, rely=0.051, relwidth=0.231, relheight=0.053)

        self.Label5Var = StringVar(value='设置单词密度')
        self.style.configure('TLabel5.TLabel', anchor='w', font=(u'宋体', 9))
        self.Label5 = Label(self.top, text='设置单词密度', textvariable=self.Label5Var, style='TLabel5.TLabel')
        self.Label5.setText = lambda x: self.Label5Var.set(x)
        self.Label5.text = lambda: self.Label5Var.get()
        self.Label5.place(relx=0.062, rely=0.904, relwidth=0.21, relheight=0.036)

        self.Label4Var = StringVar(value='设置背景颜色')
        self.style.configure('TLabel4.TLabel', anchor='w', font=(u'宋体', 9))
        self.Label4 = Label(self.top, text='设置颜色', textvariable=self.Label4Var, style='TLabel4.TLabel')
        self.Label4.setText = lambda x: self.Label4Var.set(x)
        self.Label4.text = lambda: self.Label4Var.get()
        self.Label4.place(relx=0.062, rely=0.665, relwidth=0.21, relheight=0.036)

        self.Label3Var = StringVar(value='设置生成次数')
        self.style.configure('TLabel3.TLabel', anchor='w', font=(u'宋体', 10))
        self.Label3 = Label(self.top, text='设置生成次数', textvariable=self.Label3Var, style='TLabel3.TLabel')
        self.Label3.setText = lambda x: self.Label3Var.set(x)
        self.Label3.text = lambda: self.Label3Var.get()
        self.Label3.place(relx=0.062, rely=0.785, relwidth=0.231, relheight=0.036)

        self.Label2Var = StringVar(value='*')
        self.style.configure('TLabel2.TLabel', anchor='w', font=(u'宋体', 18))
        self.Label2 = Label(self.top, text='*', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda: self.Label2Var.get()
        self.Label2.place(relx=0.642, rely=0.529, relwidth=0.044, relheight=0.053)

        self.Label1Var = StringVar(value='设置图片大小')
        self.style.configure('TLabel1.TLabel', anchor='w', font=(u'宋体', 10))
        self.Label1 = Label(self.top, text='设置图片大小', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda: self.Label1Var.get()
        self.Label1.place(relx=0.062, rely=0.546, relwidth=0.231, relheight=0.036)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command6_Cmd(self, event=None):
        # TODO, Please finish the function here!

        sc = CiYu(self.文本路径.get(),
                  self.边界路径.get(),
                  self.保存路径.get(),
                  self.长.get(),
                  self.宽.get(),
                  self.颜色.get(),
                  self.次数.get(),
                  self.字体路径.get(),
                  int(self.密度.get())
                  )
        # try:

        sc.txt_path()
        showinfo("完成！", "{}文件已生成！".format(files))
        # except:
        #     showinfo("错误", "文件或参数有误，请重新设置！")

        pass

    def 选择字体_Cmd(self, event=None):
        # TODO, Please finish the function here!
        font = tkFileDialog.askopenfilename()
        self.字体路径.delete(0, END)
        self.字体路径.insert(0, str(font))
        pass

    def 选择目录_Cmd(self, eventf=None):
        # TODO, Please finish the function here!
        fdir = tkFileDialog.askdirectory()
        self.保存路径.delete(0, END)
        self.保存路径.insert(0, str(fdir))
        pass

    def 选择边界_Cmd(self, event=None):
        # TODO, Please finish the function here!
        png = tkFileDialog.askopenfilename()
        self.边界路径.delete(0, END)
        self.边界路径.insert(0, str(png))
        pass

    def 选择文本_Cmd(self, event=None):
        # TODO, Please finish the function here!
        txt = tkFileDialog.askopenfilename()
        self.文本路径.delete(0, END)
        self.文本路径.insert(0, str(txt))
        pass


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
