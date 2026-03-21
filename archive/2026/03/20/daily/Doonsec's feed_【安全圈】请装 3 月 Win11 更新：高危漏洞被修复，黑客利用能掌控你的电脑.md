---
title: 【安全圈】请装 3 月 Win11 更新：高危漏洞被修复，黑客利用能掌控你的电脑
url: https://mp.weixin.qq.com/s/4MzCSMQlTGU_14UcDpue3w
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:00:47.707446
---

# 【安全圈】请装 3 月 Win11 更新：高危漏洞被修复，黑客利用能掌控你的电脑

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFUacVBlYf7LRNDVY9DexrZw3ghBpkFgmh1D1mJibWMj426TVHr4GkpwEgwAeWMolDdNez3WiamFJicFQQMlibCn1ic49dN5Zj30O3s/0?wx_fmt=jpeg)

# 【安全圈】请装 3 月 Win11 更新：高危漏洞被修复，黑客利用能掌控你的电脑

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

高危漏洞

科技媒体 BornCity 今天（3 月 20 日）发布博文，报道称微软本月（2026 年 3 月）推送的 Windows 10、Windows 11 安全更新，修复了文件管理器网络搜索失效问题以及 RegPwn 高危注册表漏洞。

在文件管理器方面，网络搜索失效问题可以追溯到 2025 年 12 月中旬，基于系统管理员放不开，企业域环境中的客户端在将各类文件共享映射为网络磁盘后，Windows 自带的搜索功能突然无法返回任何结果。

随后，更多受影响的用户证实了该漏洞的广泛性。受波及的操作系统不仅涵盖 Windows 11（24H2 至 25H2 版本），还向下波及了 Windows 10 22H2 版本。在以 Windows Server 2022 作为主域控制器（PDC）的网络环境中，用户在执行搜索时会遭遇严重的 " 卡顿 "，甚至完全无法工作。

在 3 月补丁星期二活动日（3 月 10 日），微软通过适用于 Windows 11 24H2/25H2 的累积更新 KB5079473，修复了搜索可靠性。此外多位受影响用户随后反馈安装本次更新后已修复该问题。

RegPwn 高危注册表漏洞方面，该漏洞追踪编号为 CVE-2026-24291，攻击者利用该漏洞，可以把一个普通的电脑账户升级为拥有最高控制权的 " 超级管理员 " 账户。**该漏洞的 CVSS 3.1 评分为 7.8 分，危险等级为 " 高 "，且被官方认定为 " 极有可能被利用 "。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFDha8fLx74iaxjCmMwrhaZ3uzLNoIO3IS5VJr7DzaoDlCcdOicAia9FpHvKj70BD1Cic0Mmicd0lwmoZDUwEEQQiaEtqUyREzC0moVo/640?wx_fmt=jpeg&from=appmsg)

英国安全研究团队 SDSec 于 2025 年 1 月发现该漏洞，在微软本月安全补丁修复后，该团队于 3 月 13 日公开了详细的技术分析报告。

报告指出，该漏洞的核心在于 Windows 无障碍基础架构（ATBroker.exe）分配关键资源权限时存在缺陷。

微软为了帮助有特殊需求的用户，在 Windows 内置了屏幕键盘、讲述人等无障碍功能。当用户启动这些功能时，系统会在注册表中创建特定的配置键值，并赋予低权限用户完全控制权。

随后，在用户登录过程中，系统进程会将这些配置数据复制到系统级注册表中。然而，系统在此过程中错误地向当前登录用户授予了写入权限，这就为攻击者留下了可乘之机。

当用户锁定屏幕或以管理员身份运行程序时，系统会同时启动两个 "atbroker.exe" 进程：一个以普通用户权限运行，另一个以 SYSTEM 权限运行。

由于低权限用户可以修改特定的注册表路径，攻击者能够利用注册表符号链接，将目标路径重定向到任意系统注册表键值。

***END***

阅读推荐

[【安全圈】iOS18 爆高危漏洞！不升危险，升级变卡](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074879&idx=1&sn=a99f5ab259944d0f68ee8f470256a869&scene=21#wechat_redirect)

[【安全圈】Aura 公司证实数据泄露，90 万营销联系人信息遭曝光](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074879&idx=2&sn=143311d48cdc9eb9cf658d5d5a45979d&scene=21#wechat_redirect)

[【安全圈】CVE-2026-3888：Ubuntu 桌面版 24.04+ 易受提权漏洞攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074879&idx=3&sn=f2683ea27641f32a563e177c417115b9&scene=21#wechat_redirect)

[【安全圈】“ AI 刺客”漏洞披露：小字等方式伪装实现执行恶意代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074842&idx=1&sn=7ee374e3e9bd7db9d13be0e70464f9c8&scene=21#wechat_redirect)

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