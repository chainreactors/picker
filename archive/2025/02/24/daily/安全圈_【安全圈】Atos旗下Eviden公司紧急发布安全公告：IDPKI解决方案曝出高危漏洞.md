---
title: 【安全圈】Atos旗下Eviden公司紧急发布安全公告：IDPKI解决方案曝出高危漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068092&idx=2&sn=07ceda3a43b852c9147f82cc1ed039fa&chksm=f36e74bcc419fdaac195c826bdb0acc22ee49a2e1a959765c9c3405ad72d8f3cb5509157f596&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-24
fetch_date: 2025-10-06T20:36:32.170087
---

# 【安全圈】Atos旗下Eviden公司紧急发布安全公告：IDPKI解决方案曝出高危漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgflLibV2lwePwibBUAxQoPT18fK30Yn6ym50SmvqEWbn4lhUePcddnibGqYX3SPia24pP1B2B8F7TqGQ/0?wx_fmt=jpeg)

# 【安全圈】Atos旗下Eviden公司紧急发布安全公告：IDPKI解决方案曝出高危漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![CVE-2024-56404 - CVE-2024-39327](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgflLibV2lwePwibBUAxQoPT1xFNscffgDRflqMqE5lxmNLJOpMgdCIXf2SicIWXYMDzTPF19mMYVIXg/640?wx_fmt=other&from=appmsg)

近日，Atos集团旗下Eviden公司发布紧急安全公告，披露在其推出的身份与公钥基础设施解决方案IDPKI中发现了多个安全漏洞。这些漏洞的CVE编号分别为CVE-2024-39327、CVE-2024-39328和CVE-2024-51505，可能导致未经授权的访问和权限提升，对使用该解决方案的用户组织构成重大安全风险。

虽然这些漏洞不会泄露证书颁发机构（CA）的私钥，但攻击者可能利用它们破坏IDPKI管理环境中的信任链和系统完整性。具体而言：

1. CVE-2024-39327：该漏洞的CVSS评分高达9.9，属于严重级别。攻击者可利用此漏洞进行未经授权的CA签名操作，从而生成非法数字证书，可能导致证书链信任关系被破坏。
2. CVE-2024-39328：该漏洞的CVSS评分为6.8，属于中危级别。在多分区环境场景下，配置管理员用户可能超越其权限范围，存在机密数据泄露的风险。
3. CVE-2024-51505：该漏洞的CVSS评分为8.0，属于高危级别。配置管理员用户可能通过竞争条件提升自身权限，进一步威胁系统安全。

Eviden公司已发布了针对上述漏洞的修复补丁，并强烈建议用户尽快升级其IDPKI部署版本至最新版。此外，该公司还提供了详细的缓解措施和临时解决方案，帮助用户在完成更新前有效降低风险。

以下是受影响产品及修复信息：

| 产品 | 是否受影响 | 修复版本 |
| --- | --- | --- |
| IDRA | 是 | 2.7.1 |
| IDRA SaaS | 部分受影响（仅CVE-2024-39327） | 2.7.1 |
| IDCA | 是（仅CVE-2024-39328） | 2.7.0 |
| IDCA SaaS | 不受影响 | 不适用 |

需要注意的是，IDPKI的软件即服务（SaaS）版本由于基于角色的权限限制，不会受到CVE-2024-39328和CVE-2024-51505的影响。

Eviden公司表示，截至公告发布时，尚未监测到利用这些漏洞的实际攻击活动。然而，公司仍建议客户立即部署修复补丁，并使用官方提供的检测脚本对系统进行全面检查，以排查潜在的利用痕迹。

用户建议：

1. 立即访问Eviden官方支持平台，下载并安装最新补丁；
2. 在完成修复前，按照官方建议启用临时缓解措施；
3. 定期检查系统日志，分析是否存在异常行为；
4. 加强权限管理，确保用户权限与其角色严格匹配。

Eviden公司承诺将持续监控漏洞态势，并在必要时提供进一步技术支持。用户如有疑问或需要协助，可通过官方渠道联系安全团队。

***END***

阅读推荐

[【安全圈】Bybit遭遇黑客攻击：15亿美元被盗](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068081&idx=1&sn=9323a8a39c23ab689a6250fecadc821d&scene=21#wechat_redirect)

[【安全圈】2025年1月国内数据泄露事件汇总](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068081&idx=2&sn=265740774dab2618251d31c1513db09f&scene=21#wechat_redirect)

[【安全圈】微软Power Pages权限提升漏洞被黑客利用，紧急修复中](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068081&idx=3&sn=6d7fd58dc0942e6b518c29bfda1a134e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过