import tkinter as tk
import numpy as np
import math
from ipynb.fs.full.main import checkFloat as checkFloat
from ipynb.fs.full.main import shortenFloat as shortenFloat
from ipynb.fs.full.main import checkInt as checkInt

#FRACTION TO PERCENT CLASS
class fraction_to_percent_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Fraction to Percent").grid(row = 0, column = 3)
        tk.Label(self.master, text = "Numerator").grid(row = 1, column = 2)
        tk.Label(self.master, text = "Denominator").grid(row = 2, column = 2)
        e1 = tk.Entry(self.master)
        e2 = tk.Entry(self.master)
        e1.grid(row = 1, column = 4)
        e2.grid(row = 2, column = 4)
        tk.Label(self.master, text = "Percent: ").grid(row = 4, column = 2)
        calculate = tk.Button(self.master, text = "Calculate", command = lambda: self.get_percent(e1, e2))
        calculate.grid(row = 3, column = 3)
        
    def get_percent(self, e1, e2):
        tk.Label(self.master, text = "", width = "30").grid(row = 4, column = 4)
        tk.Label(self.master, text = "", width = "30").grid(row = 5, column = 3)
        if(checkFloat(e1.get()) and checkFloat(e2.get())):
            result = str(float(e1.get())/float(e2.get()) *100.0) + "%"
            result = shortenFloat(result, 5)
            tk.Label(self.master, text = result).grid(row = 4, column = 4)

        else:
            tk.Label(self.master, text = "Only Numbers Allowed").grid(row = 5, column = 3)
        
    
#DOUBLING TIME CLASS
class doubling_time_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Doubling Time").grid(row = 0, column = 2)
        tk.Label(self.master, text = "% Increase per Period: ").grid(row = 1, column = 1)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 3)
        calculate = tk.Button(self.master, text = "Calculate", command = lambda: self.get_doubling_time(e1))
        calculate.grid(row = 2, column = 2)
        tk.Label(self.master, text = "Result: ").grid(row = 3, column = 1)
    def get_doubling_time(self, e1):
        tk.Label(self.master, text = "", width = "30").grid(row = 4, column = 2)
        tk.Label(self.master, text = "", width = "30").grid(row = 3, column = 2)
        if(checkFloat(e1.get())):
            if(float(e1.get()) == 0 ):
                tk.Label(self.master, text = "Infinity").grid(row = 3, column = 2)
                return
            result = float(np.log(2.0)) / float(np.log(1.0 + (float(e1.get())/100.0)))
            result = shortenFloat(result, 5)
            tk.Label(self.master, text = result).grid(row = 3, column = 2)
        else:
            tk.Label(self.master, text = "Only Numbers Allowed").grid(row = 4, column = 2)
            
#DICE ROLL CLASS
class dice_roll_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Dice Roll Probability").grid(row = 0, column = 2)
        tk.Label(self.master, text = "Sides on the dice").grid(row = 1, column = 1)
        tk.Label(self.master, text = "Number of Rolls").grid(row = 2, column = 1)
        tk.Label(self.master, text = "Number of repeats").grid(row = 3, column = 1)
        tk.Label(self.master, text = "Operation type").grid(row = 4, column = 1)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 3)
        e2 = tk.Entry(self.master)
        e2.grid(row = 2, column = 3)
        e3 = tk.Entry(self.master)
        e3.grid(row = 3, column = 3)
        var = tk.StringVar(master)
        var.set("=")
        self.result = "="
        dropdown = tk.OptionMenu(self.master, var, "=", ">=", "<=", "!=", command = self.callback)
        dropdown.grid(row = 4, column = 3)
        tk.Label(self.master, text = "Result:").grid(row = 5, column = 1)
        calculate = tk.Button(self.master, text = "Calculate", command = lambda: self.get_dice_roll(e1.get(), e2.get(), self.result, e3.get()))
        calculate.grid(row = 4, column = 2)
    def callback(self, selection):
        self.result = selection
    def get_dice_roll(self, sides, times, operation, repeat):
        tk.Label(self.master, text = "", width = "30").grid(row = 6, column = 2)
        tk.Label(self.master, text = "", width = "30").grid(row = 5, column = 2)
        if(checkInt(sides) and checkInt(times) and checkInt(repeat)):
            if(int(sides) < 4):
                tk.Label(self.master, text = "Sides must be greater than 3").grid(row = 6, column = 2)
                return
            if(int(times) == 0 or int(repeat)> int(times) or int(repeat) < 0):
                tk.Label(self.master, text = "0").grid(row = 5, column = 2)
                return
            sides = int(sides)
            times = int(times)
            repeat = int(repeat)
            if(operation == "="):
                rvalue = choose(times, repeat) * ((1/sides) ** repeat) * ((1- (1/sides))** (times-repeat))
            elif(operation == ">="):
                rvalue = 0
                for i in range(int(repeat) , int(times) +1):
                    rvalue += choose(times, i) * ((1/sides) ** i) * ((1- (1/sides))** (times-i))

            elif(operation == "<="):
                rvalue = 0
                for i in range(0, int(repeat)):
                    rvalue += choose(times, i) * ((1/sides) ** i) * ((1- (1/sides))** (times-i))
            elif(operation == "!="):
                rvalue = choose(times, repeat) * ((1/sides) ** repeat) * ((1- (1/sides))** (times-repeat))
                rvalue = 1.0 - rvalue
            else:
                tk.Label(self.master, text = "Select Value from Dropdown").grid(row = 6, column = 2)
                return
            tk.Label(self.master, text = rvalue).grid(row = 5, column = 2)
        else:
            tk.Label(self.master, text = "Sides and Times must be integers").grid(row = 6, column = 2)
            return

class combinations_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Combinations").grid(row = 0 ,column = 1)
        tk.Label(self.master, text = "Population Size").grid(row = 1, column = 0)
        tk.Label(self.master, text = "Sample Size").grid(row = 2, column = 0)
        tk.Label(self.master, text = "Result: ").grid(row = 4, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2 = tk.Entry(self.master)
        e2.grid(row = 2, column = 2)
        calculate = tk.Button(self.master, text = "Calculate", command = lambda: self.get_combinations(e1.get(), e2.get()))
    
    def get_combinations(self, n, k):
        tk.Label(self.master, text = "", width = "30").grid(row = 4, column = 2)
        if(checkFloat(n) and checkFloat(k)):
            result = choose(n, k)
            tk.Label(self.master, text = result).grid(row = 4, column = 2)
        else:
            tk.Label(self.master, text = "Only Numbers Allowed").grid(row = 4, column = 2)
def choose(n, k):
    return (math.factorial(int(n))) / ((math.factorial(int(n) - int(k))) * math.factorial(int(k)))
