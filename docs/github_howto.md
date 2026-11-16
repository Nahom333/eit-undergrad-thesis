# GitHub: how to set this up (you have no account yet)

1. Make an account at github.com (free). Use a username you are happy to show to professors.
2. Install Git on your laptop (git-scm.com). Then in a terminal:
   git config --global user.name "Nahom Zeray"
   git config --global user.email "your-email@example.com"
3. On github.com click New repository. Name it eit-thesis. Choose Private for now (you can make it public later).
4. In this folder:
   git init
   git add .
   git commit -m "Initial project structure"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/eit-thesis.git
   git push -u origin main
   (GitHub will ask you to log in. It no longer accepts your password in the terminal; use the browser login it offers, or GitHub Desktop, which is easier.)
5. After that, every week: git add . ; git commit -m "what I did" ; git push

## What to commit
Source code, notes, small CSVs, photos of the build, schematics and PCB files, the logbook.
## What not to commit
Big raw files, datasheets you do not have the right to redistribute (keep them in hardware/datasheets locally and add that folder to .gitignore), passwords.

## Good commit messages
Say what changed and why: "Noise test v1: 8-resistor ring, 200 frames, std 1.2 mV" is useful. "update" is not.
