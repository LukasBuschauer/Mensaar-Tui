# Mensaar-Tui
is a Text User Interface for quickly getting todays dishes at Saarland University's cafeteria.

## Usage


## Installation
### - Linux
```
chmod +x ./mensaartui.py
```
### - Windows
Install PyInstaller from PyPI:
```
pip install pyinstaller
```
Go to your program’s directory and run:
```
pyinstaller mensaartui.py
```
This will generate the bundle in a subdirectory called dist.
```
pyinstaller -F mensaartui.py
```
Adding -F (or --onefile) parameter will pack everything into single "exe".
```
pyinstaller -F --paths=<your_path>\Lib\site-packages  mensaartui.py
```
running into "ImportError" you might consider side-packages.
```
pip install pynput==1.6.8
```
still runing in Import-Erorr - try to downgrade pyinstaller - see [Getting error when using pynput with pyinstaller](https://stackoverflow.com/questions/63681770/getting-error-when-using-pynput-with-pyinstaller)

This exlpanation is from a reddit post you can find [here](https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen)


