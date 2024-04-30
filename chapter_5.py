# 开发者：ByShook
# 开发时间：2024/4/30 下午11:16
import random

#
# up = 100
# down = 1
#
# num = random.randint(1,100)
# # print("答案已生成！",num)
# print("答案已生成！")
#
# input_num = int(input(f"请输入你猜测的数值({down}-{up}之间):"))
#
# while input_num != num:
#     if input_num > num:
#         print("你输入的数比答案大")
#         up = input_num
#         input_num = int(input(f"请重新输入({down}-{up}之间)的数值:"))
#     elif input_num < num:
#         print("你输入的数比答案小")
#         down = input_num
#         input_num = int(input(f"请重新输入({down}-{up}之间)的数值:"))
#
# print("恭喜你，猜对了，正确答案就是：",num)


for i in range(0, 30, 1):
    if i % 5 == 0:
        continue
    print(i)

for i in range(0, 50, 3):
    print(i)
