---
title: 警惕！IceFire 勒索软件开始针对Linux系统了
url: https://www.freebuf.com/news/360054.html
source: FreeBuf网络安全行业门户
date: 2023-03-11
fetch_date: 2025-10-04T09:16:09.885377
---

# 警惕！IceFire 勒索软件开始针对Linux系统了

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

警惕！IceFire 勒索软件开始针对Linux系统了

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

警惕！IceFire 勒索软件开始针对Linux系统了

2023-03-10 14:34:42

所属地 上海

![](https://image.3001.net/images/20230310/1678430048_640acf60e82f4f58e2808.jpeg!small)

最近发现基于Windows的勒索软件IceFire现在开始针对多个领域的Linux企业网络。

SentinelLabs的研究人员发现了IceFire勒索软件新的Linux版本。该勒索软件最初只针对基于Windows的系统，主要是针对技术公司。IceFire于2022年3月首次被MalwareHunterTeam的研究人员发现，但该组织自2022年8月起便开始活跃在暗网上。

专家们观察到IceFire利用IBM Aspera Faspex文件共享软件（CVE-2022-47986，CVSS评分：9.8）的反序列化漏洞来部署勒索软件。

大多数IceFire攻击事件主要发生在土耳其、伊朗、巴基斯坦和阿拉伯联合酋长国。专家指出，这些国家通常不是勒索组织行动的重点。

SentinelOne研究人员成功地测试了IceFire Linux版本对基于英特尔的Ubuntu和Debian发行版。该勒索软件成功加密了一台运行IBM Aspera Faspex文件服务器软件的CentOS主机。该勒索软件对文件进行加密，并在文件名上附加".ifire "扩展名，然后通过删除二进制文件来自我删除。

IceFire不加密带有".sh "和".cfg "扩展名的文件，它还避免加密某些文件夹，以便受感染的机器继续可用。

通过分析，位于/home/[user\_name]/的用户配置文件目录看到的加密活动最多。IceFire针对用户和共享目录（例如，/mnt，/media，/share）进行加密；这些是文件系统中未受保护的部分，不需要提升权限来写入或修改。

该勒索软件的Windows版本通过网络钓鱼信息传播，并使用开发后的工具包进行透视。Linux变体仍处于早期阶段。

专家指出，在报告发布时，IceFire二进制文件被0/61个VirusTotal引擎检测到。赎金票据包含硬编码的凭证，用于登录托管在Tor隐藏服务上的赎金支付门户。

![](https://image.3001.net/images/20230310/1678417097_640a9cc931595dd22904c.png!small)

IceFire的这一演变证实了针对Linux的勒索软件在2023年会继续流行。Linux勒索软件，包括BlackBasta、Hive、Qilin、Vice Society aka HelloKitty等。

专家总结道：与Windows相比，Linux更难以部署勒索软件，特别是在规模上。为了克服这一点，攻击者转变方向，利用应用程序的漏洞，正如IceFire运营商通过IBM Aspera漏洞部署有效载荷所证明的那样。

> 参考链接：securityaffairs.com/143261/malware/icefire-ransomware-targets-linux.html

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