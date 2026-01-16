---
title: DIDCTF-2024盘古石杯决赛内存分析+2025陇剑杯siem与勒索软件入侵响应
url: https://mp.weixin.qq.com/s/G_xILM1YZ43vfWj92_Tvlw
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:27:12.112891
---

# DIDCTF-2024盘古石杯决赛内存分析+2025陇剑杯siem与勒索软件入侵响应

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HtG3DtQMd7NFkFazChvynvvziat2aNSR2zDqKtXc6buXS8XFbtWP7FtRGwUV4xYtevqibs7b1LqZVEQCwVv6icwmg/0?wx_fmt=jpeg)

# DIDCTF-2024盘古石杯决赛内存分析+2025陇剑杯siem与勒索软件入侵响应

原创

北渚
北渚

南有禾木

![]()

在小说阅读器中沉浸阅读

# 前言

记录DIDCTF中的2024盘古石杯决赛的内存分析题和2025陇剑杯的题目，因为题目比较少，所以这两个比赛的题目放到一起记录了。

陇剑杯只有siem和勒索软件入侵响应这两个题。

题目与检材都来自DIDCTF平台：`https://forensics.didctf.com/`

## 一、DIDCTF-2024盘古石杯-决赛-内存分析

## 检材下载

下载链接：`https://pan.baidu.com/s/14qt_m5ufWHX8yqwXVC8yiA?pwd=dzcn`

哈希值：`MD5：27457E88CB503E08087DA724795E5FC9`

挂载/解压密码：`检材容器密码: f38043615a64f2a4013b0511c89bb07f 3D案情密码: DFD99BB7E073901A33D382A1431FC90E 3D案情登录信息: 账号: 11111111111, 密码 111111`

## 1、内存分析

### 1.1、给出进程别点我.exe的进程ID

有了Lovelymem，也懒得用vol的命令了，直接把内存镜像加载进去：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2GDViabQ1nS8h05SkNlQEjby2zVU6Og8W10hhqcPrJL8l6Cnu2iawSNJQ/640?wx_fmt=png&from=appmsg)

然后点进程信息，查看运行的进程，往下翻，找到`别点我.exe`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2vZU6yB1tArUBKHlf8akCFWZAicbmLeB5RSa4tWrVa38x80vic9HUnCow/640?wx_fmt=png&from=appmsg)

进程ID：`2872`

### 1.2、FTK Imager的程序版本号

从进程中看到了FTK Imager程序的信息，本来想着从路径中看到版本号，不过可惜没有：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2u6EhJff2VbjNicGGnoogBEOTRwQVatWNDqF9KrrPQqRPvf0zrluF1aQ/640?wx_fmt=png&from=appmsg)

那就只能导出来这个文件分析了，查看全部文件，然后搜索`FTK Imager.exe`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2A92YTXic5lzsar4DMk3o5QgepqK44QTt2qH4YfjyibibCQELDZong8xDg/640?wx_fmt=png&from=appmsg)

定位到`\Program Files\AccessData\FTK Imager\FTK Imager.exe`这个文件，保存下来……

搞了半天都导不出来……最后总结一句话：这个内存镜像用Volatility2读取不了

用vol3可以导出文件：`python vol3.py" -f PC.mem  -r csv windows.filescan > filescan.txt`

```
扫描的结果如果直接输出到控制台是没问题的
如果要保存到文件中会因为编码问题报错
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2Vxe9pdBB0luiamlEUPq3D63tDmIbx78gDf5r9jPjTsFjta6F1pRjdsQ/640?wx_fmt=png&from=appmsg)

两个解决办法：

```
方案 A：临时生效
在 cmd 里先执行：set PYTHONIOENCODING=utf-8
然后再跑命令：

