---
title: PHP Composer 多个新漏洞可导致任意命令执行
url: https://mp.weixin.qq.com/s/YPVIc3MmgbXm2hFoehoFQA
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:48:36.948235
---

# PHP Composer 多个新漏洞可导致任意命令执行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfXXDzkl6hx1VksbYbXLibVJKEbfEFnqibdj5p9ALE0ZKzcX9Tc1EFM5eoWLAem1AQJtDReGKHcVUlxAX0q1KJKmZInzzYeaWoK5s/0?wx_fmt=jpeg)

# PHP Composer 多个新漏洞可导致任意命令执行

Ravie Lakshmanan
Ravie Lakshmanan

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**PHP****的包管理器 Composer 中存在两个高危漏洞，如遭成功利用可导致任意命令执行。**

这两个漏洞影响 Perforce VCS（版本控制软件），简述如下：

* CVE-2026-40175（CVSS评分7.8）是一个输入验证不当漏洞，可导致攻击者利用恶意 composer.json 中的Perforce仓库配置注入任意命令，在运行Composer的用户上下文中执行命令。
* CVE-2026-40261（CVSS评分8.8）：因转义不足导致的输入验证漏洞，攻击者可通过包含shell元字符的构造源引用注入任意命令。

维护者指出，即使系统未安装Perforce VCS，Composer仍会执行上述注入命令。这两个漏洞影响如下版本：

* >= 2.3 且 < 2.9.6（已在2.9.6中修复）
* >= 2.0 且 < 2.2.27（已在2.2.27中修复）

若无法立即打补丁，建议在运行Composer前检查composer.json文件，确保Perforce相关字段包含有效值；仅使用受信任的Composer仓库；仅对来自可信源的项目运行Composer命令；避免使用 --prefer-dist 选项或preferred-install: dist配置。

Composer表示扫描Packagist.org后并未发现攻击者通过发布包含恶意Perforce信息的软件包利用上述漏洞的证据。针对自托管Private Packagist用户，预计将发布新版本。

Composer 表示，作为预防措施，自2026年4月10日（周五）起，Packagist.org已禁用Perforce源元数据的发布。无论何种情况，建议用户立即更新Composer安装。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[这个严重的PHP漏洞正遭大规模利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522450&idx=1&sn=d780d2de95939199fea4d699bb1d2080&scene=21#wechat_redirect)

[PHPFusion 开源 CMS 中存在严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517570&idx=2&sn=7f19eccf19674dfcdf5f6515082f6989&scene=21#wechat_redirect)

[热门开源Dompdf PHP 库中存在严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515460&idx=2&sn=6ff90ed5a1a5cfe857a4aa75a16def08&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html

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