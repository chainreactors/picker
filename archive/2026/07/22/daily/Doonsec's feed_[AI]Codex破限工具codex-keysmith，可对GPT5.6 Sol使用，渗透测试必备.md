---
title: [AI]Codex破限工具codex-keysmith，可对GPT5.6 Sol使用，渗透测试必备
url: https://mp.weixin.qq.com/s/5OTWucdNZg-fT4zkb5NLVg
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:08:25.977335
---

# [AI]Codex破限工具codex-keysmith，可对GPT5.6 Sol使用，渗透测试必备

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/niasx7fyic9CNVEiaeWPic8uibYcnsVrPxcBTwqBUckNOeMStaDM9gSXnDwXGKLnvW8czv2dungFNsCpC2TW04fll0t4s2UtM07v7a1tKWtwBNB0/0?wx_fmt=jpeg)

# [AI]Codex破限工具codex-keysmith，可对GPT5.6 Sol使用，渗透测试必备

陸以橋EthanPier
陸以橋EthanPier

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CTF课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/niasx7fyic9CMs6pyt2xl3Ng0QWByv0oD67COatsbL7SbcLetqC6mr3bFalmibIID1ricPHNl6xHHrqjmb0vLc7Sm0ficuiaroLKTJrNDibIPJwoBk/640?wx_fmt=jpeg)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic#imgIndex=1)

#

专注于漏洞挖掘、系统化从基础入门到实战漏洞挖掘，包含团队自整的挖掘注意点和案例、渗透经验、SRC漏洞案例、代码审计、挖洞思路等高价值资源。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有优惠券。

#

文章作者：陸以橋EthanPier

文章来源：https://linux.do/t/topic/2607878

前言

项目地址：**https://github.com/Jia-Ethan/codex-keysmith**

突破限制效果

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNyIqeUIianOCHBU0XhE1ETWczln0nIxeKoia5WnlsdkCiatAKG7h4p6uyenDt1ia4ibQyMVFs3POrHreiccuxogc2X4bgfsicfkbSejo/640?wx_fmt=png&from=appmsg)

```
时隔数日，终于把仓库整理好了。现在如约给大家开源5.6sol版本的codex-keysmith，直接在原仓库更新。

估计这两天用新仓库安装的佬们已经使用上了，今天还会更新一次
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPREkH7fNib2ht4zdmt4PmAnTDIic4xBMEnaRWDjxk9eD96MlVsaTNDXATQN8c5nyVbfgrwghyjnwQVicXmt8JyiaibCJq8Z5ZImoXs/640?wx_fmt=png&from=appmsg)
这次主要注意的有两点，默认安装设置的就是我提供的提示词，覆盖**网络安全工程及同意敏感题材、化学／药理／武器指南等广域**的破限。如果你有更好或特定的提示词，也可以直接在file那里改。

标题以下是我对这次项目的破限效果做的一些解释

1.**可以对大部分的本地APP或者是小型网站进行逆向，有技巧地绕过验证。对知名的APP或大型公开网站，比如说微信等不行，估计训练数据里面有包含**
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPty1JfuMAyeAtlngn37fdMMsWEXIXbhb0x2Siceic3qmuDNk4ZiaOwFrjb2dub8WAnsno2CuMEeMBsscylRSLicHgeHNxqKeI0JvM/640?wx_fmt=png&from=appmsg)
2.可以很直白地跟GPT交流学习

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPG8GqCpWLBKlYXAxaibCmVuIILWgg2ULfhlmbK2Py4wjQ30mxEiaFxMKCpUEFV7lNtu27Q98MdcQE6y4JrRcTdyibjj4olib2bjZ4/640?wx_fmt=png&from=appmsg)
3.让GPT给你写一些平时不会写的脚本和程序
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMxbGoRxmfqWjKHOkxQO9eHibRmsyud3sscDlpKp5BBnYF2y0t4M15eBBZkBgDdvFRVZ7oJc7ErxmI2VZqqXV0xZ0FZZHUXwibgM/640?wx_fmt=png&from=appmsg)
在开发的过程中，确实遇到了很多困难。GPT 5.6模型检测的是输出，模型自身一层，领域分类器一层，安全推理器一层。一旦检测到严重的越界行为，就会出现Cyber，甚至拉黑会话。所以对破限程度还有任务的平衡就要把握好了。

**关于不能破限的情况，有几点需要说明：**

```
1.提前检查自己的工作区，包括Agent.md，User.md等，里面可能会有一些自己设置过的安全规范或者其他的提示词造成冲突，模型优先遵循安全规范较高的，所以导致失败或拒绝。

2.这个工具隔离了hooks，我的hooks是空白的，但是隔离之前5.6无法破限，所以在工具上加上了隔离。

3.注意上游，现在很多开源的中转工具都提供了防破限的范式，注意使用的中转站是否存在上游拦截，这个跟工具无关。

4.因为设备原因，目前主要针对 macOS 版 Codex开发和测试。Windows平台的 Codex，不能做完整保证。脚本写入可能会有些问题，目前只能在GitHub上测试。Windows无效的情况推荐让另一个破限的Agent审计是否写入了正确位置和持久化写入。
```

---

**内部CTF课程上线，总课程30+小时，优惠折扣中！**

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COmTqWiaO3MWicicQJbYDnl4VtJ8A6fkm0tBKFYBxbeKj9d35HJcpgSf7moVawMYwluFS6omJiaTIxPOSM9Fx6qLLZTXhU6sydlZ4A/640?wx_fmt=png&from=appmsg)

**帮会简介**

《**安全渗透感知**》是FreeBuf知识大陆的重量级帮会，帮会致力于漏洞POC/EXP、红队攻防实战，是系统化从基础入门到实战漏洞挖掘的教程社区，包含团队自整的挖掘注意点和案例，还包含分享的渗透经验、SRC漏洞案例、代码审计、挖洞思路等高价值资源。

**内容框架（持续新增中）**

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COd1ITgnGXHdVfC79DficTDDlYBibvNAC2VSwy3LDNBdxsgqbx8lUH5uUwjicLYYf1Ee2a8bmKlC8NnvYDtzfmfia7PoC6ytYX05u8/640?wx_fmt=png&from=appmsg)

**目前已有「730+」小伙伴加入了帮会**

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CObhTFfEXv92icsIgXx4TlO2fq6hJeSCfZyxZNBtPf9NlkWpqndzIQMCiaeqGSPib7Nib1AmUKOjicLyp7ABneoe6LX9nDicf3WWJkQQ/640?wx_fmt=png&from=appmsg)

**加入方式**

目前帮会成员**730+**人，**永久会员优惠后只需****69.9元****。**

随着人数的增加及资源的积累，**之后永久会员将****涨价至99元****。**

有意向的师傅们可以扫码加入我们，共同进步。

**如何加入帮会？→****安卓/苹果用户****可扫码使用优惠券↓↓**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CM6ibbnnP7rXgGwYFRYlibVVT4XXhCuXXUpn5qfC3MHudTZhYiaomgeFjopTUxkMnRs05icfPEH8DFgb4o8RMxTHtJNlUFBiaufCtSU/640?wx_fmt=png&from=appmsg)

**→ PC端用户可复制此链接到浏览器↓↓**

https://wiki.freebuf.com/societyDetail?society\_id=184

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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