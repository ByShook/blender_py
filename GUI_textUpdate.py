# 开发者：ByShook
# 开发时间：2024/5/4 下午10:47

import PySimpleGUI as sg

# 更新方法
# window[key].update()
# window[key].Update()
# kejian = True

layout = [
    [sg.T('BySook', key='-Text-'), sg.B('牛逼')],
    [sg.B('可见性')]
]

window = sg.Window('文本元素更新', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == '牛逼':
        window['-Text-'].update(
            value='哈哈哈哈哈哈！',  # str 更新文本
            background_color='green',  # 更新文本背景颜色
            text_color='black',  # 更新文本颜色
            font=('仿宋', 30),  # 更新字体的名称或者大小
            visible=True  # 更新元素的可见状态
        )
    if event == '可见性':
        window['-Text-'].update(
            visible=False
        )

window.close()
