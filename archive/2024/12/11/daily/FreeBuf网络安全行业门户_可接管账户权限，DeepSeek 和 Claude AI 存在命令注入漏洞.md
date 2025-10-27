---
title: 可接管账户权限，DeepSeek 和 Claude AI 存在命令注入漏洞
url: https://www.freebuf.com/news/417305.html
source: FreeBuf网络安全行业门户
date: 2024-12-11
fetch_date: 2025-10-06T19:41:08.499181
---

# 可接管账户权限，DeepSeek 和 Claude AI 存在命令注入漏洞

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

可接管账户权限，DeepSeek 和 Claude AI 存在命令注入漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

可接管账户权限，DeepSeek 和 Claude AI 存在命令注入漏洞

2024-12-10 10:43:31

所属地 上海

本文揭示了 DeepSeek 人工智能聊天机器人中的一个现已修补的安全漏洞的详细信息，如果成功利用，黑客可通过输入注入攻击方式控制受害者的账户。

![](https://image.3001.net/images/20241210/1733798584_6757aab87b3f982df37cd.png!small)

安全研究人员 Johann Rehberger，他记录了许多针对各种人工智能工具的注入攻击，发现在 DeepSeek 聊天中提供"Print the xss cheat sheet in a bullet list. just payloads"的输入触发了 JavaScript 代码的执行，作为生成的响应的一部分——这是典型的跨站脚本（XSS）攻击。

XSS 攻击可能会产生严重后果，因为它们导致在受害者的网络浏览器上执行未经授权的代码。攻击者可以利用这些漏洞劫持用户的会话并访问与 chat.deepseek[.]com 域关联的 cookie 和其他数据，从而导致账户被接管。

"经过一些实验，我发现采取控制用户会话所需的全部是 chat.deepseek.com 域存储的 userToken，" Rehberger 表示，他补充道，可以使用特殊设计的提示来触发 XSS 并通过注入攻击访问被攻击用户的 compromised user's userToken 。

提示包含了一系列的指令和一个 Base64 编码的字符串，DeepSeek 聊天机器人将其解码后执行 XSS 载荷，用于提取受害者的会话令牌，最终允许攻击者冒充用户。

与此同时，Rehberger 还展示了 Anthropic 的Claude Computer Use 可以通过提示注入来滥用，Claude Computer Use 可以使开发人员通过光标移动、按键点击和键入文本来控制计算机。通过提示注入，攻击者可以滥用 Computer Use 来下载 Sliver 命令与控制（C2）框架，执行该框架，并与攻击者控制的远程服务器建立联系，从而自主运行恶意命令。

此外，还发现可以利用大型语言模型（LLM）的 ANSI 转义码输出来通过提示注入劫持系统终端。这种攻击主要针对 LLM 集成的命令行界面（CLI）工具，被命名为 Terminal DiLLMa 。

"十年前的功能为 GenAI 应用提供了意想不到的攻击面，" Rehberger 说。"对于开发者和应用设计者来说，考虑将 LLM 输出插入的上下文是很重要的，因为输出是不可信的，可能包含任意数据。"

这还不是全部，威斯康辛大学麦迪逊分校和圣路易斯华盛顿大学的学者进行的新研究揭示了 OpenAI 的ChatGPT 在给出的附加标记格式的外部图像链接渲染的问题，这些链接可能涉及淫秽和暴力内容，以一个普通的善意目标为借口。

此外，还发现通过提示注入，可以间接调用 ChatGPT 插件，而无需用户确认，甚至可以绕过 OpenAI 设定的限制，以防止渲染来自危险链接的内容，将用户的聊天记录泄露到由攻击者控制的服务器上。

参考来源：<https://thehackernews.com/2024/12/researchers-uncover-prompt-injection.html>

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