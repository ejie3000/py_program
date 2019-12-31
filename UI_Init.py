import sys,os,tkinter
import requests, random, bs4, json, urllib
#====================================================================
#手动指定库路径，解决打包出错问题
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication
from PyQt5.QtCore import QTimer
#====================================================================
#导入库
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from tkinter import Label

#调取UI文件
from Ui_细节图下载 import Ui_xijietu

def YesGUI():
    win = tkinter.Tk()#弹窗
    win.title("成功")
    win.geometry("130x65+1215+685")
    label = Label(win, text="细节图下载成功",width=17,height=3)
    label.grid(columnspan = 2)
    win.mainloop()

def NoGUI():
    win = tkinter.Tk()#弹窗
    win.title("错误")
    win.geometry("130x65+1215+685")
    label = Label(win, text="请输入正确网址",width=17,height=3)
    label.grid(columnspan = 2)
    win.mainloop()

def on_click(self):
    value1 = ui.xijietu_lineEdit.text()
    url_pic = value1.split('=')[-1]
    url_XHR = 'https://www.uniqlo.cn/data/products/spu/zh_CN/'
    url = url_XHR + url_pic + '.json'
    #print(url)
    #官网XHR链接

    headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/79.0.3945.79 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    #请求网页
    if res.status_code == (200):
    
        bs = res.json()
        #解析网页

        img_name = bs['desc']['description']
        #获取细节图标签
        itemno_name = bs['summary']['code']
        #获取商品名

        src_list = bs4.BeautifulSoup(img_name, 'html.parser')

        #=============================================================================
        #创建文件夹
        mkpath = "C:\\DETAIL\\"
        path = (mkpath + itemno_name + '\\DETAIL')

        if not os.path.isdir(mkpath + itemno_name + '\\DETAIL'):
            os.makedirs(mkpath + itemno_name + '\\DETAIL')

        #=============================================================================
        #下载图片
        for num in src_list.find_all('img'):
            
            pic = num.attrs['src']
            #获取细节图链接
            if 'detail' in pic:
                pic_num = pic.split('/')[8][:-4]
                pic_num1 = int(pic_num) - 1
                pic_name = 'detail_' + str(pic_num1) 
            #获取细节图名字
            #print(pic)

                urllib.request.urlretrieve(pic, path+"\\"+pic_name + '.jpg')
            #下载图片并保存


        value1 = ui.xijietu_lineEdit.clear()#清除输入内容
        YesGUI()
    else:
        value1 = ui.xijietu_lineEdit.clear()#清除输入内容
        NoGUI()


#=============================================================================
#显示窗口
if __name__ == '__main__':

    app = QApplication([])

    window = QWidget()

    ui = Ui_xijietu()

    ui.setupUi(window)

    ui.xijietu_Button.clicked.connect(on_click)

    window.show()

    app.exec()
