from tkinter import *

ABS_ZERO_FAHRENHEIT = -459.67
ABS_ZERO_CELSUIS = 273.15

class TempratureConverter:
    
    def calculate_to_c(self, temp):
        temp = float(temp)
        try:
            if temp >= ABS_ZERO_FAHRENHEIT:
                result = (float(temp)-32) * 5 /9
                return f'{result:.1f} degrees Centigrade'
            else:
                return "Temprature to low"
        except ValueError:
            return("Please enter a number")
        
    def calculate_to_f(self, temp):
        temp = float(temp)
        try:
            if temp >= ABS_ZERO_CELSUIS:
                result = (float(temp)-32) * 5 /9
                return f'{result:.1f} degrees Centigrade'
            else:
                return "Temprature to low"
        except ValueError:
            return("Please enter a number")

FONT_MAIN_TITLE = "Verdana 16 bold"
FONT_HEADING = "Verdana 12 bold"
FONT_DEFAULT = "Verdana 12"

class ConvereterGUI:

    def __init__(self, root):
        self.converter = TempratureConverter()

        self.root = root
        self.root.title("Temprature Converter")
        self.root.geometry("400x150")

        self.container = Frame(self, root)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()

        self.show_frame("MainFrame")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()