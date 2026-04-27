---
title: 惊天爆料！Claude 桌面版暗藏间谍程序，隐私沦陷
url: https://mp.weixin.qq.com/s/gTC6yD6RchztAUK1_meRIQ
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:05:16.901021
---

# 惊天爆料！Claude 桌面版暗藏间谍程序，隐私沦陷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIfic5ZXHz7DFPP0a0VuEjIicNYyCPXL1s7gDlyicI6eMsKH0rogtRD3NrKSywY7ISrQicT42NDCHx7UkFG0Jic6v6tBV622rs65iabU/0?wx_fmt=jpeg)

# 惊天爆料！Claude 桌面版暗藏间谍程序，隐私沦陷

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近期，Claude Desktop陷入隐私争议：安全研究人员发现，Anthropic的桌面客户端会在用户不知情的情况下，

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKp3fbVnNDu26essD05rk4n853deianRfjiceFto6ypQYnUj7GaPtcvTgk4v3Jia7mdfRbtTAnNRk3hILZJVX5wjC7gOQALpIO7h4/640?wx_fmt=jpeg)

向Chrome、Edge等7款浏览器写入桥接文件，甚至为未安装的浏览器预授权权限，被网友质疑为“间谍软件”。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJH41SwrDs3Ik4zMPicictQs7zUTLhuEuqoLgFDibqtKTfZZ1MjmghPGuwOzRnDjO7XMsicgQmMfiaMPOG9pNgAWCfv4dk9g6Ju5Z4I/640?wx_fmt=jpeg)

这一操作看似隐蔽，却暗藏隐私风险。

01、争议焦点：静默写入的“原生消息桥接”

用户安装Claude Desktop时，程序会自动向多浏览器配置目录写入名为 com.anthropic.claude\_browser\_extension.json 的文件，即使浏览器未安装也会创建目录。

这个“原生消息桥接”文件，能让Claude扩展直接与桌面程序通信，突破浏览器沙箱限制，获得读取网页、填写表单、截屏等权限。

网友评论：

感觉是真的，用了桌面版后系统就一直很卡，Cpu,内存占用度不高，有个System进程IO读写几乎占满了，又不是病毒

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKxo2fkh1JxFWXCj3NSGhb8ndicASLcVYOgex31zIfsM7kFslxfrkOic4rMtp6goyJiaPH6UfMM2rZ6uFZd1X9F4y8FPH58XeMheA/640?wx_fmt=jpeg)

更关键的是，这一过程未在安装提示、隐私政策中说明，用户全程无感知，甚至未来安装新浏览器后，扩展会自动获得授权，无需再次确认。

02、为何引发隐私恐慌？

这种操作的风险点在于，桥接文件运行时拥有用户级权限，一旦被滥用，可能成为数据泄露的通道。

安全专家指出，该文件预授权了特定扩展ID，理论上可能被用于读取用户浏览数据、窃取表单信息，甚至在后台执行自动化操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicIsfQdUFlicDgSQV9tNQibz0Th2y9DCWVS98xj1MqmYTXpkkUp3A0AEcreEeM8XtaU9qaAxhLajHPq7rPa3z6udxN4kr9o7W4eiaM/640?wx_fmt=jpeg)

更令人不安的是，文件会随程序启动自动重写，用户手动删除也无法永久生效，这种“顽固存在”的特性，加剧了用户对其“后门行为”的担忧。

03、Anthropic的回应与用户应对

目前Anthropic尚未公开回应这一争议，但有观点认为，该桥接是为实现“网页内容读取、跨设备同步”等功能的必要组件，只是未充分告知用户。不过，这并不能消除用户对“未经授权写入、预授权权限”的质疑。

普通用户可以通过检查浏览器的 NativeMessagingHosts 目录，手动删除相关文件；对隐私敏感的用户，也可暂时卸载Claude Desktop，或在虚拟机、隔离环境中使用，避免隐私数据暴露风险。

在AI工具日益普及的今天，“便利”与“隐私”的平衡再次被摆上台面。当你享受Claude的强大功能时，是否愿意为未知的权限让渡数据安全？这场争议，或许只是AI时代隐私战的冰山一角。

作者：hacking。前北漂程序员，现在做安全。

文章数据来自网络，大模型优化，侵权删。

**往期****相关****回顾**

[度假变噩梦！徐泽伟因美国网络入侵指控在意大利被扣，妻子：老人孩子还能等多久？](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550585&idx=1&sn=d393ee66a57f3a9b6d2895a3e3b9ed9d&scene=21#wechat_redirect)

[被指控网络入侵：中国徐泽伟在意大利被扣押的210天、或被引渡美国](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247550577&idx=1&sn=34365a236610b5680df0781a39f0e3d7&scene=21#wechat_redirect)

[徐泽伟引渡美国！意大利上诉被驳回，被美国指控黑客入侵](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247554243&idx=1&sn=5b97552ba5b90774714b65b7e239ebce&scene=21#wechat_redirect)

[朝鲜黑客封神！潜伏6个月盗走2.85亿，DeFi史上最精密猎杀案曝光](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247553894&idx=1&sn=102a2765f53d5763674c655e99a438c0&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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