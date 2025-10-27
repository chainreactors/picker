---
title: APT28 样本分析报告
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458480122&idx=1&sn=2b6f4541ee1df402779618b4ba4b508c&chksm=b18e5d7086f9d4665a6eb127edd3422c559dfdd70e11906c41cf6e5d7b13bb0f0c41b9601ba6&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-11-01
fetch_date: 2025-10-03T21:26:22.093287
---

# APT28 样本分析报告

![cover_image](https://mmbiz.qlogo.cn/sz_mmbiz_jpg/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRyHeINgICKe0jVuHVthZnvWWn2km1gpgsiby3ib53ib7C5aXN2GvficWWpg/0?wx_fmt=jpeg)

# APT28 样本分析报告

逆时针向左

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRT3s6Gnc2691Jy65YqlemhLoVhjVeBrWF0L8rBrTkltep8sjvYOEbqw/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：逆时针向左

##

```
一

样本HASH
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E7quPRj1DdNZg3ob95WqhcO1nx3xYOtKn6icCu9CwPe3sfibGnnQr20r5YuDdxuIXme27JTQh75KYA/640?wx_fmt=png)

##

```
二

基本信息
```

**1、壳信息：无壳**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRVmbFoCCibl3y8oMDmmtOp4kQYUECZYk2alice6yEJ25NYo3cqyFzf84g/640?wx_fmt=png)

**2、关键API**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPR4ELIH19Zw2gmygZbZ4y4lRDhZfTJFWia7I8B5UgLBIQRHEdEyJVsibTA/640?wx_fmt=png)

**3、没注意到什么关键字符串。**

##

```
三

行为分析
```

**1、注册表监控：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRZK6ooIgybrXJZOGouiaEIXbb5a83lQacCWuic4km5ibRaSbSF7YGmpsZg/640?wx_fmt=png)
关键在设置 Environment\UserInitMprLogonScript 为 C:\Users\Reverse\AppData\Local\cdnver.bat 实现持久化。

**2、文件监控**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRYepl3Siaoq3z6WTosQEuldsLHmgiaFicHiasF9egLJOUjc7rAHEHiaUyAug/640?wx_fmt=png)
在 LOCALAPPDATA 目录下释放了两个文件：cdnver.dll 和 cdnver.bat；
cdnver.dll 的 MD5 为 AA2CD9D9FC5D196CAA6F8FD5979E3F14
bat 脚本内容为：start rundll32.exe "C:\Users\Reverse\AppData\Local\cdnver.dll",#1

**3、进程监控**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRRbicXEMyPfib88QYGY4w8tuVBxrDHDlUqtSDoylhicNKI9Nzj7C8TIzkA/640?wx_fmt=png)
创建进程 rundll32.exe，加载释放的文件：cdnver.dll；

从行为监控中也可以看出（释放隐藏文件、隐秘执行）：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRibKGNJAoVNm2Dw4elW0xl6To3ic8vsuQ1RaavFXS6MVqs3Jf1LfhvvwQ/640?wx_fmt=png)

**4、网络监控**
使用 FakeNet，捕获得域名 cdnverify.net，使用奇安信威胁分析平台查询：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRKiclRc80mr92lYNruXfF2piaI5d1Gmve7CJAM3NKWSQbR7KMx6H9oPpg/640?wx_fmt=png)
可以确定该样本与 APT 组织有关。

#

```
四

详细分析
```

使用 IDA 打开后，停在 WinMain 处，x32dbg 的 Base 为 0x00EF1000，在 IDA 中 Rebase 为 0x00EF0000，则 WinMain 的地址为 0x00EF1ECF：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRBWTXCEaSalTDzj3XHXTociaTYrnv20C3XlI3QWyXicO2f9a2ANClKh8A/640?wx_fmt=png)

在 WinMain 中，连续调用了 sub\_EF1DEF() 三次，该函数内有 XOR 等操作，猜测为字符串解密操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRNVsOeVQK7eiajqLqKeaZWiaOIK80vLDYm63VOibHHAFPh1O2xtqnL8yFQ/640?wx_fmt=png)
结合 x32dbg 可知：

```
第 1 次调用，解密字符串：SystemRoot\\SysWow64第 2 次调用，解密字符串：SystemRoot\\System32第 3 次调用，解密字符串：TEMP
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPR30lVtp1cURZn9dJMDRoXibL5HcwxOxMbHnvOO49nHShpPvdef4nGzPA/640?wx_fmt=png)
因此，重命名 sub\_EF1DEF() 为 decryptStr\_sub\_EF1DEF()；之后调用函数 sub\_EF12D3()。

