# 开发者：ByShook
# 开发时间：2024/5/3 下午10:47
import PySimpleGUI as sg

layout = [

    [sg.Text('请输入您的信息')],
    # [sg.Text('姓名',enable_events=True), sg.InputText('程序员无声')],
    [sg.Text('姓名'), sg.InputText('程序员无声', key="name")],
    # [sg.Text('性别',tooltip="男或者女"), sg.InputText('男')],
    [sg.Text('性别'), sg.InputText('男')],
    [sg.Text('国籍'), sg.InputText('汉')],
    [sg.Button('确定'), sg.Button('取消')],
    [sg.Button('确定1'), sg.Button('1取消')]

]

window = sg.Window('Python GUI', layout)

while True:

    event, values = window.read()  # 窗口的读取，有两个返回值(1.事件  2.值)

    if event == sg.WIN_CLOSED:  # 窗口关闭事件
        break
    # if event == "确定":  #按照按钮的名字来执行
    #     sg.Popup("执行了确定任务")
    # if event == "取消":
    #     sg.Popup("执行了取消任务")

    # if event in ("确定","取消"):  #点击的按钮为括号中的任意一个就执行下面的代码
    #     sg.Popup("执行了确定或者取消任务")

    if event.startswith("确定"):
        # sg.Popup("确定")
        print(values)
        print(values["name"])  # Key值
        print(values[0])  # 索引值
    if event.endswith("取消"):
        sg.Popup("取消")

    # if event == "姓名":
    #     sg.Popup("点击了姓名")
    # if event == None:  # 窗口关闭事件,第二种方法
    #     break

window.close()
