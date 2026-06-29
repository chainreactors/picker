---
title: 两伙黑客同时潜伏一家企业，用的全是合法工具
url: https://mp.weixin.qq.com/s/JsCeDpUJkKYc9gZWw3tU1Q
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:32:09.462832
---

# 两伙黑客同时潜伏一家企业，用的全是合法工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibSyDj9UTHJTqsxvbow3EuVCvAtlLLrgTgTa5nvicdcpN4iacYjibFYmONSCmPzX1NJhvk1vDAIUOiczOFrUmtOyam6P4vpUjaIAhsQ/0?wx_fmt=jpeg)

# 两伙黑客同时潜伏一家企业，用的全是合法工具

原创

承影
承影

兰花豆说网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

AI图片导读：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibQ5uzlZar3YFkNfnLt3ccaV6UXZCYlLSuzZc2GerUCYN6BR5BU6LYYF7tYRywQEm1azjRNeEHbZhKwutQEoRZbBAal3VDScxwA/640?wx_fmt=png&from=appmsg)

# 如果企业被黑了，找到攻击者、清除木马、恢复业务——这事就算完了？

未必。

微软DART团队最近披露的一起真实案例，直接把"单线程思维"的安全认知按在地上摩擦：

同一家企业网络里，同时潜伏着两支毫无关联的攻击组织。

更魔幻的是，他们大量使用的不是什么新型恶意软件，而是企业每天都在跑的合法工具。

Velociraptor、Cloudflare Tunnel、Zoho Assist、VS Code Remote SSH……

运维在用，安全团队在用，黑客也在用。

这意味着什么？

网络攻击已经进入一个"敌我难辨"的新阶段，AI时代的网络攻击尤其如此，好人坏人难分。

##

## 01 / 一次勒索调查，挖出两伙黑客

事件的起点很普通——一起勒索软件应急响应。

微软在排查中发现，攻击者通过公网暴露的SharePoint服务器漏洞切入企业内网，随后持续探测目标系统，翻找win.ini、web.config等敏感文件，寻找更多突破口。

到这里，还算"标准剧本"。

但越往深查，画风越不对。

微软确认：网络中存在Storm-2603组织的攻击痕迹。与此同时，另一支完全无关的攻击组织也在同一环境中活动。

两伙人，两套手法，一个受害者。

这对安全团队意味着什么？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibQe63QaCic7yN4XOq2pC9dicmVN5etmVEialibribFIwdDqPuIZLjOb00VliavAd1Viaw8GPWfLPAK3qyajblnEMicptypJaVgjw8ibR8yo/640?wx_fmt=png&from=appmsg)![]()

分析难度，直接翻倍。

你以为赶走了一个贼，殊不知隔壁屋还蹲着一个，还有可能两伙人在里面相互在打架了，哈哈！

##

## 02 / 攻击者为什么越来越爱"合法工具"？

这次事件最值得关注的，不是漏洞利用有多高级。

而是攻击者进了内网之后，几乎不碰恶意软件。

他们用的，全是企业自己就在跑的工具。

逐个来看：

### 🔹 Velociraptor——取证利器，反向成"侦察兵"

开源数字取证与应急响应工具，安全团队做调查的标配。

攻击者拿到SYSTEM权限后直接部署，对整个内网资产进行枚举和信息收集。

致命问题在于：安全人员看到Velociraptor在跑，第一反应是"同事在做调查"，而不是"黑客在侦察"。

### 🔹 Cloudflare Tunnel——加密隧道，流量隐身

攻击者用它建立加密通信通道，所有流量经Cloudflare网络转发。

传统边界安全设备看这些流量，和正常访问Cloudflare服务几乎没有区别。

C2通信藏在了合法CDN流量里。

### 🔹 Zoho Assist——远程运维软件，持久化神器

企业远程运维常见软件，攻击者直接拿来做远程控制。

最狠的一点：就算WebShell被清掉了，靠这条通道照样能重新进来。

清了一扇门，人家还有一扇窗。

### 🔹 VS Code Remote SSH——开发者天天在用

攻击者通过VS Code建立SSH连接，伪装成开发人员的正常开发行为。

对SOC平台来说，这种行为几乎不会触发高风险告警。

谁能分清这是程序员在写代码，还是黑客在搞事情？

除了上述工具，攻击者还顺手做了一整套"常规操作"：

● 创建新的本地管理员账户

● 创建域管理员账户

● 利用存在漏洞的驱动程序关闭安全防护

● 修改系统内存绕过EDR检测

整个过程，恶意代码反而不是重点，合法工具才是主角。

