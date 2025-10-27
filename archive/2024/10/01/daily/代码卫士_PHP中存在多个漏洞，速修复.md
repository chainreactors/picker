---
title: PHP中存在多个漏洞，速修复
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520981&idx=2&sn=804d3895d9a0ec8b221e9c44449e8673&chksm=ea94a3bfdde32aa9f5bdbcd7d9bc4439b09e511516e9c3a98c685f059104336ba92c2d6638a7&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-01
fetch_date: 2025-10-06T18:53:02.017045
---

# PHP中存在多个漏洞，速修复

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT7JPaDtodibvQo5ibo3cLMWtPabwlpP8rwnx7ytoUbYhicicNkHJdJYR0vib9l1OtARDKqXjhrriaguDCQ/0?wx_fmt=jpeg)

# PHP中存在多个漏洞，速修复

DO SON

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT7JPaDtodibvQo5ibo3cLMWttVvomNRL1NrpvbO1Vee4ZAL4aDfHaPdytN4no4kBY9yzVHVmoNy3HQ/640?wx_fmt=gif&from=appmsg)

**最近，PHP 项目发布安全公告，修复了影响PHP多个版本的多个漏洞。这些漏洞包括潜在的日志篡改、任意文件包含、破坏数据完整性等。强烈建议所有的PHP用户立即将系统更新至最新的修复版本。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT7JPaDtodibvQo5ibo3cLMWtFGJ69ZYlYIsrIKvg7nPeepRqZqZelY92bw7pgW9nSuCe76KMoF5NoQ/640?wx_fmt=gif&from=appmsg)

**主要漏洞及其影响**

CVE-2024-9026是位于PHP-FPM 中的日志篡改漏洞，可导致PHP-FPM 中的日志遭操纵，从而导致攻击者插入过多字符或者从日志条目中删除最多4个字符，阻碍事件响应和取证调查。

CVE-2024-8927 是 cgi.force\_redirect 配置绕过漏洞。攻击者可利用该漏洞绕过由 cgi.force\_redirect 配置施加的限制条件，在一定配置下可导致任意文件包含，从而导致敏感数据被攻陷以及未授权访问。

CVE-2024-8926是PHP CGI 参数注入漏洞。该漏洞是在非标准 Windows codepage 配置下对此前修复方案 (CVE-2024-4577) 的绕过。虽然在真实环境中可能不会发生，但说明了修复甚至看似危害很小的漏洞的重要性。

CVE-2024-8925是对 multipart form 数据的错误解析漏洞，可导致合法数据不被处理，违反数据完整性。攻击者可利用该漏洞在某些情况下将合法数据排除在外。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT7JPaDtodibvQo5ibo3cLMWtFGJ69ZYlYIsrIKvg7nPeepRqZqZelY92bw7pgW9nSuCe76KMoF5NoQ/640?wx_fmt=gif&from=appmsg)

**受影响和已打补丁版本**

受影响版本如下：

* PHP 8.1.30之前
* PHP 8.2.24之前
* PHP 8.3.12之前

已打补丁版本如下：

* PHP 8.1.30
* PHP 8.2.24
* PHP 8.3.12

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMT7JPaDtodibvQo5ibo3cLMWtFGJ69ZYlYIsrIKvg7nPeepRqZqZelY92bw7pgW9nSuCe76KMoF5NoQ/640?wx_fmt=gif&from=appmsg)

**立即修复**

将PHP版本尽快更新至最新已打补丁版本十分重要。这些漏洞可造成严重后果，如数据泄露、系统攻陷和服务破坏等。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[PHPFusion 开源 CMS 中存在严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517570&idx=2&sn=7f19eccf19674dfcdf5f6515082f6989&chksm=ea94b4e8dde33dfedce31e414840f4579284cf9589c84909a1efa2bda3cb52dea3b0de2e1433&scene=21#wechat_redirect)

[骚操作：为了求职，劫持十几个热门 Packagist PHP 包](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516377&idx=2&sn=0aa4f09f20d6e3b6f3d8c848b2feb158&chksm=ea94b1b3dde338a5be544243c9b76240b3f11d15a91f87175d4c6e9fe6027453a2790dc4d498&scene=21#wechat_redirect)

[PHP包管理器Composer组件 Packagist中存在漏洞，可导致软件供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514137&idx=1&sn=347691413dc7ecfc2a2dedd365115329&chksm=ea948973dde3006553ae4c52ee22cd9f9c1eb480c80a59e78eaf25d9f9c974ed002d8e053488&scene=21#wechat_redirect)

[严重的PHP缺陷可导致QNAP NAS 设备遭RCE攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247512551&idx=2&sn=62ca391c055ea2839fe4178afcd48f4b&chksm=ea94808ddde3099be6ec5044d096c7921e4abb430485bfbd3eb207e3fa39af16c7a0ca6a766b&scene=21#wechat_redirect)

[PHP修复输入验证代码中的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510661&idx=1&sn=882fe4f483a2808b85d16e7372a34df1&chksm=ea949befdde312f97669bf5ef1e1a90ed95cec1bde3fdea1c1276cfd6fa3420696d4e583bc96&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/multiple-vulnerabilities-discovered-in-php-prompting-urgent-security-updates/

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