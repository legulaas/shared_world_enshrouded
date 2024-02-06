# Enshrouded - Download and Backup Savefiles Script

## Overview

This script facilitates the backup and copying of save files from a Google Drive shared folder to the game's savefiles directory in the Enshrouded game. It includes features such as creating a backup of current save files, copying new files from the shared folder, and automatically executing the game after the copy operation.

## Important Notes

- **Disable Steam Cloud Save Feature:** Before using this script, ensure that the "Enshrouded" Steam cloud save feature is disabled.
  
- **Replace Windows User:** Modify the `windows_user` variable with your Windows username.

- **Upload Only World Files:** Only upload world files to the shared folder; common files include "3ad85aea" and "3ad85aea_info".

- **Create a Shortcut:** It is recommended to create a shortcut of the shared folder in the "Saved Games" directory.

- **Update Origin Path:** Change the `origin` variable with the correct path of the shared folder.

## Usage

1. Clone or download the script to your local machine.
   
2. Open the script in a text editor and update the `windows_user` and `origin` variables as instructed in the comments.

3. Run the script using a Python interpreter.

   ```bash
   python main.py
