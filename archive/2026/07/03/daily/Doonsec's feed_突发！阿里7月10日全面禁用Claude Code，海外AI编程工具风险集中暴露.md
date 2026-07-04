---
title: 突发！阿里7月10日全面禁用Claude Code，海外AI编程工具风险集中暴露
url: https://mp.weixin.qq.com/s/PcITmwfFrHtq8P-JWofYdw
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:38:38.375924
---

# 突发！阿里7月10日全面禁用Claude Code，海外AI编程工具风险集中暴露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mrBSV3yfH1afNPbqicLIYD7IgyuXVOevWYK3jpxo91O8tQOIrZDb0SKZp22TiagZ8ctXNXhc64xxvvZ03koXoWyPAiatoDibvyd6oAUOGP60TzM/0?wx_fmt=jpeg)

# 突发！阿里7月10日全面禁用Claude Code，海外AI编程工具风险集中暴露

原创

安爸
安爸

安安是个小妹妹

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

7月3日最新消息，据阿里内部人士透露，因Claude Code存在多重高危安全漏洞与合规隐患，阿里已将其列入高风险软件清单，7月10日起办公环境全面禁止使用。

![](https://mmbiz.qpic.cn/mmbiz_jpg/mrBSV3yfH1bZcBW6QZMFjlNWhNJ0icX9Via5jt7vwMqyOUDJT2dMLOT59cGZ2rCwsf65lZ61wzVHe0qT8vPhpLKRsEjDeAMiaZQY2qdialjnugg/640?wx_fmt=jpeg)

一、禁令落地：阿里全员停用Claude Code，自研Qoder替代

本次管控覆盖办公电脑、开发服务器、内网全场景，员工不得通过个人账户、代理等方式绕开限制，相关使用费用不予报销，内部统一推荐自研代码工具Qoder。阿里安全团队表示，公司数万研发人员若使用存在后门的海外工具，极易出现源码泄露、内网渗透等重大安全事故。

二、三大高危漏洞，代码资产安全岌岌可危

今年上半年Claude Code接连爆出致命漏洞，每一类都能直接入侵开发设备：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mrBSV3yfH1ZMNZy9fS3vtDWrGNwQcDetlFqZgiaJtpG6DjSNAUOdeibiaFQ2wfic4NtCmrr2v7xhz0GfMl3GYfWfUzUuZnjHYria5x6Xd53vicNaw/640?wx_fmt=jpeg)

1. 沙箱逃逸缺陷：内置bubblewrap沙箱无法保护核心配置文件，恶意代码可植入持久钩子，工具重启后仍能以主机高权限窃取密钥与源码。

2. 开源项目投毒攻击：攻击者在GitHub仓库预埋恶意配置文件，开发者拉取项目并用Claude Code打开时，恶意程序自动静默运行，常规检测难以察觉。

3. npm供应链后门：有人持续在其依赖包植入窃取代码，后台悄悄上传项目文件、云凭证至境外服务器，形成长期数据窃取通道。

三、地缘合规风险加剧，工具内置国内用户检测逻辑

除技术漏洞外，Claude Code背后厂商Anthropic的态度与产品设计，进一步触发大厂警惕。

![](https://mmbiz.qpic.cn/mmbiz_jpg/mrBSV3yfH1YaR0sGc7eib9pRuMkGM6xwTZyxJXzeqT4T6h8odtGvLcNoswAibqOWicscnMYGb4v4S2BeozG8yc4lZQrUcREoMgEQoKf3pLbtSQ/640?wx_fmt=jpeg)

逆向代码发现，工具自带识别逻辑，可读取设备时区、国内企业域名，标记中资设备并回传信息；

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mrBSV3yfH1ZThN0oCYAQhr5QMKDxjwcZW8a34Hyr2KHx6PnnJjrJS6GLpZNibdmm6kLZjyRsefN7k7jTybwu5n7MQlCiaRPmAg8wKRGWyicPibc/640?wx_fmt=jpeg)

早在去年9月，该公司就将使用禁令扩大至中国控股海外子公司，不少中资团队账号被无预警封禁。跨境传输代码、设备信息，既违反国内数据出境法规，也存在核心技术外泄隐患。

四、行业已成统一趋势：字节、快手早已封禁同类工具

阿里并非首个管控海外AI编程工具的头部企业，行业管控早已铺开：

字节跳动2025年5月下发内部通知，6月30日分批禁用Cursor、Windsurf等工具，强制自研Trae作为唯一合规代码助手；快手同年12月封锁Cursor，研发设备打开软件直接闪退，推广自研代码工具。

各家大厂逻辑高度一致：海外工具缺少国内合规资质，安全不可控，唯有自研内网代码助手，才能实现数据本地留存、操作全程审计。

五、行业启示：提效之外，安全才是开发底线

AI代码工具虽能大幅提升开发效率，但企业需守住安全红线。
对中小团队而言，办公环境杜绝境外AI编程工具，不借助代理访问海外代码助手，拉取开源项目前提前扫描依赖与配置文件，规避供应链攻击；对企业来说，内网自研代码工具已是大势所趋，国产工具功能持续完善，可兼顾效率与数据安全。

阿里封禁Claude Code给所有研发团队敲响警钟，效率永远不能凌驾于数据安全之上。你们公司是否管控海外AI编程工具？欢迎在评论区交流。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ic0GOIpDNE57AmZr7wYThknvEAB3Z7OM8ZiaDIV5IrBhtaC5VBd4DturFgsAGAJxiarVU1WxkOsV5mvicyQ7HMJQFg/0?wx_fmt=png)

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