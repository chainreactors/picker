---
title: ApoorvCTF Rust语言逆向实战
url: https://mp.weixin.qq.com/s/h-rQjdzGQxoSXOSGFlvEBw
source: Doonsec's feed
date: 2026-08-07
fetch_date: 2026-08-08T03:21:07.172618
---

# ApoorvCTF Rust语言逆向实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mwFvjeHDLkjMQxGYVmY877XQ0My7W1sKm0eibxicA3SCDuQyFPccB0k5GU1QFWBPgScSlOtTMeuibPJv3icNqQsiadia8d42SYzE9ecuXr4XB2yWs/0?wx_fmt=jpeg)

# ApoorvCTF Rust语言逆向实战

Ba0
Ba0

蚁景网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

之前参加过的国外的比赛，名称叫：ApoorvCTF

看一下老外的比赛跟我们有什么不同，然后我根据国内比赛对比发现，他们考点还是很有意思的，反正都是逆向，哈哈哈

## Rusty Vault

题目描述：

In the heart of an abandoned shrine, there’s an old, rusted vault said
to guard an unspeakable secret. Many have tried to unlock it, but the
door’s demands are strange and no key seems to fit.

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwVVq80aicZIg1SPOQMxZDV44ibIXuDQpMQNfiacwU2gS3pInI38yqiaMoibQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

进入main函数，开始分析

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwzoPQbrJ95KfTaSSXw8HLh7PlYyCC0G0GXJNuGyqiaTsCge3ZV7L8W5g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

这个命名方式，大概率是Rust语言

对于rust语言逆向，一般采用动态调试分析的方法

主要还是看汇编，因为F5根本看不出来啥东西。。。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwbnq73icSezY5CV7jk0Lr1DgYHwrxjKibz12hticicz4icgURlmR83I6uunQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

从if比较处，可以看到成功和失败两个结果

那么这个比较绝对很关键

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgw6gHdiaQ9jicTVicHcIzOox4TuLQM80Pc4qAlNtd7j5Lzafl6s8cVZ1rsQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

进入后发现，啥也没啊？

坏了，得看汇编，为代码估计又出问题了

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgw65je3Jeib4iawWTlY5LJjOKricxz2LvPR34hiaxQdbBHC1yRIy3zsUJj7A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

发现了check2，果然为代码啥也看不到

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwrvFib59aCKxtJh83TllkUnVtXH0oVhDfItvPjfxjclw7n7QqVSjiciaGw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

对比check1-2

发现是在检测输入的字符串的字符类型，还是冲突的，不管了继续分析

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwUCSCibgTv3yC4LaDExCm0GyYdRCdSTQsnmFo0uIT7eoFibQysvj66OFg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

下面可以看到失败

往下滑动可以看到成功

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwofsbKcSjRzhZoylvZiaEsIfh4iayWESGyBBNFW908Ec4iaBFIqaJ5W6gQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

什么意思？

我猜测这题是改条件，然后动态输出flag？还有这好事

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwvphJb1ESa9aebxm6LAxPybvwggmekWNs0yOQpFE3N4YzvgRbT97Fzw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

后面都是正常输出flag了

那么我们现在去解密的地方回溯，估计我要改一些判断，改变流程，让程序正常走到解密的地方，然后输出flag

教大家一个回溯方法

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwkaCZ5yoos67fziczfpXXEBO7BBATq7QjZEFVJRVzgdiaVGZJhCqcNAuw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

对标签疯狂X键，交叉引用定位回溯

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgw5kyqxhZ1R3Q2OjGNnlIwibV5y5G3DU8RvgoQfdzoUESocVXyDdJ6uGw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)

最终定位到密文，发现是aes\_128\_cbc模式

需要：key+IV+密文=明文

这是一种思路，大家可以尝试

本文修改流程，让他自动输出明文

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwiaXqxSNYMUvOW6pKCd1tBvljJup7icSF2vjv6raLgq6KyXc8y0RK8eWg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

现在的思路就是：

x键回溯定位关键标签，修改关键判断

让程序自动走向解密

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwZ6uu9aIHqZlUSOlicz69Ld6VuSgSxTNeN2TQSnVI9nPsINHnBqzbuQQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

nop掉check1 和 check2

让他们走向自动解密的方向

![image](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldza8PxZ0axqzJLHiakiagJxgwVqBBb911ibGw2aSef6GUc75eIuFibhwOiaNUPNrDKUeZOzoXSgqAr53lA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

最终运行程序得到flag，静态patch流程，绕过check1-chekc2

```
1. apoorvctf{P4tch_1t_L1k3_1t's_HOt}
```

这在我们国内比赛还是很少见到的，国内大概率要写脚本解密，或许国内认为加密才是CTF的重点。国外侧重逆向本身，如果可以patch修改流程得到flag，为什么要去写解密脚本呢？

锻炼了我们通过汇编分析程序流程的能力，而不是为代码一键分析。

[![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldwoHriaVoyA6JNsGroYQAQp8xrlxS8RibJWibDF8T1pmkgSXqiaWQvmVB43S1IVCFBDOKTEQFDAP0QL5g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNTIwNTkyNg==&mid=2247549615&idx=1&sn=5de0fec4a85adc4c45c6864eec2c5c56&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

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