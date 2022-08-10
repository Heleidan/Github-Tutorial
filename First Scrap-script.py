
# > Link a Github repo git git through SSH 
# $ git init
# > Add "file" and commit
# > git config --global user.mail carlos.avila5333@alumnos.udg.mx 
# $ git config --global user.name heleidan 
# $ git branch -M main
# $ git remote add origin https://github.com/Heleidan/GUI-Calculator-in-Python3.git
# $ git push -u origin main


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




