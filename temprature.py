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
                return f'{result:.1f} degrees Fahrenhight'
            else:
                return "Temprature to low"
        except ValueError:
            return("Please enter a number")

FONT_MAIN_TITLE = "Verdana 16 bold"
FONT_HEADING = "Verdana 12 bold"
FONT_DEFAULT = "Verdana 12"
root=Tk()

class ConvereterGUI:

    def __init__(self, root):
        self.converter = TempratureConverter()

        self.root = root
        self.root.title("Temprature Converter")
        self.root.geometry("400x150")
        self.root.resizable(0,0)

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

    def create_main_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")

        lbl_title = Label(frame, text= "Temprature Converter", font=FONT_MAIN_TITLE)
        lbl_title.pack()

        button1 = Button(frame, text="To Centigrade", bg= "yellow", font= FONT_HEADING, command=lambda: self.show_frame("to cFrame"))
        button1.pack()

        button2 = Button(frame, text= "To Fahrenheigt", bg= "red", font= FONT_HEADING, command=lambda: self.show_frame("to fFrame"))
        button2.pack()
        
        return frame
    
    def create_to_c_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")

        lbl2_title = Label(frame, text="Enter the temprature in Fahrenheit", font=FONT_HEADING)
        lbl2_title()

        box1=Entry(root, justify=LEFT)
        box1.pack()

        button3 = Button(frame, text="Calculate", font=FONT_DEFAULT)
        button3.pack()

        button4 = Button(frame, text="Back", font=FONT_DEFAULT)
        button4.pack()

        button5 = Button(frame, text="Reset", font=FONT_DEFAULT)
        button5.pack()

    def create_to_f_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")

        lbl3_title = Label(frame, text="Enter the temprature in Centigrade", font=FONT_HEADING)
        lbl3_title()

        box2=Entry(root, justify=LEFT)
        box2.pack()

        button6 = Button(frame, text="Calculate", font=FONT_DEFAULT)
        button6.pack()

        button7 = Button(frame, text="Back", font=FONT_DEFAULT)
        button7.pack()

        button8 = Button(frame, text="Reset", font=FONT_DEFAULT)
        button8.pack()

root.mainloop()