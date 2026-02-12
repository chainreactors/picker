---
title: 关于Notepad++更新服务遭攻击组织定向投毒事件的安全通告
url: https://mp.weixin.qq.com/s/j1rndBxjgoMDr4atsXhd-Q
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:20:13.353150
---

# 关于Notepad++更新服务遭攻击组织定向投毒事件的安全通告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbumWveematuEoN0En2tibzpPshGbdQhCQqt5OaDSup3U4RDCWUXbm6JCqHH1XlfibLcqMiaicTxosKjj6MU9CfqdaOeA9BZQqulNXBU/0?wx_fmt=jpeg)

# 关于Notepad++更新服务遭攻击组织定向投毒事件的安全通告

你信任的
你信任的

亚信安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YUnWCyLjbulO7R9HaoyTmyUR7iaicWt39kxhRjkp6MUq46fajnJib6C2n7TmogunZOD8qzXYnSj5Z0ytbljr3T4C81Q7ccUffzj8viadER1je2s/640?wx_fmt=jpeg)

近日，Notepad++官方发布声明，2025年6月至12月期间，Notepad++软件更新服务遭国家级APT组织入侵。攻击者通过劫持前托管服务商的共享服务器，定向拦截用户更新流量，将部分用户重定向至恶意服务器以投递伪装成官方更新的恶意程序。此次攻击属于供应链攻击，非Notepad++代码漏洞所致，而是托管基础设施被攻陷导致。建议所有用户立即升级至v8.8.9或更高版本，并持续关注官方安全通告。

根据披露信息显示，本次攻击者主要针对东亚政企机构（政府、金融、科研单位），攻击动机为窃取敏感数据和情报。

**事件时间轴**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

2025年6月：

攻击者入侵Notepad++前托管服务商的共享服务器，获取更新流量控制权。范围不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

2025年9月2日：

托管服务商通过内核和固件更新切断攻击者直接访问权限，但攻击者仍保留内部服务凭证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

2025年12月2日：

攻击者所有访问权限被彻底终止。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

2025年12月9日：

Notepad++发布v8.8.9版本，强化安装程序签名和证书验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

2025年12月27日：

发布v8.9版本，弃用自签名证书，改用GlobalSign合法证书。

**事件影响范围**

影响范围：Notepad++ v8.8.8及更早版本，受此攻击影响。

**应对处置建议**

* 排查网内是否有Notepad++受影响版本（v8.8.8及更早版本）；
* 移除Notepad++旧版本，清理安装目录及残留文件；
* 删除自签名证书：运行certmgr.msc，在“受信任的根证书颁发机构”中移除所有Notepad++自签名证书；
* 手动安装新版（v8.8.9及之后版本，推荐安装最新版本）或者选择其他平替软件。

**亚信安全解决方案**

面对复杂的供应链投毒与劫持攻击，亚信安全依托 TrustOne、Deep Security 及 AE 等核心产品，为政企用户构建从“源头预防”到“实时拦截”再到“行为分析”的多维防御体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

**1**

**软件供应链安全加固：从源头规避风险**

传统的直接更新模式存在被劫持风险。我们建议通过企业级内部托管分发，阻断毒源。

* **安全更新中心：**利用 TrustOne 与 Deep Security 的应用商店与实体补丁管理能力，在内部环境下统一验证并下发软件更新，彻底避免终端直接访问外部风险源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

**2**

**网络流量净化：斩断劫持路径**

针对攻击者劫持 DNS 或 CDN 的手段，我们从流量层设置“安全护栏”。

* **智能 DNS 过滤：**通过 TrustOne 的 DNS 白名单 机制，防止终端被重定向至非法服务器。
* **动态域名防护：**依托 AE 的防御能力，实时识别并拦截受劫持的非法 CDN 或恶意更新的代理域名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

**3**

**多重检测与阻断：让毒软件“落地即死”**

当恶意程序试图通过合法更新渠道混入系统时，亚信安全提供毫秒级的检测能力。

* **内核级实时查杀：**Deep Security 与 TrustOne 具备内核级防病毒引擎，在文件落盘瞬间完成扫描，精准阻断带毒更新。
* **传输监控与拦截：**AE 深度监控下载链路，一旦发现异常下载行为立即进行阻断，将威胁消除在传输过程中。
* **云沙箱深度解析：**针对未知或灰度文件，自动联动亚信安全云沙箱进行深度模拟与行为分析，快速补齐威胁情报，提升整体安全防御上限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSH8g2nVxlHIIO3FzqjyoKugFZianVbN5Dh4RJMXznEEC7UeGVT9vdnZfA/640?wx_fmt=png)

**4**

**持续威胁狩猎：精准锁定隐蔽攻击**

针对已潜伏或异常行为，通过 EDR 能力实现全回溯分析。

* **EDR 行为分析：**利用 TrustOne 与 Deep Security 强大的终端检测与响应能力，持续监控软件安装后的异常动作，快速定位并一键处置定向投毒攻击，确保企业内网持续清净。

**参考资料**

https://notepad-plus-plus.org/news/hijacked-incident-info-update/

https://notepad-plus-plus.org/assets/data/IoCFromFormerHostingProvider.txt

https://securelist.com/notepad-supply-chain-attack/118708/

了解亚信安全，请点击**“阅读原文”**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/iczzp36h0nbHibibbM15ufBwzEl7XmKf0qYkQWrLy6Kib3bicyrLrH8tGx9p996AKQPT93mOcicjK8mzibsV2yVyU6puA/0?wx_fmt=png)

亚信安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iczzp36h0nbHibibbM15ufBwzEl7XmKf0qYkQWrLy6Kib3bicyrLrH8tGx9p996AKQPT93mOcicjK8mzibsV2yVyU6puA/0?wx_fmt=png)

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