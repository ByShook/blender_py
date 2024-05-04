# 开发者：ByShook
# 开发时间：2024/5/4 下午8:45
import PySimpleGUI as sg

text = '''江南春
唐·杜牧
千里莺啼绿映红
水村山郭酒旗风
南朝四百八十寺
多少楼台烟雨中
'''
layout = [
    [sg.T(text,  # sg.Text()缩写sg.Text()
          key='-Text-',  # 元素唯一标识符，书写规范 key=‘-NAME-’。用于元素的定位。
          size=(None, None),  # 元素宽度，行高（int，int）
          font=('仿宋', 20),  # 设定字体的名称，大小， font='宋体' ， font=('宋体',int) or font=['宋体',int]
          auto_size_text=True,  # bool: 元素根据文本自动调节大小
          enable_events=True,  # bool: 事件属性,设定为True时，点击文本发生事件。
          relief='ridge',  # 浮雕设计 'raised','sunken','flat','ridge','solid','groove'
          border_width=5,  # 设定relief时，用来设定边界宽度
          text_color='#fff566',  # 文本颜色
          background_color='#560060',  # 文本背景颜色
          justification='center',  # 对齐方式: 'left','right','center'
          pad=(20, 20),  # 元素间隔设定  记住左右上下，(int, int) or ((int, int),(int,int))
          # or (int,(int,int))or ((int, int),int)
          # (left/right, top/bottom) or ((left, right), (top, bottom))
          right_click_menu=['0', ["新建", '保存', ['2-1', ['2-1-1', '2-1-2'], '2-2', ['2-2-1', '2-2-2'], '2-3', ['2-3-1', '2-3-2']], "打开", ['1-1', '1-2', '1-3'], '关闭']],  # 右击调出菜单
          # List[List[Union[List[str],str]]]# 设定后,右击此元素可以调出菜单。
          grab=False,  # bool:如果为真,点此元素可以移动拖拽窗口
          tooltip='这是古诗江南春！',  # str:悬浮文本 ,当光标置于该元素上方,会显示设定的文本。
          visible=True  # bool: 元素可见状态
          )]
]

window = sg.Window('古诗窗口：', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-Text-':
        sg.Popup("点击了古诗内容！")

window.close()
