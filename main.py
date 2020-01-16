import kivy
#kivy.require("1.11.0")
from subprocess import call
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.utils import platform as core_platform
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
import os
import string
import requests
import time
import sys
import os
import subprocess
from PyPDF2 import PdfFileReader
import tempfile
from pdf2image import convert_from_path
platform = core_platform
filesize_units = ('B', 'KB', 'MB', 'GB', 'TB')
_have_win32file = False
Window.clearcolor = (0.95,0.95,0.95,1)
Builder.load_file("Online.kv")
Builder.load_file("Offline.kv")
Builder.load_file("fileChooser.kv")
Builder.load_file("printOpt.kv")
data_color = False
data_pageNum = 1
import fileChooser
from fileChooser import *

class MainScreen(Screen):
    pass

class OfflineScreen(Screen):
    def chkDev(self):
        call(["python", "fileChooser.py"])
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
        #---------------------------------CREATE PAGE NUMBER ARRAY FROM INPUT TEXT------------------------
        #inputArray = self.ids.pageNum_input.text
        #last_array = []
        #To_array = inputArray.split(",")
        #for i in To_array:
            #if i.find("-") != -1:
              #  save_array = i.split("-")
             #   for t in range(int(save_array[0]), int(save_array[1]) + 1):
             #       last_array.append(t)
            #else:
            #    last_array.append(int(i))

        #print(last_array)
        # -------------------------------PAGE NUMBER PROTECTION----------------------------------
        data_pageNum = self.ids.pageNum_input.text
        if(data_pageNum == ''):
            data_pageNum = 1
        else:
            data_pageNum = int(data_pageNum)
        #-------------------------------READ PDF FILE PAGES NUM----------------------------------
        filename = 'Mongolian.PDF'
        pdf = PdfFileReader(open(filename,'rb'))
        allPageNum = pdf.getNumPages()
        print("ALL PAGE'S NUMBER-", allPageNum)

        # -------------------------------PDF TO IMAGE AND SAVE----------------------------------

        images_from_path = convert_from_path(filename, 150, first_page=1, last_page=data_pageNum, grayscale=data_color, size=None)
        print(images_from_path)
        base_filename = os.path.splitext(os.path.basename(filename))[0]

        save_dir = '/Users/macbook/Documents/python test/ScreenManager/save_image/'

        for i, page in enumerate(images_from_path):
            page.save(os.path.join(save_dir, base_filename  + str(i) + ".jpg"), 'JPEG')

        #for i, image in enumerate(images_from_path):
            #fname = "/Users/macbook/Documents/python test/ScreenManager/save_image/image" + str(i) + ".jpg"
            #image.save(fname, "JPEG")
        convertName = filename.split(".")
        printFile_path = '/Users/macbook/Documents/python test/ScreenManager/save_image/' + convertName[0] + '0' +'.' + 'jpg'
        print(printFile_path)
        subprocess.Popen(["open", printFile_path])

    def pageNum(self):
        #------------------------TEXT INPUT LIMIT---------------------------
        if len(self.ids.pageNum_input.text) > 4:
           user_pNum = int(self.ids.pageNum_input.text)
           user_pNum = user_pNum / 10
           self.ids.pageNum_input.text = str(user_pNum)

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

presentation = Builder.load_file("main.kv")

if __name__ == '__main__':

    class MainApp(App):
        def build(self):
            return presentation

        def process(self, *args):
            tmp = self.root.ids.input.text
            print(tmp)

    MainApp().run()