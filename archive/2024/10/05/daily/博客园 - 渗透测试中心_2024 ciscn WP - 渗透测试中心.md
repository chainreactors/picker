---
title: 2024 ciscn WP - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18447431
source: 博客园 - 渗透测试中心
date: 2024-10-05
fetch_date: 2025-10-06T18:52:28.948892
---

# 2024 ciscn WP - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [2024 ciscn WP](https://www.cnblogs.com/backlion/p/18447431 "发布于 2024-10-04 22:55")

## 一、MISC

### 1.火锅链观光打卡

打开后连接自己的钱包，然后点击开始游戏，答题八次后点击获取NFT，得到有flag的图片

没什么多说的，知识问答题

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225421094-195407480.png)

兑换 NFT

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225423012-1349203788.png)

Flag{y0u\_ar3\_hotpot\_K1ng}

### 2.Power Trajectory Diagram

方法1：

使用py中的[numpy](https://so.csdn.net/so/search?q=numpy&spm=1001.2101.3001.7020)和pandas库读取[npz文件](https://so.csdn.net/so/search?q=npz%E6%96%87%E4%BB%B6&spm=1001.2101.3001.7020)并保存为csv文件，代码如下：

import numpy as np

import pandas as pd

np.set\_printoptions(threshold=np.inf)

a1 = np.load('attachment.npz', allow\_pickle=True)

print(a1.files)

print('read:', a1)

index = a1['index']

myin = a1['input']

myout = a1['output']

mytra = a1['trace']

# print(mytra.shape)

df = pd.DataFrame(mytra)

df.to\_csv('data1.csv', index=False)

df1 = pd.DataFrame({'index':index, 'input': myin})

df1.to\_csv('data2.csv', index=False)

得到data1.csv、data2.csv，合并得到data.csv。

打开data.csv，可以看到功耗数据，根据https://zhuanlan.zhihu.com/p/157585244，我认为该题的关键是在于找到与其它字符不同的字符，就是该index的正确密码。

基于此，利用Excel的折线图功能，例如第四个字符，如图所示：

![在这里插入图片描述](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225424497-802313026.png)

可以看出，有一条绿色线与其它线都不同，为c，所以第四个字符就是c。

依次重复，得到整个密钥：`_ciscn_2024_`

即flag：`flag{_ciscn_2024_}`

方法2：

测试代码：

import numpy as np

import matplotlib

import matplotlib.pyplot as plt

matplotlib.use('tkAgg')

data = np.load("./attachment.npz")

print(data.files)

aa = data[data.files[0]]

bb = data[data.files[1]]

cc = data[data.files[2]]

dd = data[data.files[3]]

print(len(aa), aa)

print(len(bb), bb)

print(len(cc), cc)

print(len(dd), dd)

for i in range(len(dd)):

plt.scatter([i for i in range(len(dd[i]))], dd[i])

plt.show()

从 npz 文件中提取到四个文件的值，output 为空，其他 3 个文件提取的数组长度都是 520，根据   index 每 40 个可得出一个明文，大致判断共有 13 个明文。

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225425375-1250230147.png)

input是一个表

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225426348-2102281765.png)

output 为空

trace 里的数据都是小数

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225427236-1767167632.png)

尝试对 trace 里的数据画点图：

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225428016-911719087.png)

发现每组数据的最大值有很多点，最小值的点只有几个，所以我们尝试找出trace每组数据的最小值的下标：

import numpy as np

data = np.load("./attachment.npz")

dd = data[data.files[3]]

for i in range(len(dd)):

min\_index = np.argmin(dd[i])

print(f"Minimum index for group {i}: {min\_index}")

除了最后一组数据全为 985，其余数据中都有其他不同的数字

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225429043-1156571575.png)

用每四十组数据的最小值的下标再画一次图分析，发现最大值只有一个，所以我们需要继续找最大值的下标，然后再从input表中获取对应的字符即可：

![](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225430234-1674052168.png)

