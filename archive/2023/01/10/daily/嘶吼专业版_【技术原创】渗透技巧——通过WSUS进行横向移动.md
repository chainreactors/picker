---
title: 【技术原创】渗透技巧——通过WSUS进行横向移动
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247556226&idx=1&sn=0b1bda048a3ea962ed756319e96ff939&chksm=e915ccb8de6245aeb73f4e56702d49d5047b9075dc27c2cdf058bed176a582a0b0528c4ff64f&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-01-10
fetch_date: 2025-10-04T03:26:27.022250
---

# 【技术原创】渗透技巧——通过WSUS进行横向移动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYdoqMH5mhJK1uAAtlzq5TPvaQkCwia2cxp11sFw50n0lHcMcJRSSNcGQ/0?wx_fmt=jpeg)

# 【技术原创】渗透技巧——通过WSUS进行横向移动

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)0x00 前言

在内网渗透中，当我们获得了WSUS服务器的控制权限后，可以通过推送补丁的方式进行横向移动。这个利用方法最早公开在BlackHat USA 2015。本文将要整理这个利用方法的相关资料，结合思路，得出行为检测的方法。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)0x01 简介

本文将要介绍以下内容：

环境搭建

利用思路

实现工具

行为检测

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)0x02 环境搭建

本节介绍WSUS服务器搭建的过程，通过配置客户端实现补丁的推送

参考资料：

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd939822(v=ws.10)

**1.WSUS服务器搭建**

WSUS服务器需要安装在Windows Server操作系统

(1)安装

在添加角色和功能页面，选择Windows Server Update Services

需要指定补丁更新包的存放路径，这里可以设置为C:\WSUS

(2)配置

打开Windows Server Update Services进行配置

配置时选择默认选项即可，在选择Download update information from Microsoft Update时，点击Start Connecting，如果报错提示An HTTP error has occurred，经过我的多次测试，可以采用以下方法解决：

关闭当前页面

进入Windows Server Update Services，选择synchronization，点击synchronization Now，等待同步完成，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY29Z230hB9ibcDq6w5z5EUDic9FaIdkKzZbDzwwLuTJhQPzfXBqqPKHtw/640?wx_fmt=png)

选择Options，选择WSUS Server Configuration Wizard，重新进入配置页面，连接成功，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYbib4dx4ibSjwYGCS6OzELIBGKcMzWY4MAk678PDv1eNLrfqI9cGQwMHQ/640?wx_fmt=png)

配置完成后需要创建计算机组，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYTyNC5nkVde9WZ2gMIF9gD7RRzib4W2KejEUDCuSicEE7765NEhKdLzog/640?wx_fmt=png)

当同步完成后，会提示下载了多少个补丁，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYKxiaRXDrjoibfAzqchF8dTfhw6V09ucb9SLiawT2T1zAZLRlS2J3LUPZg/640?wx_fmt=png)

选择Updates页面，可以查看已下载的补丁，Unapproved表示未安装的补丁，安装后的补丁可以选择Approved进行查看，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYYVUT2ZuVS1hiciaQtuQn0KWthbuicZBn9F6eZVMLKp80f3N6ibTLu5AbGw/640?wx_fmt=png)

选中一个补丁，点击Approve...，弹出的对话框可以针对指定计算机组安装补丁，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYy8quJXUNibgtLm3WsUa32GRib69QFt0xicDlN8FSMOK19X1KRFg2oHbjg/640?wx_fmt=png)

**2.客户端配置**

客户端只要是Windows系统即可，需要通过组策略配置

依次选择Computer Configuration -> Administrative Templates -> Windows Components -> Windows Update，选择Configure Automatic Updates，设置成Auto download and notify for install，选择Specify intranet Microsoft update service location，设置更新服务器地址为http://192.168.1.182:8530

注：

需要指定端口8530

对于域环境，配置组策略后需要等待一段时间，这是因为组策略每90分钟在后台更新一次，随机偏移量为0-30分钟，如果想立即生效，可以输入命令：gpupdate /force

对于工作组环境，配置组策略可以立即生效

当客户端开始补丁更新时，WSUS服务器会获得客户端的信息，并显示在Computers页面

组策略配置的操作等同于创建注册表，具体信息如下：

(1)组策略配置自动更新后会创建注册表HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU

查询命令：REG QUERY "HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"

返回结果示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY3YSp1GrOkvaRcn2mP5HsV4icL3VzicGws7gCSyfkmBm91kpwAbXZ3kFw/640?wx_fmt=png)

(2)组策略配置服务器地址后会创建注册表HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate

查询命令：REG QUERY "HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate"

返回结果示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYWVElh3FaoW7BsZ2lVG4YXO2SUheicIF5IkhMh1KZlib9GhSnBuARhGnQ/640?wx_fmt=png)

**3.推送补丁**

在WSUS服务器的Windows Server Update Services页面，选择指定补丁，右键点击Approve...，在弹出的对话框中选择计算机组即可

等待客户端到达补丁更新时间，即可完成补丁的推送

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)0x03 利用思路

