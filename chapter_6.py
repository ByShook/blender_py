# 开发者：ByShook
# 开发时间：2024/5/1 下午10:46
# 列表
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = []

a = "yuansu"

baihulin = 12

# append向列表中增加元素
list2.append(a)

print(list2)

for i in list1:
    text = str(i)
    list2.append(text)

list3 = list1 + list2
print(list2)
print(list3)

# 删除
print(list2)
list2.pop()  # 无参数时，删除最后一个元素，有参数时删除索引对应的元素
print(list2)

list2.remove("5")  # 删除指定的字符，如果有多个每次删除一个，依次删除
print(list2)

del list2[0]  # 删除索引对应的元素
print(list2)

# print(len(list2))
# print(type(len(list2)))

# while 1:
#     if len(list2) > 0:
#         list2.pop()
#     else:
#         break
#
# print(list2)

# 查找

num567 = list2[6]
print(num567)

# 修改
list2[5] = 10000
print(list2)

character = "我是谁的爸爸"

for i in range(len(character)):
    print(character[i], end=" ")

character1 = character[0:3]
print(character1)

s = 1
print(s)
