---
title: Python 入门第三课：让程序\"开口说话\"：90% 新手都忽略的输入输出技巧
url: https://mp.weixin.qq.com/s/3SmDQEia--aZIh6y_YBG3A
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:13:06.527528
---

# Python 入门第三课：让程序\"开口说话\"：90% 新手都忽略的输入输出技巧

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kztGyHFwmfwJ2e7KDSXJJujFwtWnYfny4HZfkyibvMIQzxibDMLicMcNKSic7btkEll6RqZxRq49fvbbFdFsourIjOrblMiarKV5pEicZz9bxTuZ8/0?wx_fmt=jpeg)

# Python 入门第三课：让程序"开口说话"：90% 新手都忽略的输入输出技巧

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器中沉浸阅读

> Tip
>
> 📝 课程目标：掌握 Python 的输入输出功能，让你的程序能和用户"对话"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfytIrPDjRvXLMAZ9b7RmwubqEicef5UpAAeYRbknV8eKS9rJQ1RCDx1Fic5WGAa5XicGicS65xCIt5N9G6v9fwuFLEjKDlcicUYJvnA/640?wx_fmt=png&from=appmsg)

## 一、输出信息：print() 函数

### 1.1 基础用法

```
print("Hello, Python!")
```

### 1.2 打印多个内容

```
# 用逗号分隔，自动添加空格
print("姓名:", "张三", "年龄:", 25)

# 输出结果：姓名：张三 年龄：25
```

### 1.3 自定义分隔符

```
# 使用 sep 参数改变分隔符
print("2024", "03", "27", sep="-")
# 输出：2024-03-27

print("A", "B", "C", sep="|")
# 输出：A|B|C
```

### 1.4 控制换行

```
# end 参数控制结尾（默认是换行符\n）
print("第一行", end=" ")
print("第二行")
# 输出：第一行 第二行

print("你好", end="！\n")
print("明天见")
# 输出：你好！
#       明天见
```

## 二、获取输入：input() 函数

### 2.1 基础输入

```
name = input("请输入你的名字：")
print(f"你好，{name}！")
```

### 2.2 输入的都是字符串

```
age = input("请输入你的年龄：")
print(type(age))  # <class 'str'>

# 需要转换成数字
age_num = int(age)
print(f"明年你就 {age_num + 1} 岁了")
```

### 2.3 不同类型转换

```
# 转整数
num1 = int(input("请输入一个整数："))

# 转浮点数
num2 = float(input("请输入一个小数："))

# 转布尔值（注意：非空字符串都是 True）
flag = bool(input("请输入任意内容："))
```

## 三、实战练习

### 练习 1：个人信息卡片

```
print("=== 个人信息生成器 ===")
name = input("姓名：")
age = input("年龄：")
city = input("城市：")
hobby = input("爱好：")

print("\n" + "="*30)
print(f"📇 姓名：{name}")
print(f"🎂 年龄：{age}岁")
print(f"📍 城市：{city}")
print(f"❤️ 爱好：{hobby}")
print("="*30)
```

### 练习 2：简单计算器

```
print("=== 简易计算器 ===")
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")
print(f"{num1} ÷ {num2} = {num1 / num2}")
```

### 练习 3：问候机器人

```
print("🤖 你好！我是你的问候机器人～")
name = input("请问怎么称呼你？")
time = input("现在是早上、下午还是晚上？")

if time == "早上":
    print(f"早上好，{name}！祝你今天元气满满！☀️")
elif time == "下午":
    print(f"下午好，{name}！工作累了吗？记得休息哦～☕")
elif time == "晚上":
    print(f"晚上好，{name}！早点休息，晚安！🌙")
else:
    print(f"你好，{name}！无论何时，我都在这里帮你！✨")
```

## 四、格式化输出进阶

### 4.1 f-string（推荐）

```
name = "Python"
version = 3.12

print(f"{name} 最新版本是 {version}")
print(f"{name:_^20}")  # 居中，用_填充
# 输出：_______Python________

price = 199.5678
print(f"价格：{price:.2f}")  # 保留 2 位小数
# 输出：价格：199.57
```

### 4.2 format() 方法

```
# 位置参数
print("{} 今年 {} 岁".format("小明", 18))

# 关键字参数
print("{name} 喜欢 {hobby}".format(name="小红", hobby="编程"))

# 格式化数字
print("圆周率：{:.3f}".format(3.1415926))
# 输出：圆周率：3.142
```

## 五、常见错误与调试

### 错误 1：类型不匹配

```
# ❌ 错误
age = input("年龄：")
print(age + 1)  # TypeError: can only concatenate str to str

# ✅ 正确
age = int(input("年龄："))
print(age + 1)
```

### 错误 2：转换失败

```
# ❌ 错误
num = int(input("请输入数字："))  # 输入"abc"会报错

# ✅ 正确处理
try:
    num = int(input("请输入数字："))
except ValueError:
    print("输入无效，请输入数字！")
```

## 六、今日挑战

### 🎯 挑战 1：BMI 计算器

编写一个程序，计算用户的 BMI 指数：

* • 输入身高（米）和体重（千克）
* • 计算公式：BMI = 体重 / (身高 × 身高)
* • 输出结果并判断：

+ • BMI < 18.5：偏瘦
+ • 18.5 ≤ BMI < 24：正常
+ • 24 ≤ BMI < 28：偏胖
+ • BMI ≥ 28：肥胖

### 🎯 挑战 2：故事生成器

创建一个互动故事：

1. 1. 询问用户5个问题（名字、地点、动物、食物、心情）
2. 2. 用这些答案编一个有趣的小故事
3. 3. 用漂亮的格式输出
   示例输出：

```
📖 《小明的冒险》

在一个阳光明媚的 北京，
小明 遇到了一只会说话的 熊猫。
它们一起分享了美味的 火锅，
度过了一个非常 开心 的下午！
```

## 七、小结

|  |
| --- |
|  |

| 函数 | 作用 | 返回值类型 |
| --- | --- | --- |
| `print()` | 输出信息到屏幕 | `None` |
| `input()` | 从键盘获取输入 | `str` |

> Success
>
> 关键要点：
>
> * • `input()`返回的永远是字符串
> * • 需要数字时用`int()`或`float()`转换
> * • `f-string`是最推荐的格式化方式
> * • 用`sep` 和`end`控制输出格式

---

> Note
>
> * • [Python 入门第一课：为什么选择 Python？3 分钟搭建你的第一个程序](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389672&idx=1&sn=938cfe2512611eacb1ca135c0bab1a00&scene=21#wechat_redirect)
> * • [Python 入门第二课：变量和数据类型——给数据安个家](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389677&idx=1&sn=cd38ddf64fca37b7e6dcc243ea73da4b&scene=21#wechat_redirect)

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

攻城狮成长日记

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过