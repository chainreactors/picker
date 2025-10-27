---
title: 2024年羊城杯粤港澳大湾区网络安全大赛WP-MISC篇
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247507963&idx=1&sn=3dc5ee9f5b0d4f8e7a3660eba434b12c&chksm=fa520a45cd25835301b3d3dd4f7fc74167eef5197b2d1871e92f5f57e176db520c2ac5d7b0eb&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-09-05
fetch_date: 2025-10-06T18:27:28.420018
---

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-MISC篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgIicsWDGeC3KNzyHaU3vYibqtwuuyzsKTRapJUyIUkILHicpibAfpPpzNSw/0?wx_fmt=jpeg)

# 2024年羊城杯粤港澳大湾区网络安全大赛WP-MISC篇

原创

NEURON

山石网科安全技术研究院

## hiden

文本rot47后rot13, 使用python脚本逆推。

```
import wave

with wave.open("hiden.wav", "rb") as wav_file:
    wav_data = bytearray(wav_file.readframes(-1))  # Read all audio frames
length_bytes = bytearray([wav_data[i * 4] for i in range(3)])
data_length = int.from_bytes(length_bytes, 'little')
extracted_data = bytearray()
for i in range(data_length):
    extracted_data.append(wav_data[(i + 3) * 4])
extracted_text = extracted_data.decode('utf-8')
print("Content:\n", extracted_text)
```

输出内容如下：

ok，now you find me,so the flag give you

DASCTF{12jkl-456m78-90n1234}

## miaoro

追踪HTTP流：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgLeLtriaGibeFtrzSypGXDDOgeepmDtAicfaBLicwWO7ssV8U1v0noqwl2g/640?wx_fmt=png&from=appmsg)

‍

shiro爆破密码得到/flag1/DASCTF{B916CFEB-C40F-45D6-A7BC-/Miao49757142263800

继续分析：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgDqicXvOLbvEFWNqLibQKyrCOf4003ju03byR7G48CU6hIw8bPeSu4iaEg/640?wx_fmt=png&from=appmsg)

解密：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgLqeBTibdxU3XciacIdPWceJPMGKHNs5DjzyUvn2L8wWGM58Pg9xnUtrw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgicZlgMqzibvGqXaNn3gZFWoDcopSUkciaGcicp3u7SB3JeKtFxxiahcsj0Q/640?wx_fmt=png&from=appmsg)

数据解密：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgUrclF1MLoPMZibo9qB31ldCShnEqdPMxwmhIlyVICNqsIURFbHtbTOw/640?wx_fmt=png&from=appmsg)

文件修改高度：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgKUFyy6ehLAicZaEXwdWNJibSnLicb72MU8fOIzTMJJHGlIFLgdNbZfic5g/640?wx_fmt=png&from=appmsg)

在B站找到对应文字得到完整flag

## 不一样的数据库\_2

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgQOVupYIsT8UGD79CwyCc2MNftLGeljEKlmyM5ROts75qOLA9BILzHQ/640?wx_fmt=png&from=appmsg)

解压得到二维码，修复

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgupD9NMnSS4dmPdRKCadW1YSQ0tN9sG8rR0uia0pRCNJVZSbfwQMtckw/640?wx_fmt=png&from=appmsg)

NRF@WQUKTQ12345&WWWF@WWWFX#WWQXNWXNU

rot13：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgib1vWuyFyjoSv7ajy6n2GsNpDtJZdL00DlKffakQKsvicFlbb8s7x1kg/640?wx_fmt=jpeg&from=appmsg)

使用密码登录找到历史记录：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgwTHiaHbO0iayXEGc1eQPqh6cziboH8aLdkXm58ZIt9gkZOticvhicgnSr8w/640?wx_fmt=png&from=appmsg)

DASCTF解密aes

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgN6v3q6maU65CIZ60H1QFjaEdAt8ZmTtCDNiausfWY7r0Tib5icbicZaX1A/640?wx_fmt=png&from=appmsg)

‍

## so much

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgc9lxRwXvCpppfHzTO9BZVDHz6XK7xn7tqEXWSiabCAibib1KcicusldcUQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSg24JC5orjOs8KFpwCf5gFm1iaCCZXq0ZZCnedU0rkbTeehEFo5KggX3Q/640?wx_fmt=png&from=appmsg)‍

