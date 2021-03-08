import tkinter as tk
import numpy as np
import math
from ipynb.fs.full.main import checkFloat as checkFloat
from ipynb.fs.full.main import shortenFloat as shortenFloat
from ipynb.fs.full.main import checkInt as checkInt

class lever_MA_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Lever Mechanical Advantage").grid(row = 0, column = 1)
        tk.Label(self.master, text = "Length of Effort Arm").grid(row = 1, column = 0)
        tk.Label(self.master, text = "Length of Load Arm").grid(row = 2, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2 = tk.Entry(self.master)
        e2.grid(row = 2, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_lever_MA(e1.get(), e2.get())).grid(row = 3, column = 1)
        
    def calculate_lever_MA(self, effort, load):
        tk.Label(self.master, text = "", width = "20").grid(row = 4, column = 1)
        if(checkFloat(effort) and checkFloat(load)):
            ma = float(effort) / float(load)
            tk.Label(self.master, text = shortenFloat(ma, 5)).grid(row = 4, column = 1)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 4, column = 1)

class free_fall_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Free Fall:").grid(row = 0, column = 1)
        tk.Label(self.master, text = "Height").grid(row = 1, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_free_fall(e1.get())).grid(row = 2, column = 1)
    
    def calculate_free_fall(self, height):
        tk.Label(self.master, text = "", width = "15").grid(row = 3, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 3, column = 1)
        tk.Label(self.master, text = "", width = "15").grid(row = 3, column = 2)
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 2)
        if(checkFloat(height)):
            time = (2 * float(height) / 9.8)
            velocity = math.sqrt(2 * 9.8 * float(height))
            tk.Label(self.master, text = "Time Until Impact: ").grid(row = 3, column = 0)
            tk.Label(self.master, text = "Velocity at Impact: ").grid(row = 4, column = 0)
            tk.Label(self.master, text = str(shortenFloat(time, 5))).grid(row = 3, column = 2)
            tk.Label(self.master, text = str(shortenFloat(float(velocity), 5))).grid(row = 4, column = 2)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 3, column = 1)
            
        
class max_height_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Max Height of Object").grid(row = 0, column = 1)
        tk.Label(self.master, text = "Launch Velocity").grid(row = 1, column = 0)
        tk.Label(self.master, text = "Launch Angle").grid(row = 2, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2 = tk.Entry(self.master)
        e2.grid(row = 2, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_max_height(e1.get(), e2.get())).grid(row = 3, column = 1)
        
    def calculate_max_height(self, velocity, angle):
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 1)
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 2)
        if(checkFloat(velocity) and checkFloat(angle)):
            th = float(velocity) * math.sin(float(angle)) / 9.8
            height = (float(velocity) ** 2) * (math.sin(float(angle)) ** 2)/ (2 * 9.8)
            tk.Label(self.master, text = "Max Height: ").grid(row = 4, column = 0)
            tk.Label(self.master, text = height).grid(row = 4, column = 2)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 4, column = 1)

            
class normal_force_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Normal Force").grid(row = 0, column = 1)
        tk.Label(self.master, text = "Mass").grid(row = 1, column = 0)
        tk.Label(self.master, text = "Angle").grid(row = 2, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2 = tk.Entry(self.master)
        e2.grid(row = 2, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_normal_force(e1.get(), e2.get())).grid(row = 3, column = 1)
    
    def calculate_normal_force(self, mass, angle):
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 1)
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 2)
        
        if(checkFloat(mass) and checkFloat(angle)):
            if(float(angle) == 0.0 or angle == ""):
                normal = float(mass) * 9.8
            else:
                normal = float(mass) * 9.8 * math.cos(float(angle))
                
            tk.Label(self.master, text = "Normal Force").grid(row = 4, column = 0)
            tk.Label(self.master, text = shortenFloat(normal, 5)).grid(row = 4, column = 2)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 4, column = 1)
