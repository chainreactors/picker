---
title: 【技术原创】渗透技巧——通过WSUS进行横向移动
url: https://www.4hou.com/posts/nJAP
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-10
fetch_date: 2025-10-04T03:23:58.404522
---

# 【技术原创】渗透技巧——通过WSUS进行横向移动

【技术原创】渗透技巧——通过WSUS进行横向移动 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 【技术原创】渗透技巧——通过WSUS进行横向移动

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-01-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)143040

收藏

导语：在内网渗透中，当我们获得了WSUS服务器的控制权限后，可以通过推送补丁的方式进行横向移动。这个利用方法最早公开在BlackHat USA 2015。本文将要整理这个利用方法的相关资料，结合思路，得出行为检测的方法。

**0x00 前言**

在内网渗透中，当我们获得了WSUS服务器的控制权限后，可以通过推送补丁的方式进行横向移动。这个利用方法最早公开在BlackHat USA 2015。本文将要整理这个利用方法的相关资料，结合思路，得出行为检测的方法。

**0x01 简介**

本文将要介绍以下内容：

环境搭建

利用思路

实现工具

行为检测

**0x02 环境搭建**

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

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465274115060.png "1667465274115060.png")

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465337143769.png "1667465337143769.png")

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465349883196.png "1667465349883196.png")

当同步完成后，会提示下载了多少个补丁，如下图

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465369272438.png "1667465369272438.png")选择Updates页面，可以查看已下载的补丁，Unapproved表示未安装的补丁，安装后的补丁可以选择Approved进行查看，如下图

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465382194966.png "1667465382194966.png")选中一个补丁，点击Approve...，弹出的对话框可以针对指定计算机组安装补丁，如下图

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465398595272.png "1667465398595272.png")**2.客户端配置**

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

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465500149089.png "1667465500149089.png")其中AUOptions对应组策略配置中的Configure automatic updating，2代表Notify for download and notify for install，3代表Auto download and notify for install，4代表Auto download and schedule the install，5代表Allow local admin to choose setting

(2)组策略配置服务器地址后会创建注册表HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate

查询命令：REG QUERY "HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate"

返回结果示例：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465515694130.png "1667465515694130.png")**3.推送补丁**

在WSUS服务器的Windows Server Update Services页面，选择指定补丁，右键点击Approve...，在弹出的对话框中选择计算机组即可

等待客户端到达补丁更新时间，即可完成补丁的推送

**0x03 利用思路**

如果我们能够生成一个带有Payload的补丁，就能够通过补丁进行横向移动，但是在利用上需要注意补丁文件的签名问题：Windows的补丁文件需要带有微软的签名

通常的利用方法是使用带有微软签名的程序，例如psexec，通过psexec执行命令或者添加一个管理员用户

**0x04 实现工具**

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

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465787346772.png "1667465787346772.png")这条命令将会在Updates的Security Updates页面下创建WSUSDemo，如下图

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465801960597.png "1667465801960597.png")**2.补丁部署**

将补丁部署到指定计算机组，命令示例：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465814541007.png "1667465814541007.png")这条命令会创建计算机组Demo Group，并且把win-iruj9k30gr7移动到该组下面，如下图

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465828150181.png "1667465828150181.png")接下来需要等待客户端安装这个补丁

**3.查看补丁状态**

查看补丁是否被安装，命令示例：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465843242316.png "1667465843242316.png")补丁未安装的输出如下：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465869121377.png "1667465869121377.png")还有一种查看方法是查看计算机的补丁更新时间，示例命令：SharpWSUS.exe inspect

输出示例：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465886394636.png "1667465886394636.png")为了便于测试，可以强制客户端更新补丁，看到新的补丁信息，如下图

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465898178777.png "1667465898178777.png")**4.清除补丁信息**

命令示例：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465911163798.png "1667465911163798.png")这条命令会删除补丁，删除添加的计算机组

在整个补丁更新过程中，WSUS服务器会将psexec.exe保存在WSUS服务器本地C:\wsus\wuagent.exe和C:\wsus\WsusContent\8E\FD7980D3E437F28000FA815574A326E569EB548E.exe，需要手动清除

在测试WSUSpendu时，为了便于分析细节，可以修改以下代码：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465925761146.png "1667465925761146.png")命令行执行：powershell -ep bypass -f WSUSpendu.ps1 -Verbose，将会输出完整的信息

**0x05 行为检测**

客户端的补丁历史更新记录会保存所有的补丁安装信息：

如下图

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667465943144290.png "1667465943144290.png")

但是，攻击者如果获得了系统的管理员控制权限，可以通过命令行卸载补丁的方式清除历史更新记录，命令行卸载补丁的命令示例：

查看更新：wmic qfe list brief/format:table

卸载指定更新：wusa /uninstall /kb:976902 /quiet /norestart

**0x06 小结**

本文介绍了通过WSUS进行横向移动的方法和实现工具，结合利用思路，给出行为检测的建议。

参考资料：

https://www.blackhat.com/docs/us-15/materials/us-15-Stone-WSUSpect-Compromising-Windows-Enterprise-Via-Windows-Update.pdf

https://www.gosecure.net/blog/2020/09/03/wsus-attacks-part-1-introducing-pywsus/

https://labs.nettitude.com/blog/introducing-sharpwsus/

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ljVxVXXr)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https:...