---
title: CISA督促软件维护人员修复路径遍历漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519411&idx=1&sn=71d7f62af378983948cbcfd164e479e7&chksm=ea94bdd9dde334cf0ea19613ca4a0e169aa3a40e91e48a6e0bf7ddcd1baf7dd1713e112b9cb6&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-07
fetch_date: 2025-10-06T17:18:10.874110
---

# CISA督促软件维护人员修复路径遍历漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTDfMJ0ibTuJxSUG2QK9icP3eotUTvsSjYgq8F6W58XFcoXNG5YeKKjbntsWmRnicka0VpRMKhGM6LBA/0?wx_fmt=jpeg)

# CISA督促软件维护人员修复路径遍历漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**CISA和FBI督促软件企业审计产品并在交付前修复路径遍历漏洞。**

攻击者可利用路径遍历漏洞（也被称为目录遍历漏洞）创建或覆写用于执行代码或绕过安全机制如认证的重要文件。这类安全缺陷可导致威胁行动者访问敏感数据如凭据可用于暴力破解业已存在的账户以攻陷目标系统。另外一个可能的场景是拿下或阻止对易受攻击系统的访问权限，这些系统可被覆写、删除或损坏用于认证的重要文件（从而将所有用户登出）。

CISA和FBI指出，“目录遍历利用成功的原因是技术制造商未能将用户提供的内容视作潜在的恶意内容，因此未能正确保护客户安全。路径遍历等漏洞至少从2007年开始就被称作‘不可被原谅’的漏洞，尽管如此，目录遍历漏洞（如CWE-22和CWE-23）仍然是普遍存在的漏洞。“

**因近期关基攻击引发**

这份联合警报是对“最近的公开威胁活动利用软件中的目录遍历漏洞（如CVE-2024-1708和CVE-2024-20345）攻陷软件用户的回应，这些攻击影响关键基础设施行业，包括医疗和公共健康行业等”。例如，ScreenConnect 中的路径遍历漏洞 CVE-2024-1708 与CVE-2024-1709组合用于 Black Basta 和 Bloody勒索攻击，推送 CobaltStrike 信标和 buhtiRansom LockBit 变体。

CISA和FBI 建议软件开发人员执行“为人熟知且有效的缓解措施“，阻止目录遍历漏洞，包括：

* 为每份文件生成随机标识符并分开存储相关联的元数据，而不是在命名文件时使用用户输入。
* 严格限制可在文件名称中提供的字符类型，如限制为字母数字字符。
* 确保所上传文件没有可执行文件权限。

路径遍历漏洞在MITRE的 Top 25最危险的软件弱点中排行第8，超过界外写、XSS、SQL注入、UAF、OS命令注入和界外°漏洞。3月份，CISA和FBI发布另外一份“设计安全“警报，督促软件制造企业高管执行缓解措施，阻止SQLi漏洞。SQLi 漏洞在Top 25最危险弱点中排列第三，影响2021年至2022年的软件，仅排在界外写和XSS之后。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[今年9月底前，CISA将为联邦机构发布重要软件产品清单](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519338&idx=4&sn=d93cc10a53a449bb46ffc1b38e9e0981&chksm=ea94bd00dde334164fe8e2de442a5eaa6f379b9f3fde0d0d4ee1f39b9b720e3406747d24cae1&scene=21#wechat_redirect)

[CISA：Sisense事件也影响关键基础设施，或引发供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519274&idx=2&sn=1e4ab289a236019dcd29441ea2c972a9&chksm=ea94bd40dde334567d7f43c6b232181f011cec4f0aabc3ec5af3f4a138a1add0c38f16d957fa&scene=21#wechat_redirect)

[CISA称微软 SharePoint RCE 漏洞已遭在野利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519170&idx=2&sn=bbf2c37f65d8ab7122da6825cea54ef3&chksm=ea94baa8dde333bed9f1c3fa01b9fe5132e2e6d1eaf38be56ab90a1500647629f3819d43f19c&scene=21#wechat_redirect)

[CISA督促软件开发人员消除SQL注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519154&idx=2&sn=e5156dc817f213bae9628a3a674da4e8&chksm=ea94bad8dde333ce498ee36da84dbfce9ddeb839294d45a9916983f7515549e2bd774f39bb8b&scene=21#wechat_redirect)

[CISA提醒称 Windows 流服务漏洞已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518984&idx=2&sn=10dbd7931e85e24303fd5674c53a60ec&chksm=ea94ba62dde333748cd9313b47d1328484c132982a82eaf8a825c8d53a8d8a558c3cd7522bc7&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/cisa-urges-software-devs-to-weed-out-path-traversal-vulnerabilities/

题图：Pixabay License

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