## **4.1、sub\_EF12D3 - 解密PE**

连续两次调用 sub\_EF1063()
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRxomy4Imwd69vlD9Xb5ygxJOCYaKmqNNTp921p0fiaWVb1dlUxNIAbyQ/640?wx_fmt=png)

###

### 4.1.1、sub\_EF1063

查看 sub\_EF1063() 内部代码后，猜测也是执行字符串解密操作：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPR9yTicYwXyZH3PvsZGOmnJmZOjWpDLgfOjgsfg3iaYZMrAk0cRMfMzSgw/640?wx_fmt=png)
结合 x32dbg 可知：

```
第 1 次调用，解密字符串：cdnver.dll第 2 次调用，解密字符串：LOCALAPPDATA
```

因此，重命名 sub\_EF1063() 为 decryptStr\_sub\_EF1063()；之后调用函数 sub\_EF1000()。

### 4.1.2、sub\_EF1000

内部代码看着也像是在进行解密操作，对 0x00F0B880 处的 0x59BD 字节的数据进行解密，解密后的数据如下，可以很明显地看到 4D5A：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRVaOWdn9bbxKlqdpvQaFjcgJujibYTnXPBu9HYAIq8mqvLRlBUaJSjHg/640?wx_fmt=png)
解密出一个 PE 文件数据后，函数结束；sub\_EF12D3() 分析完成，返回到 WinMain()。

## **4.2 sub\_EF13F7 - 解压缩PE**

连续两次调用 decryptStr\_sub\_EF1DEF()，解密字符串，可以看到是与解压缩有关的 API ：RtlGetCompressionWorkSpaceSize 和 RtlDecompressBuffer；

注：RtlGetCompressionWorkSpaceSize 函数用于确定 RtlCompressBuffer 和 RtlDecompressBuffer 函数工作空间缓冲区的正确大小。

之后调用 LoadLibraryW 加载 ntdll，并调用 GetProcAddress 获取上述两个 API 的函数地址；

调用 RtlGetCompressionWorkSpaceSize 获取缓冲区大小，在调用 HeapAlloc 申请空间；

最后调用 RtlDecompressBuffer 对刚刚解密出的 PE 数据进行解压缩：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPR3SqNl8CFEU9ZTpc4qAYSCKyzNicollw10kOiciawDtUG1O9hibb9Nq04icw/640?wx_fmt=png)

##

## **4.3、sub\_EF155B - 释放DLL**

### 4.3.1、sub\_EF10CD

连续调用两次 decryptStr\_sub\_EF1DEF，解密得到字符串：SystemRoot 和 \\System32；

之后调用 GetEnvironmentVariableW 获取 LOCALAPPDATA 环境变量：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRCbZiajn8kqIlibPBUE6p4ctia6NBD83Vuvqib01dRZ68NxZClVxbGfWvXA/640?wx_fmt=png)
这里为：C:\\Users\\Reverse\\AppData\\Local，再将 "\cdnver.dll" 与之拼接得到了释放文件的目标路径：

C:\\Users\\Reverse\\AppData\\Local\\cdnver.dll
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPR5J4iaMZknTXHpCzvvwRkOichmo3SflFdJeK2PiaaUql9l62OChrT15TRQ/640?wx_fmt=png)
返回 sub\_EF155B 继续执行；

### 4.3.2、sub\_EF155B 继续执行

调用 LoadLibraryW 加载 Kernel32.dll，并获取 CreateFile 函数地址并调用，创建文件：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRMsZ0N8CpQwU2J05NQwHUnKlLjFS2z0uHAA2cLFXAWlzhgllMggIGjw/640?wx_fmt=png)
获取 WriteFile 函数地址并调用，把 PE 数据写入文件：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPR3AqBEZZ3zxTIADKoWNWYBwLQawsOuYNYwvBLRtelcXibQJGADqYwvhg/640?wx_fmt=png)
文件释放完成。

