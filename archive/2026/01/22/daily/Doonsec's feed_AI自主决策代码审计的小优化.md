---
title: AI自主决策代码审计的小优化
url: https://mp.weixin.qq.com/s/N88j3gKj0Wd1vWuuyfN5RA
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:30:46.398659
---

# AI自主决策代码审计的小优化

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/597X6b5pKfeUGKib02qPnLIM2lAFDeMHCBG210MDFWnBzxvwSk9hUDF8E5j0YWhH8OwB75KibXuUC5Iia7wHn283w/0?wx_fmt=jpeg)

# AI自主决策代码审计的小优化

原创

现在你看到我的ID了
现在你看到我的ID了

E条咸鱼

![]()

在小说阅读器中沉浸阅读

# 前言

这篇文章实际上就是上一次ai自主决策的代码审计提示词的优化

上一版后面又测了几个开源项目，虽然都能正常产出漏洞（直接未授权到获取管理员权限），但是过程比较曲折，而且还算是有点依赖人工的，所以优化了一下

# 问题

先说说问题，因为核心规则分为两个部分，实际上关于http数据包和一些越权分析的要求都放在了最后面，导致阶段任务的结果写入到代码审计文档中的时候，ai会因为上下文过长，从而忽略了最下面还有规则。

导致后面有的报告，比较杂乱，需要进行复查才能有一个比较准确的结果

# 目前工作流程&使用分享

工作流程和上一份没变

```
分析框架->找出所有接口->列出权限控制的方式->依次分阶段开始专项审计->漏洞组合利用->整合报告
```

这里也是主要给xdm分享一下我认为比较舒适的使用场景

工具当然是在准确度有了一定保障的前提下，越便宜越好，免费则是最好

所以我推荐使用ai编辑器`trae cn`，国内的版本允许免费使用`glm4.7`，在长达三四个星期的测试中，我发现在常规sql、xss、越权这类漏洞的效果实际跟`claude opus`差不多，同时solo模式也允许并行的处理任务，大大提高了审计的效率（除了中午下午的时候这个模型需要排队外）

但是考虑到并行处理会影响各个任务写入文档，所以我把提示词修改为单独输出阶段报告，然后最后整合

目前已经把最新的提示词文档放到了github上

```
https://github.com/Ernket/AI-Code-Audit-Prompt-Words
```

有兴趣的师傅可以看看，我把我调用的prompt也更新到了上面

最近在写claude code的skill，感兴趣的师傅也可以后台交流

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/597X6b5pKffETricr1okBCV7yKJLpXWW0zcP1icmMDq5YYu5ibQ44D2w3S9cA2crAwMGmFWFvhSWLJzIWjX3fM2FQ/0?wx_fmt=png)

E条咸鱼

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/597X6b5pKffETricr1okBCV7yKJLpXWW0zcP1icmMDq5YYu5ibQ44D2w3S9cA2crAwMGmFWFvhSWLJzIWjX3fM2FQ/0?wx_fmt=png)

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