from components.application import App
from configs.config import *

if __name__ == '__main__':
    myapp = App()
    myapp.master.title(WINDOW_NAME)
    myapp.master.maxsize(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT)
    myapp.mainloop()
