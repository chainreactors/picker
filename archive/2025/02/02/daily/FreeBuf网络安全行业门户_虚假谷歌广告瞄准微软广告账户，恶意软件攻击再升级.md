---
title: 虚假谷歌广告瞄准微软广告账户，恶意软件攻击再升级
url: https://www.freebuf.com/articles/web/421008.html
source: FreeBuf网络安全行业门户
date: 2025-02-02
fetch_date: 2025-10-06T20:37:49.089418
---

# 虚假谷歌广告瞄准微软广告账户，恶意软件攻击再升级

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

虚假谷歌广告瞄准微软广告账户，恶意软件攻击再升级

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

虚假谷歌广告瞄准微软广告账户，恶意软件攻击再升级

2025-02-01 08:52:00

所属地 上海

![image](https://image.3001.net/images/20250201/1738382487873773_c1f2c76f52b0432cb4d70e5bfdfdf523.png!small)

网络安全研究人员近日发现了一场针对微软广告用户的恶意广告活动。攻击者通过伪造的谷歌广告，将用户引导至钓鱼页面，窃取其登录凭证。

Malwarebytes 高级研究总监 Jérôme Segura 在周四的一份报告中表示：“这些出现在谷歌搜索中的恶意广告，旨在窃取试图访问微软广告平台的用户的登录信息。”

这一发现是在该网络安全公司曝光类似活动几周后得出的。此前，攻击者利用赞助的谷歌广告，针对通过谷歌广告平台投放广告的个人和企业。

最新一轮攻击的目标是那些在谷歌搜索中搜索“微软广告”等关键词的用户，试图诱骗他们点击搜索结果页面中的恶意链接。

## 攻击手法：规避检测与钓鱼页面伪装

攻击者采用了多种技术手段来规避安全工具的检测。例如，他们将来自 VPN 的流量重定向到一个虚假的营销网站。此外，网站访问者还会收到 Cloudflare 的验证挑战，以过滤掉机器人。

更有趣的是，试图直接访问最终登录页面（“ads.mcrosoftt[.]com”）的用户会被重定向到一个与著名网络迷因相关的 YouTube 视频。

钓鱼页面与微软的合法页面（“ads.microsoft[.]com”）极为相似，旨在窃取受害者的登录凭证和双因素认证（2FA）代码，从而使攻击者能够劫持其账户。

Malwarebytes 表示，他们发现了一些针对微软账户的钓鱼基础设施，这些基础设施可以追溯到几年前，这表明该活动已经持续了一段时间，并且可能还针对了 Meta 等其他广告平台。

值得注意的是，大多数钓鱼域名要么托管在巴西，要么使用巴西顶级域名“.com.br”，这与针对谷歌广告用户的攻击活动类似，后者主要使用“.pt”顶级域名。

《黑客新闻》已联系谷歌寻求评论，但该公司此前曾表示，他们采取措施禁止旨在欺骗用户以窃取其信息的广告，并积极致力于实施针对此类行为的反制措施。

![image](https://image.3001.net/images/20250201/1738382489411717_ddd62dfc7aac411496289104d0716221.png!small)

## 短信钓鱼攻击：冒充美国邮政服务

此次披露紧随一场短信钓鱼活动的出现，该活动利用包裹投递失败的诱饵，专门针对移动设备用户，冒充美国邮政服务（USPS）。

Zimperium zLabs 研究员 Fernando Ortega 在本周发布的一份报告中表示：“该活动采用了复杂的社会工程策略和一种前所未见的混淆手段，旨在通过恶意 PDF 文件窃取凭证并泄露敏感数据。”

这些短信敦促收件人打开附带的 PDF 文件，以更新其地址以完成投递。PDF 文件中包含一个“点击更新”按钮，将受害者引导至一个 USPS 钓鱼网页，要求他们输入邮寄地址、电子邮件地址和电话号码。

钓鱼页面还伪装成重新投递的服务费，以窃取用户的支付卡信息。输入的数据随后被加密并传输到攻击者控制的远程服务器。该活动已检测到多达 20 个恶意 PDF 文件和 630 个钓鱼页面，表明这是一次大规模行动。

Ortega 指出：“该活动中使用的 PDF 文件嵌入了可点击的链接，但没有使用标准的 /URI 标签，这使得在分析过程中提取 URL 变得更加困难。这种方法使 PDF 文件中已知的恶意 URL 能够绕过多个终端安全解决方案的检测。”

这一活动表明，网络犯罪分子正在利用移动设备的安全漏洞，进行社会工程攻击，利用用户对知名品牌和看似官方通信的信任。

类似的 USPS 主题短信钓鱼攻击还利用苹果的 iMessage 来传递钓鱼页面，这是一种已知由中文威胁行为者“Smishing Triad”采用的技术。

这些消息还巧妙地试图绕过 iMessage 的一项安全措施，该措施防止链接可点击，除非消息来自已知发件人或用户回复的账户。这是通过在消息中包含“请回复 Y”或“请回复 1”来实现的，以关闭 iMessage 的内置钓鱼保护。

值得注意的是，这种方法此前与名为 Darcula 的钓鱼即服务（PhaaS）工具包有关，该工具包已被广泛用于针对 USPS 等邮政服务和 100 多个国家的其他知名组织。

Huntress 研究员 Truman Kain 表示：“骗子们构建了这次攻击，这可能就是为什么它在野外如此常见。简单的事实是，它奏效了。”

**参考来源：**

> [Malvertising Scam Uses Fake Google Ads to Hijack Microsoft Advertising Accounts](https://thehackernews.com/2025/02/malvertising-scam-uses-fake-google-ads.html)

# web安全 # 移动安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

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