---
title: 原创 | 记一次某部内存取证比赛writeup
url: https://mp.weixin.qq.com/s?__biz=MzI4Mzc0MTI0Mw==&mid=2247496807&idx=1&sn=04c2888dd0301dbdb0112e8e600f2df7&chksm=eb84a933dcf32025f4129894186bfc422ebf1a5ecd3adbe5868e20c8981749c18b77156b1327&scene=58&subscene=0#rd
source: SecIN技术平台
date: 2023-02-09
fetch_date: 2025-10-04T06:08:11.196637
---

# 原创 | 记一次某部内存取证比赛writeup

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoslbbdYYsAxaqicorD05JmTiafQLiboMTpsWuibH5EXz6Ab0tIFa12d46FA/0?wx_fmt=jpeg)

# 原创 | 记一次某部内存取证比赛writeup

原创

Am1azi3ng

SecIN技术平台

**点击蓝字**

**关注我们**

**前言**

刚好前段时间蹭了某部的一个取证比赛，偶遇原题魔改部分内容，分享一下wp，内存取证还是比较有意思的，附上镜像文件分享给大家。

**volatility安装**

windows下载地址：https://www.volatilityfoundation.org/26

下载之后直接使用

**Linux安装volatitly2.6**

> mv volatility\_2.6\_lin64\_standalone /usr/local/sbin/volatility
>
> cd /usr/local/sbin
> echo $PATH
> volatility -h

安装成功

**volatility3下载地址**

```
https://github.com/volatilityfoundation/volatility3/releases/tag/v2.0.1
```

**使用环境python3**

