---
title: Palo Alto Networks 修复PAN-OS 中的认证绕过漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522232&idx=2&sn=3bc7a4466c3c33ff643ca604524fa401&chksm=ea94a6d2dde32fc44365c182de4b7d412b22857b005666e0a04d2e8302f064eab2a2baa037d6&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-15
fetch_date: 2025-10-06T20:36:48.504819
---

# Palo Alto Networks 修复PAN-OS 中的认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQNyLL5TFhmMvRiaw0tMJbp9XgYzuZxV3JxziaRM27RxIWibicruKHu5GE1LB3KyTUlXJoQzIQdnB2EHQ/0?wx_fmt=jpeg)

# Palo Alto Networks 修复PAN-OS 中的认证绕过漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Palo Alto Networks 公司修复了可导致认证绕过的高危PAN-OS漏洞CVE-2025-0108（CVSS评分7.8）。不过如果对该管理界面的访问权限受限于jump box （“跳板系统”），则评分下降到5.1。**

该公司在一份安全公告中提到，“Palo Alto Networks PAN-OS 软件中存在一个认证绕过漏洞，可导致对管理web界面拥有网络访问权限的攻击者绕过认证并调用某些PHP脚本。虽然调用PHP脚本无法导致远程代码执行后果，但可对PAN-OS的完整性和机密性造成负面影响。”

该漏洞影响如下版本：

* PAN-OS 11.2 < 11.2.4-h4（修复版本 >= 11.2.4-h4）
* PAN-OS 11.1 < 11.1.6-h1（修复版本 >= 11.1.6-h1）
* PAN-OS 11.0（该版本已在2024年11月17日达到生命周期，因此需升级至受支持的已修复版本）
* PAN-OS 10.2 < 10.2.13-h3（修复版本 >= 10.2.13-h3）
* PAN-OS 10.1 < 10.1.14-h9（修复版本 >= 10.1.14-h9）

Searchlight Cyber/Assetnote 公司的安全研究员 Adam Kues 发现并报送了该漏洞，他提到该漏洞与该界面 Nginx 和 Apache 组件处理进站请求之间的差距造成，可导致目录遍历攻击。

该公司还修复了如下两个漏洞：

* **CVE-2025-0109****（CVSS评分5.5）：**Palo Alto Networks PAN-OS 管理 web 界面中存在一个未认证文件删除漏洞，可导致对管理 web 界面具有网络访问权限的攻击者以 “nobody” 用户身份删除某些文件，包括有限的日志和配置文件（已在PAN-OS 11.2.4-h4、11.1.6-h1、10.2.13-h3 和 10.1.14-h9中修复）。
* **CVE-2025-0110****（CVSS评分7.3）：**Palo Alto Networks PAN-OS OpenConfig 插件中存在一个命令注入漏洞，可导致能向 PAN-OS 管理 web 界面提出 gNMI 请求的认证管理员绕过系统限制并运行任意命令（已在 PAN-OS OpenConfig 插件2.1.2中修复）。

为缓解漏洞风险，强烈建议禁用从互联网或不可信网络访问管理界面。不使用OpenConfig的客户可选择禁用或从实例中卸载该插件。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Palo Alto Networks 修复退市 Migration Tool中的高危漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522035&idx=2&sn=71c00b294647fadae4e56ffc500f1300&scene=21#wechat_redirect)

[Palo Alto 修复已遭利用的严重PAN-OS DoS 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521932&idx=1&sn=518332fa38f3263ee23df7a70c1187d3&scene=21#wechat_redirect)

[Palo Alto 防火墙 0day 由低级开发错误引发](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521617&idx=2&sn=0e9ac32a3223e727cd6cd99460e0387e&scene=21#wechat_redirect)

[Palo Alto Networks：注意潜在的 PAN-OS RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=1&sn=3bf8ff26ce74c0c7fbfeb2701a773a5f&scene=21#wechat_redirect)

[Palo Alto 修复多个严重的防火墙漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521075&idx=1&sn=2987012f618a751eabf08e620add0615&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2025/02/palo-alto-networks-patches.html

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