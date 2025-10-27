---
title: 网络犯罪分子利用 StackOverflow 推广恶意 Python 软件包
url: https://www.freebuf.com/news/402227.html
source: FreeBuf网络安全行业门户
date: 2024-05-31
fetch_date: 2025-10-06T16:51:05.547138
---

# 网络犯罪分子利用 StackOverflow 推广恶意 Python 软件包

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

网络犯罪分子利用 StackOverflow 推广恶意 Python 软件包

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

网络犯罪分子利用 StackOverflow 推广恶意 Python 软件包

2024-05-30 10:12:54

所属地 上海

![1717039498_6657f18a192d88d75eb55.png!small](https://image.3001.net/images/20240530/1717039498_6657f18a192d88d75eb55.png!small)

近日，有网络安全研究人员警告称，在Python 软件包索引（PyPI）库中发现了一个新的恶意 Python 软件包，该软件包为黑客盗取加密货币提供了便利。

该恶意软件包名为 pytoileur，截至发稿前已被下载 316 次。有趣的是，在前一版本（1.0.1）于 2024 年 5 月 28 日被 PyPI 维护者删除后，该软件包的作者（名为 PhilipsPY）上传了一个新版本（1.0.2），并且功能完全相同。

根据 Sonatype 发布的分析报告显示，恶意代码被嵌入到了软件包的 setup.py 脚本中，使其能够执行 Base64 编码的有效载荷，该有效载荷负责从外部服务器检索 Windows 二进制文件。

安全研究员 Sharma 表示：检索到的二进制文件'Runtime.exe'会利用 Windows PowerShell 和 VBScript 命令在系统上运行。

一旦安装，二进制文件就会建立持久性并投放额外的有效载荷，包括间谍软件和能够从网络浏览器和加密货币服务中收集数据的窃取恶意软件。

Sonatype 表示，它还发现了一个新创建的名为 “EstAYA G ”的 StackOverflow 账户，该账户在问答平台上回复用户的询问，并引导用户安装恶意 pytoileur 软件包，并将其作为所谓的问题解决方案。

Sharma告诉《黑客新闻》称：虽然在无法访问日志的情况下评估互联网平台上的伪匿名用户账户很难确定其归属，但这两个账户的使用年限及其发布和推广恶意 Python 软件包的目的都表明，这些账户与这次活动背后的威胁行为者有关。

Sonatype 表示：黑客公开滥用可信平台，并将其作为恶意活动的“滋生地”，这对于全球开发者来说都是一个巨大的警示信号。

鉴于 StackOverflow 平台上有很多新手开发者，他们仍在学习、提问，可能会听信恶意建议，因此 StackOverflow 的漏洞尤其令人担忧。

通过对软件包元数据仔细研究发现，它与 Checkmarx 于 2023 年 11 月披露的涉及 Pystob 和 Pywool 等虚假 Python 软件包此前的活动有相似之处。

这些发现再次说明了为什么开源生态系统仍然吸引着威胁行为者的原因，这些威胁行为者往往希望通过所谓的供应链攻击，并利用 Bladeroid 等信息窃取程序和其他恶意软件入侵多个目标。

> 参考来源：[Cybercriminals Abuse StackOverflow to Promote Malicious Python Package (thehackernews.com)](https://thehackernews.com/2024/05/cybercriminals-abuse-stackoverflow-to.html)

# python # 恶意软件 # StackOverflow

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