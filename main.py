
import pyscreeze
import os.path
from pynput.mouse import Listener
from tkinter import filedialog
from datetime import datetime

#  Repertoire ou enregistrer les captures d'écrans
screenshot_dir = filedialog.askdirectory(title="Répertoire de destination pour les captures d'écrans")
if screenshot_dir == '':
    screenshot_dir = os.path.expanduser("~")
print("Repertoire de capture d'écrans : ", screenshot_dir)


scr_counter = 1

def on_click(x, y, button, pressed):
    global scr_counter
    if pressed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
        filename = f"capture_{scr_counter}_{timestamp}.png"
        filepath = f"{screenshot_dir}/{filename}"

        print("Capture : ", filename)
        scr_counter += 1
        
        pyscreeze.screenshot(filepath)

print("Vous pouvez quitter le programme en fermant cette fenêtre")
with Listener(on_click=on_click) as listener:
    listener.join()