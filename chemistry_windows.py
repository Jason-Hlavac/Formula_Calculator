import tkinter as tk
import numpy as np
import math
from ipynb.fs.full.main import checkFloat as checkFloat
from ipynb.fs.full.main import shortenFloat as shortenFloat
from ipynb.fs.full.main import checkInt as checkInt

#GRAMS TO MOLES CLASS
class grams_to_moles_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Grams to Moles").grid(row = 0, column = 1)
        tk.Label(self.master, text = "Molar Mass").grid(row = 1, column = 0)
        tk.Label(self.master, text = "Mass").grid(row = 2, column = 0)
        tk.Label(self.master, text = "Moles").grid(row = 3, column = 0)
        e1 = tk.Entry(self.master)
        e2 = tk.Entry(self.master)
        e3 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2.grid(row = 2, column = 2)
        e3.grid(row = 3, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_grams_to_moles(e1.get(), e2.get(), e3.get())).grid(row = 4, column = 1)
        
    def calculate_grams_to_moles(self, mm, mass, moles):
        tk.Label(self.master, text = "", width = "30").grid(row = 6, column = 1)
        tk.Label(self.master, text = "", width = "15").grid(row = 5, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 5, column = 2)
        if(mm == "" or not checkFloat(mm)):
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 4, column = 1)
        elif(checkFloat(mass)):
            moles = float(mass)/float(mm)
            tk.Label(self.master, text = "Moles: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = moles).grid(row = 5, column = 2)
        elif(checkFloat(moles)):
            mass = float(moles) * float(mm)
            tk.Label(self.master, text = "Mass: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = mass).grid(row = 5, column = 2)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 6, column = 1)
        
class molality_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Molality").grid(row = 0, column = 1)
        tk.Label(self.master, text = "Moles of Solute").grid(row = 1, column = 0)
        tk.Label(self.master, text = "Mass of Solvent").grid(row = 2, column = 0)
        tk.Label(self.master, text = "Molality").grid(row = 3, column = 0)
        e1 = tk.Entry(self.master)
        e2 = tk.Entry(self.master)
        e3 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2.grid(row = 2, column = 2)
        e3.grid(row = 3, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_molality(e1.get(), e2.get(), e3.get())).grid(row = 4, column = 1)
        
    def calculate_molality(self, moles, mass, molality):
        tk.Label(self.master, text = "", width = "30").grid(row = 6, column = 1)
        tk.Label(self.master, text = "", width = "15").grid(row = 5, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 5, column = 2)
        if(checkFloat(moles) and checkFloat(mass)):
            molality = float(moles)/ float(mass)
            tk.Label(self.master, text = "Molality: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = molality).grid(row = 5, column = 2)
        elif(checkFloat(moles) and checkFloat(molality)):
            mass = float(moles)/ float(molality)
            tk.Label(self.master, text = "Mass: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = mass).grid(row = 5, column = 2)
        elif(checkFloat(molality) and checkFloat(mass)):
            moles = float(mass) * float(molality)
            tk.Label(self.master, text = "Moles: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = moles).grid(row = 5, column = 2)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 6, column = 1)
            
class percent_yield_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Percent Yield:").grid(row = 0, column = 1)
        tk.Label(self.master, text = "Theoretical Yield").grid(row = 1, column = 0)
        tk.Label(self.master, text = "Actual Yield").grid(row = 2, column = 0)
        tk.Label(self.master, text = "Percent Yield").grid(row = 3, column = 0)
        e1 = tk.Entry(self.master)
        e2 = tk.Entry(self.master)
        e3 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2.grid(row = 2, column = 2)
        e3.grid(row = 3, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_percent_yield(e1.get(), e2.get(), e3.get())).grid(row = 4, column = 1)
        
    def calculate_percent_yield(self, theoretical, actual, percent):
        tk.Label(self.master, text = "", width = "30").grid(row = 6, column = 1)
        tk.Label(self.master, text = "", width = "15").grid(row = 5, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 5, column = 2)
        if(checkFloat(theoretical) and checkFloat(actual)):
            percent = (float(actual)/ float(theoretical)) * 100
            tk.Label(self.master, text = "Percent Yield: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = str(shortenFloat(percent, 5)) + "%").grid(row = 5, column = 2)
        elif(checkFloat(theoretical) and checkFloat(percent)):
            actual = float(theoretical) * (float(percent)/100)
            tk.Label(self.master, text = "Actual: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = actual).grid(row = 5, column = 2)
        elif(checkFloat(actual) and checkFloat(percent)):
            theoretical = float(actual) / (float(percent)/100)
            tk.Label(self.master, text = "Theoretical: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = theoretical).grid(row = 5, column = 2)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 6, column = 1)
            
            
class ppm_to_molarity_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "PPM To Molarity:").grid(row = 0, column = 1)
        tk.Label(self.master, text = "PPM").grid(row = 1, column = 0)
        tk.Label(self.master, text = "Molar Mass").grid(row = 2, column = 0)
        tk.Label(self.master, text = "Molarity").grid(row = 3, column = 0)
        e1 = tk.Entry(self.master)
        e2 = tk.Entry(self.master)
        e3 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2.grid(row = 2, column = 2)
        e3.grid(row = 3, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_ppm_to_molarity(e1.get(), e2.get(), e3.get())).grid(row = 4, column = 1)
        
    def calculate_ppm_to_molarity(self, ppm, mm, M):
        tk.Label(self.master, text = "", width = "30").grid(row = 6, column = 1)
        tk.Label(self.master, text = "", width = "15").grid(row = 5, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 5, column = 2)
        if(checkFloat(ppm) and checkFloat(mm)):
            M = (float(ppm)/1000)/ float(mm)
            tk.Label(self.master, text = "Molarity: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = shortenFloat(M, 6)).grid(row = 5, column = 2)
        elif(checkFloat(ppm) and checkFloat(M)):
            mm = (float(ppm)/1000) / float(M)
            tk.Label(self.master, text = "Molar Mass: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = shortenFloat(mm, 6)).grid(row = 5, column = 2)
        elif(checkFloat(mm) and checkFloat(M)):
            ppm = (float(mm) * float(M)) * 1000
            tk.Label(self.master, text = "PPM: ").grid(row = 5, column = 0)
            tk.Label(self.master, text = shortenFloat(ppm, 6)).grid(row = 5, column = 2)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 6, column = 1)   