## **4.4、sub\_EF264C - 权限维持**

连续 7 次调用 decryptStr\_sub\_EF1DEF 进行字符串解密，得到：

```
rundll32.exe#1UserInitMprLogonScriptcdnver.dllEnvironmentLOCALAPPDATAcdnver.bat
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRcddJa1vOxMO1DD8N2rdTL2IE0t03arAOrqLNbFWRwLnnBELDYF2aQw/640?wx_fmt=png)
调用 LoadLibraryW 加载 Advapi32.dll，并获取 RegOpenKeyExW 函数地址，并调用，其中 0x80000001 是 HKEY\_CURRENT\_USER：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRR0SgCxrQDY9cl6OaO0g87y1gE5dpgsr2M3aibF2bGp0o6cyFdf7O8tw/640?wx_fmt=png)
获取环境变量，并判断：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRsku1l0VoSk6IuhoAicECdTHuUMdgZl361ic0uveSTUBUEiaAibQv9VHeoQ/640?wx_fmt=png)
从 ”cdnver.dll“ 中查找 "."，获取文件后缀：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRV7npp4laylcdI9cZopqVsYa7JGVg00gX4O4D5HJlicicW6zV7I5afOdg/640?wx_fmt=png)
之后确认只有一个 "." 出现。

###

### 4.4.1、sub\_EF2030 - bat脚本

连续 6 次调用 decryptStr\_sub\_EF1DEF 解密字符串：

```
startLOCALAPPDATAcdnver.dll#1rundll32.execdnver.bat
```

调用 WideCharToMultiByte 将宽字符转为多字节字符；

调用 LoadLibraryW 加载 Kernel32.dll，\_getenv 获取环境变量，获取 CreateFileA 的函数地址并调用创建文件C:\Users\Reverse\AppData\Local\cdnver.bat：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRsfLOVasjM1wvMeHNQibb8SSQr9DWTowSv2Yq6L4FdOI93FDaNwo1xyg/640?wx_fmt=png)
构建脚本字符串 start rundll32.exe "C:\Users\Reverse\AppData\Local\cdnver.dll",#1，调用 WriteFile 将脚本写入 bat 文件。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPR008ibYA9QqhEicR6etIyBhC5Fcs6iaboVYB7RD6RJ1RLdiaicPBb1K1kjCA/640?wx_fmt=png)
返回 sub\_EF264C 继续执行；

拼接构造字符串 C:\\Users\\Reverse\\AppData\\Local\\cdnver.bat，
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRWA7EX3l4s25W5BiaMM3o2aDfUZvjEIjNic1sMllkpibia4hjZYia21e5z3g/640?wx_fmt=png)
调用 LoadLibraryW 加载 Advapi32.dll，获取 RegSetValueExW 函数地址，
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPREfwIw5AV6u2CNTud4FI18ib7icLDlpxyApgs286ibjw2dwnDlO2hMV1rQ/640?wx_fmt=png)
设置注册表，使用 Logon Scripts 机制实现持久化：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRpUSldNdxDYaxicJeYRlU7HtEIYGJqy9dWzAzFHSiaXVfRU7DxibFdNCSw/640?wx_fmt=png)

Logon Scripts 机制：Windows允许在特定用户或用户组登录系统时运行脚本，也就是能使脚本优先于杀毒软件执行。

注册表设置前后对比：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRJxGicqJnhoeOWN8tfI7YW6SjmszCA32R5CRfic4zicsj3H2znRB67TMmA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HpIfmoah1dOUIuxHB8sibPRkFxG9TfkVFXDoq1jiaQozIVmqVKaZ6VB6rNibhjfrfguViakN0ZJlNJmg/640?wx_fmt=png)

##

## **4.5、sub\_EF1707 - 执行dll**

调用 \_wcsstr 函数在 cdnver.dll 路径中查找 ".dll"：
![](https://...