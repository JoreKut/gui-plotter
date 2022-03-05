from application import App

if __name__ == '__main__':
    myapp = App()
    myapp.master.title("PlotMaker v.2.0.0")
    myapp.master.maxsize(1000, 600)
    myapp.mainloop()