国内的安全厂商也得注意避免合法的安全产品被当成黑客工具使用，例如固信、联软、盈高等做终端管理和准入的厂商。

##

## 03 / 传统检测的三板斧，正在失灵

过去识别攻击，主要靠三个维度：

有没有木马？有没有病毒？有没有恶意程序？

文件检测、特征匹配、哈希比对——三板斧抡了几十年。

但现在，越来越多APT攻击已经变了。

攻击者大量采用一种经典思路——Living off the Land（LOTL，就地取材）。

什么意思？

利用系统已有组件、合法工具和可信软件，完成整个攻击链。

为什么有效？因为：

● 软件本身可信，数字签名正常

● 企业原本就在使用，不会引起怀疑

● 行为看起来像正常运维

于是传统安全产品面对一个尴尬的问题：

到底是管理员在运维，还是黑客在横向移动？

分不清。

这就是为什么近年来越来越多攻击事件中，真正暴露攻击者的，不再是某个恶意文件——而是多个行为串联后的异常轨迹。

检测重点，正在从"文件检测"转向"行为检测"。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibQXkul9TAia8XnnK80xVYibuHv3693QGfYOANr1935xsojsibQNe9DHOWkic0e3DbRu7aRqRaFREpYUXFKZJia9XyPmwwNPYIcz4EyA/640?wx_fmt=png&from=appmsg)![]()

## 04 / AI时代：从"黑客"到"攻击智能体"

如果说过去这些操作还需要人工完成，未来呢？

AI Agent可能进一步把攻击成本打到底。

一个具备自主能力的攻击Agent，理论上可以自动完成：

✅ 搜索可利用漏洞

✅ 自动部署远程管理工具

✅ 建立多条持久化通道

✅ 自动创建账号

✅ 绕过安全策略

✅ 根据防御情况动态切换控制方式

未来企业面对的，可能不是一名黑客，而是一个7×24小时不停歇的"攻击智能体"。

这也是AI安全越来越受关注的原因。真正需要防御的，不只是大模型和智能体本身的安全，而是AI驱动下的新型攻击方式。

##

## 05 / 企业现在该重点抓什么？

微软在此次事件中给出了值得参考的防护建议，我梳理为四个层面：

### 一、堵住入口：修复互联网暴露系统

重点关注SharePoint、Exchange、VPN等关键入口的漏洞修复，别让攻击者轻松拿到初始访问权限。大门要守好，建议大门外还要加一圈围墙。

### 二、守住身份：强化身份安全

多因素认证、最小权限管理，持续监控异常账号和权限变更。凭据滥用，是横向移动最常见的跳板。坚持零信任理念，永不信任，持续验证，做好隔离。

### 三、提升可见性：跨域关联分析

统一采集终端、身份、网络及云环境日志，构建跨域关联分析能力。让分散的异常行为，能串联成完整攻击链。通过AI进行异常行为分析，不能以身份判别人的好坏，而是要通过行为判断人的好坏。

### 四、盯紧合法工具：重点排查异常使用

Velociraptor、Cloudflare Tunnel、Zoho Assist、AnyDesk、TeamViewer、VS Code Remote SSH——这些工具本身不危险，但一旦出现在异常时间、异常设备、异常身份下，就必须触发排查。

不能因为"工具合法"就直接放行。

合法是属性，不是免检通行证。

##

## 写在最后

越来越多的真实案例在传递同一个信号：

真正危险的，已经不是那些容易识别的恶意程序，而是那些看起来一切正常的行为。不能从单一维度和行为来识别，应当通过多个维度，从整个路径链条按时间线结合起来分析异常行为。

攻击者正在学会用企业自己的工具，隐藏自己。

安全防护，也必须从"识别恶意软件"，升级到"识别异常行为"。

未来的攻防竞争，比拼的不再是谁的病毒特征库更大，而是谁能更快发现那些藏在正常业务中的异常轨迹。

合法工具不会消失，也不会被禁用。

但如何识别它们被恶意利用，将成为未来企业安全运营最核心的能力之一。

信息来源：https://cybersecuritynews.com

END

推荐阅读

