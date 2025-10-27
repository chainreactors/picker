---
title: 新的 Xiū gǒu 网络钓鱼工具席卷多个国家
url: https://www.freebuf.com/articles/414840.html
source: FreeBuf网络安全行业门户
date: 2024-11-09
fetch_date: 2025-10-06T19:18:21.021878
---

# 新的 Xiū gǒu 网络钓鱼工具席卷多个国家

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

新的 Xiū gǒu 网络钓鱼工具席卷多个国家

* ![]()
* 关注

新的 Xiū gǒu 网络钓鱼工具席卷多个国家

2024-11-08 17:51:32

![](https://image.3001.net/images/20241108/1731059422_672ddeded6e206975ae13.png!small)

网络安全研究人员发现了针对英国、美国、西班牙、澳大利亚和日本用户的“Xiū gǒu”网络钓鱼工具包。该工具包活跃于公共、邮政和银行部门，模仿合法服务来盗取数据。

Netcraft 的网络安全研究人员发现了一种名为“Xiū gǒu”的新型网络钓鱼工具包，自 2024 年 9 月以来，该工具包一直在积极针对英国、美国、西班牙、澳大利亚和日本毫无戒心的用户。

该工具包以其独特的品牌和交互功能而著称，已在 2,000 多个网络钓鱼网站中被发现，使不同领域的个人和组织面临被入侵的风险。

该网络钓鱼工具包被称为“修狗”，来源于中文互联网俚语“xiū gǒu”，翻译为“小狗”，目前专注于与驾车者、政府支付和邮政服务相关的诈骗。管理面板和相关的 Telegram 帐户以一个拿着苏打水瓶的卡通狗吉祥物为特色，为原本恶意的工具增添了娱乐元素。

根据周四发布前与 Hackread.com 分享的技术博客文章，Xiū gǒu 的前端将 Vue.js用于网络钓鱼页面和管理面板，而后端则由 Golang 通过 SynPhishServer 可执行文件提供支持。这种组合支持更活跃、更难检测的网络钓鱼基础设施。

该工具包已部署在 1,500 多个 IP 地址和网络钓鱼域中，以与驾车者、政府支付和邮政服务相关的诈骗为目标。公共部门、邮政、数字服务和银行业的组织尤其容易受到攻击。一些值得注意的冒充对象包括：

* **Evri，一家位于英国的物流和快递公司**
* **Linkt，一家澳大利亚的交通服务机构**
* **USPS，美国邮政署**
* **Lloyds，英国的一家主要商业银行**
* **Services Australia，澳大利亚政府的一个社会服务机构**
* **New Zealand Post，新西兰邮政**
* **UK Government (****gov.uk****and DVSA)，英国政府**

使用 Xiū gǒu 的威胁行为者利用 Cloudflare 的反机器人和主机混淆功能来逃避检测。他们经常使用“.top”顶级域名 （TLD） 注册域名，选择与他们的骗局相关的名称，例如“parking”或“living”，或合并目标品牌名称的一部分。

攻击流通常以包含缩短链接的 Rich Communications Services （RCS） 消息开始，该链接将受害者引导至旨在模仿 gov.uk 等合法网站的网络钓鱼网站。机器人被重定向到非恶意站点，以进一步混淆活动。一旦受害者输入他们的个人和付款详细信息，这些信息就会通过欺诈者设置的机器人泄露到 Telegram。

![](https://image.3001.net/images/20241108/1731059459_672ddf038d9aec9bf232b.png!small)由 Xiū gǒu 网络钓鱼工具包提供支持的假英国政府停车罚款支付页面（截图：Netcraft）

![](https://image.3001.net/images/20241108/1731059481_672ddf19ab18471732dde.png!small)由 Xiū gǒu 网络钓鱼工具包提供支持的假 USPS 包裹发布页面（截图：Netcraft）

Netcraft 的研究提供了一个了解工具包作者思想的窗口，他说：“我们的研究为了解工具包背后的作者的思想和方法提供了一个有趣的视角，我们可以通过 xiū gǒu 对特定脚本语言的使用以及包含用户教程来看到。“

“作者还选择衡量和分析他们工具包的使用情况，很可能是为了让他们随着时间的推移优化和提高竞争力。我们还了解到就像狗狗吉祥物一样——作者如何在他们的工具包中注入个性和幽默感，留下自己独特的印记。

Xiū gǒu 网络钓鱼工具包仍然活跃，并且是针对企业和个人的持续全球活动的一部分。为了保护自己，请谨慎处理未经请求的消息，并按照以下步骤操作，以免成为下一个受害者：

* **点击前验证链接**：始终将鼠标悬停在电子邮件或文本中的链接上以检查实际 URL，除非经过验证，否则请避免点击缩短的链接。网络钓鱼工具包经常使用误导性 URL 来欺骗用户。
* **小心个人信息**：避免在通过未经请求的消息访问的网站上输入敏感信息，尤其是在该网站要求提供个人或付款详细信息时。
* **启用 Multi-Factor Authentication （MFA）：**MFA 增加了一层额外的保护。即使网络钓鱼工具包收集了您的凭证，MFA 也可以帮助防止对您的账户进行未经授权的访问。
* **使用反网络钓鱼软件**：许多反网络钓鱼工具可以检测可疑站点并阻止您访问它们，即使您不小心点击了网络钓鱼链接。
* **了解网络钓鱼策略**：随时了解常见的网络钓鱼策略和指标，例如不寻常的语言或可疑域名，这可以帮助您在威胁成为问题之前识别威胁。

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)