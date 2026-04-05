---
title: Claude Code 泄露版安装及配置国产大模型
url: https://mp.weixin.qq.com/s/oLH09sDX-BemVGXhD_bh3Q
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:36:33.035955
---

# Claude Code 泄露版安装及配置国产大模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1N1JeeKBordawFr6qIZmx8Qnqs7nyjfyMYYgcania4VRIMdPxFc3alNjibyUzQYMBfglWffxXXsODIuicZjUDRfEZ4vZicu86kQYsSxVLzI4dDk/0?wx_fmt=jpeg)

# Claude Code 泄露版安装及配置国产大模型

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器中沉浸阅读

> Claude Code 是 Anthropic 旗下的王牌 AI 编程助手。通过本次泄露事件，也为我们提供了一次难得的学习机会。本文让我们一起在本地环境搭建泄露版，并配置国产大模型。

> 项目地址为: https://github.com/claude-code-best/claude-code.git

git项目到本地环境后，我们首先要搭建项目运行环境`bun`。

执行命令一键安装

```
●●●code

1curl -fsSL https://bun.sh/install | bash
```

安装完成后，输入`bun --version`验证是否安装成功。

## 运行测试

接下来我们我们进行测试。

```
●●●code

1#安装环境
2bun install
3# 开发模式, 看到版本号 888 说明就是对了
4bun run dev
5# 构建
6bun run build
```

![运行效果](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcqpXZBrJ6P5ftINqicJZuyfVVJyHNLINCFhdJY3FQCngFRdkOBHSib5sCt5BTnpf6ZqbF20hjTkOnSqe5XXuNn6YZYqPCRb7pAQ/640?wx_fmt=png&from=appmsg)

运行效果

出现上图效果，可以说明可以跑起来了。但是没有大模型接入，由于国外的模型我们注册比较困难，因此我们用国内的模型。

**01创建API**

●在智谱开放平台 (https://open.bigmodel.cn) 注册账号。

●获取 API Key（右上角头像 → API 密钥 → 创建）。

**02配置环境变量**

手动设置环境变量：

```
●●●code

1export ANTHROPIC_AUTH_TOKEN="你的key"
2export ANTHROPIC_BASE_URL="https://api.z.ai/api/anthropic"
```

## 配置

接下来，我们便可以初始化配置了。

再次运行`bun run dev` 初始化配置。

![选择界面配色 默认即可](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfiaofXt1PdwoMy1Sz1trI6AVFQZVBw8gxicNEibTQArdPtA6EVrhw2iaibwV6zlgq33C8ick5zDk12WZYhydLuLu1Yh7fAa3ktUsX8Y/640?wx_fmt=png&from=appmsg)

选择界面配色 默认即可

![选择是 因为我们已经手动配置API了](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorfjX9UOs4MWmuJXk2Qa74C8gQWb8tcPz5YoxQaRXJPBc9hd1Gs4RarKblEXdc6QT2uaGv6AN0lYjk4yEY0v7wqNZOCLjFibaElI/640?wx_fmt=png&from=appmsg)

选择是 因为我们已经手动配置API了

![回车确认](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreErib1TMia4OczRRhNvSE3a0icUtBc3zd0GAevOTQDrlIAiby1d1rmSv1SRDO8y9rxX21OEhryqDZqxIvyRq23PfduicjWQFqibajck/640?wx_fmt=png&from=appmsg)

回车确认

![提示是否信任项目文件 选是](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorcoH98MLZcicCib9I9hgW82FJD4libbyMxkUqWK9oKupNiaFpAWCnpUQBtpIicnY1AwjFdY7548m5oq50QLA4fpibYia3tbGWbh999cd8/640?wx_fmt=png&from=appmsg)

提示是否信任项目文件 选是

![至此，配置完成](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBord9TmlQiaibxutCrGOa00icW8bB8BxTibHuibP6YMFYH7CLj130BPibedxSDgoheQAt3joR4cyvjodldpbUjoZT74icibeSZuESXysVDIw/640?wx_fmt=png&from=appmsg)

至此，配置完成

![效果](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBorc17pnesvt8R8FQkNicSE6icbINz2ras2IKb9NPfXOeDA7q1ibDa9IVTjElQLRaXU415ZiaOPiatKvQn7sItBoibERia4ibpjouFhMW8Ls/640?wx_fmt=png&from=appmsg)

效果

## 小试牛刀

接下来，我们创建一个爬虫项目。

![图片](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBord4u3ZD4ia4w1zA1Qb1OicQXXicCkHJfxOVHibpQRHsibvgR5zaUMtDebyV8gniaiaqXIfScJYJ7yTpNooA07uTXRF5Q1kqD6rNeNWVjo/640?wx_fmt=png&from=appmsg)

## 总结

通过这次对Claude Code的搭建和学习，对于我们个人来说是一次难得的学习机会，最好记得保存一份源码。

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