import easygui as g
import os

file_name = g.fileopenbox('请选择需要打开的文本', filetypes='*.txt')
file_n = os.path.basename(file_name)
fw = open(file_name, encoding='Utf-8')
text1 = fw.read()
msg = "文件【" + file_n + "】的内容如下:"
text2 = str(g.textbox(msg, title='显示文件内容', text=text1))
if text1 != text2:
    ret_opr = g.buttonbox('检测到文件内容发生改变，请选择以下操作:', title='警告', choices=('覆盖保存', '放弃保存', '另存为'))
    if ret_opr == '覆盖保存':
        fw.close()
        f1 = open(file_name, 'w', encoding='Utf-8')
        f1.write(text2)
        f1.close()
    elif ret_opr == '另存为':
        fw.close()
        g.filesavebox()
    else:
        fw.close()
else:
    fw.close()