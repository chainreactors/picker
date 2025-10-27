---
title: 威胁者利用Microsoft Teams语音通话传播勒索软件
url: https://www.freebuf.com/news/420574.html
source: FreeBuf网络安全行业门户
date: 2025-01-23
fetch_date: 2025-10-06T20:10:20.226694
---

# 威胁者利用Microsoft Teams语音通话传播勒索软件

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

威胁者利用Microsoft Teams语音通话传播勒索软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

威胁者利用Microsoft Teams语音通话传播勒索软件

2025-01-22 20:04:00

所属地 上海

![](https://image.3001.net/images/20250122/1737549515_6790e6cb6b5cfcb373bcf.jpg!small)

Sophos 托管检测与响应（MDR）团队发现了两起勒索软件攻击活动，攻击者利用Microsoft Teams获取目标组织未授权访问权限。

这两起攻击活动分别由代号STAC5143和STAC5777的威胁行为者发起，他们利用Microsoft Teams的默认配置，允许外部用户与内部用户发起聊天或会议。

Sophos 研究人员指出，威胁行为者采用了多步骤的攻击策略，攻击手法多样且复杂：

* 邮件轰炸：目标在一小时内收到多达 3,000 封垃圾邮件。
* 社交工程：攻击者伪装成 IT 支持人员，通过 Microsoft Teams 呼叫受害者。
* 远程访问：威胁行为者引导受害者安装 Microsoft Quick Assist 或使用 Teams 内置的远程控制功能。
* 恶意软件部署：一旦获得控制权，攻击者会执行恶意负载。

## 攻击活动详情

### STAC5143攻击活动

* 使用 Java 归档文件（JAR）和基于 Python 的后门程序。
* 部署了经过混淆的 RPivot（一种反向 SOCKS 代理工具）。
* 使用类似于 FIN7 技术的 Lambda 函数进行代码混淆。
* 通过 80 端口连接到命令与控制（C2）服务器。

![](https://image.3001.net/images/20250122/1737549555_6790e6f3160203e15a2bd.jpg!small)

Python代码来自winter.zip存档中的混淆RPivot副本（来源：Sophos ）

### STAC5777攻击活动

* 利用合法的 Microsoft 可执行文件（OneDriveStandaloneUpdater.exe）侧加载恶意 DLL（winhttp.dll）。
* 使用未签名的 OpenSSL 工具包驱动程序建立 C2 连接。
* 修改注册表：

> reg add "HKLM\SOFTWARE\TitanPlus" /v 1 /t REG\_SZ /d "185.190.251.16:443;207.90.238.52:443;89.185.80.86:443" /f

* 创建服务和 .lnk 文件以实现持久化。
* 进行 SMB 扫描以实现横向移动。
* 尝试卸载安全软件和多因素认证（MFA）解决方案。

## 恶意软件功能

这些攻击活动中使用的恶意软件能够进行以下操作：

* 收集系统和操作系统信息。
* 获取用户凭据。
* 使用 Windows API 记录键盘输入。
* 进行网络发现和横向移动。
* 窃取敏感数据。

![](https://image.3001.net/images/20250122/1737549660_6790e75c7bf3c6c9effd6.jpg!small)攻击者的活动被Microsoft Office 365集成捕获（来源：Sophos ）

在一次攻击中，STAC5777试图部署Black Basta勒索软件，但被Sophos终端防护成功拦截。

## 缓解策略建议

* 限制来自外部组织的 Teams 通话。
* 限制使用 Quick Assist 等远程访问应用程序。
* 实施应用程序控制设置，阻止未经授权的 Quick Assist 执行。
* 利用 Microsoft Office 365 集成进行安全监控。
* 提高员工对社交工程攻击的防范意识。

Sophos 已针对这些攻击活动中使用的恶意软件部署了检测机制，包括 ATK/RPivot-B 、Python/Kryptic.IV 和 Troj/Loader-DV 。

**参考链接：**

> <https://cybersecuritynews.com/threat-actors-delivering-ransomware-via-microsoft-teams/>

# 资讯

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

攻击活动详情

* STAC5143攻击活动
* STAC5777攻击活动

恶意软件功能

缓解策略建议

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