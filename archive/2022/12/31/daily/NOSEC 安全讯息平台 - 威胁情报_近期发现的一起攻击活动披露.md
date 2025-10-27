---
title: 近期发现的一起攻击活动披露
url: https://nosec.org/home/detail/5054.html
source: NOSEC 安全讯息平台 - 威胁情报
date: 2022-12-31
fetch_date: 2025-10-04T02:47:54.839019
---

# 近期发现的一起攻击活动披露

[![](https://nosec.org/home/image/logo.png)](/)

[登录/注册](https://nosec.org/home/caslogin)

[投稿](https://nosec.org/home/caslogin)

[首页](/home/index)
[威胁情报](/home/index/threaten.html)
[安全动态](/home/index/security.html)
[漏洞预警](/home/index/hole.html)

数据泄露

* [新闻浏览](/home/index/leakage.html)
* [图表统计](/home/index/graphshtml)

[专题报告](/home/index/speech.html)
[技术分析](/home/index/skill.html)
[安全工具](/home/index/tool.html)

# 近期发现的一起攻击活动披露

![](https://nosec.org/home/image/headImg.png)ddddddd9  1008天前

# ![top.png](/avatar/uploads/attach/image/c5d98030f28f040989069217090f773d/top.png)

# 摘要

近期，白帽汇在用户现场发现一起持续活跃的恶意软件攻击活动，本次活动的恶意软件为Plug X RAT 新变种。后续根据攻击时间和攻击手法关联，推测本次攻击者同样使用了gh0st RAT。本次发现的攻击活动中检测到攻击手段为：传播影音播放下载器、迈克菲杀毒软件、TG通讯软件，后续下载安装RAT工具。我们通过流量监测设备发现异常告警并后续定位到了恶意软件。根据资产测绘搜索到的开放情况、捕获样本、威胁情报综合判断该活动开始于2022年10月，至今处于活动状态，攻击较为频繁。

# 异常告警

```
【Suricata-告警信息】
时间：2022-11-17 11:34:11
详情：ET TROJAN Trojan.Win32.DLOADR.TIOIBEPQ CnC Traffic
攻击流向：172.16.xx.xx:xx166 -> 45.116.161.95:53
IP详情：
172.16.xx.xx （xxxx - xxxx中心）
45.116.161.95 （None）
```

## 流量日志

域环境，办公内网客户端的DNS解析服务由内建服务器承担，恶意程序的域名查询指定8.8.8.8响应DNS-query。

```
[zeek.dns] {"ts":1668657146.372384,"uid":"CmxrDs3cd5ZPsVS3pg","id.orig_h":"172.16.xx.xx","id.orig_p":57620,"id.resp_h":"8.8.8.8","id.resp_p":53,"proto":"udp","trans_id":21178,"rtt":0.745607852935791,"query":"googleupdate.luckfafa.com","qclass":1,"qclass_name":"C_INTERNET","qtype":1,"qtype_name":"A","rcode":0,"rcode_name":"NOERROR","AA":false,"TC":false,"RD":true,"RA":true,"Z":0,"answers":["45.116.161.95"],"TTLs":[64.0],"rejected":false}
```

* 指定谷歌DNS 8.8.8.8进行响应 DNS-listener的请求日志

![1.png](/avatar/uploads/attach/image/5aa422f896224344a41a4503f7b3befb/1.png)

响应日志C2：45.116.161.95 UDP：53

DNS answer : unknown type=1024

rcode :0 NOERROR无错误条件

![2.png](/avatar/uploads/attach/image/7056e3aa5c4abaa534b837279f2e9fd8/2.png)

UDP ：137

![3.png](/avatar/uploads/attach/image/240ee076d1491c0e0fce76022791c5ff/3.png)

TCP：53 DNS 服务

rcode：6 YXDOMAIN 6确实存在一些不应该存在的名称。

![4.png](/avatar/uploads/attach/image/1f69a83f22438448cc891cac5930918c/4.png)

HTTP记录日志，理解为心跳包

![5.png](/avatar/uploads/attach/image/77a3e12824ee297536cb1a537b5b86ca/5.png)

![替补2.png](/avatar/uploads/attach/image/23613a963a674eda2542bb1e6aabd925/替补2.png)

通讯端口统计分布

UDP  DNS Port 53，137

TCP HTTP Port 8080,443,80

![总计.png](/avatar/uploads/attach/image/1f7ca46757f4e571ec678a2ad67e2372/总计.png)

流量中数据包大小

![替补3.png](/avatar/uploads/attach/image/850289708570cc681ad9ef856b563710/替补3.png)

# 威胁情报

在看到告警后，查看流量日志行为，同时使用开源威胁情报查询，查找到1个域名关联该IP信息，然后查询子域名总共获取3个子域名；

攻击者创建域名，多为常用软件服务名，更新update这些关键字组合创建。

```
googleupdate.luckfafa.com 45.116.161.95
wpsupdate.luckfafa.com 14.192.67.187
microsoftdefender.luckfafa.com     210.56.54.12
www.luckfafa.com
```

## Virustotal

<https://www.virustotal.com/gui/ip-address/45.116.161.95/relations>

![6.png](/avatar/uploads/attach/image/7b3cf7717824abeaa7efc40750bf2e6e/6.png)

## 子域名

# ![7.png](/avatar/uploads/attach/image/52f23449fe7d061d27b84aa1810cb84c/7.png)

# 捕获样本

## 回连恶意IP

```
Process Nmae: svchost.exe
PID : 7216
```

看到运行的程序是svchost.exe，恶意程序注册服务运行；

![8.png](/avatar/uploads/attach/image/22a22ef2b39faf0fc9e80c0acd8fa580/8.png)

## 删除日志

可以看到机器中10.25存在删除日志的行为，并且当天无任何其他安全日志。这时候体验到了没有日志记录的难题，攻击者删除之后相当于真的找不到了……

![图片2.png](/avatar/uploads/attach/image/15ca7a8cfd9e89cde4664f2acd8cfcd7/图片2.png)![图片3.png](/avatar/uploads/attach/image/ea4d2acd33903a8635e3b6803a81cc60/图片3.png)

## attrib隐藏属性

后面使用Autorunx64.exe发现了和子域名相同命名的服务`wpsupdate`和`googleupdate`同时运行的程序为`ASUS.exe`，使用everything查找到了文件的具体位置，这里攻击者使用了`attrib.exe`这一个命令将木马文件和所在目录全部设置增加了系统属性和隐藏属性，我们需要在该目录中使用相同的命令以管理员权限将上述属性取消，随后看到了目录下的恶意程序。

```
attrib -S -H *
木马路径 系统属性 隐藏属性
C:\windows\programdata\googleupdate\
C:\windows\programdata\wpsupdate\
C:\windows\programdata\timo\
```

服务信息如下：

* 服务名称 googleupdate /wpsupdate
* ASUS Com Service
* ASUSTeK Computer Inc

![9.png](/avatar/uploads/attach/image/2cc5ccb82f0f05aee63ba80b27080037/9.png)

## 键盘记录器文件

仔细查看了键盘记录器记录的东西，相对是很详细的，时间戳、进程名、执行的动作、浏览器中的点击。

![10.png](/avatar/uploads/attach/image/30e383554a884995ddeef82c8c25d011/10.png)

![11.png](/avatar/uploads/attach/image/7b09d4b3fe364b2e5e0c7e5ffe533ecc/11.png)

使用SublimeText打开，更改编码查看如下:

![12.png](/avatar/uploads/attach/image/b39146657b117494a8b5890880f28587/12.png)

## 恶意样本

![13.png](/avatar/uploads/attach/image/18b3de252d5365e7c96d37efde4dc4b1/13.png)

```
➜   tree
.
├── googleupdate
│   ├── ASUA.exe
│   ├── ATKEX.dll
│   ├── debug.dump
│   └── NvSmart.x64.hlp
├── timo
│   ├── ATKEX.dll
│   ├── debug.dump
│   └── logo.png data
└── wpsupdate
    ├── ASUA.exe
    ├── ATKEX.dll
    ├── debug.dump
    ├── NvSmart.hlp
    └── NvSmart.x64.hlp

3 directories, 15 files
```

通过获取到的`ATKEX.dll`在virustotal关联到样本父文件`61402F53A8918246C791E332FB33848D`关联到RAT情报

SHA-256

057e908cd15f95a9768989c0455ae9a24a65c46a5022f5fa1adfe7c7a8a4b6a7

![14.png](/avatar/uploads/attach/image/f475669873ea0b842783aebeb137e80c/14.png)![15.png](/avatar/uploads/attach/image/d1b911d3c479d7dff4efa5b111c3ad34/15.png)

本次发现的为该工具Plug X RAT的新变种

同时从本次获取到的恶意木马回连IP中一共获取到3个已经公开的恶意样本

![16.png](/avatar/uploads/attach/image/1feaebd2533784a6de9a0f3e2715fb4c/16.png)

<https://www.virustotal.com/gui/file/7fa8231dc167ec6aa87874a10d3daf798407a37c11bb921efb05664dfafdb38f/relations>

<https://www.virustotal.com/gui/file/160c121252521823abba5263da264469baf1489766f18b074334cf41ca3d0546/relations>

## 情报关联

由`c81b31f8986cc40ff2d31c3bafd7abdf275826ccb5859eba8d927144e38bc7f3`程序关联到的威胁情报中已经公开样本程序`<https://www.virustotal.com/gui/file/c81b31f8986cc40ff2d31c3bafd7abdf275826ccb5859eba8d927144e38bc7f3/relations>`![17.png](/avatar/uploads/attach/image/e92abdec38295d2465f75e715a532d3b/17.png)

威胁情报关联到的gh0st RAT样本

![18.png](/avatar/uploads/attach/image/68b6b1fd02578cf8735c06564a70f166/18.png)![19.png](/avatar/uploads/attach/image/ba525f1617ecdf04a006e3cc39f4d21b/19.png)

# 木马程序基本执行流程

![20.png](/avatar/uploads/attach/image/f300225ebf9fa1f87d255ab96efded2f/20.png)1. 有签名白程序 + 黑 dll 注册服务运行

2. 复制到指定目录；

3. 设置自身和目录为系统属性（attribute +S +H）；

4. 将目录设置为隐藏属性；

5. 将带有签名的程序注册为服务执行程序为ASUS.exe； 创建1个挂起的svchost进程，将shellcode注入目录结构中data属性文件为shellcode；

# Fofa

* 目标的53端口为HTTP协议

![21.png](/avatar/uploads/attach/image/0a070cc926f1a135a721a93173c9990f/21.png)![22.png](/avatar/uploads/attach/image/42c4f2ef004b167c05a85ffddfb3bcb9/22.png)

## listener 特征

通过fofa搜索到的开放端口和组件，监听的HTTP-Listener，提取到所有特征，然后根据该特征搜索整个互联网上符合的IP。

```
header="Server: Apache 1.3.27" && header="Content-Type: text/html" && header="Accept-Ranges: bytes" && header="Content-Length: 80" && header="HTTP/1.1 404 Not Found" && header="Connection: close" && body="<B>The Page You Requested Was Not Found!</B>"
```

# ![23.png](/avatar/uploads/attach/image/f00aaef34c0f9f581bbcca7cb5fd121e/23.png)![24.png](/avatar/uploads/attach/image/1e68372e5697c47ec8d8e264107491e9/24.png)

# 时间线

本次发现的攻击活动的时间点2022-11-17 11:34:11 发现告警 随即开展排查和后续定位

* 木马运行时间 2022-10-25 10:05 （根据木马程序系统时间获得）
* 日志删除时间 2022-10-25 09:57:23 （根据主机事件查看器日志获得）
* C2通讯时间 2022-11-03 08:21:14 （根据流量日志记录获得）
* 键盘记录一 时间 2022-11-04 09:11:43 （根据发现的键盘记录器存储文件获得）
* 键盘记录二 时间 2022-11-08 12:07:29 （同上）
* 流量异常发现时间 2022-11-17 11:12:10 监测到流量异常行为的时间

![替补.png](/avatar/uploads/attach/image/f9fddbb88f053b7dd6bcb6f6be2fa1b4/替补.png)

# 总结

* C2平台：Plug X RAT、gh0st
* 前期：攻击者载荷投递方式为在破解软件/绿色软件需求的论坛和群组；
* 权限维持：白加黑的方式，注册系统服务保障自身每次开机自动运行；
* 痕迹清理：在软件安装完成后自动删除当天日志；睡眠间隔7天后与C2域名进行通讯；
* 信息窃取：小流量数据包，利用键盘记录器获取受害者信息；
* 受害者：根据已知信息推测为中文使用者，习惯性获取破解软件的人员；

本次攻击活动完整攻击流程

1. 攻击者在相关站点批量投放恶意软件；

2. 受害者安装运行之后注册自身系统服务并开启键盘记录器；

3. 安装运行完成之后删除系统安全日志；

4. 睡眠间隔7天之后与C2域名进行通讯回传获取到的受害者信息；

本次在应急过程中从流量异常行为到定位主机，捕获样本，并根据防守现状做出响应，后续通过威胁情报和fofa对本次攻击活动进行快速分析。

本次事件，在发现并确认异常后随即加入防火墙黑名单阻断，但是后续观察阶段，攻击者新增域名microsoftdefender.luckfafa.com，并且公开情报显示2022.12.13，仍持续有样本公开，持续开展攻击活动。

在整个应急响应过程中，协同现场运维人员和业务人员共同梳理被控机器和人员的权限，同时对日志按照时间线回溯暂未发现横向痕迹。

结合上述信息，我们推测，攻击者批量开展攻击活动，安装恶意软件后启动键盘记录器，利用键盘记录器获取受害者信息，间隔7天后与C2域名进行通讯，不排除后续会根据键盘记录器获取到的信息针对特殊用户开展深层次的横向移动和内网攻击活动。

# IOCs

## C&C

```
googleupdate.luckfafa.com 45.116.161.95
wpsupdate.luckfafa.com 14.192.67.187
microsoftdefender.luckfafa.com     210.56.54.12
...