exp：

import numpy as np

import matplotlib.pyplot as plt

f = np.load('./attachment.npz')

index = f['index']

ip = f['input']

tr = f['trace']

flag = ""

for \_ in range(13):

t = []

table = ip[40\*\_:40\*(\_+1)]

for i in range(40):

# 每个列表画一个散点图，发现最小值

# plt.scatter([i for i in range(len(tr[\_\*40+i]))], tr[\_\*40+i])

# plt.show()

# 获取该列表的最小值的下标

min = np.argmin(tr[\_\*40+i])

# 将最小值的下标插入新列表

t.append(min)

# 用 40 个列表的最小值的下标作为数据，画图，发现有最大值

for i in range(len(t)):

plt.scatter([i for i in range(len(t))], np.array(t))

plt.show()

# 求最大值的下标

mins = np.argmax(t)

# 用下标从表里取字符

ind = table[mins]

# 把字符加到flag里

flag += ind

print(flag)

得到：\_ciscn\_2024\_a

由于前面最后一组数据全是 985，因此最后一组数据得出的 a 不算

去掉 a 得到最终flag为：flag{\_ciscn\_2024\_}

### 3.神秘的文件

方法1：

究极套娃，看的眼睛都要花了，真就纯找。得到PPT文件，直接改后缀为.zip去找

part1

在docProps目录下的两个xml中，app.xml提示了解密算法，core.xml提示了密文和密钥key，直接上赛博

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225431066-1776316267.png)

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225431732-1559310269.png)

part2

在ppt/embeddings文件夹下的docx中，从PPT打开的话就是第二章左上角那块黑色的，双击就行，打开后全选，改字体大小，改颜色，凯撒偏移量10解密，然后base64解密，得到part2

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225432382-1931494586.png)

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225433200-1501217227.png)

part3

在vbaProject.bin中，这个真的找了好久，后来也是网上搜得到说ppt隐写可能跟宏和宏脚本有关系，叫VBA工程解密。先010打开vbaProject.bin，找DPB字节，把最后一位改成x，然后保存，之后改后缀为.zip，直接打开会发现其中内涵的文件，打开VBA文件夹下的模块一

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225434134-1770170252.png)

发现一段密文，不知道是啥但是提示是base64之后的，那就先解密呗，然后得到乱码，一般这种特殊字符多的不是RC4就是rot，最后发现是无密码RC4解密，然后再解一层base64

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225434895-1920071602.png)

part4

直接打开PPT（因为它是由media文件夹下的图片拼成的），第三张，好像是要选可见隐藏字符，因为我电脑自动默认选的所以直接可以看，base64解码

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225435748-1099940221.png)

part5

是在第五章ppt的注释中，直接赛博厨师帽跑，多层base64解码，得到第五部分

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225436620-2146103775.png)

part6

是在第五张PPT正文边界的左上角，把它界面缩放或者直接拆media文件夹都可以，base64解码

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225437537-1704852607.png)

part7

是在ppt\slides下的slides4.xml中，id4的位置，下面提示rot13 all，暗示包括number，base64解码

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225438254-1024081489.png)

part8

在slideLayout2.xml中，南平，最开始没理解最后是啥意思，连一起了才看懂。。。。，就是要除去上面字符串中的Bb13。。。然后base64解码

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225439014-105488333.png)

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225439873-14791292.png)

part9

直接在media文件夹下，看那个猫人的图片左下角，base64解码

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225440656-201472929.png)

part10

在comment1.xml中，维吉尼亚解码，密钥是furry

![image](https://img2023.cnblogs.com/blog/1049983/202410/1049983-20241004225441517-482148777.png)

总之最后flag是flag{e675efb3-346f-405f-90dd-222b387edee9}

方法2：

先是一些简单容易找到的，按照提示规则进行 base64、维吉尼亚、凯撒等解码即可

PPT 里面找到了很多东西：

![](https://img2023.cnblogs.com/blog/1049...