方案 B：改成 UTF-8 控制台
chcp 65001
set PYTHONIOENCODING=utf-8
```

然后再执行 vol 命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2oRkgeyYyPcqvH6ngSVB0SPic8XQwODbiaymOL0HmmZo6pia7eJtT7RiaYA/640?wx_fmt=png&from=appmsg)

然后导出文件：`python vol3.py -f PC.mem -o D:\output windows.dumpfiles --virtaddr 0xab866311aec0`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2AAH2Via0jzKh4aQTicROyAr4u3DUvZn61UFdOuSMS8odHJ4o9iaw0yzRA/640?wx_fmt=png&from=appmsg)

导出来后右键查看其详细信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2ZtNh3beN5ibv9cnK3iblR80bYsInJECcCiaduvpGJNu9Ka0ccFPRhUMibw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2gBKj1vLVn082ZMTAnVHSlDibGBzPGAdQw07rg1jZpFGfn44ZrwpBQMA/640?wx_fmt=png&from=appmsg)

版本号：`4.7.1.2`

### 1.3、给出向日葵使用时，计算机内网的IP地址

先看看目前计算机有没有运行向日葵，如果在运行，就直接看网络连接就有IP地址：`python vol3.py -f PC.mem -r csv windows.pslist > pslist.txt`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2M4ZkabfaMFiaCryYOic2zvvjMZLloWxBrlES46o1JKQBvzCEMnqTlGAA/640?wx_fmt=png&from=appmsg)

发现向日葵是在运行的，那么查看网络连接即可：`python vol3.py -f PC.mem  -r csv windows.netstat > netstat.txt`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2V6LZtSoAxHuHmZKBunoKnk4nVjaCGsibR8XmImNPNNAvibRlF8n6EXvA/640?wx_fmt=png&from=appmsg)

然后看到了`SunloginClient`的连接：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2mX7fT4znnvStRKSZaMBSvnL4mOTEZUERiaazX3A9sR1VBswYPzQhvhw/640?wx_fmt=png&from=appmsg)

所以内网地址就是：`192.168.217.172`

## 二、DIDCTF-2025陇剑杯-siem与勒索软件入侵响应

## 案情介绍

siem：https://pan.baidu.com/s/1VwOhElaFgj71IVu66m4HYg?pwd=8n7j

解压密码：x2p1nsWFG4KfXp5BXegb

Web地址：http://IP:80

账号密码admin/admin

---

勒索软件入侵响应：https://pan.baidu.com/s/1NxLZj-TOWaMcMJkAhK6qcQ?pwd=ms5w

解压密码：4iuxXAaJ6ogjFhh61KFW

虚拟机系统密码：joomla/5fe6cebe-386b-417f-84d5-8d17e8801950

## 1、siem

先把题目提供的`wazuh-2-wazuh.ova`创建成虚拟机：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2WmFXSMy9bBOO8J1icqoJRjtjH0gfV3oVwic8x3PQiaG2ygZwDLjs5z1dw/640?wx_fmt=png&from=appmsg)

看到虚拟机描述：

```
Wazuh enhances security visibility in your infrastructure by monitoring endpoints at the operating system and application levels. Its capabilities include log analysis, file integrity monitoring, intrusion detection, and compliance monitoring.

