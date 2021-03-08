import tkinter as tk
import numpy as np
import math
from ipynb.fs.full.main import checkFloat as checkFloat
from ipynb.fs.full.main import shortenFloat as shortenFloat
from ipynb.fs.full.main import checkInt as checkInt

class pythagorean_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Pythagorean Theorem").grid(row = 0, column = 1)
        tk.Label(self.master, text = "a:").grid(row = 1, column = 0)
        tk.Label(self.master, text = "b:").grid(row = 2, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2 = tk.Entry(self.master)
        e2.grid(row = 2, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_pythagorean(e1.get(), e2.get())).grid(row = 3, column = 1)
    
    def calculate_pythagorean(self, a, b):
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 0)
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 1)
        tk.Label(self.master, text = "", width = "15").grid(row = 4, column = 2)
        if(checkFloat(a) and checkFloat(b)):
            c = math.sqrt(((float(a) ** 2) + (float(b) ** 2)))
            tk.Label(self.master, text = "c:").grid(row = 4, column = 0)
            tk.Label(self.master, text = c).grid(row = 4, column = 2)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 4, column = 1)
            
class distance_between_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Distance Between Points").grid(row = 0, column = 1)
        tk.Label(self.master, text = "x1:").grid(row = 1, column = 0)
        tk.Label(self.master, text = "y1:").grid(row = 2, column = 0)
        tk.Label(self.master, text = "x2:").grid(row = 3, column = 0)
        tk.Label(self.master, text = "y2:").grid(row = 4, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        e2 = tk.Entry(self.master)
        e2.grid(row = 2, column = 2)
        e3 = tk.Entry(self.master)
        e3.grid(row = 3, column = 2)
        e4 = tk.Entry(self.master)
        e4.grid(row = 4, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_distance_between(e1.get(), e2.get(), e3.get(),e4.get())).grid(row = 5, column = 1)
        
    def calculate_distance_between(self, x1, y1, x2, y2):
        tk.Label(self.master, text = "", width = "20").grid(row = 6, column = 1)
        if(checkFloat(x1) and checkFloat(y1) and checkFloat(x2) and checkFloat(y2)):
            x1 , y1, x2,y2 = float(x1), float(y1), float(x2), float(y2)
            distance = abs(math.sqrt( ((x2 - x1) ** 2)+ ((y2 - y1) ** 2)))
            tk.Label(self.master, text = str(shortenFloat(distance, 6))).grid(row = 6, column = 1)
        else:
            tk.Label(self.master, text = "Enter Valid Values").grid(row = 6, column = 1)
    
    
class sphere_volume_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Sphere Volume").grid(row = 0, column = 1)
        tk.Label(self.master, text = "r:").grid(row = 1, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_sphere_volume(e1.get())).grid(row = 2, column = 1)
    
    def calculate_sphere_volume(self, r):
        tk.Label(self.master, text = "", width = "20").grid(row = 3, column = 1)
        if(checkFloat(r)):
            volume = (4/3) * math.pi * (float(r) ** 3)
            tk.Label(self.master, text = str(shortenFloat(volume, 8))).grid(row = 3, column = 1)
        else:
            tk.Label(self.master, text = "Enter Valid Value").grid(row = 3, column = 1)

class cube_area_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        tk.Label(self.master, text = "Cube Surface Area").grid(row = 0, column = 1)
        tk.Label(self.master, text = "Side Length:").grid(row = 1, column = 0)
        e1 = tk.Entry(self.master)
        e1.grid(row = 1, column = 2)
        tk.Button(self.master, text = "calculate", command = lambda: self.calculate_cube_area(e1.get())).grid(row = 2, column = 1)
    
    def calculate_cube_area(self, a):
        tk.Label(self.master, text = "", width = 20).grid(row = 3, column = 1)
        if(checkFloat(a)):
            area = 6 * (float(a) ** 2)
            tk.Label(self.master, text = str(shortenFloat(area, 7))).grid(row = 3, column = 1)
        else:
            tk.Label(self.master, text = "Enter Valid Value").grid(row = 3, column = 1)
