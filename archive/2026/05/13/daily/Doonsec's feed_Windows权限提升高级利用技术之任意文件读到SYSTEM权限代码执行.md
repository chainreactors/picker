---
title: Windows权限提升高级利用技术之任意文件读到SYSTEM权限代码执行
url: https://mp.weixin.qq.com/s/vn_ve-_IwNGcC3Zmy5ps8g
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:37.664840
---

# Windows权限提升高级利用技术之任意文件读到SYSTEM权限代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5FtPcWDnic0fnDQANiblyJFDA4ddeWnbUcRwAWZ9Bzan2t9P94MiaWB1G0cH8AKpu7VcpvaRpvdz7s7EvanM1hPm7xEz0KcaUB4a1zhLCWSsWM/0?wx_fmt=jpeg)

# Windows权限提升高级利用技术之任意文件读到SYSTEM权限代码执行

原创

ybdt
ybdt

卡卡罗特取西经

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 前言

逛推特时发现一个项目：https://github.com/sailay1996/vss-fr2system
我帮作者翻译一下项目名：vss-file-read-to-system，Windows下借助VSS将任意文件读取漏洞转化为System权限的代码执行

# 基本原理

## 前置知识

VSS（Volume Shadow Copy，卷影复制）：Windows 会定期为系统盘创建“快照”（卷影复制），里面备份着当前正在使用的文件

机会锁：分为二级机会锁、独占机会锁、批量机会锁
二级机会锁：允许多个用户对一个资源进行同时读，一旦操作系统检测到有对这个资源的写请求，当前锁会被回收
独占机会锁：允许一个用户对一个资源进行读写，一旦操作系统检测到有对这个资源的请求，当前锁会被回收
批量机会锁：和独占机会锁类似，但是，一旦操作系统检测到有对这个资源的请求，当前锁会保留，让其他对象等待

EICAR文件：并不是一个真的病毒程序，只是一个文本文件，内容是一段由欧洲反病毒研究所（EICAR）定义的标准测试字符串，当你把下面这行字符串保存成一个 .exe 或 .com 文件时，它就成为了一个“EICAR 测试文件”

```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

## 漏洞原理

正常情况下，Windows中普通用户无法创建Volume Shadow Copy，需要管理员权限或SYSTEM权限才能创建，但BlueHammer的作者发现了一个巧妙的利用链

当释放一个EICAR文件触发Windows Defender扫描时，Windows Defender在处理恶意文件时由于要备份会先创建VSS，处理完恶意文件后会删除VSS，整个创建和删除的过程极其短暂，但是可以在Windows Defender创建VSS后，删除VSS前，找到一个它访问的文件，提前在这个文件加上批量机会锁，这样Windows Defender访问到这个文件时，由于批量机会锁会被挂起，此时我们就有了一个可供我们访问的VSS，BlueHammer作者找的文件是RstrtMgr.dll

为防止批量机会锁出现意外而导致VSS被删除，BlueHammer的作者又加了一层保险，将程序的工作目录设置为“云同步根目录”，对操作系统来说，这个目录下应该存储的是云端文件的“占位符”，当前目录下只有我们的攻击程序，所以还需要创建一个占位符文件，创建完成后，对占位符文件施加批量机会锁，以及对“云同步根目录”施加回调函数

Defender在识别到EICAR文件后，会创建VSS、删除EICAR文件，然后还会扫描进程的工作目录（也就是“云同步根目录”），在扫描工作目录时就会访问占位符文件触发回调函数，回调函数中调用CfExecute，CfExecute由于批量机会锁会被阻塞，导致Defender被阻塞

不过vss-fr2system的作者发现，自Windows 11 24H2起，只有OneDrive进程发起“云同步根目录”才被允许，否则会被拒绝，经过他测试，对RstrtMgr.dll施加批量机会锁已经足够，所以没有使用“云同步根目录”相关代码，项目vss-fr2system的前半部分就是基于这个利用链

由于VSS中的文件也遵循操作系统ACL，想访问VSS中的SAM和SECURITY文件需要管理员权限或SYSTEM权限，所以这个项目的漏洞利用还需要一个任意文件读取漏洞，从VSS中提取SAM和Security文件后，就可以先从它们中提取密钥，再解密NTML Hash，最后借助NTML Hash以SYSTEM权限执行代码，这就是项目的后半部分

# 代码实现

项目共包括2个程序，程序1：vss\_freeze，程序2：fr2system，主要讲解vss\_freeze

## 开头部分

代码加注释一共732行

文件开头是包含需要的头文件、包含需要的静态库文件，定义宏、定义函数原型、定义结构体类型、定义变量类型

## GetWDPID

函数 static DWORD GetWDPID(void) 用于获取Windows Defender进程的PID，其中static表示此函数仅当前文件可见

## CountVSS 和 VSSFinderThread

函数 static int CountVSS(BOOL verbose) 和 static DWORD WINAPI VSSFinderThread(void\* arg) 用于获取Defender创建的VSS，其中CountVSS用于获取Defender创建VSS前VSS的数量，VSSFinderThread会每隔100毫秒检测一次，是否有新的VSS创建，这个新创建的VSS就是Defender创建的VSS

Defender创建的VSS编号是有规律的，HarddiskVolumeShadowCopy1、HarddiskVolumeShadowCopy2、HarddiskVolumeShadowCopy3，所以发现新增的1个，取最后一个编号

## CfFetchCallback 和 FreezeVSSThread

函数 static void CALLBACK CfFetchCallback(CONST CF\_CALLBACK\_INFO\* ci, CONST CF\_CALLBACK\_PARAMETERS\* cp) 和 static DWORD WINAPI FreezeVSSThread(void\* arg) 用于调用云文件同步相关的API，实现调用CfRegisterSyncRoot把当前目录注册成一个特殊的“云同步根目录”，对操作系统来说，这个目录下应该存储的是云端文件的“占位符”，当前目录下只有我们的攻击程序，所以还需要再创建一个占位符文件

对占位符文件施加批量机会锁后，再调用CfConnectSyncRoot对“云同步根目录”设置一个回调函数，一旦有任何进程（比如Defender）试图访问这个目录下的占位符文件，就会触发回调函数

Defender在识别到EICAR文件后，会创建VSS、删除EICAR文件，然后还会扫描进程的工作目录（也就是“云同步根目录”），在扫描工作目录时就会访问占位符文件触发回调函数，回调函数中调用CfExecute，CfExecute由于批量机会锁会被阻塞，导致Defender被阻塞

## ProbeVSSLiveness

函数 static BOOL ProbeVSSLiveness(const wchar\_t\* devicePath) 用于检测新生成的VSS是否可用

## CtrlHandler

函数 static BOOL WINAPI CtrlHandler(DWORD type) 用于处理快捷键Ctrl-C

## PrintUsage

函数 static void PrintUsage(const char\* prog) 用于显示用法及处理参数

## main

函数 int main(int argc, char\* argv[]) 用于对RstrtMgr.dll施加批量机会锁，查询VSS数量，释放EICAR文件，轮询查询VSS数量，发现新增的VSS，就是Defender创建的

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6GUJytibkzlaPC9BibnGbtkOsLB2JpGBK0ytS84MUWncFTBYPicJMyRtju9EhxEYo92iaBPicxzdbK9t7aDWUB5dhKA/0?wx_fmt=png)

卡卡罗特取西经

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6GUJytibkzlaPC9BibnGbtkOsLB2JpGBK0ytS84MUWncFTBYPicJMyRtju9EhxEYo92iaBPicxzdbK9t7aDWUB5dhKA/0?wx_fmt=png)

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