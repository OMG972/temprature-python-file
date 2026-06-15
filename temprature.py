from tkinter import *

ABS_ZERO_FAHRENHEIT = -459.67
ABS_ZERO_CELSUIS = -273.15

class TempratureConverter:
    
    def calculate_to_c(self, temp):
        try:
            temp = float(temp)
            if temp >= ABS_ZERO_FAHRENHEIT:
                result = (float(temp)-32) * 5 /9
                return f'{result:.1f} degrees Centigrade'
            else:
                return "Temprature to low"
        except ValueError:
            return("Please enter a number")
        
    def calculate_to_f(self, temp):
        try:
            temp = float(temp)
            if temp >= ABS_ZERO_CELSUIS:
                result = (float(temp * 9 /5) + 32) 
                return f'{result:.1f} degrees Fahrenhight'
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
        self.root.geometry("370x150")
        self.root.resizable(0,0)

        self.container = Frame(self.root)
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
        frame = Frame(self.container, padx=20, pady=20)
        frame.grid(row=0, column=0, sticky="nsew")

        lbl_title = Label(frame, text= "Temprature Converter", font=FONT_MAIN_TITLE)
        lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 25), sticky="ew")

        button1 = Button(frame, text="To Centigrade", bg= "yellow", font= FONT_HEADING, command=lambda: self.show_frame("to_cFrame"))
        button1.grid(row=1, column=0)

        button2 = Button(frame, text= "To Fahrenheigt", bg= "red", font= FONT_HEADING, command=lambda: self.show_frame("to_fFrame"))
        button2.grid(row=1, column=1)
        
        return frame
    
    def create_to_c_frame(self):
        frame = Frame(self.container, padx=20, pady=15)
        frame.grid(row=0, column=0, sticky="nsew")

        lbl2_title = Label(frame, text="Enter the temprature in Fahrenheit", font=FONT_HEADING)
        lbl2_title.grid(row=0, column=0, columnspan=3, pady=(0, 5), sticky="W")

        box1 = Entry(frame, justify=LEFT, font=FONT_DEFAULT)
        box1.grid(row=1, column=0, columnspan= 3, sticky= EW, pady=(0, 10))

        lbl_result = Label(frame, text="", font=FONT_DEFAULT, fg="blue")
        lbl_result.grid(row=2, column=0, columnspan= 3, pady=(0, 10))
        
        button3 = Button(frame, text="Calculate", font=FONT_DEFAULT, width= 10, command=lambda: lbl_result.configure(text=self.converter.calculate_to_c(box1.get())))
        button3.grid(row=3, column=0)

        button4 = Button(frame, text="Back", font=FONT_DEFAULT, width= 10, command=lambda: self.show_frame("MainFrame"))
        button4.grid(row=3, column=1)

        button5 = Button(frame, text="Reset", font=FONT_DEFAULT, width= 10, command=lambda: [box1.delete(0, END), lbl_result.configure(text="")])
        button5.grid(row=3, column=2)



        return frame

    def create_to_f_frame(self):
        frame = Frame(self.container, pady=20, padx=15)
        frame.grid(row=0, column=0, sticky="nsew")

        lbl3_title = Label(frame, text="Enter the temprature in Centigrade", font=FONT_HEADING)
        lbl3_title.grid(row=0, column=0, columnspan=3, pady=(0, 5), sticky="W")

        box2=Entry(frame, justify=LEFT, font=FONT_DEFAULT)
        box2.grid(row=1, column=0, columnspan= 3, sticky= EW, pady=(0, 10))

        lbl_result2 = Label(frame, text="", font=FONT_DEFAULT, fg="blue")
        lbl_result2.grid(row=2, column=0, columnspan= 3, pady=(0, 10))

        button6 = Button(frame, text="Calculate", font=FONT_DEFAULT, width= 10, command=lambda: lbl_result2.configure(text=self.converter.calculate_to_f(box2.get())))
        button6.grid(row=3, column=0)

        button7 = Button(frame, text="Back", font=FONT_DEFAULT, width= 10, command=lambda: self.show_frame("MainFrame"))
        button7.grid(row=3, column=1)

        button8 = Button(frame, text="Reset", font=FONT_DEFAULT, width= 10, command=lambda: [box2.delete(0, END), lbl_result2.configure(text="")])
        button8.grid(row=3, column=2)

        return frame

root = Tk()
app = ConvereterGUI(root)
root.mainloop()