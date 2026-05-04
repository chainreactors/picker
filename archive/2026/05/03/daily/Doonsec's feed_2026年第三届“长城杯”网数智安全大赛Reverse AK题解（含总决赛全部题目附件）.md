---
title: 2026年第三届“长城杯”网数智安全大赛Reverse AK题解（含总决赛全部题目附件）
url: https://mp.weixin.qq.com/s/Yiu77nsqNRP5yk0IG9HNew
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:31:04.430036
---

# 2026年第三届“长城杯”网数智安全大赛Reverse AK题解（含总决赛全部题目附件）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XkUCeyh2WibiariceInrmE5HXKYxbvKB0zvSHkDM41G85MPU7cBkls8zR8zPU68BqxjGtOiaKt5R8jeTkpQ6oApZF9QoFv1L4ib5Cx9zgdDkrPiaY/0?wx_fmt=jpeg)

# 2026年第三届“长城杯”网数智安全大赛Reverse AK题解（含总决赛全部题目附件）

原创

Real返璞归真
Real返璞归真

Real返璞归真

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 公众号

欢迎关注公众号【Real返璞归真】，我们将不定期分享**CTF竞赛、二进制安全、JS/安卓逆向、AI安全**等领域的前沿知识与技术内容。

公众号后台回复【长城杯2026】获取总决赛全部题目附件（AI、Pwn、Re、Web）下载地址。

## 前言

Reverse方向共三道题目：1个签到题 + 1个错题 + 1个非预期。

## DokiLogic

### 逆向分析

游戏题目，需要对游戏进行逆向分析：

![image-20260429172951792](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2Wibjia7I2OVPMTRa2Lov8RW8G2NQYjfKcKNgteuNP2JBx8N8NC7yfEgjazhSpe7MvZWbLZhb8a82OwYwKWgMINeQTDlRwNbScm5Dg/640?wx_fmt=png&from=appmsg)

运行后会让用户输入flag：

![image-20260429174305165](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibg8OAQ1Sa48FFQeMm4joqCkjYKSo0xcbppr84fhO0xy0iaAtMbauaXQaqYSkLoWjCJtrJBPRMpk9iarBicPQcmfO5fHvw3apR6rIk/640?wx_fmt=png&from=appmsg)

根据文件目录名，发现该游戏使用`renpy`游戏引擎，包含大量`.py`文件：

![image-20260429174405450](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibgLV3C0F0axTSaBM3qFtO3V06j9gEoynkCdZWFicI0XicRZPqd4kWqQL8jtibrOcHaugDO88vcYkZDxBG5n2TA3INqdgt3kmmiaATc/640?wx_fmt=png&from=appmsg)

每次启动游戏后，`renpy`游戏引擎会加载`game`目录下的`.rpyc`文件：

![image-20260429174556994](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibjUesic1uxxkIibykuzXt9Rdgw1Yic0ZOyrg8umPogLVV56icGjEGuuibzsJ6wGhlOw1j6ibL7FulE0N5IUU8HrsoUAxGZHiaiapZEYic04/640?wx_fmt=png&from=appmsg)

### 解题思路

修改`renpy`引擎源代码，运行游戏，引擎在加载`,rpyc`文件时，将其输出到日志即可得到游戏逻辑代码。

### 题解

在`renpy/script.py`的`Script`类下的`load_file`函数中将加载的`.rpyc`打印到日志：

![image-20260430105309993](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibh1WsVaB4DOuauibKEzGnJeXDG3KMpHYpibCevibI3xNhgPyjfOdRiaGFzDicV9O6AG7TLeaGdQZdTWobw3zWfDHnRO2qQ1FUiaP7NVI/640?wx_fmt=png&from=appmsg)

运行游戏并查看日志：

![image-20260430105703782](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibia0WZJy9vnAEUBI49ZwJF2RrPwy8fJMXOtJEJdOiaKnwTL19CgbicdVgib1udib9PQxKjd05PcncRFhN5puVacNqbtC60W4ecuDhTs/640?wx_fmt=png&from=appmsg)

得到包含乱码的Python代码（pickle序列化），手动删除乱码后可以大致看到代码逻辑：

```
user_input = renpy.input("just input your answer: ", length=60)
user_input = user_input.strip()
encry_input = l11111l1ll1l(user_input)
encry_input == ll111l11l111
```

