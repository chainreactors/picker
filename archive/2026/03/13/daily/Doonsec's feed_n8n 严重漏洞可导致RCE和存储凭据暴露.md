---
title: n8n 严重漏洞可导致RCE和存储凭据暴露
url: https://mp.weixin.qq.com/s/eGIBIGvlRRzD5hqb_VYe-Q
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:07:41.000150
---

# n8n 严重漏洞可导致RCE和存储凭据暴露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfWTfs2iagq8uvq65Vp7kRuuC3Xt38BDlaG9ictysV3UZNOibpn7EKoIWbO3OTFEL6NJFf0ZqiaPHQxZPGDFJ8Ru5U47CTwkdl6dw3w/0?wx_fmt=jpeg)

# n8n 严重漏洞可导致RCE和存储凭据暴露

Sergiu Gatlan
Sergiu Gatlan

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究人员披露了位于n8n工作流自动化平台中的两个严重漏洞，它们可导致任意命令执行，现已修复。**

CVE-2026-27577（CVSS评分：9.4）是一个表达式沙箱逃逸漏洞，可导致远程代码执行（RCE）后果。CVE-2026-27493（CVSS评分：9.5）是通过n8n表单节点进行未经身份验证的表达式评估漏洞。

这两个漏洞由 Pillar Security 公司的研究员 Eilon Cohen 发现并报送，他表示，“CVE-2026-27577是表达式编译器中的一个沙箱逃逸漏洞：抽象语法树重写器中的一个缺失案例让进程能够未经转换而溜过，使任何经过身份验证的表达式都能获得完整的RCE能力。"

该研究员提到，CVE-2026-27493是位于n8n表单节点中的一个"双重评估漏洞"，攻击者可利用表单端点默认公开且无需身份验证或n8n账户这一特性，通过表达式注入滥用该漏洞。成功利用该漏洞只需利用一个公开的"联系我们"表单，通过在姓名字段中输入有效载荷即可执行任意shell命令。

n8n在上月底发布的安全公告中表示，拥有创建或修改工作流权限的认证用户可以通过在工作流参数中构造恶意表达式，利用CVE-2026-27577在运行n8n的主机上触发意外的系统命令执行。

n8n还指出，CVE-2026-27493与类似CVE-2026-27577的表达式沙箱逃逸漏洞结合使用时，可能"升级为在n8n主机上的远程代码执行"。这两个漏洞均影响n8n的自托管和云部署版本，包括 1.123.22以下版本、2.0.0及以上且 2.9.3以下版本，以及2.10.0及以上且2.10.1以下版本，它们已在2.10.1、2.9.3和1.123.22版本中修复。

如果无法立即修复CVE-2026-27577，思科建议用户仅允许完全受信任用户拥有工作流创建和编辑权限，并在加固环境中部署n8n并限制操作系统权限和网络访问权限。

对于CVE-2026-27493，n8n建议采取以下缓解措施：

* 手动检查表单节点的使用情况是否满足上述前提条件。
* 将n8n-nodes-base.form添加到NODES\_EXCLUDE环境变量，禁用表单节点。
* 将n8n-nodes-base.formTrigger添加到NODES\_EXCLUDE环境变量，禁用表单触发节点。

维护者提醒称："这些变通方案不能完全消除风险，应仅作为短期缓解措施使用。"

研究人员表示，攻击者可利用这些漏洞读取N8N\_ENCRYPTION\_KEY环境变量，并解密存储在n8n数据库中的所有凭证，包括AWS密钥、数据库密码、OAuth令牌和API密钥。

n8n版本2.10.1、2.9.3和1.123.22还修复了其它两个严重漏洞，可用于执行任意代码：

* CVE-2026-27495（CVSS评分：9.4）——拥有创建或修改工作流权限的认证用户可能利用JavaScript任务运行器沙箱中的代码注入漏洞，在沙箱边界之外执行任意代码。
* CVE-2026-27497（CVSS评分：9.4）——拥有创建或修改工作流权限的认证用户可能利用合并节点的SQL查询模式在n8n服务器上执行任意代码并写入任意文件。

除了仅允许受信任用户拥有工作流创建和编辑权限外，n8n还为每个漏洞概述了以下变通方案：

* CVE-2026-27495：使用外部运行器模式（N8N\_RUNNERS\_MODE=external）限制影响范围。
* CVE-2026-27497——通过将n8n-nodes-base.merge添加到NODES\_EXCLUDE环境变量来禁用合并节点。

虽然n8n未提及这些漏洞已遭在野利用，但建议用户升级至最新版本获得最佳防护措施。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[n8n出现新漏洞，可用于执行系统命令](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525056&idx=1&sn=15cdf06676ec490a668ee9af2a579306&scene=21#wechat_redirect)

[n8n 两个高危漏洞可导致认证RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524999&idx=1&sn=29baedb21e9e4bef4466b10bc66abcde&scene=21#wechat_redirect)

[n8n 满分漏洞 Ni8mare 可导致服务器遭劫持](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524822&idx=1&sn=e3ab93e00fc28bdb1a256d94e84507f3&scene=21#wechat_redirect)

[n8n严重漏洞可导致任意代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524734&idx=1&sn=7accfa41ad8e25a3c0a292eb451552af&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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