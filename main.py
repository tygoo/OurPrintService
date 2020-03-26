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
from subprocess                 import call
from kivy.app                   import App
from kivy.lang                  import Builder
from kivy.uix.widget            import Widget
from kivy.core.window           import Window
from kivy.uix.screenmanager     import ScreenManager, Screen, FadeTransition
from kivy.lang                  import Builder
from kivy.utils                 import platform as core_platform
from kivy.uix.button            import ButtonBehavior
from kivy.uix.image             import Image
from kivy.core.audio            import SoundLoader
from kivy.clock import Clock
from datetime import datetime
from datetime import timedelta
import kivy.uix.filechooser
from kivy.uix.filechooser import *
from kivy.uix.carousel import Carousel
from kivy.uix.slider            import Slider
from kivy.graphics              import Rectangle, Color, RoundedRectangle, Ellipse
from functools                  import partial
from kivy.uix.button            import Button
from kivy.factory               import Factory
from kivy.properties            import ObjectProperty
from kivy.uix.popup             import Popup
from kivy.uix.anchorlayout      import AnchorLayout
from kivy.uix.gridlayout        import GridLayout
from kivy.uix.textinput         import TextInput
from kivy.uix.boxlayout         import BoxLayout
from kivy.uix.floatlayout       import FloatLayout
from pdf2image.pdf2image        import convert_from_path
from kivy.input.motionevent     import MotionEvent
_have_win32file     = False
PageChooserValue    = True
data_color          = "-color"
data_pageNum        = 1
save_value          = 0
Online_CntNum       = 0
Request_Value       = 0
# with io.open("Online.kv", encoding='utf8') as f:
#     Builder.load_string(f.read())
# with io.open("Offline.kv", encoding='utf8') as f:
#     Builder.load_string(f.read())
# with io.open("fileChooser.kv", encoding='utf8') as f:
#     Builder.load_string(f.read())
# with io.open("printOpt.kv", encoding='utf8') as f:
#     Builder.load_string(f.read())
Builder.load_file("Online.kv")
Builder.load_file("Offline.kv")
Builder.load_file("fileChooser.kv")
Builder.load_file("printOpt.kv")
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
platform = core_platform
filesize_units = ('B', 'KB', 'MB', 'GB', 'TB')
sys.path.insert(0, '/Users/macbook/Documents/python test/ScreenManager/docx2pdf-master2/docx2pdf/__init__.py')
sys.path.insert(0, "/Users/macbook/python test/lib/python2.7/site-packages/kivy/uix/fileChooser.py")
Window.clearcolor = (0.95,0.95,0.95,1)
checkerVariable = ['.DS_Store']
class MainScreen(Screen):
    def soundMain(self):
        Sound()

    def pointTouch(self):
        if self.ids.touchLabel.opacity == 1:
            self.ids.touchLabel.opacity = 0
        else:
            self.ids.touchLabel.opacity = 1
    pass
class ImageButton(ButtonBehavior, Image):
    pass