现在需要追溯得到密文`ll111l11l111`和加密函数`l11111l1ll1l()`：

```
open(\'.1.exe\', \'wb\') as llll11ll1l11:
     llll11ll1l11.write(_f)
     l11l1ll111l1 = subprocess.run(\'./.1.exe\', stdout=subprocess.PIPE).stdout\nos.remove(".1.exe")
l11l1ll111l1 = subprocess.run(\'./.1.exe\', stdout=subprocess.PIPE).stdout
ll111l11l111 = l11l1ll111l1.decode(\'latin-1\')

def l11111l1ll1l(ll1llll1l11l):
 llll1l111ll1 = 35
    return ''.join((chr(ord(ll1l111ll11l) ^ llll1l111ll1) for ll1l111ll11l in ll1llll1l11l))
```

可以发现，程序创建`./1.exe`程序并执行，得到密文后迅速将程序删除。

加密逻辑很简单，直接将密文异或35即可还原明文。

可以编写Python脚本进行文件监控，在`.1.exe`删除前将其拷贝：

```
import os
import shutil
import time

while True:
    if os.path.exists(".1.exe"):
        shutil.copy2(".1.exe", "123.exe")
        break
    time.sleep(0.5)
```

拿到`.1.exe`后UPX脱壳：

```
upx.exe -d 123.exe
```

![image-20260430112143183](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibjrrdndKibe8J6VMibG2vBlPaibUUGdkOxyia1sLia4oKgST5bgjZd1wjr4PTqHL2JjyyicgOnDPr7rhicLdEeyARJtt8vVlciaa9kqIn4/640?wx_fmt=png&from=appmsg)

动态调试拿到Buffer数组中的密文，然后编写脚本解密即可：

```
# def enc(param):
#     key = 35
#     return ''.join((chr(ord(x) ^ key) for x in param))

enc = [0x45,0x12,0x14,0x40,0x16,0x10,0x40,0x10,0xE,0x47,0x40,0x11,0x15,0xE,0x17,0x15,0x41,0x12,0xE,0x41,0x10,0x14,0x10,0xE,0x11,0x40,0x42,0x13,0x13,0x42,0x15,0x42,0x15,0x14,0x11,0x12]

for x in enc:
    print(chr((x) ^ 35), end='')

# f17c53c3-dc26-46b1-b373-2ca00a6a6721
```

## notjavaweb

> ❝
>
> 题目描述：公司内部开发了一个Java Web应用，不过好像并没有那么简单......

### 逆向分析

题目给出两个文件：

![image-20260430112405760](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibgfIXYobtWJK49zeLp7uHsTyWQRFiagnnQCICLJqK6GOjOr9LmzaaZzWvOlgMLM0NMcdDXSUcUOLAlTSSuMCZicxshQ0G5H6YtBU/640?wx_fmt=png&from=appmsg)

流量包逻辑很清晰，是用户与服务端的交互：

![image-20260430112459365](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibgPWbRQNHE7iadzngEZHR1rFj6pKpCzzSxHMh4zJfRK2jjZMiae41pMZW0axFhobVqwpCAoIiasX2TaQIK8Wd4s0Sziang4XqjPOmo/640?wx_fmt=png&from=appmsg)

用户调用`login`接口登录后，多次调用`/api/reviews/add`接口和`/api/user/avatar`接口，然后调用`logout`接口退出。

使用`jadx`工具对jar文件进行逆向：

![image-20260430112734295](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2WibiaWn3HgQt49Hm88mxia3PriaTJXyCGf5s0dUUyLEAWejRUtmcMsZG2A853ovZsLGDHmWmPDQNPFicpX3HysgneAWqyjF2iandm6o2M/640?wx_fmt=png&from=appmsg)

发现`com.example.moviereview.analytics`包下有一个**基于栈结构的VM虚拟机**。

对其进行交叉引用，发现`logout`接口会调用该虚拟机：

![image-20260430112834368](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibjVfLekXlfLluq9ibuWl9wP4WCSKR52OgLPozpxMGdM8ogyebiclVXh3lYvaHcv3XiannKOicjrngLRkAXibp5TRlVV4grhKMFqZ0Mk/640?wx_fmt=png&from=appmsg)

