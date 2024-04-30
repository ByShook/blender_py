import bpy
#if判断

samples = input("Enter number of samples: ")

# print(type(samples))

input_samples = int(samples)

# print(samples,type(samples))

if samples <= 0:
    print("采样必须是正值，请重新输入：")
    samples = input("Enter number of samples: ")
    input_samples = int(samples)
    print(input_samples)
elif samples > 1000:
    print("你输入的采样太大了，请重新输入：")
    samples = input("Enter number of samples: ")
    input_samples = int(samples)
    print(input_samples)
else:
    print(f"你输入的采样是：{samples}")

