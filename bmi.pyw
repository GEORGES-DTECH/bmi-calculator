from tkinter import *


class Bmi:

    def __init__(self, root):
        root.title('BODY MASS INDEX CALCULATOR (B.M.I)')
        root.geometry('1150x650+0+0')
        root.config(background='#037bfc')
        title_lable = Label(root, text='METRIC FORMULA', font='arial 13 bold')
        title_lable.grid(row=0, column=0)
        root.iconbitmap('C:/Users/user/Desktop/bmi/bmi.ico ')

        # =====================================VARIABLES============================================#
        # ===metric bmi calculation variables======#
        self.weightkg = DoubleVar()
        self.heightm = DoubleVar()
        self.bmimetric = DoubleVar()

        # ===imperial  bmi calculation variables======#

        self.weightpds = DoubleVar()
        self.heightinches = DoubleVar()
        self.bmiimperial = DoubleVar()

        # ===converter weight variables===#
        self.weightinpd = DoubleVar()
        self.weightinkg = DoubleVar()

        # ===converter height variables===#
        self.foot = DoubleVar()
        self.inches = DoubleVar()
        self.inchesonly = DoubleVar()

        self.heightmtrs = DoubleVar()
        # =============================BMI METRIC FORMULA SECTION==========================#

        WEIGHT_IN_KG = Label(root, text="WEIGHT IN KG", font='bold')
        WEIGHT_IN_KG.grid(row=2, column=0, pady=10)

        WEIGHT_IN_KG_ENTRY = Entry(root, font='arial 13 bold', bd=5, textvariable=self.weightkg)
        WEIGHT_IN_KG_ENTRY.grid(row=2, column=1)

        HEIGHT_IN_METRES = Label(root, text="HEIGHT IN METERS", font='bold')
        HEIGHT_IN_METRES.grid(row=3, column=0, pady=10)

        HEIGHT_IN_METRES_ENTRY = Entry(root, font='arial 13 bold', bd=5, textvariable=self.heightm)
        HEIGHT_IN_METRES_ENTRY.grid(row=3, column=1)

        BMI = Label(root, text="YOUR BMI", font='bold')
        BMI.grid(row=4, column=0, pady=10)

        BMI_ENTRY = Entry(root, font='arial 13 bold', bd=5, textvariable=self.bmimetric)
        BMI_ENTRY.grid(row=4, column=1)
        # ========================CONVERTER SECTION==========================================#
        CONVERTER = Label(root, text="WEIGHT CONVERTER", font='arial 13 bold')
        CONVERTER.grid(row=6, column=0, pady=10)

        WEIGHT_IN_POUNDS = Label(root, text="WEIGHT IN POUNDS", font=' bold')
        WEIGHT_IN_POUNDS.grid(row=7, column=0, pady=8)

        WEIGHT_IN_POUNDS_ENTRY = Entry(root, font='arial 13 bold', bd=5, textvariable=self.weightinpd)
        WEIGHT_IN_POUNDS_ENTRY.grid(row=7, column=1, padx=5)

        WEIGHT_IN_KG_LABLE = Label(root, text="WEIGHT IN KG", font=' bold')
        WEIGHT_IN_KG_LABLE.grid(row=8, column=0, pady=8)

        WEIGHT_IN_KG_CONVERT = Entry(root, font='arial 13 bold', bd=5, textvariable=self.weightinkg)
        WEIGHT_IN_KG_CONVERT.grid(row=8, column=1, padx=5)

        # ===========================HEIGHT CONVERTER=====================================#
        HEIGHT_CONVERTER = Label(root, text="HEIGHT CONVERTER", font='arial 13 bold')
        HEIGHT_CONVERTER.grid(row=10, column=1, pady=10)

        HEIGHT = Label(root, text="HEIGHT IN FOOT", font=' bold', width=20)
        HEIGHT.grid(row=11, column=0, pady=5)

        HEIGHT_IN_FOOT = Entry(root, font='arial 13 bold', bd=5, width=10, textvariable=self.foot)
        HEIGHT_IN_FOOT.grid(row=11, column=1)

        HEIGHT_INCHES = Label(root, text="HEIGHT IN INCHES", font=' bold', width=20)
        HEIGHT_INCHES.grid(row=11, column=2, pady=5)

        HEIGHT_IN_INCHES = Entry(root, font='arial 13 bold', bd=5, width=10, textvariable=self.inches)
        HEIGHT_IN_INCHES.grid(row=11, column=3)

        HEIGHT_INCHESONLY_LABLE = Label(root, text="HEIGHT IN INCHES ONLY", font=' bold', width=20)
        HEIGHT_INCHESONLY_LABLE.grid(row=12, column=0, pady=9)

        HEIGHT_IN_INCHESONLY = Entry(root, font='arial 13 bold', bd=5, textvariable=self.inchesonly)
        HEIGHT_IN_INCHESONLY.grid(row=12, column=1)

        HEIGHT_METERS_LABLE = Label(root, text="HEIGHT IN METERS", font=' bold', width=20)
        HEIGHT_METERS_LABLE.grid(row=13, column=0, pady=9)

        HEIGHT_IN_METERS = Entry(root, font='arial 13 bold', bd=5, textvariable=self.heightmtrs)
        HEIGHT_IN_METERS.grid(row=13, column=1)
        # ================================IMPERIAL FORMULA==========================================#
        imperial_lable = Label(root, text='IMPERIAL FORMULA', font='arial 13 bold')
        imperial_lable.grid(row=0, column=4)

        Weight_pounds = Label(root, text="WEIGHT IN PDS", font='bold')
        Weight_pounds.grid(row=1, column=4)

        weight_pounds_entry = Entry(root, font='arial 13 bold', bd=5, textvariable=self.weightpds)
        weight_pounds_entry.grid(row=1, column=5)

        height_inches = Label(root, text="HEIGHT IN INCHES ONLY", font='bold')
        height_inches.grid(row=2, column=4, pady=10)

        height_inches_entry = Entry(root, font='arial 13 bold', bd=5, textvariable=self.heightinches)
        height_inches_entry.grid(row=2, column=5)

        bmi = Label(root, text="YOUR BMI", font='bold')
        bmi.grid(row=3, column=4, pady=10)

        bmi_entry = Entry(root, font='arial 13 bold', bd=5, textvariable=self.bmiimperial)
        bmi_entry.grid(row=3, column=5)
        # ===========================analysis=============================#
        self.analysis = Label(root, text='BMI ANALYSIS', font='helvetica 13 bold').grid(row=5, column=4, pady=5)
        self.underweight = Label(root, text='Underweight= BMI<18.5', font='arial 13 bold').grid(row=6, column=4)
        self.normalweight = Label(root, text='Normal weight= BMI 18.5 to 24.9', font='arial 13 bold').grid(row=7,
                                                                                                           column=4)
        self.overweight = Label(root, text='Over weight= BMI 25 to 29.9', font='arial 13 bold').grid(row=8, column=4)
        self.obese = Label(root, text='Obese=BMI of 30 or greater', font='arial 13 bold').grid(row=9, column=4)

        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command( label="A mascular person ,who is generally healthy may show bmi that reads overweight since muscle is weighs more than fat.")
           
        menubar.add_cascade(label="BMI LIMITATION", menu=filemenu)
        root.config(menu=menubar)

        #         =========================buttons===================================================#
        CONVERT_BUTTON = Button(root, text='CONVERT WEIGHT', bd=5, relief=RAISED, command=self.convertweight)
        CONVERT_BUTTON.grid(row=9, column=1, pady=5)

        BMI_BUTTON = Button(root, text='CALCULATE BMI', bd=5, relief=RAISED, command=self.metricformula)
        BMI_BUTTON.grid(row=5, column=1, pady=5)

        bmi_button = Button(root, text='CALCULATE BMI', bd=5, relief=RAISED, command=self.imperialformula)
        bmi_button.grid(row=4, column=5, pady=5)

        CONVERT_HEIGHT_BUTTON = Button(root, text='CONVERT HEIGHT', bd=5, relief=RAISED, command=self.convertheight)
        CONVERT_HEIGHT_BUTTON.grid(row=14, column=1, pady=5)

        RESET_BUTTON = Button(root, text='RESET VALUES', bd=5, relief=RAISED, command=self.reset)
        RESET_BUTTON.grid(row=14, column=0, pady=5)

        # ============================functionality======================================================================#

    def metricformula(self):
        height = self.heightm.get() ** 2
        metricbmi = round(self.weightkg.get() / height, 2)
        self.bmimetric.set(metricbmi)

    def imperialformula(self):
        height = self.heightinches.get() ** 2
        imperialbmi = round(703 * self.weightpds.get() / height, 2)
        self.bmiimperial.set(imperialbmi)

    def convertweight(self):
        if self.weightinkg.get() > 1:
            convertedweight = round(self.weightinkg.get() * 2.20462, 1)
            self.weightinpd.set(convertedweight)
        else:
            convertedkgweight = round(self.weightinpd.get() / 2.20462, 1)
            self.weightinkg.set(convertedkgweight)

    def convertheight(self):
        heightinches = self.foot.get() * 12 + self.inches.get()
        self.inchesonly.set(heightinches)
        heightmeters = round(heightinches / 39.3701, 1)
        self.heightmtrs.set(heightmeters)

    def reset(self):
        self.weightkg.set('')
        self.heightm.set('')
        self.bmimetric.set('')
        self.weightpds.set('')
        self.heightinches.set('')
        self.bmiimperial.set('')
        self.weightinpd.set(0)
        self.weightinkg.set(0)
        self.foot.set(0)
        self.inches.set(0)
        self.inchesonly.set(0)

        self.heightmtrs.set(0)


root = Tk()
b = Bmi(root)
root.mainloop()
