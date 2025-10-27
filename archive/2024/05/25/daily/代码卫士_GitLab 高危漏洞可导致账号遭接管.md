---
title: GitLab 高危漏洞可导致账号遭接管
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519584&idx=1&sn=8ca7ba7442a6234b2f5910147094c5bb&chksm=ea94bc0adde3351ccee634db2e180e9bc4d66ff43d4aa7e08ca703c79df1444bcf27d1b960de&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-25
fetch_date: 2025-10-06T17:18:06.115986
---

# GitLab 高危漏洞可导致账号遭接管

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRWyjibjcoF9UM0DrochwkhSbtlnEkJ8KjYHGVnz4FR5tEkVAECOibkxZSWlR9IOaUdheK3zyGS8ia8A/0?wx_fmt=jpeg)

# GitLab 高危漏洞可导致账号遭接管

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**GitLab 修复了一个高危漏洞，它可导致未认证攻击者在跨站点脚本攻击中接管用户账户。**

该漏洞的编号是CVE-2024-4835，是位于VS 代码编辑器 （Web IDE）中的一个XSS弱点，可导致威胁行动者使用恶意构造的页面窃取受限制的信息。虽然攻击者可在无需认证的攻击中利用该漏洞，但仍然需要用户交互，因此增加了攻击的复杂性。

GitLab 指出，“今天，我们发布GitLab 社区版 (CE) 和企业版 (EE) 17.0.2、16.11.3和16.10.6。这些版本中包括重要的漏洞和安全修复方案，我们强烈建议将所有的 GitLab 立即升级至这些版本。”

本周三，GitLab还修复了6个中危漏洞，包括通过 Kubernetes Agent Server 实现CSRF 的漏洞 CVE-2023-7045以及可导致攻击者中断 GitLab web 资源加载的拒绝服务漏洞 (CVE-2024-2874)。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRWyjibjcoF9UM0DrochwkhSzfXpNsSe8z7Kvb1f6tcWW1GvOCCMEPqBqv7HYZUFgpqQ4bd92xhlCw/640?wx_fmt=gif&from=appmsg)

**老旧账户劫持漏洞遭活跃利用**

因托管多种类型的敏感数据如API密钥和专有代码，GitLab称为热门目标。

因此，被劫持的GitLab 账户可造成重大影响，如供应链攻击：如果攻击者将恶意代码插入CI/CD环境，则可攻陷组织机构的仓库。正如CISA在本月初提醒的那样，威胁行动者们正在活跃利用GitLab 在1月份劫持的另外一个零点击账户劫持漏洞CVE-2023-7028。该漏洞CVSS评分为10，可导致未认证攻击者通过密码重置接管GitLab 账户。尽管Shadowserver 在1月份发现超过5300个易受攻击的 GitLab 实例暴露在网上，但目前不到一半的还可被触及。CISA在5月1日将该漏洞添加至必修清单，要求美国联邦机构在三周内即5月22日前修复该漏洞。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[GitLab 提醒注意严重的零点击账户劫持漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518669&idx=1&sn=e9e78678e6c35cd6c0c37b638d5a988c&chksm=ea94b8a7dde331b16bdf8306a2700a04ea240bc5baa204b72ab3c9664a58b77c6fc92b1841f4&scene=21#wechat_redirect)

[GitLab 督促用户安装安全更新，修复严重的管道漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517701&idx=2&sn=9efeb89e9c34a3dcb192e347897ea5d3&chksm=ea94b76fdde33e79439751b5f121c7f1c6903963de1ec1e650ed19876271b10ebc9271391861&scene=21#wechat_redirect)

[GitLab强烈建议尽快修复 CVSS 满分漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516580&idx=1&sn=3e272b8a4ba9c8f7b596e5bc1c9f6576&chksm=ea94b0cedde339d8dee6f14566aaa4da84cb44e202cc0582353695ecd4620c832ba4c9ddab91&scene=21#wechat_redirect)

[GitLab修复GitHub import函数中的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514207&idx=1&sn=eda12473aec122dcbe50bf0b2545da32&chksm=ea948935dde300234feefd9ebdb2e36056f43a607bd274323e86088fbc98d2737efa2f63658f&scene=21#wechat_redirect)

[GitLab 远程代码执行漏洞安全风险通告](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513707&idx=1&sn=6c80379607fc2214bebf651c01750491&chksm=ea948701dde30e17d699dd8ce24dd9852b091e66462aee72c89a53dae49d8d3027bb1ddb3c99&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/high-severity-gitlab-flaw-lets-attackers-take-over-accounts/

题图：Pexels License

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