---
title: OpenClaw 开发Skills实践 微信自动储存图片到NAS
url: https://mp.weixin.qq.com/s/-V5RKVaxbuHysZNCNQwIjw
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:35:01.363865
---

# OpenClaw 开发Skills实践 微信自动储存图片到NAS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1N1JeeKBordq0IjYN4cNqic2vZVxW5cGo0KvaPZXiaeuic0qBLbscnbyLn8LKra7uWA10VYGg68Jicicd51fRoK9tmC40HrDoo2IhclWV2S8ib9gM/0?wx_fmt=jpeg)

# OpenClaw 开发Skills实践 微信自动储存图片到NAS

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器中沉浸阅读

> 通过前几期的文章，想必大家对`OpenClaw`已经有了深刻的认识。它由传统的交互“对话”转变为“动手”。大大提高了人们的工作效率！

`OpenClaw`之所以强大，不仅依赖于大模型的支持，更重要的是有着强大的Skills（技能）支持！目前官网ClawHub已收录超过3000款技能。在上篇文章中，我们也讲到了如何下载和安装对应的技能，详见下方文章。

[![让你的OpenClaw更智能 -（安装Skills篇）](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcggz4eibVOYibMcvd4ueR5JLzLqWpYjHNHjeIEmAAKSyk3d5uBIn68uW8ersrYjJnpgKYFUM1bicwxehhjqiaQNrBd7C8hBJ9qw6o/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxMzIwNTY1OA==&mid=2247516432&idx=1&sn=bcfe454937cafd60efaada0e401bbc34&scene=21#wechat_redirect)

让你的OpenClaw更智能 -（安装Skills篇）

而本文，我们将一起探讨如何开发属于自己的`Skills`。

**0****1**

**开发需求**

在日常工作中，我们会用微信接收很多重要的文件，如图片、PDF、办公文档等。有时，由于太忙或者消息太多，来不及保存文件。到需要文件时，发现文件已经过期或者清除，无法使用。即使保存，又忘记保存在什么地方了！

因此，我们需要给其开发一项技能。当我发送文件给`微信ClowBot`他会自动保存文件到我本地`NAS`并进行文件分类。先来看看实际效果！

![发送文件后 自动保存到本地](https://mmbiz.qpic.cn/mmbiz_jpg/1N1JeeKBoreedn7zG5TQDD1sHXMAhrwBgBV0tURWP6NKSP9yk8seltK20sp5jkp5ZO870sZZ4JmZRsfWsnVRWIYibBPspUODjgn6Z78UFnC0/640?wx_fmt=jpeg&from=appmsg)

发送文件后 自动保存到本地

![保存本地效果](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordcg26QCKBoiavibWXBHg5cYRtPzzzRmAQxLiaLPh2pp8JPSgw25iaQqlQDVsQs9S9JHOS7ZKPcdlFSEw4TOd2aBlXCprzHeHs66f4/640?wx_fmt=png&from=appmsg)

保存本地效果

**0****2**

**技能开发流程**

接下来，我们来聊聊如何开发技能。

**❤️技能存放位置**

我们需要在`~/.openclaw/skills/`目录创建技能文件夹。当然，你下载的技能也需放到这里。

![这里创建了auto-save-files文件夹](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorf7OLkAzWGuA7uymVJ3YkXyMOmnbCYYuhlniadJ01eibOZLNuESbbkq7MsR84vRt7yCgbd8xN2FFyEIq9kDiaalydghbgjc7Ey6DQ/640?wx_fmt=png&from=appmsg)

这里创建了auto-save-files文件夹

**😘编写 SKILL.md**

`SKILL.md`文件是技能的核心文件。他会告诉 Agent 这个技能是什么、何时触发、如何执行。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordqH9gQmJKsu58MSze8iaVDTUEEM94KuQJsriafLBynNp8BhMq1PluDX7gvK5PJU4mHL1D7MmZqOUiaVMLcI9byGbKE6XF0l2iazW8/640?wx_fmt=png&from=appmsg)

在开发时，这部分只需要我们提供完整的思路。让AI帮助我们自动完成。

需要注意的是，`name`和`description`不要用中文。

**✈️编写脚本**

在该技能目录下创建 `scripts`文件夹，可以python或shell进行编写对应的脚本。

```
●●●code

#!/bin/bash
# scripts/your-script.sh
echo "执行你的逻辑"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreOkoJ9y9CEko1PKjclKBgbDiciblhwBOxGqc0BuKNjNlPskRr04S3fFJfVxeokBL8oNFQvPiaDuunzrIia5yf6IGvz0hYC9tTZOoU/640?wx_fmt=png&from=appmsg)

脚本完成后，可以重启Gateway，技能自动注册。

```
●●●code

# 重启
openclaw gateawy restart
# 查询当前技能
openclaw skills list
```

![出现ready证明加载成功](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfh4ppHg36Lbq9nkaY0YnzPK03oudoicLWyd7pwTL43M604tiaHK0Gh6bibXiaHiaueW60liawU29wV5UVkLMaNB4k0bA0x6CrUnBdXk/640?wx_fmt=png&from=appmsg)

出现ready证明加载成功

![在WEB UI中也出现了](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcQ4mdksJeQ6zRQ27jxkD4P4rO9fByL9yqh0oibTicCZCyglClO2iaCEJFkoFRHWrW5YpybbccJwTyCTb6Qcic4ntrQXm7JX6885SY/640?wx_fmt=png&from=appmsg)

在WEB UI中也出现了

完成后，便可以通过微信ClawBot发送测试了。

需要注意的是，如果你是Python编写，需要提前解决脚本运行的依赖环境。否则可能会导致脚本运行不成功。

**0****3**

**总结**

以上便是个人开发Skills的几步步骤。如果你编程能力较差，只需要提供详细的工作流程，OpenClaw会自动帮你完成。

更多精彩文章 欢迎关注我们

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

kali笔记

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

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