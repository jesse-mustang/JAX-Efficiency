# Jesse Hudkins - BOM update
# Collaborator: Polly Zou
# code written on computer with resolution of 1920 x 1080 and Google Chrome with bookmark bar showing
# # = ctrl + / = "turn a piece of code off"

# locateCenter function require pixel perfect image, opencv_python allows for "blur"
# 1) run code
# 2) fill out form
# 3) press start

import pyautogui
import os
import time
import tkinter as tk
from tkinter import messagebox
import pandas as pd

# auto GUI Settings
pyautogui.pause = 1
pyautogui.failsafe = True  # if True, program will stop if mouse is dragged to the top left corner

# screen resolution
sc_width, sc_height = pyautogui.size()
print('screen resolution:', sc_width, 'x', sc_height)

# #For dev purpose only
# time.sleep(3)
# x1, y1 = pyautogui.position()
# print(x1, y1)

# define automated tasks 20210111 - update only includes upload_file functionality
def go_home():
    cord_home = pyautogui.locateCenterOnScreen('home.png', confidence=.75)
    pyautogui.click(cord_home)
    time.sleep(2)


def find_product():
    pyautogui.click(224, 139)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite("%s\n" % (e4.get()))
    time.sleep(2)


def open_BOM():
    cord_specs = pyautogui.locateCenterOnScreen('specifications.png', confidence=.75)
    pyautogui.click(cord_specs)
    cord_materials = pyautogui.locateCenterOnScreen('materials.png', confidence=.75)
    pyautogui.click(cord_materials)
    time.sleep(3)


def select_pfolder():
    print(e4.get())
    pyautogui.click(826, 320)
    pyautogui.click(826, 375)
    time.sleep(2)


def choose_factory():
    print(e2.get())
    pyautogui.click(826, 365)
    if e2.get() == 'BBY':
        pyautogui.typewrite('TDP Compliant Spec (001)\n')  # issue with these codes being different for each product
    elif e2.get() == 'JAX':
        pyautogui.typewrite('TDP Compliant Spec (002)\n')
    else:
        messagebox.showerror("Factory Code Mismatch", "Please select manually")
    time.sleep(2)


def choose_colourway():
    print(e3.get())
    pyautogui.click(745, 390)
    pyautogui.typewrite("%s\n" % (e3.get()))
    messagebox.showinfo("Review", "Please check that the fields are chosen correctly, if not, fix as needed")


def click_update():
    cord_update = pyautogui.locateCenterOnScreen('update button.png', confidence=.75)
    pyautogui.click(cord_update)
    time.sleep(14)  # BOM loading time


def click_wide():
    cord_wide = pyautogui.locateCenterOnScreen('wide goods.png', confidence=.75)
    pyautogui.click(cord_wide)
    time.sleep(1)


# import file
def upload_file():
    messagebox.showinfo("Next Step", "Open overrides & update first line & ensure all sizes are visible")

    ROOT = tk.Tk()
    ROOT.withdraw()
    # For now, always a file named "1" on the desktop

    ###########ERIC LOOK AT ME###################
    xls = pd.ExcelFile(r'1.xlsx') # FILE LOCATION
    #############################################

    # Trims data based on what's entered for Gerber model
    df1 = pd.read_excel(xls, usecols=[0, 1, 3], skiprows=4)
    df2 = df1.loc[df1['MODEL'] == e1.get()]
    df3 = df2.set_index('SIZES')

    count_row = df3.shape[0]    # count of rows in df3

    row_process = 0
    while row_process < count_row:
        size = df3.index[row_process]
        area = str(df3.at[size, 'TOTAL AREA'])
        fileloc = os.path.join(size + '.png')
        location = pyautogui.locateCenterOnScreen(fileloc, confidence=.90)
        #print(location)
        x, y = location
        pyautogui.click(x + 130, y)
        #print(area)
        pyautogui.typewrite(area)
        row_process += 1


def save_checkin():
    pyautogui.scroll(2000)
    cord_save = pyautogui.locateCenterOnScreen('save.png', confidence=.75)
    pyautogui.click(cord_save)
    time.sleep(2)
    cord_ok = pyautogui.locateCenterOnScreen('ok.png', confidence=.75)
    pyautogui.click(cord_ok)


# "start" event
def start():
    print("Automation Initiated")
    # go_home()  # still an open question if this is needed...probably not
    # find_product()
    # open_BOM()
    # select_pfolder()
    # choose_factory() #This function may put the wrong factory if user enters in wrong loc info
    # choose_colourway()
    # click_update()
    # click_wide()
    upload_file() #upload file + scans it + fill in the BOM for quantities
    #save_checkin()  #disable in-case of multiple item update
    print("Automation Over")

# build button and entry interface
master = tk.Tk()
master.title("BOM update")
master.geometry("320x75") # 4 buttons ==> 320x180

tk.Label(master, text="Gerber Model:").grid(row=0, padx=50, pady=5)
# tk.Label(master, text="Factory:").grid(row=1, padx=50, pady=5)
# tk.Label(master, text="Colour(# only):").grid(row=2, padx=50, pady=5)
# tk.Label(master, text="Product:").grid(row=3, padx=50, pady=5)

e1 = tk.Entry(master)
# e2 = tk.Entry(master)
# e3 = tk.Entry(master)
# e4 = tk.Entry(master)

e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# e3.grid(row=2, column=1)
# e4.grid(row=3, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
tk.Button(master, text='Start', command=start).grid(row=4, column=1, sticky=tk.W, pady=10)

tk.mainloop()
