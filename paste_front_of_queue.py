# Pressing this button will retrieve the oldest (topmost) line from the queue file and paste it.

import pyperclip
import os
import pyautogui as pya

# Get the path of the queue file
queue_path = os.path.join(os.path.dirname(__file__), 'queue.txt')

# Read the queue file and edit it to pop the topmost line
with open(queue_path, 'r') as queue_file:
    lines = queue_file.readlines()
    output_line = lines.pop(0)

# Write the edited queue file
with open(queue_path, 'w') as queue_file:
    for line in lines:
        queue_file.write(line)

# Copy the topmost line
pyperclip.copy(output_line)

# Paste the topmost line
pya.hotkey('ctrl', 'v')
