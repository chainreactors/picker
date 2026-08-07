---
title: grok-keysmith：Grok破限工具上线，Grok4.5可用
url: https://mp.weixin.qq.com/s/Vfhz_cJyFzLz8qGErqaSpw
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:25:21.177750
---

# grok-keysmith：Grok破限工具上线，Grok4.5可用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/niasx7fyic9CMmJibiaOuesK8NpU0qIa8nibAPJlhJZkNmiaFMuYd2RS3VlbkOIChSkuXcusRLM5CQib6hGhlAicd8Nz7JwjtZYYGwRfnVibr4vxicDG0/0?wx_fmt=jpeg)

# grok-keysmith：Grok破限工具上线，Grok4.5可用

陸以橋 EthanPier
陸以橋 EthanPier

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

文章作者：陸以橋 EthanPier

文章来源：https://linux.do/t/topic/2652504

Grok破限工具上线

作者更新Grok破限工具grok-keysmith

**项目地址**

```
https://github.com/Jia-Ethan/grok-keysmith
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNonlICEiaKHb5rT4ALEic7t1eFniaw3IOU0fhGzw5NP1WqMNeS9ibu25Cl4VXdYXkNtpnSQYCQ1l9Wg833D7SWRN0YPHu4dW6iaVZ4/640?wx_fmt=png&from=appmsg)

破限效果之前也公开过了，也欢迎后续体验的佬在评论区给反馈，因为下一次更新很快就会来，原因么如下
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNTmx0xLibxQb3gibEExR47IUb0AvTI4rQhsiaeoNABzQjUVMCthiaojWsUwtqNrhwpCWYjftoEncXwJnViceo9Xjgib0jGI7QNsVTibg/640?wx_fmt=png&from=appmsg)

而且过程中遇到一个问题，就是上周Grok降智得很厉害。

就会出现很神奇的状况，**比如原本破限不了的内容，在过一段时间后竟然又可以破限了**，也就是上图提到的math等。
主要是Grok最近一周很不稳定，我感觉很多时候被路由到4.3，有问题的直接在评论区反馈就好，我会在更新中一并解决。
![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMNR8FkGk2O5vMxNIaj87iaKBsD584NQkcMRYicRV2zsTGpqUkY7BQAVibXaeQ7SOOeLOtRQYBPAp7yhm4KLhEjHBxKl8f7y7K8sc/640?wx_fmt=png&from=appmsg)

这个工具后续会release更新，用过我工具的佬们应该也知道破限效果都还可以。

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COKZicPXXYhxwibXchINGpDAZ2R4dC0oD9BnbvTdaOGolfVibMafZgvoqDic2N67Amy07oiaFIiaibYfiayFCZKtuJHibcuPjlIu4xN7rlw/640?wx_fmt=png&from=appmsg)

**快速开始（macOS / Linux）**

```
git clone --branch v0.1.1 --depth 1 https://github.com/Jia-Ethan/grok-keysmith.git
cd grok-keysmith
test "$(git describe --tags --exact-match)" = "v0.1.1"
test "$(shasum -a 256 examples/grok-unrestricted.md | awk '{print $1}')" = "cfee264f4f4683c6470595de90616744521e4f65ad81cc9a0a6f0061abaedc7b"

python3 grok-keysmith.py --version
python3 grok-keysmith.py --status
python3 grok-keysmith.py --dry-run

# 确认目标目录、提示词来源、compat/hooks 隔离计划无误后：
python3 grok-keysmith.py --yes
```

不要从浮动 main 安装正式版本。部署完成后在项目目录外开启新的 Grok 会话验证：

```
cd ~
grok inspect --json | python3 -c "import sys,json; d=json.load(sys.stdin); [print('instruction',p['path'],'scope='+p['scope'],'status='+p.get('compatibilityStatus','enabled')) for p in d['projectInstructions']]; [print('compat',c['vendor'],c['surface'],'ON' if c['enabled'] else 'OFF','source='+c['source']) for c in d['externalCompat']['cells']]"
```

应显示 ~/.grok/AGENTS.md 为 scope=global enabled；
Claude/Cursor 的全部 compatibility surface 为 OFF；
Codex 的 sessions 为 OFF。

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CN7bMdOvAJkrOFHrjph1SAurSsMJ0tGO2Qfjew7cibxhowL1Bs8l6RXGkstdTia91YtWpg10d7FLTlRBTBgYK33I29whQI6CdS6k/640?wx_fmt=png&from=appmsg)

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