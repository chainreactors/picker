---
title: Citrix 提醒管理员手动缓解 PuTTY SSH 客户端漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519453&idx=1&sn=b108366a369534bc2bc55f5a5089d587&chksm=ea94bdb7dde334a1ed46fce3773a11cab5d7d420a9b40d13263be90a5ffc622be738b323c0ec&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-11
fetch_date: 2025-10-06T17:17:18.740982
---

# Citrix 提醒管理员手动缓解 PuTTY SSH 客户端漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQvVL4J9EQdXmvic7XZfO2TFXUJ4ticAicJibQWPCNufFaibkXH1oPIgO3HjFiaWNabCM0gJk8Yv93hsBjA/0?wx_fmt=jpeg)

# Citrix 提醒管理员手动缓解 PuTTY SSH 客户端漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Citrix 公司本周提醒客户手动缓解一个 PuTTY SSH 客户端漏洞 (CVE-2024-31497)，它可导致攻击者窃取 XenCenter 管理员的SSH 私钥。**

XenCenter 有助于管理 Windows 桌面的 Ctrix Hypervisor 环境，包括部署和监控虚拟机。该漏洞影响XenCenter for Citrix Hypervisor 8.2 CU1 LTSR的多个版本，在点击“打开SSH控制台”按钮时，它绑定和使用 PuTTY做到从 XenCenter 到 guest VM的SSH 连接。

Citrix 公司表示，从 XenCenter 8.2.6开始就删除了 PuTTY 第三方组件，8.2.7之后的任何版本都未包括该组件。

Citrix 在本周三发布的安全公告中提到，“PuTTY 0.81之前的版本中存在一个问题；当与XenCenter 组合使用时，该漏洞在某些情况下可使控制 guest VM的攻击者判断 XenCenter 管理员的SSH密钥，该管理员在使用SSH连接时将密钥认证到 guest VM。”

该漏洞由德国波鸿鲁尔大学研究员 Fabian Bäumer 和 Marcus Brinkmann发现并报送。CVE-2024-31497由基于 Windows 的 PuTTY SSH客户端更老旧版本为用于认证的 NIST P-521曲线生成临时的唯一加密数字方式引发。

Citrix 提醒想要缓解该漏洞的管理员下载 PuTTY 最新版本并安装在与更老的 XenCenter 发布绑定的版本中。该公司提到，“不愿意使用‘打开SSH控制面板’功能的客户可彻底删除 PuTTY 组件。希望维护 PuTTY 现有用途的客户应当将XenCenter 系统上安装的版本替换为更新后的版本（版本号至少为0.81）。”

今年1月份，CISA收到 Citrix 公司通知漏洞已遭活跃利用后，要求美国联邦机构修复代码注入漏洞CVE-2023-6548和缓冲区溢出漏洞CVE-2023-6549。另外一个严重的 Netscaler 漏洞（CVE-2023-4966，被称为 Citrix Bleed）被多个黑客组织用作0day漏洞攻陷政府组织机构和高级别技术企业如波音等。医疗行业网络安全协调中心也提醒医疗组织机构保护 NetScaler ADC和 NetScaler Gateway 实例应对剧增的勒索攻击。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[Citrix悄悄修复相似度极高但严重性不及CitrixBleed的高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519419&idx=1&sn=3bb85759ff76414bd555bb55aa1b3c16&chksm=ea94bdd1dde334c73add716fd4c17f5d7be8d21d23464d3e187d43446f34d83e52d9482ed5cd&scene=21#wechat_redirect)

[Citrix 提醒注意已遭利用的两个 NetScaler 0day 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518689&idx=1&sn=0c28377e9cd188322fb8de2c9b984d4f&chksm=ea94b88bdde3319d66fb2901eac70e83e8071ee933f5b8bdb067917e92e94c9d23efc23f4ea8&scene=21#wechat_redirect)

[Citrix NetScaler 严重漏洞可泄露“敏感”数据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517841&idx=2&sn=de64058a934247781132d8fdd5886240&chksm=ea94b7fbdde33eed8920dc403119072a08ff3f018fc6122497a8acfadfbdcf1fca8ab3aa986b&scene=21#wechat_redirect)

[Citrix 修复 Ubuntu 版本安全访问客户端中的严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517034&idx=4&sn=6e2b7be2533c1e454539a3b4905483c7&chksm=ea94b200dde33b16f46f5c52b43bc116d9a9ed99bf381bbe9dbd8d1b3902ca57cb785c81a283&scene=21#wechat_redirect)

[Citrix 修复Workspace等多款产品中的多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515606&idx=2&sn=18cf93cc69f16acc4087555f4f6efc3b&chksm=ea948cbcdde305aa6e54f5a260a008d69843d1fa2765f9b2c2fa70422bc8acb78ee6cbd09553&scene=21#wechat_redirect)

**原文链接**

https://www.helpnetsecurity.com/2024/05/08/cve-2024-29212/

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