class OfflineScreen(Screen):
    def refresh(self):
        self.ids.filechooser._update_files()
    def chkDev(self, Send_path):
        print(Send_path)
        Sound()
        global save_path1, k
        flash_path = '/Users/macbook/Documents/python test/ScreenManager/FLASH'
        files = os.listdir(flash_path)
        print("ohh" ,files)
        if files != checkerVariable:
            if Send_path != []:
                self.ids.WarningText.text = "DO YOU CONTINUE?"
                self.ids.btn1.opacity = 1
                self.ids.btn2.opacity = 1
                self.ids.btn1.disabled = False
                self.ids.btn2.disabled = False
                self.ids.opLbl_true.opacity = 0
                self.ids.opLbl_false.opacity = 0
                self.ids.opLbl_true.opacity = 1
                self.ids.opLbl_false.opacity = 1
            else:
                self.ids.WarningText.text = "PLEASE CHOOSE YOUR FILE!"
        else:
            self.ids.WarningText.text = "PLEASE ENTER YOUR DEVICE!"

    def del1(self):
        Sound()
        self.ids.WarningText.text = "PLEASE ENTER YOUR DEVICE"
        self.ids.btn1.opacity = 0
        self.ids.btn2.opacity = 0
        self.ids.btn1.disabled = True
        self.ids.btn2.disabled = True
        self.ids.opLbl_true.opacity = 0
        self.ids.opLbl_false.opacity = 0

    def checkStr(self, Chkstr):
        print(Chkstr)
        if Chkstr != []:
            DataString = str(Chkstr).split(".")
            DataString = DataString[1].split("'")
            if DataString[0] == 'pdf' or DataString[0] == 'PDF' or DataString[0] == 'DOC' or DataString[0] == 'DOCX' or \
                    DataString[0] == 'doc' or DataString[0] == 'docx' or \
                    DataString[0] == 'XLS' or DataString[0] == 'xls' or DataString[0] == 'TXT' or DataString[0] == 'txt':
                self.ids.save.disabled = False
                print(Chkstr)
            else:
                self.ids.save.disabled = True
            print(DataString[0])
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
#----------------------------------------------------PRINT PAGE---------------------------------------------
class PrintScreen(Screen):
    kb_x = 0
    kb_y = 0
    def print_service(self):
        global data_color, data_pageNum, PageChooserValue
        pdf = PdfFileReader(open(getDocumentName(), 'rb'))
        TotalPage = pdf.getNumPages()
        # -------------------------------PAGE NUMBER PROTECTION----------------------------------
        if PageChooserValue is False:
            data_pageNum = self.ids.pageNum_input.text
            if(data_pageNum == ''):
                data_pageNum = '1' + '-' + str(TotalPage)
            else:
                data_pageNum = data_pageNum
        else:
            pdf = PdfFileReader(open(getDocumentName(), 'rb'))
            TotalPage = pdf.getNumPages()
            data_pageNum = '1' + '-' + str(TotalPage)
        #-------------------------------READ PDF FILE PAGES NUM----------------------------------
        # -------------------------------PDF SAVE----------------------------------
        inputArray = data_pageNum
        To_array = inputArray.split(",")
        page_counter = 0
        for i in To_array:
            if i.find("-") != -1:
                save_array = i.split("-")
                print(save_array)
                #---------------------------------Call printDev Function---------------------------------
                # page_counter = printDev(int(save_array[0]), int(save_array[1]), page_counter, getDocumentName())
            else:
                # ---------------------------------Call printDev Function---------------------------------
                # page_counter = printDev(int(i), int(i), page_counter, getDocumentName())
                print(int(i))

    def pageNum(self):
        #------------------------TEXT INPUT LIMIT---------------------------
        pdf = PdfFileReader(open(getDocumentName(),'rb'))
        TotalPage = pdf.getNumPages()
        # print("ALL PAGE'S NUMBER-", TotalPage)
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

    def sliderFunc(self, value):
        max_value = 4
        ConvertedImages = "/Users/macbook/Documents/python test/ScreenManager/ConvertedImage/Image"
        if self.ids.slider.range == [1, max_value]:
            if self.ids.slider.value + value <= max_value:
                self.ids.slider.value += value
                self.ids.slider_text.text = str(int(self.ids.slider.value))
                self.ids.imageView.source = ConvertedImages + str(int(self.ids.slider.value)) + ".png"
        else:
            self.ids.slider.range = (1, max_value)

    def pageValue(self, selected_value):
        global PageChooserValue
        PageChooserValue = selected_value
        if PageChooserValue == True:
            self.ids.print_service.disabled = False
        # print("All or Custom", PageChooserValue)

    def Copies_Num(self, value):
        copyNum = int(self.ids.copies_input.text)
        if copyNum + value >= 1 and copyNum + value < 100:
            copyNum += value
        else:
            copyNum = copyNum
        self.ids.copies_input.text = str(copyNum)
        print(self.ids.copies_input.text)

    def ColorChoose(self, Selected_value):
        if Selected_value is False:
            global data_color
            data_color = "-gray"
            # print('SET UP IN GRAYSCALE MODE')
        else:
            data_color = "-color"
            # print('SET UP IN COLOR MODE'

    def pageNum_input_del(self):
        self.ids.pageNum_input.text = self.ids.pageNum_input.text[:-1]

    pass

