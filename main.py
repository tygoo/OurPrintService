import kivy
#!/usr/bin/env python
#kivy.require("1.11.0")
# -*- coding: utf-8 -*-
import os
import string
import requests
import time
import sys
import re
import os
import io
import subprocess
import tempfile
from subprocess import call
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.utils import platform as core_platform
from functools import partial
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from pdf2image.pdf2image import convert_from_path
with io.open("Online.kv", encoding='utf8') as f:
    Builder.load_string(f.read())
with io.open("Offline.kv", encoding='utf8') as f:
    Builder.load_string(f.read())
with io.open("fileChooser.kv", encoding='utf8') as f:
    Builder.load_string(f.read())
with io.open("printOpt.kv", encoding='utf8') as f:
    Builder.load_string(f.read())
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
platform = core_platform
filesize_units = ('B', 'KB', 'MB', 'GB', 'TB')
sys.path.insert(0, '/Users/macbook/Documents/python test/ScreenManager')
sys.path.insert(0, '/Users/macbook/Documents/python test/ScreenManager/docx2pdf-master2/docx2pdf/__init__.py')
sys.path.insert(0, "/Users/macbook/python test/lib/python2.7/site-packages/kivy/uix/fileChooser.py")
UsrPathSaverTxtFile = "aaa.txt"
Window.clearcolor = (0.95,0.95,0.95,1)
_have_win32file = False
data_color = False
data_pageNum = 1
save_value = 0
checkerVariable = ['.DS_Store']

class MainScreen(Screen):
    pass

class OfflineScreen(Screen):
    def chkDev(self):
        global save_path1, k
        path = '/Users/macbook/Documents/python test/ScreenManager/FLASH'
        files = os.listdir(path)
        print("ohh" ,files)
        if files != checkerVariable:
            call(["python", "/Users/macbook/python test/lib/python2.7/site-packages/kivy/uix/fileChooser.py"])
            f = open(UsrPathSaverTxtFile, "r")
            filePath_text = f.read()
            f.close()
            if filePath_text != '':
                self.ids.WarningText.text = "YOUR FILE HAS SAVED. DO YOU CONTINUE?"
                self.ids.btn1.opacity = 1
                self.ids.btn2.opacity = 1
            else:
                self.ids.WarningText.text = "PLEASE CHOOSE YOUR FILE!"
        else:
            self.ids.WarningText.text = "PLEASE ENTER YOUR DEVICE!"

    def del1(self):
        self.ids.WarningText.text = "PLEASE ENTER YOUR DEVICE"
        self.ids.btn1.opacity = 0
        self.ids.btn2.opacity = 0
        SaveButtonChk(False)

    # def convertFile(self):
        # f = open(UsrPathSaverTxtFile, "r")
        # filePath_text = f.read()
        # convert_path = filePath_text.split("'")
        # checkFile = convert_path[1].split('.')
        # if checkFile[1] == "docx" or checkFile[1] == "DOCX" or checkFile[1] == "doc" or checkFile[1] == "docx":
        #     convert(convert_path)
        #     convert(convert_path, "output.pdf")
        #     convert("/Users/macbook/Documents/python test/doc2image")

        # print(convert_path[1])
    pass
