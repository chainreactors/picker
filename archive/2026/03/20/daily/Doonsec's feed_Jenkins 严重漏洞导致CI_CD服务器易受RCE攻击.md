---
title: Jenkins 严重漏洞导致CI/CD服务器易受RCE攻击
url: https://mp.weixin.qq.com/s/tLwt4cFmsrQkoDPOnXlBrg
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:02:15.020347
---

# Jenkins 严重漏洞导致CI/CD服务器易受RCE攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfUHV7ibTB55VgK4nSQmsHYibr2mDzAl4p3Z2w3SrlVkTZSYLGZjXUaq8YO0SzJNahdrM8RR51wyPfFs9sCsr7gzNdX8C71LqSSAw/0?wx_fmt=jpeg)

# Jenkins 严重漏洞导致CI/CD服务器易受RCE攻击

Ddos
Ddos

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Jenkins****项目发布安全公告，修复了可导致系统遭完全攻陷的两个严重漏洞CVE-2026-33001和CVE-2026-33002。这两个漏洞对于 DevOps 团队而言风险极大，可导致攻击者直接在软件开发生命周期的关键阶段注入恶意代码。**

最直接的威胁是高危的任意文件创建漏洞CVE-2026-33001，影响 Jenkins 2.554和之前版本以及 LTS 2.541.2和之前版本。这些版本在提取 .tar 或 .tar.gz 文档时未能安全处理这些符号链接，从而导致构造的文档能够将文件写入文件系统上的任意位置，仅受运行 Jenkins 的用户文件系统访问权限限制。

该漏洞对于在控制器上提取的文档影响严重。攻击者可通过“将恶意脚本写入 JENKINS\_HOME/init/groovy.d/directory”或者部署恶意插件的方式实现远程代码执行 (RCE) 后果。该利用能够由任何具有 “Item/Configure” 权限或者能够控制智能体进程的人员控制，因此尤为危险。

第二个高危漏洞CVE-2026-33002主要针对通过 WebSockets 访问时的 Jenkins 命令行界面。研究人员发现 Jenkins 使用不安全的 HTTP 请求标头来验证这些链接的来源，导致DNS 重绑攻击风险。通过诱骗受害者访问使用 DNS 重绑定的恶意网站来解析 Jenkins 控制器的 IP 地址，攻击者可从不受信任来源建立与 CLI 端点的 WebSocket 连接并以匿名用户身份执行 CLI 命令。如果该匿名用户身份被授权权限，或者该服务器使用了“任何人都可做任何事”的策略，则攻击者可利用 Groovy 脚本命令执行任意代码。

除了这些核心修复方案外，Jenkins 还修复了 LoadNinja 插件（v2.1及之前版本）中的敏感数据泄露漏洞CVE-2026-33003和CVE-2026-33004。该插件“在 job config.xml 文件中存储了 LoadNinja API 未加密密钥”并未能在 web 接口进行掩码处理，可被具有 “Item/Extended Read” 权限的任何用户捕获。

Jenkins 督促管理员立即升级实例，并发布如下补丁：

* Jenkins Weekly: 更新至 2.555 版本。
* Jenkins LTS: 更新至2.541.3 版本。
* LoadNinja Plugin: 更新至 2.2版本。

如无法立即更新修复 CLI 漏洞，则管理员应当“为 Jenkins 控制器设置认证机制并删除匿名用户的权限”。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Jenkins 修复CSRF和开放重定向等多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522429&idx=2&sn=de12997404efb67be58ceb4d9f00b64c&scene=21#wechat_redirect)

[CISA：严重的 Jenkins 漏洞已被用于勒索攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520541&idx=2&sn=c8001046f4088bb94fd3ffcd7e6926b0&scene=21#wechat_redirect)

[Jenkins 出现严重漏洞，可导致代码执行攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515862&idx=2&sn=559cb44fa0529b875f5361b1112c5b60&scene=21#wechat_redirect)

[Jenkins 披露插件中未修复的XSS、CSRF等18个0day漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513380&idx=3&sn=643da5e5ad5ec30250e2a3e9dca17e51&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/pipeline-poison-critical-jenkins-vulnerabilities-rce-cve-2026-33001/

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