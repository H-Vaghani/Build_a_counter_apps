
import tkinter as tk


class counterapp:
    def __init__(self,master):
        self.master = master
        self.counter = 0

        self.label = tk.Label(self.master, text=f"counter: {self.counter}")
        self.label.pack()

        self.btn = tk.Button(self.master,text="Increment",command=self.Increment).pack()

    def Increment(self):
        self.counter += 1
        self.label.config(text=f"counter: {self.counter}")

if __name__ == "__main__":
    root = tk.Tk()
    app =counterapp(root)
    root.mainloop()



