---
title: 2025年首个满分漏洞，PoC已公布，可部署后门
url: https://www.freebuf.com/news/419788.html
source: FreeBuf网络安全行业门户
date: 2025-01-15
fetch_date: 2025-10-06T20:10:33.879512
---

# 2025年首个满分漏洞，PoC已公布，可部署后门

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

2025年首个满分漏洞，PoC已公布，可部署后门

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

2025年首个满分漏洞，PoC已公布，可部署后门

2025-01-14 11:25:27

所属地 上海

云攻击者正在大肆利用名为Max - Critical Aviatrix RCE漏洞（编号CVE - 2024 - 50603），此漏洞在CVSS评分中高达10分（满分10分），能够在受影响系统上执行未经身份验证的远程代码，网络犯罪分子借此漏洞植入恶意软件。

![](https://image.3001.net/images/20250114/1736832746_6785f6ea797c9e60ff4f6.png!small)

最坏的情况下，该漏洞会让未经身份验证的远程攻击者在受影响系统上运行任意命令，进而完全掌控该系统。目前，攻击者利用此漏洞在易受攻击的目标上部署XMRig加密货币挖矿恶意软件和Sliver后门。

## CVE - 2024 - 50603：高风险漏洞

研究人员于1月10日在博客中警示，该漏洞在亚马逊Web服务（AWS）云环境中尤为危险，因为在此环境中，Aviatrix Controller默认允许权限提升。

“依据我们的数据，约3%的云企业环境部署了Aviatrix Controller。在这些环境里，托管Aviatrix Controller的虚拟机中有65%存在通向管理云控制平面权限的横向移动路径。”

数百家大型企业运用Aviatrix的技术管理AWS、Azure、谷歌云平台（GCP）以及其他多云环境中的云网络。常见应用场景包括自动化部署与管理云网络基础设施，以及管理安全、加密和连接策略等，其客户包括不少大型集团企业。

CVE - 2024 - 50603是由于Aviatrix Controller未能正确检查或验证用户，通过其应用程序编程接口（API）发送的数据而产生。这是最新暴露出来的一个与各类组织（不论规模大小）日益增多的API使用相关的安全风险漏洞。其他常见的API相关风险还包括因配置错误、缺乏可见性以及安全测试不足而产生的风险。

该漏洞存在于所有版本低于7.2.4996或7.1.4191的受支持Aviatrix Controller版本中。Aviatrix已经发布了针对该漏洞的补丁，并且建议相关组织进行补丁安装或者升级到Controller的7.1.4191或7.2.4996版本。

Aviatrix公司指出：“在某些情形下，补丁在控制器升级过程中并非完全持久有效，即便控制器状态显示为‘已打补丁’，也必须重新应用，例如在不受支持的控制器版本上应用补丁这种情况。”

## 黑客发动机会性云攻击

安全研究员Jakub Korepta（来自SecuRing）发现了这一漏洞并向Aviatrix报告，于1月7日公开披露了该漏洞的详细信息。仅一天之后，一个针对该漏洞的概念验证利用程序就在GitHub上可获取，随即引发了近乎立即利用的网络攻击与入侵活动。

Wiz人工智能与威胁研究副总裁Alon Schindel表示：“自概念验证发布以来，Wiz观察到大多数易受攻击的企业都未曾更新修复补丁。目前我们也看到，客户正在对自己的系统进行修补，从而抵御攻击者的攻击。”

Schindel将到目前为止的利用活动描述为主要是一种机会性的活动，是扫描器和自动化工具集在互联网上搜寻未打补丁Aviatrix企业的结果。

他表示：“尽管在某些情况下，所使用的有效载荷和基础设施表明在一些案例中有更高的复杂性，但大多数尝试看起来像是广泛的扫描，而非针对特定组织的高度定制化或者有针对性的攻击。”

现有的数据表明，多个威胁行为者（包括有组织的犯罪团伙）正在以多种方式利用该漏洞。“依据环境的设置，攻击者可能会窃取敏感数据、访问云或本地基础设施的其他部分或者扰乱正常运营。”

## API相关网络风险的警示

Ray Kelly称，Aviatrix Controller漏洞再次让人们意识到API端点日益增长的风险，以及应对这些风险所面临的挑战。该漏洞表明仅仅一个简单的网络调用就可能攻破服务器，凸显了对API进行彻底测试的必要性。鉴于API的规模、复杂性以及相互依赖性，并且许多API是由外部软件和服务提供商开发和管理的，这样的测试可能极具挑战性。

Kelly进一步表示：“缓解这些风险的一个有效方法是建立针对第三方软件明确的‘治理规则’。这包括实施针对第三方供应商的全面审查流程、执行一致的安全措施以及持续监控软件性能和漏洞。”

Schindel表示，受新Aviatrix漏洞影响的组织最佳应对策略是尽快应用该漏洞的补丁。无法立即打补丁的组织应该立即限制对Aviatrix Controller的网络访问，仅允许受信任的来源进行访问。他们还应当密切监控日志和系统行为中的可疑活动或者已知利用指标，针对与Aviatrix相关的异常行为设置警报，并减少云身份之间不必要的横向移动路径。

Aviatrix发言人Jessica MacGregor表示，鉴于该漏洞潜在的严重性，公司在2024年11月就发布了针对该漏洞的紧急补丁。该安全补丁适用于所有受支持的版本，并且对已经结束两年支持的Aviatrix Controller版本同样适用。该公司还通过多个有针对性的活动私下联系客户，以确保受影响的组织应用了补丁，MacGregor称。

虽然相当一部分受影响的客户已经应用了补丁并采取了推荐的加固措施，但仍有一些组织尚未进行操作。MacGregor指出，正是这些客户正在遭受当前的攻击。“虽然我们强烈建议客户保持软件的最新状态，但在Controller版本6.7 +上应用了安全补丁的客户，即使没有升级到最新版本也能够得到保护。”

参考来源：<https://www.darkreading.com/cloud-security/cloud-attackers-exploit-max-critical-aviatrix-rce-flaw>

# 漏洞 # 漏洞分析

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

CVE - 2024 - 50603：高风险漏洞

黑客发动机会性云攻击

API相关网络风险的警示

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