class PrintScreen(Screen):
    def switch_callback(self, switchObject, switchValue):
        # -------------------------------COLOR CHECK----------------------------------
        # Switch value are True and False
        if (switchValue):
            global data_color
            data_color = False
            print('SET UP IN COLOR MODE')
        else:
            data_color = True
            print('SET UP IN GRAYSCALE MODE')
        return data_color

    def print_service(self):
        global data_color, data_pageNum
        # -------------------------------PAGE NUMBER PROTECTION----------------------------------
        data_pageNum = self.ids.pageNum_input.text
        if(data_pageNum == ''):
            data_pageNum = 1
        else:
            data_pageNum = data_pageNum
        #-------------------------------READ PDF FILE PAGES NUM----------------------------------
        # -------------------------------PDF TO IMAGE AND SAVE----------------------------------
        inputArray = self.ids.pageNum_input.text
        last_array = []
        To_array = inputArray.split(",")
        page_counter = 0
        for i in To_array:
            if i.find("-") != -1:
                save_array = i.split("-")
                #---------------------------------Call printDev Function---------------------------------
                page_counter = printDev(int(save_array[0]), int(save_array[1]), page_counter, getDocumentName())
            else:
                # ---------------------------------Call printDev Function---------------------------------
                page_counter = printDev(int(i), int(i), page_counter, getDocumentName())

    def pageNum(self):
        #------------------------TEXT INPUT LIMIT---------------------------
        # if len(self.ids.pageNum_input.text) > 4:
        #    user_pNum = int(self.ids.pageNum_input.text)
        #    user_pNum = user_pNum / 10
        #    self.ids.pageNum_input.text = str(user_pNum)
        #
        pdf = PdfFileReader(open(getDocumentName(),'rb'))
        TotalPage = pdf.getNumPages()
        print("ALL PAGE'S NUMBER-", TotalPage)
        PageInputValue = self.ids.pageNum_input.text
        if PageInputValue != '':
            pattern = '0123456789,-'  #zuwshuurugduh temdegtuud
            StrCount = 0
            for i in range(len(PageInputValue)):
                if pattern.find(PageInputValue[i]) != -1:
                    StrCount += 1
            if (StrCount == len(PageInputValue)):
                if PageInputValue.find(',,') != -1 or PageInputValue.find('--') != -1 or PageInputValue.find(
                        ',-') != -1 or PageInputValue.find('-,') != -1:
                    self.ids.Error_comment.text = "ERROR: ,, or -- or ,- or -,"
                    self.ids.print_service.disabled = True
                    print("ERROR: ,, or -- or ,- or -,")
                elif PageInputValue.startswith(',') or PageInputValue.endswith(',') or PageInputValue.startswith(
                        '-') or PageInputValue.endswith('-'):
                    self.ids.print_service.disabled = True
                    self.ids.Error_comment.text = "ERROR: start or end"
                    print("ERROR: start or end")
                else:
                    max_page = re.findall('\d+', PageInputValue)
                    max_page = map(int, max_page)
                    max_page = max(max_page)
                    if (max_page <= TotalPage):
                        self.ids.Error_comment.text = ''
                        self.ids.print_service.disabled = False
                        print("NO ERROR")
                    else:
                        self.ids.print_service.disabled = True
                        self.ids.Error_comment.text = "limit is " + str(TotalPage)
                        print("limit is ", TotalPage)
            else:
                self.ids.print_service.disabled = True
                self.ids.Error_comment.text = "invalid page range, use e.g 1-5,8,11-13"
                print("invalid page range, use e.g 1-5,8,11-13")

        print(self.ids.pageNum_input.text)

    pass

class OnlineScreen(Screen):
    def register(self):
        # -------------------------------SEND REQUEST TO SERVER----------------------------------
        print('Entered Number by User:', self.ids.input.text)

    def chkUserNum(self):
        # -------------------------------USER CODE INPUT----------------------------------
        if len(self.ids.input.text) > 8:
            user_number = int(self.ids.input.text)
            user_number = user_number / 10
            self.ids.input.text = str(user_number)
        print(len(self.ids.input.text))
        print(self.ids.input.text)

    def clr_btn(self):
        self.ids.input.text = ''

    def delete_input(self):
        self.ids.input.text = self.ids.input.text[:-1]
    pass

class ScreenManagement(ScreenManager):
    pass

class textinp(Widget):

    pass
def getDocumentName():
    filename = 'ThePearl.PDF'
    return filename
#------------------------------------------FILE PRINTING FUNCTION---------------------------------
def printDev(pageNum_1, pageNum_2, counter, filename):
    save_dir = '/Users/macbook/Documents/python test/ScreenManager/save_image/'
    images_from_path = convert_from_path(getDocumentName(), 150, first_page=pageNum_1, last_page=pageNum_2,
                                         grayscale=data_color, size=None)
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    for tmp, page in enumerate(images_from_path):
        page.save(os.path.join(save_dir, base_filename + str(counter) + ".jpg"), 'JPEG')
        counter += 1

    return counter

global savePath_func

def savePath_func(save_path):
    if save_path != '0':
        print(save_path)
        file = open(UsrPathSaverTxtFile, "w+")
        file.write(save_path)
        file.close()
        return save_path

def SaveButtonChk(SaveData):
    if SaveData != True:
        file = open(UsrPathSaverTxtFile, "w+")
        file.write('')
        file.close()

with io.open("main.kv", encoding='utf8') as f:
    presentation = Builder.load_string(f.read())

if __name__ == '__main__':

    class MainApp(App):
        def build(self):
            return presentation

        def process(self, *args):
            tmp = self.root.ids.input.text
            print(tmp)



    MainApp().run()