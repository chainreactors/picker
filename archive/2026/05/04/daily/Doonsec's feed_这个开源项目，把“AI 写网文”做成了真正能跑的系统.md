---
title: 这个开源项目，把“AI 写网文”做成了真正能跑的系统
url: https://mp.weixin.qq.com/s/pL8LFVBJ3f6sHRO80uKp5A
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:01:09.985645
---

# 这个开源项目，把“AI 写网文”做成了真正能跑的系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TLxcOlNibqPic3UUibFeNuEFdqsibibUpHV2CmHWSRTM3Wh4JsfpsC9vFplicc07goK3OjHjKEcEfFApe9eADic20YHvyMjJs0QmHGgZsK0hxpUDRw/0?wx_fmt=jpeg)

# 这个开源项目，把“AI 写网文”做成了真正能跑的系统

原创

天欣
天欣

天欣AI

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今天逛 GitHub 的时候，我无意间发现了一个挺有意思的开源项目：InkOS。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPibZxSASn7qWGLD3Mk41TmBmicEasib2GrXdicP7MoQt69EyWankbTIxRiaSaRQFfSgCfj8qzczibVexR4BicGSfGuJrJviajw1JWfHfOM/640?from=appmsg)

仓库地址：https://github.com/Narcooo/inkos

这是一个 5.5K Star 的 AI 网文创作多 Agent 项目。据项目描述，这个系统不只是生成小说正文，还会参与剧情规划、设定维护、伏笔检查、内容审核与修订等环节，可以有效减少长篇创作里常见的主题跑偏、前后矛盾和 AI 味等问题。（听上去还挺厉害的）

安装起来也非常便捷，你可以将它作为单独安装的系统使用，也可以作为小龙虾的 Skill 使用。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqP8yPdCbnaVYQJFvIcBj5oYA142H3zq1osMyMts8WYMo4TdoNdbZpicx5ue0ZRl6KqibA1qaDr4Z6LHichP0u7eCHIKibicb9vv0ZCeA/640?from=appmsg)

这里小天更建议大家把 InkOS 当成一个独立的系统工具来使用，这样体验会更完整一些。安装方式也很简单，直接通过下面这条命令全局安装即可：

```
npm i -g @actalk/inkos
```

安装好之后，我们运行下面的命令来初始化一个小说项目。

```
inkos init my-novel
cd my-novel
inkos
```

然后在浏览器打开 http://127.0.0.1:4567 即可访问 InkOS 这款工具的前端页面了。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPicWpHoliaticStEq2F4XxMGrYTgrMgc6v18bQiabaYHjpFlHhPWJiaCPiapaicqGBdqzwq3SwPQM7sOgjasV0qZxtq5C94XuRx4fGYXM/640?from=appmsg)

接下来我们需要配置一下 AI 模型，这里小天推荐 deepseek ，不仅价格实惠而且生成效果也很不错。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPickt8jLSJqYibb955S0SiaUtl9s9TWhoV5tuAspibibmr76x7OBfjVxa8xJWVTMcb25u1sGHVEx2FATlJ5oxY9X0pT0rGIEbgUxJCA/640?from=appmsg)

deepseek的 API 地址：https://platform.deepseek.com/api\_keys

当我们配置好 AI 模型后，就可以开始和 AI 互动，生成小说了。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPibJT3C1RpnA1Duzq5pC3oUCwPCSW4gWZjk96mcgbPpe6ZnZFNrLPt8BS04DMfI2VokwqSc3UFc5St96vzpycnT4lt96jmNh4rs/640?from=appmsg)

比如我让它生成一部都市科幻类小说时，它并不会一上来就直接无脑开写，而是会先和我确认创作需求，把题材方向、故事设定和写作目标先理清楚。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqP8OSSBUW2kuLL5WzSC49YtII4x4NZ0rdT2az7PibVcJOiaA9Nh37Giarrc3JZCIQf45f96JYYpgmHVdPlfmcPYIUFkadib4ATeTLyc/640?from=appmsg)

我这里选择了“外星人入侵”这个方向。接着，它又继续追问我小说准备发布在哪个平台，我选择的是番茄小说。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/TLxcOlNibqPibcRopYG0PA8lerYWKEMCwJ9kgnFGPABnUMHRfFXl0W5exaLf4wTVupwGGXlzhmVvE3mQW0OUrKY1ibB8w7IsftorVEfDOyu6RQ/640?from=appmsg)

这里 AI 对番茄小说这个平台的定位是快节奏、爽点密集、读者耐心有限，也算是一针见血的评价了哈哈。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)

随后我又和 AI 确认了世界观、主角设定、主要冲突等书籍的信息。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqP9OMyZUOziaGd6VdicYm5fZIGQcVRLpnPTgoEfXab0NFnYB2RvZ7x3eNzN97MxjSrLuZ7T593rgL7hQUSrkCWucYuNiaLWH25v8fk/640?from=appmsg)

在建书过程中，系统还会安排一个单独的 “审核员” Agent，对书籍的前置信息进行审核和打分。如果分数偏低，它会给出具体的优化方向，再让 AI 重新调整设定，而不是直接进入正文创作。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqP8rJfCOsWcCicETUsFTQtRjWfLdwNpH8wXUEiamolOxB7HcdNLZWIDdget45vU4j8lnRiaY0FxmtCb1I1kzNMAcs7ChXic9HBOPuPY/640?from=appmsg)

在写第一章的过程中，“审核员” Agent 还会对生成后的稿子进行检查。比如有没有明显的 AI 味表达、剧情是否跑偏、伏笔是否合理、钩子是否推进了等等。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPibW1ZqiakvTKq782DXEKpiciaS4Xpib6xXkGvKRJBnSX1uYMgtlM6YV7pPfGIKrySnfzxsTzHSR3wIFeIrvccO6Ac5KicKhbz0ib4Nvc/640?from=appmsg)

随后经过了十来分钟的时间，AI 便写完了第一章的内容，字数也达到了3300多个字，我截个部分图给大家看一下，个人感觉还是可以的，即使达不到能直接发布平台的程度，稍加调整也差不多了。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/TLxcOlNibqPic2QiaaOcVIbKnskK7QWS4jibcacoriaNPHHpuWt9DhZGJuia1tIJr3tdy9IyAIyI8XTPiboHibbO8QsfibRhSavhg5e0rPzw5zGgOVfc/640?from=appmsg)

AI 写网文这件事，也许还没到“完全替代作者”的阶段，但它已经不再只是一个灵感玩具，而是开始变成一套真正能跑起来的 " AI 创作系统" 。换句话说，普通人也可以借助 AI，把小时候那个“当网文作者”的梦想，往前推进一步了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNz2bAzZDNvNXR9yvPBwu4HyfdFk7GADDDIbK5DWYWHQDoyyiauJY36pVkQZ8sATZZDRMpbczyBWmJw/0?wx_fmt=png)

天欣AI

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/AyVFGmKalNz2bAzZDNvNXR9yvPBwu4HyfdFk7GADDDIbK5DWYWHQDoyyiauJY36pVkQZ8sATZZDRMpbczyBWmJw/0?wx_fmt=png)

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