---
title: 499个客户邮箱躺在抄送栏，某电信运营商这波草台
url: https://mp.weixin.qq.com/s/OlmcFX8WuHyGTVxvPgR3Og
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:05:12.439869
---

# 499个客户邮箱躺在抄送栏，某电信运营商这波草台

# 499个客户邮箱躺在抄送栏，某电信运营商这波草台

原创

X观察
X观察

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PvafVAHibVaaUB2P0kjAiadxz9ZXaKKLCT8QwOzrmcUZjicmfeibEYeLibWSJw80dSbtAVr1VBJ713LYNQmUOGDpFdnFeDia19YLVibE/640?from=appmsg)
> **导语**：11月10日中午，某大型电信运营商的国际公司发出一封客户满意度调研邮件，收件人栏没用密送，499个客户邮箱明文可见。一封群发，秒变一份公开客户名单，华为、阿里、中兴、中行全在表里。

---

## 一、抄送不是密送

发件人 `cs_survey@×××××.com`（域名已做模糊处理），发送时间 11 月 10 日 12:12，主题是《2026 年客户满意度调研（XX Telecom's 2026 Customer Satisfaction Survey）》。收件人栏用的是抄送，不是密送（BCC），编号从 1 一路排到 499，每一个地址都明文躺在里面，谁收到信谁就能存一份完整名单。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N93ayHyMssKJKlEL9f5sqhIov5hScrXsMfpXD0MicHvFLicEOQxljDqP6SoaxvRqOFF8oxuU2gcWiaHlqyHiaWfTcEcOWjgdGTCfY/640?wx_fmt=png&from=appmsg)

名单里可不只是普通用户。华为、阿里、联想、字节、中兴、海康威视、大华、顺丰、中行、工行、招行、BlackRock、eBay、思科、丰田、FedEx、施耐德、NATO，还有大疆。跨国、跨行业、跨组织，全挤在一栏里。

更扎眼的是里面还混着一批个人邮箱——163、QQ、Gmail、126 都有，多半是中小企业对接人的私人信箱，而这些人根本不知道自己被抄送了。这条名单等于把"哪些公司在用这家运营商的国际业务"这张关系图，直接摊给了每一个收件人。

## 二、英文正文里写着"严格保护您的数据"

正文是英文的，给的是非中文客户，写得很规矩：感谢长期支持，承诺"守护您的个人数据，遵守所有适用的数据保护法规（通用数据保护条例）"。

同一封信的抬头，把 499 个客户邮箱同时递给了 499 个人。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PMYqEt9D7r394zZKj31P8icB6UCUIJon1ziassoZuyJPwdCIc1V0fhp0sRsgjnk6NmUwCHkk7J4X2fZ3Re8R9xkUs8qta1icXwBg/640?wx_fmt=png&from=appmsg)

评论区最扎心的一句是：公开的企业邮箱不算隐私，"就像你公司门牌印在广告上一样"。也有人反驳——上面挂着自然人姓名和企业域名，就是可识别的身份信息，跨境传输还牵扯别的法域。

## 三、评论区在笑什么

原帖 11 月 10 日出现在 V2EX 的信息安全板块，标题《论某电信到底有多草台班子》（原标题里的公司名已隐去），一天不到就 5800 次点击、32 条回复。转到 X 之后，@realNyarime 那条"某电信运营商国际公司的非中文用户用中文邮件调研"拿了 365 个赞、31 条讨论。

几条热评挺能代表大家的心态：

* "最大的问题不是用抄送把所有的客户邮箱全开盒了吗？"
* "评价为不会 BCC"
* "这不跟 Cloudflare 有得一拼"
* "之前有家公司（四大其中一个）也犯了相同的错误，直接把泄露用户数据的人开除了"

顺带一提，标题说的"用中文邮件调研"其实只对了一半：主题行中文、正文英文，截图里那个"接受调查"的按钮也是中文，三个语种混在一封信里。

## 四、这一脚踩了四个点

不是钓鱼，不是社工，就是一次基础操作失误，但踩得相当全：

1. **抄送代替密送** —— 一键把客户名单公开，这是最致命的一脚。
2. **国际化只做了一半** —— 主题中文、正文英文、按钮中文，模板管理一塌糊涂。
3. **合规声明自己打自己脸** —— 承诺遵守通用数据保护条例，抄送栏里全是客户邮箱。
4. **对外披露没脱敏** —— 邮件头里的邮箱属于个人信息，扩散之后很难回收。

补救也不复杂：系统侧撤回、要求收件人别再转发，原帖作者随后删了图。但名单已经在 X 和 V2EX 传开了，5800 次点击意味着更多人截了图。

到现在这家运营商的国际公司没给出公开说明，也没人知道这 499 个地址是一封模板群发、还是某个销售为了省事手动拉了列表。

## 五、结论

这事最扎眼的地方不在"草台"本身，而在于它同时暴露了三层短板：客户数据没有分级，批量邮件系统没有对 Bcc 的强制约束，国际化流程全靠人工。三个环节任何一环有人戴手套，都不会是这个结果。

---

**版权声明**：本文由华盟网原创发布，保留所有权利。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N3Lo0WF5H9xx3zCOvtOxXRyLZuAn65vQU5oZYl8JibHsr2BuvUI41WnXRdcMpeGia9Tpx9R8HpB3ibhzMHqV3f3sOF6OPqOsE2ico/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6McGWf8McoOhR4wqJ4DK1aUVf7Eic5DzLTwic0RL3sh8kzW8HibSVynwC2JaKSfMbNibpdibLtCQ0r0QcThFJQxDZw3YmJZLYhwiaAWE/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PmPvccHxGbfEiae0ygpnLSUNkoiadtsv4CbILqvoly3jiaMVAkxPrhiceVa9ver666kmVg4KjbGmz9wtDLQpibHTOr5l54Q3rplR6s/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PXJqWibxNWFAgdvdiatYPUdAkiaf5Au6znicUAWMVNc1LjdGU8fOL61gBVmn1Lcmj5IGdHRMKlmQqtIgZDTv6sfCbFSZS0zo3K9Nk/640?from=appmsg)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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