---
title: Progress 提醒注意严重的 MOVEit 自动化认证绕过漏洞
url: https://mp.weixin.qq.com/s/Mz1h3sZza39OfrZxPbCzDQ
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:34.926435
---

# Progress 提醒注意严重的 MOVEit 自动化认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfWfVr9jSuyAPxbOOFUh4j3ohBibzxzTIcjG4wSiaVmS09ZQx9smDrUEjL1udJ6libzBsbpJjMl0TibW1w8pQq8boKozJ3JVMAFQPu8/0?wx_fmt=jpeg)

# Progress 提醒注意严重的 MOVEit 自动化认证绕过漏洞

Sergiu Gatlan
Sergiu Gatlan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Progress Software公司提醒客户修复MOVEit Automation企业级托管文件传输 (MFT) 应用程序中的一个严重身份验证绕过漏洞CVE-2026-4670。该漏洞影响2025.1.5、2025.0.9及2024.1.8之前版本的MOVEit Automation。远程威胁攻击者可在无需权限、无需用户交互的低复杂度攻击中利用该漏洞。**

MOVEit Automation能够自动处理复杂的数据工作流，无需手动编写脚本，并可作为一个集中的自动化编排工具，用于调度和管理不同系统之间（包括本地服务器、云存储以及外部合作伙伴）的文件传输。

该公司在上周四的一份公告中表示：“该漏洞已被修复，Progress MOVEit Automation团队强烈建议执行升级到最新版本。使用完整安装程序升级到已打补丁的版本是修复此问题的唯一方法。升级过程中系统将出现中断。”

同一天，Progress还发布了安全更新，解决同一个软件中因输入验证不当导致的一个高严重性权限提升漏洞（CVE-2026-5174）。

根据PwnDefend网络安全顾问Daniel Card分享的Shodan搜索结果，超过1400个MOVEit Automation实例暴露在互联网上，其中十多个与美国地方和州政府机构有关联。然而，目前尚无信息表明这些系统中有多少已经针对CVE-2026-4670攻击做好了安全防护。

尽管该公司尚未将这些安全问题标记为已遭在野利用，但近年来其它MoveIT MFT漏洞已成为攻击目标。例如，根据Emsisoft的估计，Clop勒索软件团伙在2023年利用MOVEit Transfer安全文件传输平台中的一个 0day 漏洞，发起了一系列大规模的数据窃取攻击，影响了超过2100个组织和逾6200万个人。MFT软件历来是勒索软件行为者的攻击目标，此前Clop的数据窃取活动就曾瞄准Accellion FTA、SolarWinds Serv-U、Gladinet CentreStack、GoAnywhere MFT以及Cleo等产品中的安全漏洞。

Progress Software表示，MOVEit MFT解决方案在全球范围内的企业用户超过3000多家，用户超过10万名。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Progress ShareFile 漏洞可用于发动预认证 RCE 攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525643&idx=2&sn=46f21b64114594cdb5db7473129e09a8&scene=21#wechat_redirect)

[Progress：尽快修复 WhatsUp Gold 中的多个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520960&idx=1&sn=919fb43b3860018ef3997b0e4159dee6&scene=21#wechat_redirect)

[Progress 紧急修复影响 LoadMaster 的超危RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520732&idx=1&sn=8fafa0f4d8f56d2a8361866cce3ac84c&scene=21#wechat_redirect)

[Progress 提醒注意Telerik Report Server中的严重RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520228&idx=1&sn=d9e2734ebb4a13c747b20000c240d7bd&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/moveit-automation-customers-warned-to-patch-critical-auth-bypass-flaw/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

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