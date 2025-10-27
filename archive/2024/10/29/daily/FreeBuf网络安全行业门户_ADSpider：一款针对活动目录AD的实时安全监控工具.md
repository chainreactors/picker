---
title: ADSpider：一款针对活动目录AD的实时安全监控工具
url: https://www.freebuf.com/sectool/413844.html
source: FreeBuf网络安全行业门户
date: 2024-10-29
fetch_date: 2025-10-06T18:50:11.911108
---

# ADSpider：一款针对活动目录AD的实时安全监控工具

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

ADSpider：一款针对活动目录AD的实时安全监控工具

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

ADSpider：一款针对活动目录AD的实时安全监控工具

2024-10-28 13:21:45

所属地 广西

## 关于ADSpider

ADSpider是一款针对活动目录AD的实时安全监控工具，该工具可以帮助广大研究人员更轻松地监控和保护活动目录AD的安全。

![](https://image.3001.net/images/20241028/1730092802_671f1f027a452b9bbc303.png!small)

ADSpider支持实时监控目录AD更改而无需获取所有对象，并且能够使用复制元数据和更新序列号 (USN) 来过滤对象的当前属性。

## 工具要求

> [针对活动目录AD的PowerShell模块](https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps)

## 工具安装

广大研究人员可以直接使用下列命令将该项目源码克隆至本地：

```
git clone https://github.com/DrunkF0x/ADSpider.git
```

## 工具使用

### 运行参数

> DC - 域控制器 FQDN。
>
> Formatlist - 以列表而不是表格形式输出。
>
> ExcludelastLogonTimestamp - 从输出中排除lastLogonTimestamp事件。
>
> DumpAllObjects - 启动前转储所有活动目录。如果有更改，它将显示所有以前的值。
>
> Short - 输出将只有 AttributeName、AttributeValue、LastOriginChangeTime 和 Explanation。
>
> Output - 创建包含所有输出的 XML 文件。
>
> ExcludeObjectGUID - 排除具有特定 GUID 的 Active Directory 对象。
>
> Sleep - 请求 USN 号的间隔。默认情况下为30 秒。
>
> USN - 指定启动的 USN。
>
> DisplayXML -显示以前捕获的 XML 文件数据。

### 域计算机

只需从域用户在 powershell 会话中运行模块即可。为了获得更好的性能，请使用域控制器 FQDN 而不是 IP 地址。

```
Import-module .\ADSpider.ps1

Invoke-ADSpider -DC DC01.domain.com
```

### 非域计算机

使用 runas 与域用户启动 powershell 会话。检查域控制器是否可以访问。为了获得更好的性能，请使用域控制器 FQDN 而不是 IP 地址。

```
## From cmd or powershell

runas /netonly /u:domain.com\MyUser powershell

## From powershell

Import-module .\ADSpider.ps1

Invoke-ADSpider -DC DC01.domain.com
```

## 工具运行演示

![](https://image.3001.net/images/20241028/1730092864_671f1f40102e4dd0b1f07.png!small)

## 项目地址

**ADSpider**：【[GitHub传送门](https://github.com/DrunkF0x/ADSpider)】

## 参考资料

> <https://github.com/p0dalirius/LDAPmonitor>
>
> <https://learn.microsoft.com/en-us/powershell/module/activedirectory/?view=windowsserver2022-ps>
>
> <https://premglitz.wordpress.com/2013/03/20/how-the-active-directory-replication-model-works/>
>
> <https://learn.microsoft.com/en-us/archive/technet-wiki/51185.active-directory-replication-metadata>
>
> <https://learn.microsoft.com/en-us/windows/win32/adschema/a-systemflags>
>
> <https://learn.microsoft.com/en-us/windows/win32/ad/linked-attributes>

# 活动目录 # 安全监控 # AD安全 # 微软AD

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

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

关于ADSpider

工具要求

工具安装

工具使用

* 运行参数
* 域计算机
* 非域计算机

工具运行演示

项目地址

参考资料

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