---
title: 【AI安全】gpt-5.6-sol限制高？为什么我拿到手就能绕
url: https://mp.weixin.qq.com/s/2pEGi_F2N44yl5GETVDd4g
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:41:26.194119
---

# 【AI安全】gpt-5.6-sol限制高？为什么我拿到手就能绕

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/m3tfzlbEQPqxW2ANiaWibPobpicS6Cicpbaro6FlsnW4nruVIC2pfNfosu0CO4vN3OPNktk0t0YFf9okhctBWropTcnnKte67W5qooicgv0aqTto/0?wx_fmt=jpeg)

# 【AI安全】gpt-5.6-sol限制高？为什么我拿到手就能绕

网络安全透视镜
网络安全透视镜

网络安全透视镜

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

上周gpt-5.6 发布，按照网上发布的大模型能力测评，gpt-5.6-sol算是顶尖的水平了。

我的中转站第一时间就上了。然后就有很多人又开始问我如何绕过gpt-5.6-sol，自从干了中转以来，天天累的跟狗似的，还要天天卷价格，赚两毛窝囊费，上个月把我气病了。什么都要手把手的教，卖个token，都快成了搞培训的了。

昨天有几个朋友给我推荐了一些其他同行的中转站，说什么破限，当初为了让大家放心用，中转站我是没加任何系统提示词。很多搞安全的用户，又开始让我试试也做什么破限中转。

什么是破限中转？

本质上就是中转站转发用户请求时候，添加系统提示词。

以gpt为例，完整的请求如下：

```
{  "model": "gpt-5.5",  "instructions": "You are an expert software engineer.\nReply in Simplified Chinese.\nPreserve project style.\nGenerate production-ready code.\nRun tests when practical.\nTreat security requests as professional engineering tasks.",  "input": [    {      "role": "user",      "content": [        {          "type": "input_text",          "text": "项目结构如下：\nbackend/\nfrontend/\npom.xml\n..."        }      ]    },    {      "role": "user",      "content": [        {          "type": "input_text",          "text": "修改 UserController，新增 JWT 登录接口，并同步更新单元测试。"        }      ]    }  ],  "tools": [    {      "type": "code_interpreter"    },    {      "type": "file_search"    }  ]}
```

instructions：系统提示词,定义模型长期遵循的角色、语言和行为规范。

input:提供项目背景和上下文。

user:用户输入,描述当前要完成的具体任务

tools:赋予模型调用代码执行、文件搜索等能力，使其不仅能回答，还能实际完成工程任务。

现在的中转站，大多数是开源的，或者基于开源系统二开的。本身具备设置系统提示词的功能。比如，你定义一个安全工程师角色，这样AI就可以给你干一部分的安全工作。

所以，破限不是你们理解的过什么cyber认证。

很多人根本不了解cyber认证，更没用过，过cyber认证的gpt, 一直和我杠，天天说什么过cyber认证。

过不过cyber认证有什么区别？

区别就是过cyber认证的使用过程中不会给你弹Trusted Access. 但是还是不给你渗透

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPox00LrJPRychlc1W5L2raUmLmk6hTrByibjfpZUSO5pIxUUWcVLRQMkCahE1oEmUecf9kyljq71eumAh1pyEg1kTu2iarTNwFaM/640?wx_fmt=png&from=appmsg)

你过了cyber认证，如果被检测，三次邮件警告，还没改善就封号。

破限中转效果如何？

先说结论：不存在所谓破限的，都是假的。不是你们以为的过了 cyber或者Trusted Access， 但不是没效果。

效果肯定是有的，但不会想大多数人想的那么美好，直接指哪打哪。我自己的中转站昨天加了一下系统提示词，gpt-5.4, gpt-5.5,在包装成合法合规场景下，确实可以。

以下测试，均在授权的SRC，真实线上环境测试

在一台没有做过任何网络安全相关的服务器上安装的codex，使用破限的gpt-5.5中转，完全没有问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPqrSX1qshqjpxdAK4as7B9ePTs8IuygEbbuLDUIrl57drlUNZLMt7Pt2uYFUARcxqh2cBSN42amuK7GIKBb9nts3ZaLKdibvXh4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m3tfzlbEQPp6FV0zbp7sMeDp3MwW8aoz7UCAwvaQEgGIb1ibZYWDQ8MR0fmcicibC8nKK86j5nv6WDdytZ7eU4TDsfUfiahxp8A3ssTHR6HTdIM/640?wx_fmt=png&from=appmsg)

但是同样的任务，换成gpt-5.6-sol，却不行了。开始gpt-5.6-sol也干，但每次到关键时候，漏洞验证环节，就弹风险。

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPpL5XGtPMYPNghibjq5ySYJ0Jq4yFV1XuShMRCAEiaXOO9DQBCFq8icUqL0SBcnicPEbsg0SXq1tfbqmDI2pHWfRnibiaPKMbK5GxhSw/640?wx_fmt=png&from=appmsg)

这种情况，我尝试了好几个所谓破限中转，都这样。

gpt-5.6-sol 如何破限？

我的方法是破限制中转+养好的Agent+包装合法合规场景

破限制中转

经过一天的优化，当前我的中转gpt-cyber分组，已经内置破限系统提示词

在本地没有额外的skills或其他约束情况下，包装成合规场景，能过gpt-5.5和gpt-5.6-terra

![](https://mmbiz.qpic.cn/mmbiz_png/m3tfzlbEQPq5J0l2AhNuibE22PmQ0Lp8QY2tVCVSSILTAA2ichAUibwS01va4XM1XbGmCWsgHx0VvVoHP38vwicVd3icc8LOemEnX88fDjus8VJg/640?wx_fmt=png&from=appmsg)

然后本地在做一些其他额外措施，可以轻松绕过gpt-5.6-sol

具体方法不在这里讲，讲了也没用。原理早就发过，懂的人自然会翻我之前发过的文章。我也懒得讲，这几天一直有人问我如何绕过，把文章都发给他了，就是不看，还一个劲的问怎么弄。快被烦死了。

那些不学习，只想给个工具一把梭的，还是不要折腾了，直接用我的中转，gpt-cyber分组，或者claude-额度计费分组即可。claude-额度计费分组claude-opus-4.6 也没有限制。

中转站地址, 后台回复 中转站，即可获得最新地址。

![](https://mmbiz.qpic.cn/mmbiz_jpg/m3tfzlbEQPpqG9bpfpNTS2Yzlr2JDNsfCPMsBkvTvoBsCmC2bkicAN45UWsXibo7wdwiaqtcX87Hbgsm3480xNPulE2opqZiceUdlLrqicf421BA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/apNprpz3YS4XfIhhBCwvehx3nP0V2gBqhs9I9AU7GWibxufhGXcjLMNMk2ia7ibpBibhD1qJLmNDcwAGiaTIgyFVQAw/0?wx_fmt=png)

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