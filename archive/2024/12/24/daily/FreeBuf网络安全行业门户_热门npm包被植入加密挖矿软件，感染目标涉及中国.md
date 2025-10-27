---
title: 热门npm包被植入加密挖矿软件，感染目标涉及中国
url: https://www.freebuf.com/news/418283.html
source: FreeBuf网络安全行业门户
date: 2024-12-24
fetch_date: 2025-10-06T19:40:04.717423
---

# 热门npm包被植入加密挖矿软件，感染目标涉及中国

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

热门npm包被植入加密挖矿软件，感染目标涉及中国

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

热门npm包被植入加密挖矿软件，感染目标涉及中国

2024-12-23 10:56:23

所属地 上海

近日，有研究人员发现，一些热门的npm包遭到入侵，攻击者利用窃取到的令牌将带有加密挖矿恶意软件的版本发布到了官方包注册表中。

![](https://image.3001.net/images/20241223/1734923188_6768d3b43b4aef9d56e84.png!small)

Rspack 的开发人员透露，他们的两个npm 包@rspack/core 和 @rspack/cli均被入侵。Rspack 被宣传为 webpack 的替代品，是一款用 Rust 编写的“高性能 JavaScript 打包工具”。最初由字节跳动开发，现在已经被阿里巴巴、亚马逊、 Discord 和微软等几家公司采用。受影响的两个包每周的下载量分别超过 30万次和 14.5万次，表明它们颇受开发人员欢迎。

对这两个库的恶意版本进行的分析显示，它们包含了调用远程服务器（“80.78.28[.]72”）的代码，用于传输敏感的配置信息，例如云服务凭据。同时它们还通过向“ipinfo[.]io/json”发出 HTTP GET 请求来收集 IP 地址和位置信息。为了取得性能和隐秘性的平衡，恶意加密挖矿活动还将CPU使用率限制在了75%。

值得注意的是，这种攻击还把感染范围限制在了特定一些国家，如中国、俄罗斯、中国香港、白俄罗斯和伊朗。攻击的最终目标是在安装这些包时，在受影响的 Linux 主机上触发 XMRig 加密货币挖矿软件的下载和执行。这一操作需通过“package.json”文件中指定的一个 postinstall 脚本来实现。

目前含有恶意软件的版本已被撤下，新发布了安全的1.18版本。此外，项目维护人员还表示，他们已经作废了所有现有的 npm 令牌和 GitHub 令牌，检查了代码库和 npm 包的权限，并审核了源代码是否存在潜在的漏洞，对令牌被窃取的根本原因进行了调查。

据悉，针对 Rspack npm包的攻击还包含另一个名为Vant的npm 包，该包每周下载量超过 4.1 万次。 Sonatype的研究人员表示，攻击者成功地将几个被感染的版本发布到了 npm 注册表中，包括 2.13.3 、2.13.4 、2.13.5 、3.6.13 、3.6.14 、3.6.15 、4.9.11 、4.9.12 、4.9.13 和4.9.14版本。目前，最新的安全版本4.9.15已发布，建议受影响的用户及时升级。

**参考来源：**

> [Rspack npm Packages Compromised with Crypto Mining Malware in Supply Chain Attack](https://thehackernews.com/2024/12/rspack-npm-packages-compromised-with.html)

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