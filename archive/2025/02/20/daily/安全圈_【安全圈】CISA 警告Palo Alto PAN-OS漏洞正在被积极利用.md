---
title: 【安全圈】CISA 警告Palo Alto PAN-OS漏洞正在被积极利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067894&idx=4&sn=85a6a4431ee456852c1e21ec6d1e5c65&chksm=f36e7476c419fd6000d9d45304d2355d038ef135174afcc1f809e8523cd87ae9ff867c33af28&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-20
fetch_date: 2025-10-06T20:35:56.148324
---

# 【安全圈】CISA 警告Palo Alto PAN-OS漏洞正在被积极利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhlDoYd4Q0sLjkoTGwVZdic6YOKRNI1cn5icNCvM6WX0KSZx6c3pyEfy38rdrr5dEypzkHGCJPZulTQ/0?wx_fmt=jpeg)

# 【安全圈】CISA 警告Palo Alto PAN-OS漏洞正在被积极利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhlDoYd4Q0sLjkoTGwVZdic684vVXd5aGHOHquDHK6ZbXDSWP8LGwhKOa4IwkGLBicpt3e5Hgdt65fA/640?wx_fmt=jpeg&from=appmsg)近期，美国网络安全与基础设施安全局（CISA）发布了一则紧急警报，矛头直指帕洛阿尔托网络公司（Palo Alto Networks）防火墙设备所搭载的操作系统 PAN-OS。该系统现正遭受黑客攻击，其存在的一个高严重性身份验证绕过漏洞（CVE-2025-0108）已被黑客们积极利用。

据监测，全球范围内已有超过 25 个恶意 IP 地址对未安装补丁的系统发动攻击。联邦当局联合网络安全专家发出警告：攻击者很可能将这一漏洞与其他漏洞串联起来，从而对关键网络基础设施造成严重破坏。

CVE-2025-0108 的通用漏洞评分系统 3.1 版评分为 7.8，这意味着，未经身份验证但能够访问 PAN-OS 管理 Web 界面的攻击者，可以借此绕过身份验证控制，进而执行特定的 PHP 脚本。虽说这一漏洞本身不会直接导致远程代码执行，但攻击者通过未经授权访问敏感功能，已然对系统的完整性和保密性构成了严重威胁。

帕洛阿尔托网络公司确认，若将 CVE-2025-0108 与 CVE-2024-9474（一个在 2024 年 11 月已修复的权限提升漏洞）结合利用，黑客便能完全控制设备。

受此次漏洞影响的版本包括 PAN-OS 10.1（10.1.14-h9 之前的版本）、10.2（10.2.13-h3 之前的版本）、11.1（11.1.6-h1 之前的版本）以及 11.2（11.2.4-h4 之前的版本）。不过，云下一代防火墙（Cloud NGFW）和 Prisma Access 部署目前不受影响。

## 攻击趋势与溯源

GreyNoise 的监测数据显示，攻击态势在短时间内急剧恶化。从 2 月 13 日仅 2 个恶意 IP 地址发起攻击，到 2 月 18 日，这一数字已激增至 25 个。进一步调查发现，这些攻击流量主要源自美国、德国和荷兰。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhlDoYd4Q0sLjkoTGwVZdic6ZWF6iaF0DzfxSVJpwB5kyaE9WcmE3As3oicebFlvxhDsCK8rXtY6oA1g/640?wx_fmt=jpeg&from=appmsg)

攻击者利用的是公开的概念验证（PoC）漏洞利用程序，而这些程序的技术细节，大多来源于 Assetnote 研究人员的披露。他们在调查早期 PAN-OS 漏洞时，首次发现了 CVE-2025-0108 这个漏洞。

2 月 19 日，帕洛阿尔托网络公司更新了安全公告，明确指出针对未安装补丁的防火墙，尤其是面向互联网的管理界面的攻击数量正在 “不断增加”。

对此，帕洛阿尔托网络公司发言人史蒂文・泰（Steven Thai）强调：“我们强烈敦促所有客户立即应用更新，并严格限制管理界面的访问权限。”

## 应对措施与建议

CISA 和帕洛阿尔托网络公司共同给出了以下应对建议：

1. 立即应用补丁：尽快将 PAN-OS 升级到 10.1.14-h9、10.2.13-h3、11.1.6-h1 或 11.2.4-h4 版本，这些版本已修复 CVE-2025-0108 漏洞。
2. 限制管理界面访问：只允许受信任的内部 IP 地址进行连接，坚决避免管理界面暴露在公共互联网中。
3. 禁用未使用的服务：若不需要 OpenConfig 插件，应及时将其停用，以防它成为额外的攻击入口。
4. 监测攻击行为：借助 GreyNoise 等威胁情报平台，实时跟踪与 CVE-2025-0108 相关的恶意 IP 地址。

Assetnote 的舒巴姆・沙阿（Shubham Shah）指出，CVE-2025-0108 的真正威胁在于，它为攻击者提供了初始访问途径。他强调：“攻击者会将这个漏洞与二次漏洞利用程序结合，从而实现命令执行。” 这种攻击策略并非首次出现，与之前利用 CVE-2024-0012 和 CVE-2024-9474 针对 PAN-OS 身份验证机制的攻击活动如出一辙。

对于依赖帕洛阿尔托防火墙的联邦机构和企业而言，当务之急是优先部署补丁，因为未受保护的设备随时都有被攻击的风险。CISA 发布这一警报，与其 “设计安全” 倡议高度契合，旨在敦促供应商和客户从源头上消除关键基础设施中的默认暴露风险。

随着攻击活动的持续升级，各组织务必争分夺秒，尽快缓解 CVE-2025-0108 带来的安全隐患。在帕洛阿尔托网络公司全力遏制威胁的同时，管理员必须严格落实访问控制措施，并假定未安装补丁的设备已被入侵，提前做好应对准备。

**来源：**https://cybersecuritynews.com/pan-os-vulnerability-actively-exploited/

***END***

阅读推荐

[【安全圈】短视频平台“封号圈”乱象猖獗，IP查询如何助力防范](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=1&sn=77b78d28e626bb57cf51f82d0c472aa6&scene=21#wechat_redirect)

[【安全圈】俄罗斯黑客利用 7-Zip 零日漏洞攻击乌克兰](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=2&sn=634853ba2d9852cc240a7d5d46ce82c5&scene=21#wechat_redirect)

[【安全圈】微软发现用于加密货币盗窃的 XCSSET macOS 恶意软件变种](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=3&sn=b875bcdbb815582bbc7966d6ebc3a164&scene=21#wechat_redirect)

[【安全圈】马斯克与 OpenAI 的交锋：收购提案遇冷，立场分歧引争议](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067874&idx=4&sn=38c4e0921e00478f77d52173d75865fa&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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