class OnlineScreen(Screen):
    def register(self):
        # -------------------------------SEND REQUEST TO SERVER----------------------------------
        global Request_Value
        Sound()
        print('Entered Number by User:', self.ids.input.text)
        # self.ids.Error_comment.text = "Please wait for a few second"
        Request_Value = "asdfg12345"
        if (self.ids.input.text == Request_Value):
            self.ids.Error_comment.text = "Correct"
            self.parent.current = "printOpt"
        elif len(self.ids.input.text) < 10:
            self.ids.Error_comment.text = "Please enter your code"
        elif (self.ids.input.text != Request_Value and len(self.ids.input.text) == 10):
            self.ids.Error_comment.text = "Incorrect. Please check your code!"
        else:
            self.ids.Error_comment.text = " "


    def chkUserNum(self):
        global Online_CntNum
        # -------------------------------USER CODE INPUT----------------------------------
        Sound()
        if len(self.ids.input.text) > 10:
            self.ids.input.text = self.ids.input.text[:-1]
        if len(self.ids.input.text) == 10:
            self.ids.Error_comment.text = "Are you sure?"
        print(len(self.ids.input.text))
        print(self.ids.input.text)

    def clr_btn(self):
        Sound()
        self.ids.input.text = ''

    def delete_input(self):
        self.ids.input.text = self.ids.input.text[:-1]

    def btn_one_clk(self):
        global Online_CntNum
        Online_CntNum += 1
        Online_CntNum = Online_CntNum % 2
        if (Online_CntNum != 0):
            self.ids.bq.text = 'Q'
            self.ids.bw.text = 'W'
            self.ids.be.text = 'E'
            self.ids.br.text = 'R'
            self.ids.bt.text = 'T'
            self.ids.by.text = 'Y'
            self.ids.bu.text = 'U'
            self.ids.bi.text = 'I'
            self.ids.bo.text = 'O'
            self.ids.bp.text = 'P'
            self.ids.ba.text = 'A'
            self.ids.bs.text = 'S'
            self.ids.bd.text = 'D'
            self.ids.bf.text = 'F'
            self.ids.bg.text = 'G'
            self.ids.bh.text = 'H'
            self.ids.bj.text = 'J'
            self.ids.bk.text = 'K'
            self.ids.bl.text = 'L'
            self.ids.bz.text = 'Z'
            self.ids.bx.text = 'X'
            self.ids.bc.text = 'C'
            self.ids.bv.text = 'V'
            self.ids.bb.text = 'B'
            self.ids.bn.text = 'N'
            self.ids.bm.text = 'M'
        else:
            self.ids.bq.text = 'q'
            self.ids.bw.text = 'w'
            self.ids.be.text = 'e'
            self.ids.br.text = 'r'
            self.ids.bt.text = 't'
            self.ids.by.text = 'y'
            self.ids.bu.text = 'u'
            self.ids.bi.text = 'i'
            self.ids.bo.text = 'o'
            self.ids.bp.text = 'p'
            self.ids.ba.text = 'a'
            self.ids.bs.text = 's'
            self.ids.bd.text = 'd'
            self.ids.bf.text = 'f'
            self.ids.bg.text = 'g'
            self.ids.bh.text = 'h'
            self.ids.bj.text = 'j'
            self.ids.bk.text = 'k'
            self.ids.bl.text = 'l'
            self.ids.bz.text = 'z'
            self.ids.bx.text = 'x'
            self.ids.bc.text = 'c'
            self.ids.bv.text = 'v'
            self.ids.bb.text = 'b'
            self.ids.bn.text = 'n'
            self.ids.bm.text = 'm'

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

def Sound():
    sound = SoundLoader.load('click.mp3')
    #sound.play()

presentation = Builder.load_file("main.kv")

if __name__ == '__main__':

    class MainApp(App):
        def build(self):
            return presentation

        def process(self, *args):
            tmp = self.root.ids.input.text
            print(tmp)



    MainApp().run()