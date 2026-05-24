---
title: 网安原创文章推荐【2026/5/22】
url: https://mp.weixin.qq.com/s/mCCJfUi1bmYtspNkh0FJ3w
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:59:33.797412
---

# 网安原创文章推荐【2026/5/22】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJABhVHR3gB7lApC1LbdYiauv4d3XZtYmh9lugP2kZhI0o2ibzHfmrSzAZnqeYicwyfRkiaCV3VDjbP9e3SPYHqA1ehga3zsse4RyoHQ/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/5/22】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-05-22 微信公众号精选安全技术文章总览

> 洞见网安 2026-05-22

---

### 0x1 [前后端分离渗透实战：当API成为盲区，你还在扫目录？](https://mp.weixin.qq.com/s?__biz=Mzk0NTc2MTMxNQ==&mid=2247485805&idx=1&sn=45a353272f7d5b8be508e6b140b29509&scene=21#wechat_redirect "前后端分离渗透实战：当API成为盲区，你还在扫目录？")

> 昆仑AI安全实验室 2026-05-22 22:54:09

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3oR6eMARh6zSPQ6t0torzZ6x3tLcwibmX05W73NFiaWQQGway4gwFfzytVlNUGgyNWqZzk3AaTfUI0jpnianIPBI7C7u8oKeR88sI0zqhPNK5E/640?wx_fmt=jpeg)

本文深入探讨了前后端分离架构下的网络安全问题，分析了攻击者如何利用前后端分离的漏洞进行渗透。文章首先阐述了前后端分离架构中信任前移带来的安全风险，随后详细介绍了信息收集的方法，包括JS逆向、Swagger文档泄露、GraphQL内省查询等。接着，文章重点分析了认证绕过、授权突破等攻击手法，如JWT密钥泄露、API接口无认证、BOLA/IDOR漏洞等。此外，文章还讨论了CORS配置错误、SSRF、数据导出漏洞等问题，并提出了相应的防御措施。最后，文章强调了安全防御必须在API层进行重构，并提醒安全从业者在进行安全评估和红队演练时需获得明确书面授权。

API安全

渗透测试

Web应用安全

漏洞挖掘

代码审计

安全防御

安全配置

安全最佳实践

安全意识

---

### 0x2 [【工具更新】EasyShell v1.7版本更新，修复诸多bug，同时新增诸多新功能](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484859&idx=1&sn=55dfff811f27f24c3d35ae3b6f3e6ace&scene=21#wechat_redirect "【工具更新】EasyShell v1.7版本更新，修复诸多bug，同时新增诸多新功能")

> 渗透云记 2026-05-22 18:40:13

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfO0XCNPrNpCkzibLmnVkW6LzdsFV9lzopqIUyG39tFibCicnJ7JqknNcGLIwMVdEG7C6UIIqpkPc8vcKSHZYeSKMibbXPFTbIbWMSsJicb5Zzxg/640?wx_fmt=jpeg)

这篇文章是新版本EasyShell的更新说明。新版本修复了诸多bug，并新增了多项功能。主要新增功能包括DNS监听协议，支持DNS协议上线，优化客户端体积，并将不必要的功能以插件形式实现。更新了EasyShell插件集合，主要新增了适用于Linux和Mac的信息收集命令。修复的问题包括隧道代理偶尔失败、文件上传无反应、文件管理模块卡死、客户端生成Win11黑框框、Linux客户端无法后台运行、插件日志显示混乱、插件日志面板遮挡按钮、交互式shell自动关闭等。此外，还修复了文件管理上传下载导致客户端卡死的bug，并采用后端异步操作优化了使用体验。隧道代理也进行了更新，修复了连接卡顿和偶尔断连的情况。EasyShell插件集现在支持根据目标主机自动加载对应的脚本进行调用。Linux插件新增了一键实现用户态程序与网络的隐藏功能，效果明显。文章最后还介绍了如何加入渗透云记的《叮叮当当》小圈子，以及渗透云记博客会员与叮叮当当纷传圈子权益共享的信息。

---

