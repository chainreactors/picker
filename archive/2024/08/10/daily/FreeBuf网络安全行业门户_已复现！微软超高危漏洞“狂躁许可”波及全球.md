---
title: 已复现！微软超高危漏洞“狂躁许可”波及全球
url: https://www.freebuf.com/news/408285.html
source: FreeBuf网络安全行业门户
date: 2024-08-10
fetch_date: 2025-10-06T18:05:08.538526
---

# 已复现！微软超高危漏洞“狂躁许可”波及全球

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

已复现！微软超高危漏洞“狂躁许可”波及全球

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

已复现！微软超高危漏洞“狂躁许可”波及全球

2024-08-09 17:47:07

所属地 上海

近期，微软披露最新的远程代码执行**超高危漏洞CVE-2024-38077**，CVSS评分高达9.8，可导致开启了远程桌面许可服务的Windows服务器完全沦陷。

漏洞影响**Windows****Server 2000****到Windows server 2025**所有版本，已存在**近30年**。该漏洞**可稳定利用、****可远控、可勒索、可蠕虫等**，破坏力极大，攻击者无须任何权限即可实现远程代码执行。

这一漏洞存在于Windows远程桌面许可管理服务(RDL)中，该服务被广泛部署于开启Windows远程桌面(3389端口)的服务器，用于管理远程桌面连接许可。攻击者**无需任****何前置条件，无需用户交互(零点击)便可直接获取服务器最高权限，执行任意操作。**

![](https://image.3001.net/images/20240809/1723196717_66b5e52dcc82580368c35.png!small)

微软官网公告

一旦漏洞被恶意攻击者或APT组织利用，将快速蔓延，或波及全球所有使用微软服务器的用户。这是自“永恒之蓝”后，**Windows首次出现影响全版本且能高稳定利用的认证前RCE漏洞**。建议尽快通过官网公告更新安全补丁。

## **漏洞详情**

**漏洞名称：**CVE-2024-38077

**漏洞类型：**远程代码执行

**影响范围：**开启Windows Remote Desktop Licensing（RDL）Service 的Windows服务器

**影响版本：**Windows Server 2000 - Windows Server 2025

**综合评价：**

<利用难度>：容易

<威胁等级>：严重

**官方解决方案：**微软官方已发布补丁公告

## **影响范围**

### **影响范围**

Windows Server 2012 R2 (Server Core installation)

Windows Server 2012 R2

Windows Server 2012 (Server Core installation)

Windows Server 2012

Windows Server 2008 R2 for x64-based Systems Service Pack 1 (Server Core installation)

Windows Server 2008 R2 for x64-based Systems Service Pack 1 (Server Core installation)

Windows Server 2008 R2 for x64-based Systems Service Pack 1

Windows Server 2008 R2 for x64-based Systems Service Pack 1

Windows Server 2008 for x64-based Systems Service Pack 2 (Server Core installation)

Windows Server 2008 for x64-based Systems Service Pack 2 (Server Core installation)

Windows Server 2008 for x64-based Systems Service Pack 2

Windows Server 2008 for x64-based Systems Service Pack 2

Windows Server 2008 for 32-bit Systems Service Pack 2 (Server Core installation)

Windows Server 2008 for 32-bit Systems Service Pack 2 (Server Core installation)

Windows Server 2008 for 32-bit Systems Service Pack 2

Windows Server 2008 for 32-bit Systems Service Pack 2

Windows Server 2016 (Server Core installation)

Windows Server 2016

Windows Server 2022, 23H2 Edition (Server Core installation)

Windows Server 2022 (Server Core installation)

Windows Server 2022

Windows Server 2019 (Server Core installation)

Windows Server 2019

### **其他受影响组件**

无

## **漏洞分析**

Windows远程桌面许可服务在解码用户输入的许可密钥包时，会将用户输入的编码后的许可密钥包解码并存储到缓冲区上，但是在存储前没有正确地检验解码后数据长度与缓冲区大小之间的关系，导致缓冲区可以被超长的解码后数据溢出。攻击者可以利用这个漏洞进一步实现远程命令执行攻击。

## **处置建议**

### **安全更新**

采用以下官方解决方案及缓解方案来防护此漏洞：

**Windows自动更新**

Windows系统默认启用 Microsoft Update，当检测到可用更新时，将会自动下载更新并在下一次启动时安装。还可通过以下步骤快速安装更新：

1、点击“开始菜单”或按Windows快捷键，点击进入“设置”

2、选择“更新和安全”，进入“Windows更新”（Windows Server 2012以及Windows Server 2012 R2可通过控制面板进入“Windows更新”，步骤为“控制面板”-> “系统和安全”->“Windows更新”）

3、选择“检查更新”，等待系统将自动检查并下载可用更新

4、重启计算机，安装更新

系统重新启动后，可通过进入“Windows更新”->“查看更新历史记录”查看是否成功安装了更新。对于没有成功安装的更新，可以点击该更新名称进入微软官方更新描述链接，点击最新的SSU名称并在新链接中点击“Microsoft 更新目录”，然后在新链接中选择适用于目标系统的补丁进行下载并安装。

**手动安装补丁**

另外，对于不能自动更新的系统版本，可参考以下链接下适用于该系统的补丁并安装：

https://msrc.microsoft.com/updateguide/vulnerability/CVE-2024-38077

**参考来源：**

https://mp.weixin.qq.com/s/nNYTRnoOUePm4Fvbh0SIgw

# 微软 # 微软漏洞 # 微软安全漏洞

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

漏洞详情

影响范围

* 影响范围
* 其他受影响组件

漏洞分析

处置建议

* 安全更新

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)