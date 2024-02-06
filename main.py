#
#   Author: Matheus Fragoso
#   
#   Description: Script to backup and copy save files from Google Drive shared folder to the game savefiles directory.
#
#   IMPORTANT NOTES: 
#   - To use this script, you need to disable the "Enshrouded" Steam cloud save feature.
#   - Replace the "windows_user" variable with your Windows username.
#   - Upload only world files to the shared folder, the most common files are "3ad85aea" and "3ad85aea_info".
#   - The script will create a backup of the current save files before copying the new ones.
#   - The script will execute the game after copying the files.
#   - Is recommended to create a shortcut of the shared folder in the "Saved Games" directory.
#   - Remember to change the "origin" variable with the correct path of the shared folder.

import shutil
import os
import subprocess
from datetime import datetime

windows_user = 'YOUR WINDOWS USER'  # Replace this with your Windows username

origin = rf'C:\Users\{windows_user}\Saved Games\Enshrouded_Shared' # Replace this with your shortcut directory of Google Drive Shared Folder
dest = rf'C:\Users\{windows_user}\Saved Games\Enshrouded'

executable = r'C:\Program Files (x86)\Steam\steamapps\common\Enshrouded\enshrouded.exe'

# Obtain the current date and time
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

backup = rf'C:\Users\{windows_user}\Saved Games\Backup_Saves' + '\\' + timestamp

try:
    print(f'Making backup of {dest} to {backup}...')
    shutil.copytree(dest, backup, dirs_exist_ok=True, copy_function=shutil.copy2)

    print(f'Copying files of {origin} to {dest}...')
    shutil.copytree(origin, dest, dirs_exist_ok=True, copy_function=shutil.copy2)

    print('Files copied successfully.')

    print(f'Running... {executable}...')
    subprocess.Popen([executable])

except Exception as e:
    print(f'Failed to copy files. Check permissions or existence of directories.\nError: {e}')

