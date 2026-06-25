---
title: 一种用于逃避EDR的激活上下文劫持新方法
url: https://mp.weixin.qq.com/s/CNf2yXaJ2b2CYVno00OA4A
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:45.864608
---

# 一种用于逃避EDR的激活上下文劫持新方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zqnzfCSS1kCcyRNevea1OFUIAkfJoibL42pZ5csOP4icoeFgl13PwcCWVDwNhzPb7n8T1ORV0OPm8fW4wFVkwBWIc9gdNlrhhibGOy7mmWe5aI/0?wx_fmt=jpeg)

# 一种用于逃避EDR的激活上下文劫持新方法

r3xmax
r3xmax

Hack分享吧

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| Ima知识库名称 | 加入条件 |
| --- | --- |
| 潇湘信安协同知识库（更新~ing!） | 免费加入 |
| 潇湘信安学习资料库（更新~ing!） | ≥3年粉丝 |
| 潇湘信安内部知识库（更新~ing!） | 星球成员 |

**工具简介**

PhantomCtx 是一款能够自动劫持激活上下文的工具，其目的是将任意 DLL 加载到绝大多数已签名的可执行文件中（例如 Microsoft、Adobe、Mozilla）。

该加载器被视为传统 DLL 劫持和侧加载技术的现代替代方案：与传统方法需要在目标系统上找到已签名的易受攻击的二进制文件，或者依赖于 HijackLibs 等页面上列出的已知易受攻击的 Microsoft 二进制文件（这些文件通常会受到监控）不同，该工具不需要特定的易受 DLL 劫持的二进制文件。

只要目标可执行文件通过其导入地址表 (IAT) 导入 DLL（几乎涵盖系统上的所有二进制文件），它就是 PhantomCtx 的有效目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zqnzfCSS1kDwYyMvSVWPaOicjicofUias9ZRv3IP7PfPXUBd5m0jV7vF8wSkbvJkN9V3E3WiaN5xmPGAiayvgvxt2YXdfeibRZzInWQZz7pJGxas0/640?wx_fmt=png&from=appmsg)

Elastic Cloud XDR 没有触发任何警报

![](https://mmbiz.qpic.cn/mmbiz_png/zqnzfCSS1kAV8NwRjrqrTgpDpJWFibAdIuCVB5Zjcc40icunvffEmUJQMR2DUf8K0DINM88A2RmBibZJMMYHbX0vSTfnowLF4j51BaNjG4tfsQ/640?wx_fmt=png&from=appmsg)

**下载地址**

Github地址：
https://github.com/r3xmax/PhantomCtx

作者博客文章：
https://rexmax.dev/posts/phantomctx-new-approach-to-activation-context-hijacking-for-edr-evasion/

---

**知 识 星 球**

星球已过800人，暂不再发放优惠券，如还有需要的师傅可加我VX：**S\_3had0w，**等你一起来学习**...！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/79gZQNibQ6ucZmnEM4ic7BNGMGr4B0qcmNL0s67Upd0MjN2OS0GomjDySCNHCb9ONP8Bqrt98luYMEkt8BVsn4Tg/640?wx_fmt=jpeg&from=appmsg)

| Ima知识库名称 | 加入条件 |
| --- | --- |
| 潇湘信安协同知识库（更新~ing!） | 限时免费 |
| 潇湘信安学习资料库（更新~ing!） | ≥3年粉丝 |
| 潇湘信安内部知识库（更新~ing!） | 星球成员 |

|  |  |
| --- | --- |
|  |  |

往期推荐工具

[红队必备：不进系统，扒光虚拟机所有密码](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493081&idx=1&sn=5b6d531e21f4d4c7e5f3f99547e13ca2&scene=21#wechat_redirect)

[微信小程序捡洞神器：自动反编译+扫密钥](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493056&idx=1&sn=8b89bb66e8f0e141149cf8803a8fd953&scene=21#wechat_redirect)

[Everything 这两大新功能太牛了！](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493019&idx=1&sn=5133b5ccc33c4e5d463dc62d758231fb&scene=21#wechat_redirect)

[把AI大脑装进BurpSuite，自动挖洞来了！](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247493002&idx=1&sn=5d6c6773aa3e5c7e2402f71ad5a88d19&scene=21#wechat_redirect)

[高级WebShell管理与后渗透神器](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492971&idx=1&sn=431cbbda7d6da109c86dd2c9254b0ed1&scene=21#wechat_redirect)

[263+上传漏洞检测与绕过工具](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492915&idx=1&sn=156543f9b79e9cde446cd8bae695ee43&scene=21#wechat_redirect)

[ProxyBridge (Proxifier替代工具)](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492808&idx=1&sn=139b4696d1d90983b55c3d8ef139a831&scene=21#wechat_redirect)

[基佬的"自动化"渗透测试扫描工具](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492716&idx=1&sn=a9b49b3ddf8da8f73008d36764b4eddf&scene=21#wechat_redirect)

[最好用的下一代目录爆破工具](https://mp.weixin.qq.com/s?__biz=MzA4NzU1Mjk4Mw==&mid=2247492620&idx=1&sn=b3f78bc0af5e231ea4cae18b381b8afa&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/79gZQNibQ6udVsppUXB8icSrqs3DgXGQmtNTUU8UDwxIvyu0V7s0jZy28sf6rLNTHviad1N9qQicqsibACs6YRQwdhw/0?wx_fmt=png)

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