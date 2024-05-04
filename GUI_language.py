# 开发者：ByShook
# 开发时间：2024/5/4 下午11:23
import PySimpleGUI as sg

layout = [
    [sg.B('中文', key='Ch'), sg.B('English', key='En')],
    [sg.T('请输入基本信息!', key='-Title-')],
    [sg.T('姓名：', key='-Name-', size=(5, 1)), sg.In()],
    [sg.T('性别：', key='-Sex-', size=(5, 1)), sg.In()],
    [sg.T('年龄：', key='-Age-', size=(5, 1)), sg.In()],
    [sg.B('确认', key='-Confirm-', size=(8, 1)), sg.B('取消', key='-Cancel-', size=(8, 1))],
]

window = sg.Window('Language', layout)

while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'En':
        window['-Title-'].Update('Please enter basic information!')
        window['-Name-'].Update('Name:')
        window['-Sex-'].Update('Sex:')
        window['-Age-'].Update('Age:')
        window['-Confirm-'].Update('Confirm')
        window['-Cancel-'].Update('Cancel')
    if event == 'Ch':
        window['-Title-'].Update('请输入基本信息!')
        window['-Name-'].Update('姓名')
        window['-Sex-'].Update('性别')
        window['-Age-'].Update('年龄')
        window['-Confirm-'].Update('确认')
        window['-Cancel-'].Update('取消')

window.close()
