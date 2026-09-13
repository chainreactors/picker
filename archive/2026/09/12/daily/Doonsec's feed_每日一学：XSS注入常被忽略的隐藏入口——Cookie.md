---
title: 每日一学：XSS注入常被忽略的隐藏入口——Cookie
url: https://mp.weixin.qq.com/s/bCtgKBmJf95VjKAos8tqLg
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:59:07.548175
---

# 每日一学：XSS注入常被忽略的隐藏入口——Cookie

# 每日一学：XSS注入常被忽略的隐藏入口——Cookie

原创

森林之家zbs
森林之家zbs

allby森林之家

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

01

XSS到底是个啥

XSS英译中叫**跨站脚本攻击**，听着是不是感觉乱七八糟的不知何意味？

那就让我再用中译中译中一下：

XSS就是黑客输入的内容，被网站当成程序执行了。

举个例子，比如网站有个留言板，用户在框里打字“你好”，网站就显示“你好”。

但黑客在框里输入一行代码，比如 `&lt;script&gt;alert(1)&lt;/script&gt;`网站对这行字没拦、没转义，直接把它当成代码给渲染了出来，然后浏览器也真就把这行代码给运行了。

等于黑客借着这个网站的壳，在别人浏览器里插了句嘴，想说什么说什么，想执行什么代码都可以：

比如偷Cookie、改页面、冒充你干坏事、偷走登录凭证、直接顶替账号操作。

02

被90%人忽略的那个隐藏入口

XSS注入大家都在测，下面三个“传参点”想必各位都耳熟能详了：

**URL参数**：网址问号后面的 `?id=`最常见。

**POST表单**：登录框、搜索框、提交框，往里塞payload。

**请求头**：User-Agent、Referer、X-Forwarded-For，也能被后端拼进页面。

90%的人对着这三处测了个底朝天，然后发现没洞就收工。

可还有一个隐藏入口常常被忽略——那就是Cookie

03

不信？我拿实战经历讲

之前测一个后台系统，弱口令一把梭，进去之后老套路：测SQL注入、测XSS、测文件上传、查框架有没有已知CVE。

然后就是磨，在GET里翻，POST里翻，各种路径各种参数一轮一轮碰，结果全都没有回显。

就当我准备收工前，多看了一眼Cookie。

Cookie的 `shenfen` 字段，原样躺在了页面上。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2wf8V0A7uBclnIe3ruuzHh6pqHRc0UJw0beB3gPVhj9TDDoqtTZUNjUZU4zSSNia3RviblhczWCHNYPR5bnpU9yYCCiaKibN0MCrMvnCEyKvr4U/640?wx_fmt=jpeg&from=appmsg)

Cookie里的shenfen字段，和页面输入内容一模一样

啥意思？后台把Cookie字段内容渲染在了页面上，原样输出——**没过滤，没转义，原封不动，**这不就是XSS的入口吗？

简单说下Cookie是什么东西：它就是服务器和浏览器之间来回传的**一张小纸条；**服务器用 `Set-Cookie` 响应头，往浏览器里塞一段数据，每次请求都自动带上；HTTP协议本身记不住谁是谁，全靠这张纸条认人。

问题就出在这，如果后端把**用户可控的数据**塞进了Cookie，那这张纸条就不是服务器单方面写的，用户也能往里面塞东西。

而且改Cookie根本不用什么高级工具，浏览器F12开发者工具，存储标签里直接改，连Burp都不用开。

那为什么测XSS的时候，这么多人都忽略了Cookie？因为平时在测XSS时，默认的“传参”清单里都没有它，Cookie更像“服务器的身份凭证”，更偏向于其他漏洞侧。

XSS入口找到了，然后就是验证走个流程。

把 `shenfen` 的值换成经典payload：`&lt;script&gt;alert(1)&lt;/script&gt;`

刷新页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2wf8V0A7uBdBzJxrbDk7UI4eUKficia7FBVWcsZl029zIgGaX0FlNdo8TQvg2F7Mdc5bCjiacMhqQQfthicCLGMRU4YDclEu4mviaGaZicN4GaHJE/640?wx_fmt=jpeg)

shenfen改成脚本payload，页面直接弹出alert(1)

一个反射型XSS到手(o^^o)

**特别提醒：**能证明漏洞就交报告！别碰删除和修改！测完收手，这是底线。

04

漏洞危害与修复

XSS不只是“弹个框”。

如果这个 `shenfen` 是后台管理员会自动携带的，攻击者的玩法是：搭一个恶意网页，让管理员访问（社工钓鱼、挂广告、劫持页面都行），这个网页用JS偷偷改掉管理员的 `shenfen` Cookie值，写入一段恶意脚本。

管理员下次打开后台，页面渲染时原样输出，浏览器执行。

可以参考我之前的文章：

[模拟安全案发现场：网站管理员上班刷美女照片导致公司服务器被黑](https://mp.weixin.qq.com/s?__biz=Mzg3NjY2NTYzOQ==&mid=2247484700&idx=1&sn=b54971047e45a31e07dae072c89f69c3&scene=21#wechat_redirect)

那漏洞要怎么修复呢？开发朋友可以参考下面四条：

**1. 后台访问加IP白名单**

**2. Cookie传参值做HTML实体化编码**

**3. Cookie加上 HttpOnly 和 Secure 两个标志**

**4. Cookie里加token随机值**

漏洞不一定藏在你熟知的地方，往往藏在你压根没想过“这也能传参”的地方。

Cookie当传参通道这种写法，比想象中常见得多，所以别只按模板走流程，多看一眼那些你默认“不可能”的地方。

你测站点的时候，遇到过哪些“打死也想不到”的传参点？Cookie、Referer，还是哪个冷门HTTP头？评论区聊聊吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZEY5a7YmV0vemdjA6fvqqblGxKWCcN4CTJCB2ujDEQP5r90enPicrtUGtNvOQIl2a61SGXtT8OcClCWGfhwv5DQ/0?wx_fmt=png)

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