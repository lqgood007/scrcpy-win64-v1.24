from pywinauto.application import Application

app = Application().start('notepad.exe')
app.Notepad.Edit.type_keys('Hello{SPACE}World!')