然后提取时间戳：

```
import os

file_mod_times = [''] * 344
for j in range(344):
 file_path = 'E:\\' + str(j) + '.crypto'
 try:
  file_mod_times[j] = os.path.getmtime(file_path)
 except FileNotFoundError:
  file_mod_times[j] = None
print(file_mod_times)
flag = ''
for time in file_mod_times:
 if str(time) == '1628151585.73009':
  flag += '0'
 else:
  flag += '1'
print(flag)
tmp = ''
for char in flag:
 tmp += char
 if len(tmp) == 8:
  print(chr(int(tmp, 2)), end='')
tmp = ''
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgXDib1skFtYyptPW0a0J9p0jILshEzCw0NWkslpVptZhGI5cofUiaZSYQ/640?wx_fmt=png&from=appmsg)

时间戳二进制转换。

使用密码在Encrypto中解密01两个文件：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSg6VMLDaKxoxcoZ1a24ubTapcaLfFbzuhiaDwgIwzMUodvicG3PrMyKrAA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRBrw0oV4YpZ3ibcIBs2JTSgKOLWMkABHibtP9zOLia0TDgr1spMiaBI3LhoaO0ic7rYiaJ4JtIThYicu6bA/640?wx_fmt=png&from=appmsg)

## Checkin

首先解压缩得到一个Flag.txt文本发现里面的16进制首先16进制转文件发现文件损坏打不开，接着拿去16进制解密保存得出一个流量包：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT5iadVicAO65Y9ZR5iaKQA0IBswZOH1yIz4elFvpznbCtAOhJObVn9OQFOEH9w3m59Y8fAGSicRdv5KQ/640?wx_fmt=png&from=appmsg)

分析流量包先分析http流量无果，发现有很多TLS协议想解密但是没密钥，看到压缩包注释下有个base58：5unVpeVXGvjFah，拿去解密得出：Welcome2GZ，但是TLS协议的密钥不是这种格式的，联想到提示：解开txt的第二层面纱，使用工具wbStego进行解密，密码是：Welcome2GZ

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT5iadVicAO65Y9ZR5iaKQA0IBvhOwrIWSLvz0AvhuHUtSvXk0I4PP3On5LYJ1RrRCzQWooS0ln157cA/640?wx_fmt=png&from=appmsg)

得出一个.log文本拿去当密钥解开TLS协议流量包导入密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT5iadVicAO65Y9ZR5iaKQA0IBuLLe8YrXV8Sqgotibnw1SDLIjPGKz1dSuvWhljZOZWBfzaWZibzYiaJtw/640?wx_fmt=png&from=appmsg)

发现多了一些http的POST请求，追踪http流在33个流上发现了一个flag.gif动图。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT5iadVicAO65Y9ZR5iaKQA0IB4kY6gxcqiacSpnWT3tibVvu5RkZCZDlFxIbzmfTwtf8b7X2picxKmS1aw/640?wx_fmt=png&from=appmsg)

提取出图片，gif图片经过测试发现是gif图片间隔时间隐写。

使用kali自带命令提取间隔时间：

```
identify -format "%s %T \n" flag.gif
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT5iadVicAO65Y9ZR5iaKQA0IBXWhuKYIM6xsCZlOfFUGtkhSP1IgkO1SV1D949a2fadVxRlzjSATs2w/640?wx_fmt=png&from=appmsg)

得出3 23 3 23 3 23 3 23 3 23 3 23 23 23 23 23 3 3 23 23 3 3 3 3 3 23 23 23 3 23 23 23 3 23 3 3 23 23 23 3 3 23 3 23 23 23 23 23 3 3 23 23 3 3 3 23 3 23 3 23 3 23 3 3

进行二进制转换3转为0，23转为1，然后进行二进制转字符得出数据，数据就是flag。

0101010101011111001100000111011101001110010111110011000101010100

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnT5iadVicAO65Y9ZR5iaKQA0IBWXyGeqmLiaanbea6fuYNBgsBbiaTOfwbUM2UnobwzsmNX87WqaL4QawQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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