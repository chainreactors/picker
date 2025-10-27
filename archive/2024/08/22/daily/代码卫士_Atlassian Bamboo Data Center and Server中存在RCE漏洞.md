---
title: Atlassian Bamboo Data Center and Server中存在RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520541&idx=1&sn=f403f1139228e0543f485dc49192281e&chksm=ea94a077dde32961ced8bbf8b9f4d047894c070f5256758fbcda18bd2c501885e592e9ba6f05&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-22
fetch_date: 2025-10-06T18:03:49.873364
---

# Atlassian Bamboo Data Center and Server中存在RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQibwR6SUgJumVNbN5C6vI1QTf3nXYKbydib9AaVqOcFlBmTNaUwQVhYcUPB9pbvNLUK2JGLeIaDr0A/0?wx_fmt=jpeg)

# Atlassian Bamboo Data Center and Server中存在RCE漏洞

DO SON

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Atlassian 公司发布 Bamboo Data Center and Server 产品安全公告，修复了一个高危的远程代码执行 (RCE) 漏洞CVE-2024-21689，CVSS评分为7.6，可为使用受影响软件版本带来严重风险。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQibwR6SUgJumVNbN5C6vI1Q0Lfx5wy9xdjBl3Vbf3VbnzqEb7QAUrydNPwficAZJPtwzmtNVwe78Yg/640?wx_fmt=gif&from=appmsg)

CVE-2024-21689影响 Bamboo Data Center and Server 9.1.0至9.6.0版本，可导致认证攻击者在 Bamboo 环境中执行任意代码，从而造成多种后果，包括强烈影响目标系统的机密性、完整性和可用性。

该漏洞对依赖 Bamboo进行持续集成和部署流程的组织机构影响尤其大。鉴于Bamboo 在自动化构建、测试和发布中的作用，攻击者可利用RCE获得越权代码执行权限，从而攻陷整个软件开发管道。

Atlassian 公司已发布修复方案并督促客户升级 Bamboo 实例。该公司建议无法升级的用户更新至如下包括补丁的版本：

* Bamboo Data Center and Server 9.2：升级至9.2.17或后续版本
* Bamboo Data Center and Server 9.6：升级至9.6.5或后续版本

管理员应优先升级至这些版本，缓解该漏洞，避免所在组织机构遭受重大威胁如数据泄露、服务终端和恶意利用等。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Atlassian 修复Confluence等产品中的多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520092&idx=2&sn=cc02ff9f6ef98e6d539f13b4c6c892c2&chksm=ea94be36dde3372074c503b63e7b5eb83dec6be08550d41b4537fcb9fc282e8691c7bd3597c3&scene=21#wechat_redirect)

[Atlassian Confluence 高危漏洞可导致代码执行](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519665&idx=2&sn=86259d3f96b173403f1a65b601fc1989&chksm=ea94bcdbdde335cd0f308951f098245eea81c0364b1a3726dc92bad88f1ce58de6b53eef24ec&scene=21#wechat_redirect)

[Atlassian 发布20多个漏洞，含严重的 Bamboo 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519117&idx=2&sn=c0c8035f5617c6f76c73e71b9e73f04f&chksm=ea94bae7dde333f1efbbaeff72b89df023bbc2e6d408df713a753e060c09ff210656828d17d9&scene=21#wechat_redirect)

[Atlassian Confluence 远程代码执行漏洞(CVE-2023-22527)安全风险通告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518678&idx=1&sn=aedf682361f621f14474e78244d3242e&chksm=ea94b8bcdde331aa278b8d6c8fe7f1df9ec253aa21e960355a967894be85796756b54e173c95&scene=21#wechat_redirect)

[Atlassian 修复多款产品中的多个严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518302&idx=1&sn=9ede9c29a5c7c063571222672e754926&chksm=ea94b934dde330222c90b770d277247b3ad535c2b85b8082228c17630922ff9ea123ab19691f&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/cve-2024-21689-rce-vulnerability-in-atlassian-bamboo-data-center-and-server/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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