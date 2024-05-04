# 开发者：ByShook
# 开发时间：2024/5/4 下午12:45
import PySimpleGUI as sg

# sg.theme_previewer()  #预览主题样式
# print(sg.theme_list())  #打印所有主题名称
# sg.theme('')    #随机主题
# sg.theme('LightGreen3')  # 指定的主题
# sg.Popup('Welcome to PySimpleGUI')  # 生成弹窗
# print(sg.theme_button_color())  # 获取按钮的颜色
#
# sg.theme_button_color(('#abcfff', '#6D9F85'))  # 设置颜色
# sg.popup('Welcome to PySimpleGUI', "按键文字变颜色")  # 弹窗信息
# print(sg.theme_button_color())  # 生成弹窗

# 使用for循环快速布局
# layout = [
#     [sg.Text(i) for i in "abcd"],  # 元素主体是字符串sg.XXXX的生成的窗口元素从左到右排列
#     [[sg.In(i)] for i in ["北京", "上海", "广州", "深圳", "西安"]],  # 元素主体是列表[sg.XXXX]的生成的窗口元素从上到下排列
#     [sg.Button(i) for i in ['确定', '取消', '忽略']],
#     [[sg.Button(i)] for i in ['s1', 's2', 's3']]
# ]

# 另一种布局方式
layout1 = [
              [sg.Text('请输入基本信息')],  # 逗号连接的元素从上到下排列
              [sg.Text("姓名")] + [sg.In()]] + [  # 同行的元素可以使用加号连接
              [sg.Text('性别')] + [sg.In()]] + [  # 不同行的元素使用每行使用[]括起来，然后使用加号连接
              [sg.Text('国籍')] + [sg.In()],
              [sg.Button('确定'), sg.Button('取消')]
          ]

# window = sg.Window('Python GUI', layout)
window = sg.Window('Python GUI', layout1)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