```
python3 setup.py build python3 setup.py installpip3 install -r requirements.txt
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWofhhFfhYq7Hv7wgTftIdLzVUvq7aVcRDXu2d01MraiaSxUgsujQXe6dQ/640?wx_fmt=jpeg)

**常用命令**

```
volatility -f winxp.raw imageinfo                      # 查询镜像基本信息volatility -f winxp.raw --profile=WinXPSP3x86 pstree   # 查运行进程进程树volatility -f winxp.raw --profile=WinXPSP3x86 pslist   # 查正在运行的进程volatility -f winxp.raw --profile=WinXPSP3x86 memdump -p 324 --dump-dir=/home/lyshark    # 将PID=324的进程dump出来volatility -f winxp.raw --profile=WinXPSP3x86 procdump -p 324 --dump-dir=/home/lyshark   # 将PID=324进程导出为exevolatility -f winxp.raw --profile=WinXPSP3x86 dlldump -p 324 --dump-dir=/home/lyshark    # 将PID=324进程的所有DLL导出volatility -f winxp.raw --profile=WinXPSP3x86 getsids -p 324  # 查询指定进程的SIDvolatility -f winxp.raw --profile=WinXPSP3x86 dlllist -p 324  # 查询指定进程加载过的DLLvolatility -f winxp.raw --profile=WinXPSP3x86 threads -p 324  # 列出当前进程中活跃的线程volatility -f winxp.raw --profile=WinXPSP3x86 drivermodule    # 列出目标中驱动加载情况volatility -f winxp.raw --profile=WinXPSP3x86 malfind -p 324 -D /home/lyshark   # 检索内存读写执行页volatility -f winxp.raw --profile=WinXPSP3x86 iehistory # 检索IE浏览器历史记录volatility -f winxp.raw --profile=WinXPSP3x86 joblinks  # 检索计划任务volatility -f winxp.raw --profile=WinXPSP3x86 cmdscan   # 只能检索命令行历史volatility -f winxp.raw --profile=WinXPSP3x86 consoles  # 抓取控制台下执行的命令以及回显数据volatility -f winxp.raw --profile=WinXPSP3x86 cmdline   # 列出所有命令行下运行的程序volatility -f winxp.raw --profile=WinXPSP3x86 filescan  # 列出文件volatility -f winxp.raw --profile=WinXPSP3x86 connscan    # 检索已经建立的网络链接volatility -f winxp.raw --profile=WinXPSP3x86 connections # 检索已经建立的网络链接volatility -f winxp.raw --profile=WinXPSP3x86 netscan     # 检索所有网络连接情况volatility -f winxp.raw --profile=WinXPSP3x86 sockscan    # TrueCrypt摘要TrueCrypt摘要volatility -f winxp.raw --profile=WinXPSP3x86 timeliner # 尽可能多的发现目标主机痕迹volatility -f winxp.raw --profile=WinXPSP3x86 hivelist                                       # 检索所有注册表蜂巢volatility -f winxp.raw --profile=WinXPSP3x86 hivedump -o 0xe144f758                         # 检索SAM注册表键值对volatility -f winxp.raw --profile=WinXPSP3x86 printkey -K "SAM\Domains\Account\Users\Names"  # 检索注册表中账号密码volatility -f winxp.raw --profile=WinXPSP3x86 hashdump -y system地址 -s SAM地址               # dump目标账号Hash值volatility -f winxp.raw --profile=WinXPSP3x86 printkey -K "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"  # 查最后登录的用户
```

**题目一**

**题目提示：你能帮助小明提取出内存镜像隐藏的密码吗？**

> volatility\_2.6\_win64\_standalone.exe -f memory.img imagesinfo

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWo6kYcEmmsLtJavibpkOhw3spbA5WqvBOI8d5nUicNyBfBt8tgSdTQdia4A/640?wx_fmt=jpeg)

> volatility\_2.6\_win64\_standalone.exe -f memory.img -profile=Win2003SP1x86 pslist //查进程

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoe5ic38hDDkz9t61v63ibSGBNWPT23t6CS6ag1HV1hzibh4iaq8OVmAKmoQ/640?wx_fmt=jpeg)

异常进程`DumpIt.exe`,dump内存

> volatility\_2.6\_win64\_standalone.exe -f memory.img --profile=Win2003SP2x86 cmdscan //查看历史命令

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoCBrXdic4mmib2OaL9MceTR6gdA1FzeNtGsyq9BiaPJElkiasbuibC51NU6w/640?wx_fmt=jpeg)

历史命令涉及的进程只有两个

> volatility\_2.6\_win64\_standalone.exe -f memory.img --profile=Win2003SP2x86 memdump -p 1992 --dump-dir=./ //dump出内存

使用foremost提取文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoDUZo0n4Y8aPGic7ia1bpUzEGzCY2pwJFH1psy9vcSy8IIOoY1P8JPDog/640?wx_fmt=jpeg)

```
key: Th1s_1s_K3y00000iv: 1234567890123456
```

```
jfXvUoypb8p3zvmPks8kJ5Kt0vmEw0xUZyRGOicraY4=
```

使用在线解密，aes解密，偏移量和key都有了，解密

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWo66h1FcUibrjYibcXgAFXRCM6pGLBDpUhMqYsmtSodtBiaBQzrmwCj7OuA/640?wx_fmt=jpeg)

**题目二**

**题目：小明的文件被加密了，你能帮助小明解密吗？**

**链接：https://pan.baidu.com/s/1zTIKWY1k9IsQyRZiZIsoGQ
提取码：e6nh**

> volatility\_2.6\_win64\_standalone.exe -f mem.dump imageinfo //查看Profile

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWo1tFRKtEvXceCFo4niaef2Tq5NZAjsK9ac2wibRn3fgzIMn2IMEgt8wKg/640?wx_fmt=jpeg)

> volatility\_2.6\_win64\_standalone.exe -f mem.dump --profile=Win7SP1x64 hivedump //查询所有注册表蜂

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWovrDwicmInggWr0wypgW2Mj1f5puwRYeOBrxb1ibiapwP9wp8xhygVLBKQ/640?wx_fmt=jpeg)

实际上第二个箭头读取hash值的时候为空

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoJlb90u5ia6Xsj1N5cmNqM1hqRFiahkLXj3RBgnmQziabea8goicdTcTKdA/640?wx_fmt=jpeg)

获取到管理员用户的的ntlm值，解密，查询历史命令

> volatility\_2.6\_win64\_standalone.exe -f mem.dump --profile=Win7SP1x64 cmdscan

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoicXicia1xZwNfeoAXmZdwjvIxmtFhcauwB0OF9AQOcJ2FFJpzicoIia24zA/640?wx_fmt=jpeg)

发现提示flag.ccx\_password\_is\_same\_with\_Administrator

首先提取出flag.ccx文件然后解密

> volatility -f mem.dump --profile=Win7SP1x64 filescan |grep "flag.ccx"

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWo9ZIm7AL59xhGLtSYoYJmaRbf0OgBBBJkzvxyUhz0T4GQ1l32DgCBXg/640?wx_fmt=jpeg)

windows下无法使用查询命令，linux查询到加密文件，dump出来

> volatility -f mem.dump --profile=Win7SP1x64 dumpfiles -Q 0x000000003e435890 --dump-dir=./

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoEWy9YPaqeFYQGKWnYkEqqLVDjRt065qnLYNicrscj2HmppIibf5SsaOw/640?wx_fmt=jpeg)

且进程中存在进程"encryto.exe",所以使用该程序解密即可，挂载flag.ccx,使用密码读取文件即可

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoKaG1jxVGJbib6AIq92YVTjqP2a9CgHlEtYKhsnvibUgTOVGmBTibYkhvA/640?wx_fmt=jpeg)

**题目三**

**题目：最近小明喜欢上了维吉尼亚，小明的磁盘文件被损坏了你能帮他恢复数据，解决谜题吗？**

**链接：****https://pan.baidu.com/s/1UjnKWx2KgDBKyvs5s1ld6Q**

**提取码：o2oq**

> volatility -f easy\_dump.img imageinfo

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoxUXA9hrKicUBYzeSFtGCvia8k5nLMT8HicUKUtibS2clySibiaoxh5SxqXFg/640?wx_fmt=jpeg)

> volatility -f easy\_dump.img --profile=Win7SP1x64 pslist //查看进程

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWodZQDe5VDdAW63SyGiapbZZvzjibLyqm0d3o9Dib0GMPsicxDiciccEYoddEQ/640?wx_fmt=jpeg)

题目给出了文件损坏，涉及到内存镜像应用，提取内存数据volatility -f easy\_dump.img --profile=Win7SP1x64 memdump -p 2500 --dump-dir=./

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoujoLzNSmfCshVoDQIQII5qjoLMdl4oW1gjGnq99Vw1GpmIibOEtft3Q/640?wx_fmt=jpeg)

因为查询是否还存在镜像文件使用命令时发现存在图片，使用foremost分离

> foremost 2500.dmp

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWouxiaCU8TXlSB3HaibeicoH3IwBHhyQdjn24RNPvS6OjzibW74toL0kMR1w/640?wx_fmt=jpeg)

分离出的文件夹存在一个txt和压缩包等，压缩包使用binwalk分离，发现存在img文件，挂载的时候发现镜像损坏，需要恢复数据

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoyjAufKjHpicxBGZeZI65L6NOyKSXrvPTib0hEPw5z0B47k1V8wf0wrXw/640?wx_fmt=jpeg)

这里我使用磁盘恢复工具DiskGenius无法恢复，kali下自带磁盘恢复工具testdisk

> testdisk message.img

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoib1RJQwco4cl4862f2PxD1Ck4pOTAqmLMicKNhg1icjQZwl0fpE0OTRxw/640?wx_fmt=jpeg)

`c`恢复文件，q退出可以看到恢复的文件.message.swp

![](https://mmbiz.qpic.cn/mmbiz_jpg/xkA3iaCzeYprbpSm7KU3OSQtXlxhILVWoayiaXZZ51Io5jKUqWvlQmaQZtYPksyffprJfE1aWNubXPrCpWfeY0Jg/640?wx_fmt=jpeg)

hint.txt中的数据类似于坐标，根据脚本还原

```
import matplotlib.pyplot as pltimport numpy as np
x = []y = []with open('hint.txt','r') as f:   datas = f.readlines()   for data in datas:        arr = da...