并将`vmContext`的内容作为**虚拟机的指令和数据**，分析`VmContext`类：

![image-20260430112950828](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibg1LJHgSAkxuHXCh5MUnuKhRyINj7UZeZKVD8FJpMee5ibzTuyRDZonPqtOoSFJt2ldMkRsl2jhPcecRMtmVakZwiahxloeXrXKo/640?wx_fmt=png&from=appmsg)

对其`appendEvent()`方法进行交叉引用，发现有三个调用点：

![image-20260430113037293](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2Wibjz5M5fpskCdrP4FfiapzUH24zUvbdHTaQnxamSZOewU2iaulPtILmGwZNxnRuFdHMhlcQicEciaJHTbLjpbrzPI4woufN2ckWiaeQ4/640?wx_fmt=png&from=appmsg)

发现前两个调用点使用了AOP编程：

![image-20260430113134343](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2Wibga5o8PHU2Dk29SKck7ekyfz2McKPZY6BZ1kProfTXyhGlDu7TBar6x7vVazrCxpHlg0hkicJXG8JSl2KvgA1aiaIDkpFbv62ToA/640?wx_fmt=png&from=appmsg)

切点位于`updateAvatar()`和`addReview()`方法，即在这两个函数被调用时触发：

![image-20260430113457964](https://mmbiz.qpic.cn/sz_mmbiz_png/XkUCeyh2WibjxkcpYCx9GUGrSEibTgr82RDiab30ZBDkJULvYVPE7Geia1HquPLO9s2DuXR8CuIYotc24CkhbIJ6Ufe1WoH863YhKzuibwzwENaI/640?wx_fmt=png&from=appmsg)

注意：这里有个坑，`addReview()`方法实际上并不存在！

第三个调用点位于`/api/reviews/add`接口：

![image-20260430113316005](https://mmbiz.qpic.cn/mmbiz_png/XkUCeyh2Wibg8vvOmoW2az5lRoo5Yjn04J8tkKbY7FlqSrrgG9iaF0K4frEBpZBicibEhf2jWh08oRTdWs7bMORoYfO1lJib3dPnSS6v6uc2ia6rM/640?wx_fmt=png&from=appmsg)

### 解题思路

逻辑非常清晰：

1. `api/reviews/add`接口和`api/user/avatar`接口的参数会被存储到`vmContext`作为**虚拟机的指令和数据**。
2. 当用户调用`logout`接口退出登录时，会执行VM虚拟机。

我们需要做的就是将流量包的指令集和数据提取出来，然后丢进VM虚拟机执行，分析其行为。

### 提取流量

将用户请求的流量包复制到`res.txt`文件，然后编写Python正则表达式提取参数：

```
import re

from numpy.core.defchararray import isnumeric

log_data = open('./res.txt').read()

pattern = r'"emojiAvatarId"\s*:\s*(\d+)|"content"\s*:\s*"[^"]*\[([^\]]+)\]"'

results = []
for match in re.finditer(pattern, log_data):
    if match.group(1):
        results.append(match.group(1))
    elif match.group(2):
        val = match.group(2)
        results.extend(['"' + val + '"'])

for i, val in enumerate(results, 1):
    print('vmContext.appendEvent(', end='')
    print(val, end='')
    print(');')

# vmContext.appendEvent("/payload.enc");
# vmContext.appendEvent(10);
# vmContext.appendEvent(17);
# vmContext.appendEvent("0");
# vmContext.appendEvent(18);
# vmContext.appendEvent("102");
# vmContext.appendEvent(18);
# vmContext.appendEvent("2");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# vmContext.appendEvent("2");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# vmContext.appendEvent(23);
# vmContext.appendEvent("58");
# vmContext.appendEvent(18);
# vmContext.appendEvent(22);
# vmContext.appendEvent("3");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# vmContext.appendEvent("2");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# vmContext.appendEvent(11);
# vmContext.appendEvent(20);
# vmContext.appendEvent(26);
# vmContext.appendEvent("1");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# vmContext.appendEvent(13);
# vmContext.appendEvent("2");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# vmContext.appendEvent(23);
# vmContext.appendEvent("4");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# vmContext.appendEvent("3");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# vmContext.appendEvent("2");
# vmContext.appendEvent(18);
# vmContext.appendEvent(25);
# ...