简单理解：
Wazuh 是一款开源的 XDR 与 SIEM 一体化安全平台，通过在终端部署代理，从操作系统与应用层持续监控，提升基础设施的安全可见性，核心能力覆盖日志分析、文件完整性监控、入侵检测与合规监控，适配本地、云与容器化环境
```

开机后直接能看到User和Password：`wazuh-user/wazuh`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2mp78FTGm2qllbyib3NYp6a5YwKDebI8Tpibshg5N5FNsMicmvrSkyaOTQ/640?wx_fmt=png&from=appmsg)

那也不用重置密码了。

### 1.1、攻击者的ip是什么

既然这个wazuh有入侵检测，这个题应该就是让分析流量的，先访问平台

不知道端口，查看一下`netstat -ntlp`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2VYUTCCibrsDXE4uj1ibsiclicGGrMZhmUVtpfMj8f6iaOS68HlKmx56JdEw/640?wx_fmt=png&from=appmsg)

开启了443端口，尝试直接https访问：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2HiaOUetfZuot0FM7Q3SQRKtd10Vicibibt77QpibZtY3uogx2bhhODaUBicg/640?wx_fmt=png&from=appmsg)

访问到了，题目介绍中说了web服务的账号密码是`admin/admin`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2mOQoYBogYNuGHvgtjicCJv58akVfyzlGJau0icfafWVT3FfKAOPDSaGA/640?wx_fmt=png&from=appmsg)

进来后也是胡乱一通点，最后在`Discover`页面看到了捕获的攻击日志：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2gTx8Dv8yPnhGUqQcyW8Uc62N4ZKfySzx7B1ma7o0eqGa1tS1Eicxzmw/640?wx_fmt=png&from=appmsg)

这里记得右上角给时间跨度拉的大一些，有捕获记录的是`Dec 18, 2024`，其中尤其在14:22左右流量最多：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR20ZEpyiamxRLo4KwpxOaW01BVc8iaqgwjVPtnR42Elc5sVbgicWVWlFxfw/640?wx_fmt=png&from=appmsg)

看这些请求的流量数据，就是在目录扫描，所以这个肯定是攻击者了，注意wazuh的字段：

```
agent.ip是探针的IP
data.script是这条请求的源IP
```

所以攻击者IP：`192.168.41.143`

### 1.2、在攻击时间段一共有多少个终端会话登录成功

做这个题之前先重启一下wazuh服务，不然网站的数据是异常的：`sudo systemctl restart wazuh-manager`

定位攻击时间是`Dec 18, 2024 @ 14:21:48.525`，攻击者就是从这一条开始进行的目录扫描：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2v4rXdJicg4qzia1SnDCd8OqbmHa65vSDcZ1UbjntwSMEX00AK3pCJc3A/640?wx_fmt=png&from=appmsg)

然后点开`Threat Hunting`页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2vVibqYJXtgjL7kMdsn2fmY4ibgIWIHqEYPkJ4f2auKufgibAkWUIHwKUA/640?wx_fmt=png&from=appmsg)

进去页面后右上角把时间调整到`Dec 18,2024`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2P5kibymTHWUBMeBtYhYAkCnQb1DvDBwnicfvZSE8qcjcUEdtGrjRlhVg/640?wx_fmt=png&from=appmsg)

这里已经能看到`Authentication success`的次数是`13`

### 1.3、攻击者遗留的后门系统用户是什么

点开`Threat Hunting`的`Events`页面，调整时间为攻击时间段：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2kS4jUMRt8DYK9xGezVQJkLUGxYEjvyrsibibuwNYTAZvs1z7tLnqIXSA/640?wx_fmt=png&from=appmsg)

然后往下拉，能找到添加用户的日志：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR23EyQyvVRJGRDGzc7MpwbJ4lUvKGHsdha1F4Pd0SJesawdnSrqqNtAQ/640?wx_fmt=png&from=appmsg)

点击左边的放大镜图标，查看详细信息，new user: name=`hacker`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2vvynsqz9kRcuwiaKoqTKPViar4lIdzjwPg41rs8IF8cVkHYfJXaNticPA/640?wx_fmt=png&from=appmsg)

### 1.4、提交攻击者试图用命令行请求网页的完整url地址

用命令请求地址的话大概率就是`curl`了，去Discover界面里直接搜：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2rInWeDaa0b9uBI1cSRunfia6TY7nGKDIsaKFlThAu46ibhtEP5BIibvxQ/640?wx_fmt=png&from=appmsg)

筛选出来了两条日志，但是第二条明显是本地执行了SQL查询，所以肯定是第一个，题目问的是完整URL地址，把鼠标放到`/.back.php?pass=id`这个位置，右下角直接出来了完整的链接：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2XD65nkZHnMNSCStZkyvps8JF6iaVm8hv3T3lKiaYUe30icxNQicdOsxITw/640?wx_fmt=png&from=appmsg)

完整URL：`https://192.168.41.146/.back.php?pass=id`

### 1.5、提交wazuh记录攻击者针对域进行哈希传递攻击时被记录的事件ID

首先wazuh中关于哈希传递的关键字是`Possible Pass the hash attack`（不知道这个的话确实没法搞啊）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HtG3DtQMd7NFkFazChvynvvziat2aNSR2mPfrDaiaB71RWoZkib77F3tj6Ou4R9KA0boDEle8y2rCKv6ZUw165f9Q/640?wx_fmt=png&from=appmsg)

然后...