[美国水务系统频遭黑客攻击，为何中国很少发生？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493543&idx=1&sn=4a93a012083d5160b92489a71c9428ec&scene=21#wechat_redirect)

2026-06-27

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibTkqkPAfxxeiad7rWK5ic4Rq9NkMsfys95JDyCYCu2Wqy6OFgf5JCRL2DZApUTYRJLzB3qdl4E1iaSpJRnbicWAu6IDUpThWzydxLw/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493543&idx=1&sn=4a93a012083d5160b92489a71c9428ec&scene=21#wechat_redirect)

[网站自动跳转"小黄网"？鄂尔多斯一煤矿企业栽了，被网信办立案处罚！](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493537&idx=1&sn=58dc126018002f3c8ba2bdb26797c16d&scene=21#wechat_redirect)

2026-06-20

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibRnRP1e3dAgYPaaicYMPbKaAArbc2Ov1NY0jJ9lu7JPLvVcszEaiaY9EbfByThDBEdODD3nWOE5LdZXls7wZt8lmM6sZAotByDbs/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493537&idx=1&sn=58dc126018002f3c8ba2bdb26797c16d&scene=21#wechat_redirect)

[高考填志愿，网安专业还值得报吗？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493531&idx=1&sn=b4d6d1d50b6fbb69539aef8852c1a5af&scene=21#wechat_redirect)

2026-06-19

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibSHBtPknVjZMJibVT3jiaw5Sict2ibLCYqVAxmWEcjI0tdDRfWXmkaMljOV87n957DatC2UtSibjOjbSotbJfKKS3bAcysp15NGl67U/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493531&idx=1&sn=b4d6d1d50b6fbb69539aef8852c1a5af&scene=21#wechat_redirect)

[LockBit勒索病毒的前世今生和应对策略](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493531&idx=2&sn=bdc4d137e79f6199aafc61720ef61ec1&scene=21#wechat_redirect)

2026-06-19

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AiaxibnzDXa1aGlsMrkTiaz1icibiahYNheLOLjnicF1n7vIuyyMWZgAnOV0RCXmuLJI8OPGrvZhhIia8N2LibFPqyuiampw/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493531&idx=2&sn=bdc4d137e79f6199aafc61720ef61ec1&scene=21#wechat_redirect)

[2026年，网络安全公司该怎么活？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493524&idx=1&sn=c99d8a56e9d2d29232f9ad5b152eed0f&scene=21#wechat_redirect)

2026-06-18

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTrOUOVZZ5qHgXhIxOe4yRmXLfFt80cPEMF9bXk1Hsyziaia16uriaMdzianhGZaVHU4Er6MWcPn7oyr7Ey7W46FX0RJlzicGLahQds/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493524&idx=1&sn=c99d8a56e9d2d29232f9ad5b152eed0f&scene=21#wechat_redirect)

[2026年，传统安全产品创业，还有出路吗？](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493519&idx=1&sn=1f564d76914744f830776049ee058413&scene=21#wechat_redirect)

2026-06-17

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibRfIBnHj0qsYcWmfiaOz0QwsUDicGcHkmmLGMmWQOlo4vdJISuRib8u2ciaEnB3sG9C738LBu1GicPUjXeDVJCvCFlWvP7FK1Aq9erg/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493519&idx=1&sn=1f564d76914744f830776049ee058413&scene=21#wechat_redirect)

[小白入门 | 渗透测试系统Kali安装全过程](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493514&idx=1&sn=e914183bdcc6d69da342e74bcdf226aa&scene=21#wechat_redirect)

2026-06-16

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibTAaR3nHZuRYiaIMN0aJhicbZM9ic8WH5n88xVUib2m4oTR07pvPNzIHDibAIyibvqZnWvWxM93yKYoqkfKHRiaQnicnw0LZ6w05BeEsibk/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493514&idx=1&sn=e914183bdcc6d69da342e74bcdf226aa&scene=21#wechat_redirect)

[小白入门 | 社会工程学模拟工具setoolkit](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493514&idx=2&sn=37331fdc6657fedf80f91283a8a6c952&scene=21#wechat_redirect)

2026-06-16

[![](https://mmbiz.qpic.cn/mmbiz_jpg/ribStUdgfRibRj8Hiaw5UPCuHnAjqXY8ibHPbdG7ia7OfRXpXcgt7lSZD2oGSCIkSIqk9ee8c3wbLMu8eFicREt6lO3Rcdq9daibcaKTlY19IFqzpg/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493514&idx=2&sn=37331fdc6657fedf80f91283a8a6c952&scene=21#wechat_redirect)

[没有安全数据积累，就别谈AI赋能网络安全](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=2247493261&idx=1&sn=2cdc303a546c6b59ce790f346e53d993&scene=21#wechat_redirect)

2026-06-14

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ribStUdgfRibSYZ2Q6oYKyVAgvgCPsQLLRjvicmybAjun0NibJVxpJ3oibRewaIPvLEu1DC6EYH7N7Y9Pqg8Xkmuich14BoPLPWx6ia88k5Xk5CdsQ/640?wx_fmt=jpeg)![]()](https://mp.weixin.qq.com/s?__biz=MzI3NzM5NDA0NA==&mid=224749...