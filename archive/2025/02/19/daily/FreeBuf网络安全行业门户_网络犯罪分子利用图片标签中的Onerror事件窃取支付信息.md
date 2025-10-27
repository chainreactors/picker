---
title: 网络犯罪分子利用图片标签中的Onerror事件窃取支付信息
url: https://www.freebuf.com/articles/web/422085.html
source: FreeBuf网络安全行业门户
date: 2025-02-19
fetch_date: 2025-10-06T20:40:04.634210
---

# 网络犯罪分子利用图片标签中的Onerror事件窃取支付信息

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

网络犯罪分子利用图片标签中的Onerror事件窃取支付信息

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

网络犯罪分子利用图片标签中的Onerror事件窃取支付信息

2025-02-18 10:56:00

所属地 上海

![image](https://image.3001.net/images/20250218/1739862345660963_e5d7fb13257c41908ce27da0c5ee35ce.png!small)

网络安全研究人员近期发现了一种窃取信用卡信息的恶意软件活动，该活动主要针对运行Magento的电商网站。为了逃避检测，攻击者将恶意内容隐藏在HTML代码的图片标签中。

## MageCart恶意软件的新伎俩

MageCart是一种专门从在线购物网站窃取敏感支付信息的恶意软件。此类攻击通常会利用客户端或服务器端的技术手段，通过植入信用卡信息窃取程序来实施盗窃。通常情况下，这种恶意软件会在用户访问结账页面输入信用卡信息时被触发或加载，要么通过展示虚假表单，要么实时捕获受害者输入的信息。

“MageCart”这一名称来源于这些网络犯罪组织的原始目标——为在线零售商提供结账和购物车功能的Magento平台。多年来，此类攻击活动通过编码和混淆技术，将恶意代码隐藏在看似无害的资源中，如假图片、音频文件、网站图标，甚至是404错误页面。

Sucuri研究员Kayleigh Martin表示：“在这种情况下，影响客户端的恶意软件的目标同样是保持隐蔽。它通过将恶意内容隐藏在HTML的`<img>`标签中来达到这一目的，使其容易被忽略。”

## 利用Onerror事件执行恶意代码

与普通的`<img>`标签不同，此次攻击中的`<img>`标签充当了诱饵，其中包含指向JavaScript代码的Base64编码内容。当检测到onerror事件时，该代码就会被激活。这种攻击方式更加隐蔽，因为浏览器默认信任onerror函数。

Martin解释说：“如果图片加载失败，onerror函数会触发浏览器显示一个破损的图片图标。然而，在此次攻击中，onerror事件被劫持以执行JavaScript代码，而不仅仅是处理错误。”

此外，攻击者还利用了`<img>`HTML元素的“无害性”来增加攻击的成功率。恶意软件会检查用户是否处于结账页面，并等待毫无戒备的用户点击提交按钮，从而将他们输入的敏感支付信息窃取到外部服务器。

![image](https://image.3001.net/images/20250218/1739862348066746_43e1bb766a2e4b2d9bc684cf0bf5534b.png!small)

恶意脚本的设计目的是动态插入一个包含三个字段（卡号、有效期和CVV）的恶意表单，并将窃取的信息发送到wellfacing[.]com。

Martin补充道：“攻击者通过这个恶意脚本实现了两个令人印象深刻的目标：一是将恶意脚本编码到`<img>`标签中以规避安全扫描器的检测，二是确保最终用户在恶意表单被插入时不会注意到异常变化，从而尽可能长时间地保持隐蔽。”

## 针对电商平台的持久性攻击

针对Magento、WooCommerce、PrestaShop等平台的攻击者，其目标是尽可能长时间地不被发现。他们注入网站的恶意软件通常比影响其他网站的常见恶意软件更为复杂。

与此同时，网络安全公司还详细披露了一起涉及WordPress网站的事件。攻击者利用mu-plugins（或必用插件）目录植入后门，并以隐蔽方式执行恶意PHP代码。

Puja Srivastava指出：“与常规插件不同，必用插件在每次页面加载时都会自动加载，无需激活或出现在标准的插件列表中。攻击者利用此目录来保持持久性并规避检测，因为放置在此处的文件会自动执行，并且无法通过WordPress管理面板轻易禁用。”

**参考来源：**

> [Cybercriminals Exploit Onerror Event in Image Tags to Deploy Payment Skimmers](https://thehackernews.com/2025/02/cybercriminals-exploit-onerror-event-in.html)

# 网络安全 # web安全

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