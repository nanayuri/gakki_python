import easygui as g
import os

file_name = g.fileopenbox('请选择需要打开的文本', filetypes='*.txt')
file_n = os.path.basename(file_name)
fw = open(file_name, encoding='Utf-8')
lines = fw.read()
msg = "文件【" + file_n + "】的内容如下:"
g.textbox(msg, title='显示文件内容', text=lines)
