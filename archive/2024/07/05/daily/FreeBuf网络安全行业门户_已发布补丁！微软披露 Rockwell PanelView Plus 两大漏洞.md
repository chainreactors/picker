---
title: 已发布补丁！微软披露 Rockwell PanelView Plus 两大漏洞
url: https://www.freebuf.com/news/405173.html
source: FreeBuf网络安全行业门户
date: 2024-07-05
fetch_date: 2025-10-06T17:43:21.654162
---

# 已发布补丁！微软披露 Rockwell PanelView Plus 两大漏洞

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

已发布补丁！微软披露 Rockwell PanelView Plus 两大漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

已发布补丁！微软披露 Rockwell PanelView Plus 两大漏洞

2024-07-04 11:28:27

所属地 上海

近日，微软在 Rockwell PanelView Plus 设备中发现并披露了两个重大漏洞，未经身份认证的攻击者可远程利用这些漏洞执行远程代码和发起拒绝服务（DoS）攻击。

微软的调查结果揭露了在广泛使用这些人机界面（HMI）图形终端的工业领域存在的严重安全漏洞，凸显了在工业自动化系统中采取强有力的安全措施以防止潜在破坏的迫切需要。

![Microsoft-Findings.webp](https://image.3001.net/images/20200701/1593550745.png!small)

## RA PanelView Plus 设备漏洞细节

远程代码执行 (RCE) 漏洞被识别为 CVE-2023-2071，CVSS 评分为 9.8，涉及对设备中两个自定义类的利用。攻击者可滥用这些类上传并执行恶意 DLL，从而有效获得设备的远程控制权。

DoS 漏洞被识别为 CVE-2023-29464，CVSS 评分为 8.2，利用相同的自定义类发送设备无法处理的伪造缓冲区，导致系统崩溃。

## 漏洞发现和披露

PanelView Plus 设备在工业自动化领域发挥着至关重要的作用，因此发现的漏洞尤其令人担忧。攻击者利用这些漏洞可以远程执行代码，可能导致运行中断，给受影响的组织造成重大经济损失。

### 漏洞发现

Microsoft Defender for IoT 研究团队的主要职责之一是确保对操作技术 (OT) 和物联网 (IoT) 协议进行全面分析。

在调查过程中，该团队观察到两个通过通用工业协议 (CIP) 通信的设备之间存在合法的数据包捕获。一个涉及注册表值“ProductCode”路径的可疑远程注册表查询引起了对潜在漏洞的担忧。

* 协议深度分析

CIP是一种为工业自动化应用设计的面向对象协议。信息针对的是由类 ID 和对象实例 ID 标识的特定对象。该协议包括一个服务代码，表示要在对象上执行的操作。

微软的分析显示，观察到的通信涉及特定供应商的服务 ID 和类 ID 值，这促使对 HMI 固件进行进一步调查。

* 固件分析和利用方法

PanelView Plus HMI 在 Windows 10 IoT（或 Windows CE 上的旧版本）操作系统上运行。微软团队从固件中提取了相关 DLL 和可执行文件，以了解设备如何处理 CIP 请求。

他们发现，某些 DLL 管理着负责读取和写入注册表键值的自定义 CIP 类，这一发现导致确定了两个可被利用来远程执行代码的自定义类。

第一个自定义类接受 DLL 路径、函数名称和参数，加载 DLL 并执行指定函数。尽管验证功能将函数名称限制为预定义值，但微软还是找到了利用该类的方法。第二个自定义类允许在设备上读写文件，但验证不那么严格，为上传恶意 DLL 提供了途径。

微软通过编译与 Windows 10 IoT 兼容的恶意 DLL 演示了一种利用方法。他们使用第二个自定义类来上传 DLL，并将其放置在特定文件夹中。然后，使用第一个自定义类执行名为 remotehelper.dll 的 DLL，使攻击者能够远程控制设备。这一概念验证证实了漏洞的严重性和被利用的可能性。

### 漏洞披露

微软安全漏洞研究（MSVR）团队在分析发现这些漏洞后，于 2023 年 5 月和 7 月通过协调漏洞披露（CVD）与 Rockwell Automation 分享了他们的发现。 Rockwell Automation  迅速做出响应，于 2023 年 9 月和 10 月发布了公告及安全补丁。

## 缓解和保护措施

为降低与这些漏洞相关的风险，微软建议采取以下措施：

* 应用补丁： 确保受影响的设备已更新最新的安全补丁。具体来说，安装补丁 PN1645 和 PN1652 以解决已识别的漏洞。
* 网络隔离： 断开 PLC、路由器和 PC 等关键设备与互联网的连接，并确保正确的网络分段。
* 访问控制： 限制只有授权组件才能访问 CIP 设备。
* 利用工具： 使用 GitHub 上提供的 Microsoft 工具对 Rockwell Rslogix 设备进行扫描和取证调查，以确定受影响的设备并确保其相应的安全。

参考来源：

https://www.hendryadrian.com/cyware-rce-dos-exploits-found-in-rockwell-panelview-plus-patch-now/

# 安全漏洞 # 恶意DLL # Rockwell Automation

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

RA PanelView Plus 设备漏洞细节

漏洞发现和披露

* 漏洞发现
* 漏洞披露

缓解和保护措施

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