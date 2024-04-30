# 开发者：ByShook
# 开发时间：2024/4/30 下午10:02
import bpy

samples = int(input("请输入你的采样: "))

if samples != 64:
    print("你输入的采样不是64")
    if samples > 64:
        print("大于64")
    elif samples < 64:
        print("小于64")
else:
    print("你输入的采样是64")