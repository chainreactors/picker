---
title: 红队工具MacroPack已被攻击者滥用
url: https://www.freebuf.com/news/410268.html
source: FreeBuf网络安全行业门户
date: 2024-09-06
fetch_date: 2025-10-06T18:26:51.747338
---

# 红队工具MacroPack已被攻击者滥用

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

红队工具MacroPack已被攻击者滥用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

红队工具MacroPack已被攻击者滥用

2024-09-05 10:43:21

所属地 上海

据BleepingComputer消息，一款最初被设计为红队演练之用的工具MacroPack近来正被攻击者滥用并部署恶意负载 Havoc、Brute Ratel 和 PhatomCore ，所发现的恶意文档已涉及多个国家和地区。

MacroPack 是由法国开发人员 Emeric Nasi （dba BallisKit） 创建的专注于红队演习演练和对手模拟的专有工具，提供反恶意软件绕过、反逆技术、使用代码混淆构建各种文档有效负载、嵌入无法检测的 VB 脚本等多项高级功能。

Cisco Talos 的安全研究人员研究了来自美国、俄罗斯和巴基斯坦等国家和地区在 VirusTotal 上提交的恶意文档，这些文件的诱饵、复杂程度和感染载体各不相同，表明 MacroPack 正被多个攻击者滥用，已成为一种潜在的威胁趋势。

这些被捕获的野外样本都有在 MacroPack 上创建的痕迹，包括基于马尔可夫链的函数和变量重命名、删除注释和多余的空格字符（这些字符可将静态分析检测率降到最低）以及字符串编码。

当受害者打开这些恶意Office 文档时会触发第一级 VBA 代码，该代码会加载恶意 DLL，并连接到攻击者的命令和控制 (C2) 服务器。

![](https://image.3001.net/images/20240905/1725504260_66d91b04edd9aef32aad1.png!small)攻击链

Cisco Talos 报告了一些与MacroPack 滥用相关的重要恶意活动集群：

> **美国：**2023 年 3 月上传的一份文件伪装成加密的 NMLS 更新表格，并使用马尔可夫链生成的函数名来逃避检测。 该文档包含多级 VBA 代码，在尝试通过 mshta.exe 下载未知有效载荷之前会检查沙盒环境。
>
> ![](https://image.3001.net/images/20240905/1725504365_66d91b6d9d82de6af2308.png!small)装成加密的 NMLS 更新表格
>
> **俄罗斯：**2024 年 7 月，一个俄罗斯 IP 上传的空白 Excel 工作簿提供了 PhantomCore，这是一个基于 Golang 的用于间谍活动的后门 。 该文件运行多级 VBA 代码，试图从远程 URL 下载后门。
>
> **巴基斯坦：**从巴基斯坦各地上传了以巴基斯坦军事为主题的文件。 其中一份文件伪装成巴基斯坦空军的通知，另一份伪装成就业确认书，部署了 Brute Ratel 獾。 这些文件通过 HTTPS DNS 和亚马逊 CloudFront 进行通信，其中一个文档嵌入了 base64 编码的 blob 以用于 Adobe Experience Cloud 跟踪。

BleepingComputer 已就观察到的滥用行为联系了 开发者Emeric Nasi，但目前尚未收到回复。

**参考来源：**

> [BleepingComputer](https://www.bleepingcomputer.com/)

# 恶意软件

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