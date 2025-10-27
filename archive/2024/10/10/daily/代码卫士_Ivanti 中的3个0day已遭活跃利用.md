---
title: Ivanti 中的3个0day已遭活跃利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521006&idx=2&sn=9a5993bb8ee14a8ab3071f40bb56c909&chksm=ea94a384dde32a92ccb1a8526ad5c231c4b03f141939c534f660d161815dae61f90ad81795c6&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-10
fetch_date: 2025-10-06T18:54:20.994838
---

# Ivanti 中的3个0day已遭活跃利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTmd846yz8iaLyDtZZqk0sdUd0UjRHwDAViaibHicFyb2GSicQGy8GzNEtaMEuykMfmhPp7Meq1hv5icmnw/0?wx_fmt=jpeg)

# Ivanti 中的3个0day已遭活跃利用

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Ivanti 公司提醒称影响其云服务设备 (CSA) 的三个新漏洞已遭在野活跃利用。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTmd846yz8iaLyDtZZqk0sdUb8NG6oJATs6RZicDrCT8KViaKIpKnjEbWUMkENPY1VYufoGdgVBkaWFQ/640?wx_fmt=gif&from=appmsg)

这些0day漏洞与CSA中上个月修复的另外一个漏洞组合利用。这些漏洞遭成功利用可导致具有管理员权限的认证攻击者绕过限制、运行任意SQL语句或获得远程代码执行权限。

Ivanti 公司提到，“我们发现运行CSA 4.6 补丁518及之前版本的数量有限的客户遭CVE-2024-9379、CVE-2024-9380和CVE-2024-9381与CVE-2024-8963的组合利用。”目前尚未有证据表明运行 CSA 5.0的客户环境遭利用。这三个漏洞的简要介绍如下：

* CVE-2024-9379（CVSS评分6.5）：位于 Ivanti CSA 5.0.2之前版本管理员web 控制台中的SQL注入漏洞，可导致具有管理员权限的远程认证攻击者运行任意 SQL 语句。
* CVE-2024-9380（CVSS评分7.2）：位于 Ivanti 5.0.2之前版本管理员 web 控制台中的操作系统命令注入漏洞，可导致具有管理员权限的远程认证攻击者获得远程代码执行权限。
* CVE-2024-9381（CVSS评分7.2）：位于 Ivanti CSA 5.0.2之前的路径遍历漏洞，可导致具有管理员权限的远程认证攻击者绕过限制。

Ivanti 公司观察到的攻击活动组合利用此前提到的漏洞与CVE-2024-8963（CVSS评分9.4）。后者是一个严重的路径遍历漏洞，可导致远程未认证攻击者访问受限制的功能。该公司表示这三个新漏洞是调查CVE-2024-8963和CVE-2024-8190（CVSS评分7.2，位于CSA中的已修复OS命令注入）漏洞利用过程中发现的。

除了更新至最新版本 5.0.2 外，Ivanti 公司还建议用户查看该设备中是否存在被修改或新增加的管理员用户，查看是否存在攻陷指标或者安装在设备上的端点检测和响应 (EDR) 工具是否发出警报。

不到一周前，美国网络安全和基础设施安全局 (CISA) 将影响 Ivanti 端点管理器 (EPM) 的一个漏洞 (CVE-2024-29824，CVSS评分9.6) 纳入必修清单。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[CISA：这个严重的 Ivanti vTM 漏洞已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520913&idx=2&sn=2148647cf20c87cf57d601cf283f4805&chksm=ea94a3fbdde32aed7e1bc8dad03d352202f8a631fd67d368bec1d9d01ce90fda64458ba4cdb2&scene=21#wechat_redirect)

[CISA 和 Ivanti：Cloud Services Appliance 高危漏洞已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520811&idx=1&sn=890fffef04e0244ca4a0fe359dfb3886&chksm=ea94a341dde32a57534c153b9526fd132574d3fa54a5c70c2bf6fe73dcf1c38e1c35c88ce3d1&scene=21#wechat_redirect)

[Ivanti 修复Endpoint Management 软件中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520759&idx=2&sn=1fc5e0f7a15b2f6ee85191294e7148e0&chksm=ea94a09ddde3298b03f1d93d760c4ebe1bbf0831c2823c5d15bdc98a012ee7662c48075afa5d&scene=21#wechat_redirect)

[Ivanti 修复Endpoint Manager 中的严重RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519584&idx=3&sn=2aa72d7f1d783c31f298fa9a0f01f07f&chksm=ea94bc0adde3351c1cf417917d51eb468cc181088b1cf49ea4d38cc9f05da775e3aa19c6dd05&scene=21#wechat_redirect)

[Ivanti：注意！Avalanche MDM 解决方案中存在多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519303&idx=2&sn=e86decfa003bf7ebcb19d43552440c7f&chksm=ea94bd2ddde3343b1eba25473eb57c432ce40d7ded22623619060fbc6c299c461dc0087f1d1b&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/zero-day-alert-three-critical-ivanti.html

题图：Pexels License

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