### 0x3 [SmartBi后台远程代码执行漏洞简单分析](https://mp.weixin.qq.com/s?__biz=MzkxNzUxMjU5OQ==&mid=2247485616&idx=1&sn=a5105bfefc3fc4bed6c1a97d7db5d11a&scene=21#wechat_redirect "SmartBi后台远程代码执行漏洞简单分析")

> 安全逐梦人 2026-05-22 07:17:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vOGOib9z4Wz4fl0IBseVZ2A7Feuz0rHHys6oWDMYgkO7jTSuEZsY4Tj7VSaTapPict13ialu7mNKfq3TKPMUxjYEQ/640?wx_fmt=jpeg)

本文对SmartBi后台远程代码执行漏洞进行了简单分析。首先介绍了SmartBi漏洞的影响版本和环境搭建所需的环境，包括源代码、SQL Server 2016和Tomcat等。接着，通过分析Smartbi-SmartbixSmartbi.jar中的MetricsModelForVModule和checkExpression类，发现checkExpression方法使用了ScriptEngineManager类和ScriptEngine API，这可能导致命令执行漏洞。文章详细分析了漏洞触发点和复现过程，并提供了相关链接以供参考。最后，文章展示了漏洞复现的详细步骤和结果，包括后台回复和相关的数据包扫描信息。

远程代码执行漏洞

Java安全漏洞

代码审计

SmartBi安全

漏洞复现

版本漏洞

数据库安全

Tomcat安全

---

### 0x4 [1day CVE-2026-5118 Divi 表单构建器 <= 5.1.2 | 通过角色注入进行未经身份验证的权限提升](https://mp.weixin.qq.com/s?__biz=MzkyMzcyMjgwNA==&mid=2247484157&idx=1&sn=086e1382c9e92e70493c17f5431d38cd&scene=21#wechat_redirect "1day CVE-2026-5118 Divi 表单构建器 <= 5.1.2 | 通过角色注入进行未经身份验证的权限提升")

> 爱坤sec 2026-05-22 02:30:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/uqtLGQlJSxXPHtzFLdJdOuwBUWmHicM5AkvRLiaA3K27LyoqCrak9cleI5wrickiaSISSLHTwsWMTicSGh9lV3gqYdtW9eVm84G2r4ibAT3ka6Kbk/640?wx_fmt=jpeg)

本文分析了WordPress插件Divi Form Builder的CVE-2026-5118漏洞。该漏洞存在于版本5.1.2及以下版本中，允许攻击者通过角色注入的方式实现未经身份验证的权限提升。漏洞的CVSS评分高达9.8，表明其严重性。文章提供了漏洞的影响版本、搜索语法、影响范围等详细信息，并指出受影响的资产大约有2968个。同时，文章提供了一个用于利用该漏洞的脚本链接，并强调了工具、思路和操作手法仅用于本地安全测试和教育目的，禁止用于非法入侵或攻击他人系统。此外，文章还提醒用户在下载工具后的24小时内删除，并提供了更多相关文章和工具分享的途径。

WordPress 漏洞

未经身份验证的权限提升

角色注入

CVE-2026-5118

插件安全

CVSS评分

安全测试与教育

---

> 本站文章为人工采集，目的是为了方便更好的提供免费聚合服务，如有侵权请告知。具体请在留言告知，我们将清除对此公众号的监控，并清空相关文章。所有内容，均摘自于互联网，不得以任何方式将其用于商业目的。由于传播，利用此文所提供的信息而造成的任何直接或间接的后果和损失，均由使用者本人负责，本站以及文章作者不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vML07fExwAdpcFbk9icEKB6QPwpicFcfu6QHCmkibP2yszUiaajx3CdP1cmNyq7ZGL40Q92d5QRpsY9yBTcgGlLNcg/0?wx_fmt=png)

洞见网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vML07fExwAdpcFbk9icEKB6QPwpicFcfu6QHCmkibP2yszUiaajx3CdP1cmNyq7ZGL40Q92d5QRpsY9yBTcgGlLNcg/0?wx_fmt=png)

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