如果我们能够生成一个带有Payload的补丁，就能够通过补丁进行横向移动，但是在利用上需要注意补丁文件的签名问题：Windows的补丁文件需要带有微软的签名

通常的利用方法是使用带有微软签名的程序，例如psexec，通过psexec执行命令或者添加一个管理员用户

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)0x04 实现工具

开源的工具有以下三个：

https://github.com/nettitude/SharpWSUS

https://github.com/AlsidOfficial/WSUSpendu

https://github.com/ThunderGunExpress/Thunder\_Woosus

以上三个工具的实现原理基本相同，都是创建一个调用psexec执行命令的补丁，将补丁推送至指定计算机，等待目标计算机更新补丁

创建补丁的操作需要连接SQL数据库，依次实现以下操作：

ImportUpdate

PrepareXMLtoClient

InjectURL2Download

DeploymentRevision

PrepareBundle

PrepareXMLBundletoClient

DeploymentRevision

**1.创建补丁**

SharpWSUS在创建补丁时需要注意转义字符，命令示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYhfh6An5TYwr3sibianJneZnhda7b0GuuA1maCpzpPQIhduibjyEZxrdZQ/640?wx_fmt=png)

这条命令将会在Updates的Security Updates页面下创建WSUSDemo，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY87icd576jedibXw6llpkKZL7Via4MGL8bWHyMW7neFXMZeUHghapBicSKA/640?wx_fmt=png)

**2.补丁部署**

将补丁部署到指定计算机组，命令示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYAhKeeSy2ribMh9KBv2TprYRkTpF5ibd9GexMcKWZxRmtk3PVtF7xuOBw/640?wx_fmt=png)

这条命令会创建计算机组Demo Group，并且把win-iruj9k30gr7移动到该组下面，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYKNmeCVhUwcbLEDjQgDPP8hJm6dPSbCZeOTxX2qRjfpCoib4FoIVpWTw/640?wx_fmt=png)

接下来需要等待客户端安装这个补丁

**3.查看补丁状态**

查看补丁是否被安装，命令示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYAb0HOC7nLo0xcicLPghngr3zGEeo0oerCEp1ax2nBSq5ic2t8Uo2f0VA/640?wx_fmt=png)

补丁未安装的输出如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY2osWarg4RA4B2r6KAFibzCibPEt4I6xRUfnptOLREJZJqDiaojOYEfH7A/640?wx_fmt=png)

还有一种查看方法是查看计算机的补丁更新时间，示例命令：SharpWSUS.exe inspect

输出示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY0zGW1WHxBJB7StzPWFH0lDj6iaF8lPicucyyUQWqGVw0c5G1BbOticrpg/640?wx_fmt=png)

为了便于测试，可以强制客户端更新补丁，看到新的补丁信息，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY8Tj9OBE8YFyjp8fRAFlCFu3QHqWGq6SorC1nJACvgOIAiaFicXhrb1fA/640?wx_fmt=png)

**4.清除补丁信息**

命令示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYQQEX5fJcAC70N34GViaewmNpvXgQTZGjX9HJI9FUnLrgejMzYpIq2BA/640?wx_fmt=png)

这条命令会删除补丁，删除添加的计算机组

在整个补丁更新过程中，WSUS服务器会将psexec.exe保存在WSUS服务器本地C:\wsus\wuagent.exe和C:\wsus\WsusContent\8E\FD7980D3E437F28000FA815574A326E569EB548E.exe，需要手动清除

在测试WSUSpendu时，为了便于分析细节，可以修改以下代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYIuuGV3RBVLygickFu3XDKFcibSAVjDMX0MtGGEmL4ibZkdwHKtenpDTkA/640?wx_fmt=png)

命令行执行：powershell -ep bypass -f WSUSpendu.ps1 -Verbose，将会输出完整的信息

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)0x05 行为检测

客户端的补丁历史更新记录会保存所有的补丁安装信息：

如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYRhSPfZia0xgAQUhKl9nAehopHLs9BqNdAibzE5vzqrSthyskeU5vANcg/640?wx_fmt=png)

但是，攻击者如果获得了系统的管理员控制权限，可以通过命令行卸载补丁的方式清除历史更新记录，命令行卸载补丁的命令示例：

查看更新：wmic qfe list brief/format:table

卸载指定更新：wusa /uninstall /kb:976902 /quiet /norestart

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTYtw69phYKEjJhK2ViaLE45r5HufoiaNbBzYztq7noyic3aJWoVjgymPNIQ/640?wx_fmt=png)0x06 小结

本文介绍了通过WSUS进行横向移动的方法和实现工具，结合利用思路，给出行为检测的建议。

参考资料：

https://www.blackhat.com/docs/us-15/materials/us-15-Stone-WSUSpect-Compromising-Windows-Enterprise-Via-Windows-Update.pdf

https://www.gosecure.net/blog/2020/09/03/wsus-attacks-part-1-introducing-pywsus/

https://labs.nettitude.com/blog/introducing-sharpwsus/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAthTY8ibUfL0VE1I201h1RRVZobiaLSUzGMPqtSuhCASCo6U7iavsibpcVNtYIw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28zLT9Mjgjh9VULmAoAth...