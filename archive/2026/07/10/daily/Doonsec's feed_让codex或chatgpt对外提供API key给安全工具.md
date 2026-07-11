---
title: 让codex或chatgpt对外提供API key给安全工具
url: https://mp.weixin.qq.com/s/sDngs1Wd5fTeUT6uhTKflg
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:07.852822
---

# 让codex或chatgpt对外提供API key给安全工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVkrLJz0gey7piabB58KNonE4uIc3snzial0SL7NQUiayBDl0tnJLoB9upv8ztp2rWiaws5qOKd0rZUtpeU2C6v15qJTL41fEgdzgxI/0?wx_fmt=jpeg)

# 让codex或chatgpt对外提供API key给安全工具

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 472，阅读大约需 3 分钟

## 前言

本来标题只有 codex 的，但写完想起来，今天 codex 和 chatgpt 已经合并，统一叫 chatgpt 了。

马上台风来了，师傅们记得注意安全。

## codex-proxy

今天介绍一款工具：codex-proxy。

将 Codex Desktop 的能力以 OpenAI / Anthropic / Gemini 标准协议对外暴露，无缝接入任意 AI 客户端。

项目地址：https://github.com/icebear0828/codex-proxy

![c647670d363652e54f396bdd9c37dd27.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnbupJjjy7B4bliaSiae4ibbnVG8flFiapebv3Qfh9NIcjCx4fJGr7ibPf1iaN9dsaXSRM0hvAndUqBCyib9DRZDNhxX2Ljb2N0RpM94g/640?from=appmsg "null")

c647670d363652e54f396bdd9c37dd27.png

## 为什么要介绍

有师傅可能觉得，为什么要多此一举。chatgpt 本身就有 AI 客户端，用起来也是最合适的一档。

正常来说，个人来用，确实没必要换。可以理解为这是在本地搭建了一个简单的中转站，其他人也能用到 codex proxy 提供的 API。

除此之外，还有一个用途。就是 github 上一些开源的网络安全工具，提供了添加大模型的功能，但是添加只能添加 API 和 key，工具才能正常使用。

而订阅的 chatgpt plus/pro 是不对外提供 API 和 key，在要用到的时候，就只能换别的。

有了 codex proxy，就能直接用自己的了。

## windows 配置

在 release 中下载 exe 的 codex-proxy

运行
![06de3249b1c1d1ca885aa4860f2f49ee.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVktfDiaaDhw7SVC2UOXg4nEJEyZu9TpYT5wkIF0T1tgUicbYChUPPWvoj8alxk4Yaic6icGX74IiaZn9KsRqujlTgfSjkluc6pibjTQ8/640?from=appmsg "null")

06de3249b1c1d1ca885aa4860f2f49ee.png

点击添加账号，然后登录自己的 chatgpt 账号，如果需要可以配置上游代理
![a212ed4b32548cce67ed01357f286dfc.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmsgsw28UU0o3LK8ALnfPUl4EmwXGtlFjYGIF15CLmB9jDF9vMfuUfOT8OGffhZOwqpDtcKqAZA7Ogd2oEWMHTD4gfiaSZcCwP4/640?from=appmsg "null")

a212ed4b32548cce67ed01357f286dfc.png

然后访问 `设置`，在其中获取相关接口和 key 信息
![17fcad4ff569fb45bd45d0503f4a8e15.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVm8TB06o3NVIPR7a9WjicB7aKzL54DPss0c4KaW3aZbMtUcAz7Y5AvbiaIqG3VznxKdBfbjiaoaGRS4o3gpuRLNxFicMGJUib7ibAFd8/640?from=appmsg "null")

17fcad4ff569fb45bd45d0503f4a8e15.png

curl 请求验证
![32e9a885f822ad9960eb506591ea1838.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVm3mt39Gz5KFIHDrSx9ZdAYwlojBy9JflVvLicIraGq8BWwaNs5KSDpTOVZ6ugcYkx2XiasKt7WicBIh7pbBKpOAECXzFYWBDx704/640?from=appmsg "null")

32e9a885f822ad9960eb506591ea1838.png

可以配置在其他需要的 AI 客户端中

在 cc-switch 中演示

![253aadf0edd159b4380d5a5812b5e9e3.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlwaiaMIJrJ2S9T47iaNcPHYSPI0ctrpLwtia8MxiaywhHpY978QZibX2lon4By3clegFj169s3N5hyz9IMibhq5hypuRbGt6Cpff7JU/640?from=appmsg "null")

253aadf0edd159b4380d5a5812b5e9e3.png

用 opencode 演示
![f2b1dea26dc60abe9d37eedcf9d1ce23.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkP28UKmrnAN2M9wTqPDwLxkW4uam1o2QaACudLibZ3NvbjTum18ytwkON7QQLAK85jqGrXFFuYAlvOIP6tBWMJonsAssrLX3FM/640?from=appmsg "null")

f2b1dea26dc60abe9d37eedcf9d1ce23.png

可以看到成功调用了 codex 中的接口

## 安全工具举例

拿前几天介绍的 CipherBridge 来说

项目地址：https://github.com/CuriousLearnerDev/CipherBridge

![32ec8d2ff5765b2e7ea64f388316af2a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkhQL7GCnYmJicmE9BxfwJMQeC1OP792c5sJ4Xtt8HogeTBjC75HzF6vgibNyg6XVxwcAZUDjZ8soLPky5UbZCXqpXGxEnAqKWXs/640?from=appmsg "null")

32ec8d2ff5765b2e7ea64f388316af2a.png

AI 分析，可以正常使用
![2143fa84fae154136784c5b955c61604.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVk1W4rtIgBGcjiblSsbzgMPhM5x8KFwVwmV891TYUFAibhgNQwZXP9gNANMCYAyJvt17SMxJdc0k5OB2ljk2HLficTwZjAiaUu8szY/640?from=appmsg "null")

2143fa84fae154136784c5b955c61604.png

如果乱码，提示词添加：

```
格式要求：JSON Unicode \\uXXXX 转义输出
```

具体介绍：

* • 面向 APP/Web 加解密逆向分析的工具 [https://mp.weixin.qq.com/s/YBKCGTC5CIBUo0\_cux5vWg](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247490286&idx=1&sn=89d9f23cd0c0559095dc894d85155744&scene=21#wechat_redirect)

## 总结

有时候，这个技巧挺有用的。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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