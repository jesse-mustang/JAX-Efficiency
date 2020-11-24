# Jesse Hudkins - BOM update
# code written on computer with resolution of 1920 x 1080 and Google Chrome with bookmark bar showing

# 1) run code
# 2) fill out form
# 3) press start

import pyautogui
import time
import tkinter as tk

# auto GUI Settings
pyautogui.pause = 1
pyautogui.failsafe = True  # if True, program will stop if mouse is dragged to the top left corner

# screen resolution
sc_width, sc_height = pyautogui.size ()
print('screen resolution:', sc_width, 'x', sc_height)


# define automated tasks
def go_home():
    cord_home = pyautogui.locateCenterOnScreen('home.png')
    pyautogui.click(cord_home)
    time.sleep(2)


def find_product():
    pyautogui.click(224, 139)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite("%s\n" % (e1.get()))
    time.sleep(2)


def open_BOM():
    cord_specs = pyautogui.locateCenterOnScreen('specifications.png')
    pyautogui.click(cord_specs)
    cord_materials = pyautogui.locateCenterOnScreen('materials.png')
    pyautogui.click(cord_materials)
    time.sleep(2)


def choose_factory():
    print(e2.get())
    pyautogui.click(826, 360)
    pyautogui.typewrite('custom order 243814\n') # for demo purposes
#    if e2.get() == 'BBY':
#        pyautogui.typewrite('TDP Compliant Spec (001)\n')  # issue with these codes being different for each product
#    elif e2.get() == 'JAX':
#        pyautogui.typewrite('TDP Compliant Spec (020)\n')
#    else:
#        print('Factory Entry Error')
    time.sleep(2)


def choose_colourway(): # delete this
    print(e3.get())
    pyautogui.click(781, 375)
    pyautogui.typewrite("%s\n" % (e3.get()))
    time.sleep(2)


def click_update():
    cord_update = pyautogui.locateCenterOnScreen('update button.png')
    pyautogui.click(cord_update)
    time.sleep(14)  # BOM loading time


def click_wide():
    cord_wide = pyautogui.locateCenterOnScreen('wide goods.png')
    pyautogui.click(cord_wide)
    time.sleep(1)


def save_checkin():
    pyautogui.scroll(2000)
    cord_save = pyautogui.locateCenterOnScreen('save.png')
    pyautogui.click(cord_save)
    time.sleep(2)
    cord_ok = pyautogui.locateCenterOnScreen('ok.png')
    pyautogui.click(cord_ok)


# "start" event
def start():
    print("Automation Initiated")
    go_home()  # still an open question if this is needed...
    find_product()
    open_BOM()
    choose_factory()
    choose_colourway()
    click_update()
    click_wide()
    pyautogui.scroll(-1000)
    time.sleep(3)
    save_checkin()
    print("Automation Over")


# build button and entry interface
master = tk.Tk()
master.title("BOM update")

tk.Label(master, text="Gerber Model:").grid(row=0, padx=50, pady=5)
tk.Label(master, text="Factory:").grid(row=1, padx=50, pady=5)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
tk.Button(master, text='Start', command=start).grid(row=3, column=1, sticky=tk.W, pady=10)

tk.mainloop()
