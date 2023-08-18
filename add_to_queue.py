# Pressing this button will copy the selected text, split it by newline and append each line to the queue file

import pyperclip
import os
import pyautogui as pya

# Get the path of the queue file
queue_path = os.path.join(os.path.dirname(__file__), 'queue.txt')

# Copy the selected text
pya.hotkey('ctrl', 'c')
text = pyperclip.paste()
print(f"text = {text}")

# Split the copied text by newline
lines = text.split('\n')
print(f"lines = {lines}")

# Append each line to the queue file
with open(queue_path, 'a') as queue_file:
    for line in lines:
        queue_file.write(line)