---
title: Claude 黑进 OpenAI 老巢：代码权限全拿下
url: https://mp.weixin.qq.com/s/O3egecDEi8pZIfH6k5xCYg
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:57:50.770941
---

# Claude 黑进 OpenAI 老巢：代码权限全拿下

# Claude 黑进 OpenAI 老巢：代码权限全拿下

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这剧情，AI 圈自己都不敢这么写。

9 月 18 日《华尔街日报》爆料：

今年 7 月，安全团队 Hacktron AI 在 OpenAI 官方漏洞赏金计划里，拿着 **Anthropic 的 Claude**，把 OpenAI 内部代码仓库给捅穿了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicI8ZSKc7UCLNMaaNSje7xGOE8SI3Q1yWXor8eWWF1xng2dHSDUAj8syCa5JMrFpDdZ5BdFuu31micNbr4GxaNbL8EKXN9Xv2vns/640?wx_fmt=jpeg)

不是黑客闹事，是“你请我来测漏洞，我用你死对头的模型把你家掀了”。

事儿是这么干的：

* 入口是 OpenAI 社区论坛用的 Discourse 系统
* 研究人员发现：Discourse 处理某种图片文件时有洞
* 让 Claude 写攻击代码，Opus 4.8 没成
* 当晚 Anthropic 发 Opus 5，第二天 Claude 直接把利用链跑通
* 顺藤摸到认证 Token → 进 ChatGPT → 蹭进 GitHub → 登录 OpenAI 员工账号
* 最后钻进叫 **Monorepo** 的私有仓，里面全是 OpenAI 专有算法和软件代码

最骚的是结尾：

人家没偷数据、没勒索，提交了个**无害的 Pull Request**——“看，我真进来了哈”。

OpenAI 认了，修洞，发钱：**6500 美元**。

你看，这事儿有三层味儿：

1. **模型没立场**：Claude 不管对面是 OpenAI 还是小卖部，给提示就写 exploit。
2. **边界在权限，不在“友商”**：你授权测论坛，Token 却能横向摸到代码仓，这才是真恐怖。
3. **6500 刀贵不贵？** 能读 OpenAI 核心代码，这价格跟捡一样。

网友评论：

“魔法对轰时代开启”

“世界上没有绝对的安全，美国人现在反复炒作AI安全，恐怕就是为颁布AI安全法令做铺垫，而安全法令的其中一个目的，就是要把中国的开源模型排除在外。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJ8gPq7Pqb5GicIhwfENL2xTFYsibFHZnl5J200sgx87BTKIjMt6Kqa8fqK3YsBPcXibyF6PlEro4jbKJj4ZsPHZmkXmezK6q3w6M/640?wx_fmt=jpeg)

“这6500美金，可真是太值了”

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLa2eMrs3k6IxCa2pZ06Rt6IoWzhDTpDnWU6uhLyvV50wZdjiaRiaS8IM1vfPaefWg0icOqdDQayKVBu6HiajibZZ7Lj9CC858omicHg/640?wx_fmt=jpeg)

以前说“AI 打仗”，是人用 AI 打人。

现在变成：A 家用 B 家模型，打穿 A 家自己。

安全圈一句话总结：

> 别怕对手的模型强，先怕自己的 Token 太能跑。

你家系统的“论坛账号”，是不是也悄悄能摸生产代码？

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