#!/usr/bin/env python
# coding: utf-8
#>Create and link a github repo
# $ git init
# > Add "file" and commit
# > git config --config carlos.avila5333@alumnos.udg.mx 
# # git config --config user.name heleidan 
# Nuevo cambio al repositorio: 
# $ git add "/file"
# $ git commit -m "type a commit message"
# $ git push -u origin main

# In[1]:

import tkinter as tk
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x467")
        self.window.resizable(0, 0)
        self.window.title("Quickie Calculator")
        #self.display_frame = self.create_display_frame()
        #self.buttoms_frame = self.create_buttoms_frame()
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    calc = Calculator()
    calc.run()

print("This is a second change")


# In[ ]:




