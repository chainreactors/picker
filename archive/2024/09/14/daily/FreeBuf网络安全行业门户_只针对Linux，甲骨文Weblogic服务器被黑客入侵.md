---
title: 只针对Linux，甲骨文Weblogic服务器被黑客入侵
url: https://www.freebuf.com/news/410985.html
source: FreeBuf网络安全行业门户
date: 2024-09-14
fetch_date: 2025-10-06T18:27:12.085287
---

# 只针对Linux，甲骨文Weblogic服务器被黑客入侵

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

只针对Linux，甲骨文Weblogic服务器被黑客入侵

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

只针对Linux，甲骨文Weblogic服务器被黑客入侵

2024-09-13 18:46:25

所属地 上海

网络安全研究人员发现了一场针对Linux环境的新恶意软件活动，目的是进行非法加密货币挖矿和传播僵尸网络恶意软件。云安全公司Aqua指出，这项活动特别针对甲骨文Weblogic服务器，旨在传播一种名为Hadooken的恶意软件。

该恶意软件利用的是Oracle Weblogic中的一个已知漏洞，即CVE-2020-14882。该漏洞允许攻击者获得对Weblogic服务器的未经授权访问，并执行任意代码。

![1726224683_66e4192b5242abd6486fc.png!small](https://image.3001.net/images/20240913/1726224683_66e4192b5242abd6486fc.png!small)

安全研究员Assaf Moran表示，“当Hadooken行动被执行时，它会释放一种名为Tsunami的恶意软件，并部署一个加密货币挖矿程序来获取加密货币，如门罗币（XMR）。”

攻击链利用已知的安全漏洞和配置错误，例如弱密码，以获得初始立足点并在易受攻击的实例上执行任意代码。这是通过启动两个几乎相同的有效载荷来完成的，一个用Python编写，另一个是shell脚本，两者都负责从远程服务器（“89.185.85[.]102”或“185.174.136[.]204”）检索Hadooken恶意软件。

Morag进一步表示，“shell脚本版本试图遍历包含SSH数据（如用户凭据、主机信息和秘密）的各种目录，并利用这些信息攻击已知服务器。然后它在组织内或连接的环境中横向移动，以进一步传播Hadooken恶意软件。”

![1726224668_66e4191cda32420b34f6f.png!small](https://image.3001.net/images/20240913/1726224668_66e4191cda32420b34f6f.png!small)

Hadooken勒索软件内置了两个组件，一个加密货币挖矿程序和一个名为Tsunami（又称Kaiten）的分布式拒绝服务（DDoS）僵尸网络，后者有针对部署在Kubernetes集群中的Jenkins和Weblogic服务的攻击历史。

此外，该恶意软件还负责通过在主机上创建cron作业以不同频率定期运行加密货币挖矿程序来建立持久性。

Aqua指出，IP地址89.185.85[.]102在德国注册，隶属于托管公司Aeza International LTD（AS210644），Uptycs在2024年2月的先前报告将其与8220 Gang加密货币活动联系起来，该活动滥用Apache Log4j和Atlassian Confluence Server及数据中心中的漏洞。

第二个IP地址185.174.136[.]204虽然目前处于非活动状态，但也与Aeza Group Ltd.（AS216246）有关。正如Qurium和EU DisinfoLab在2024年7月强调的，Aeza是一家在莫斯科M9和法兰克福的两个数据中心都有业务的防弹托管服务提供商。

研究人员在报告中说：“Aeza的运作方式和快速增长可以通过招募与俄罗斯防弹托管服务提供商有关联的年轻开发者来解释，这些提供商为网络犯罪提供庇护。”

> 参考来源：https://thehackernews.com/2024/09/new-linux-malware-campaign-exploits.html

# 系统安全 # 数据安全

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