---
title: 俄APT组织利用虚假汽车销售广告传播HeadLace后门
url: https://www.freebuf.com/articles/407808.html
source: FreeBuf网络安全行业门户
date: 2024-08-06
fetch_date: 2025-10-06T18:04:39.106020
---

# 俄APT组织利用虚假汽车销售广告传播HeadLace后门

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

俄APT组织利用虚假汽车销售广告传播HeadLace后门

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

俄APT组织利用虚假汽车销售广告传播HeadLace后门

2024-08-05 13:54:51

所属地 上海

近日，Palo Alto Networks的研究人员发现，一个被称为Fighting Ursa（也被称作APT28、Fancy Bear或Sofacy）的与俄罗斯有关联的威胁行为者，通过发布虚假的汽车销售广告来传播HeadLace后门恶意软件，主要针对外交官。

![](https://image.3001.net/images/20240805/1722836883_66b06793f0600a63dc72d.png!small)这场活动始于2024年3月，攻击者采用了多年来对外交官有效的网络钓鱼策略，利用能够吸引目标的敏感主题发起攻击，并依赖于公共和免费的服务来托管攻击的各个阶段。

Unit 42指出，2023年，其他类似的威胁组织如Cloaked Ursa，也曾使用出售宝马汽车的广告来针对乌克兰的外交使团。

2023年6月，Insikt Group的研究人员观察到俄罗斯GRU的APT28利用HeadLace信息窃取器和凭证收集网页针对整个欧洲的网络。

2023年4月到12月期间，该APT分三个不同阶段部署 Headlace，分别使用网络钓鱼、被破坏的互联网服务和本地二进制文件。而这些凭据收集页面旨在针对乌克兰国防部、欧洲交通基础设施和阿塞拜疆的一个智库，通过在合法服务和被破坏的Ubiquiti路由器之间转发请求，绕过双因素认证和CAPTCHA挑战。

乌克兰国防部和欧洲铁路系统的相关网络被破坏后，攻击者能够收集情报以影响战场战术和更广泛的军事战略。此外，他们对阿塞拜疆经济和社会发展中心的兴趣也表明他们有意了解并影响地区政策。Insikt Group推测这次行动旨在影响地区和军事动态。

今年5月，Fighting Ursa利用合法服务Webhook.site通过托管恶意HTML页面启动了感染链，该页面在2024年3月14日提交给VirusTotal，其中包含用于确定访问者的计算机是否运行Windows的脚本。非Windows用户会被重定向到ImgBB上托管的诱饵图片。HTML 还从 Base64 文本中创建了一个 ZIP 压缩包供下载，并利用 JavaScript 自动完成该过程。攻击者使用了一张奥迪Q7 Quattro SUV的图片作为诱饵，虚假宣传它是“外交用车出售”，其中包括虚假的联系方式以增加网络钓鱼计划的可信度。

ZIP归档包含三个文件：一个伪装成图像文件的合法Windows计算器可执行文件calc.exe（"IMG-387470302099.jpg.exe"），一个DLL文件（"WindowsCodecs.dll"），以及一个批处理文件（"zqtxmo.bat"）。

IMG-387470302099.jpg.exe文件用于加载WindowsCodecs.dll，这是HeadLace后门的一部分，可运行批处理脚本。该脚本执行了一个Base64编码的命令，从另一个webhook[.]site URL检索文件。

Palo Alto Networks的分析报告指出：“批处理文件将从第二个Webhook.site URL下载的内容保存在用户的下载目录中为IMG387470302099.jpg，然后将其移动到%programdata%目录，并更改文件扩展名从.jpg到.cmd。最后，批处理文件执行IMG387470302099.cmd，然后删除自身，以消除恶意活动的明显痕迹。”

专家认为，Fighting Ursa组织将继续在其攻击基础设施中使用合法的网络服务。

Recorded Future的一份最新报告也指出，该组织使用的基础设施一直在不断变化和发展。其他行业报告也展示了该组织在尝试投放HeadLace恶意软件时使用的各种诱饵。

为了防御此类攻击，建议限制对这些类似托管服务的访问，并仔细审查这些免费服务的使用，以识别可能的攻击载体。

**参考来源：**

https://securityaffairs.com/166496/apt/russia-apt-headlace-malware.html

# 后门 # 网络钓鱼 # 恶意软件 # 网络钓鱼攻击

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