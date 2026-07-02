---
title: Firefox‑Reverse：网页版AI自动化逆向算法工具
url: https://mp.weixin.qq.com/s/Rf-aL_pHxpDN_Pr3gsBVHQ
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:56:06.174920
---

# Firefox‑Reverse：网页版AI自动化逆向算法工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicLbcOrYDW0uoNgEicNzEm6VjqXo1jBiaWNSchHzekKdDc2P25SYoaErEtIQic5ictxIVJoPwRT1ZLSWbMfhlGEwBicTk9OUfudAeTns/0?wx_fmt=jpeg)

# Firefox‑Reverse：网页版AI自动化逆向算法工具

原创

网安工具库
网安工具库

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[K8sPenTool：一款面向Kubernetes集群的综合渗透测试评估平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487757&idx=1&sn=34e2084e5d8e8dee47faddcffb2d3c61&scene=21#wechat_redirect)

·[CTF²: 推荐一个比较全面的CTF靶场](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487722&idx=1&sn=f12056918c209179a318d1f904d05210&scene=21#wechat_redirect)

·[Bug Hunter：一个代码安全审计的skills](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487714&idx=1&sn=b02dcacd5efb02443bd0a213b80ef99e&scene=21#wechat_redirect)

·[NextWQ：一款QQ小程序安全测试分析工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487701&idx=1&sn=91f799ebe8d87bb92f33a04230e5814c&scene=21#wechat_redirect)

·[MPScan：微信小程序自动化敏感信息审计工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487683&idx=1&sn=1c45d8b5233e471633e7f430d93c0ec3&scene=21#wechat_redirect)

·[cloudTools：一款集成多平台的OSS接管和管理工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487669&idx=1&sn=1ddc86d05e10c5fc4219df5917374322&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**背景分析**

![Firefox-Reverse logo](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIdA8TKllDVicpUkgkjf1ItDfOGLPsIrFibibUPMiccYdyuCugkCaJgwAS5j9ibBibDqy4WpbLdJiaKpmJsRHqRWaU7vJpibQ89IJw12Og/640?wx_fmt=png&from=appmsg)

    很多网站发请求时会带一个加密参数——签名 sign、令牌 token、风控指纹等。想在浏览器之外（你自己的 Node / Python 脚本里）复现这个请求，就得搞清楚这个参数是怎么算出来的。这就是 JS 逆向，而它通常很难：逻辑被混淆、塞进 JSVMP（JS 虚拟机保护）、或编译成 WASM，还深度依赖一堆浏览器环境指纹。传统做法要在 DevTools 里手动下断点、补环境、反复试值，耗时且容易兜圈。

    Firefox‑Reverse 把这套活儿交给一个内置的 AI Agent。 它住在浏览器侧边栏里，能像一名专业逆向工程师那样自己抓包、读代码、在引擎 C++ 内核层打点（页面察觉不到）、补环境、写脚本、实打接口验证——目标是把一个加密参数还原成你能在 Node.js 里独立跑出来的纯算法。

    与「AI + 普通浏览器自动化」最大的不同：它的关键观测工具（签名器入参追踪 / JSVMP 逐指令 trace / WASM import 边界 / 引擎级分支差分）都做在 SpiderMonkey/Gecko 的 C++ 引擎里——这些是页面 JS 反射不到、检测不出的「上帝视角」，对抗反调试 / 反 hook 的强站点尤其关键。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**工具获取**

GitHub地址：

```
https://github.com/WhiteNightShadow/firefox-reverse/releases
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLBKVbBia6Oic8laRwSWw0UNNBBZ3WvnBZV2NgM63kNCTSR1kEz2jhjWhub8Vt8ickDYdKqcHgibicwHsPI4sPrBltR2jC4zLLiamUvQ/640?wx_fmt=png&from=appmsg)

根据系统选择相应的版本下载即可。

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIiao3Zia7J6LZibHJzBh1TSMVorxjpxKZQLVhIgaflPRsu4YkkGhDjRB6v8soRsPwkKtjbJ3iazGjGjB2nBd5ut9ZlTEeVd2Yue20/640?wx_fmt=png&from=appmsg)

    点击.exe文件启动工具即可。

    若 SmartScreen 拦截 → 「更多信息」→「仍要运行」

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**功能介绍**

启动后会看到主页：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJSK54akJPZL8wfpMiapmW1qCkQ79xPcQMnSNVCicyUnmkUqprteiaDLu0goRpIVPfjetibQH4jN6VAduKFP5GoWy4pDJ2BicpGvDUg/640?wx_fmt=png&from=appmsg)

    点击左上角的AI侧边栏，然后点右侧边栏的 Firefox‑Reverse 工具图标（机器人/逆向图标），打开 Agent 面板：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicL4bhnD7FlRcDDTOBIPLictRicoJy3D0gxfWqib5ybS941JpzeucxCMXj5Aw1uIBupbAGJibOYkzNFWjeaLBeialPBhxibRky11YdmqI/640?wx_fmt=png&from=appmsg)

    然后点面板右上角 ⚙️ 设置 → 选一个模型供应商，填上你的 API Key：

    模型支持：

```
支持 DeepSeek、智谱 GLM、Kimi（Moonshot）、MiniMax、通义千问（Qwen）、Claude、OpenAI，或任何 OpenAI / Anthropic 协议兼容的自定义端点（填 baseUrl + token + 模型名即可）。
```

    然后可用选择模式，分为“全自动”和“AI辅助”两个模式，全自动模式可以给它目标接口/参数，它一条龙自己搞定；而ai辅助它先出方案、每做完一个阶段就停下、给你方向选项，你来拍板、逐步推进。

    然后把目标告诉模型按下面这个格式把任务说清楚（信息越具体，AI 越少走弯路）：

```
【站点URL】https://example.com/list          # 能看到目标请求的页面【接口URL】GET https://example.com/api/v1/list?page=1   # 你最终想复现的请求【目标参数】请求头里的 X-Sign（签名）。若还有其他动态参数（时间戳 / 设备指纹 / token 等）一并列出【输出目标】① 黑盒可用版：用 Node.js 还原参数生成算法，脱离浏览器独立把接口请求成功      ② 白盒纯算版：进一步把它还原成不依赖原始混淆代码的纯 JS 实现（可选）
```

    然后看它自己抓包、定位、补环境、实打验证。产物（脚本、还原代码、笔记）都会落到你为这个会话指定的工作目录里。

    这里使用Bugku上面题目game1网站的示例：

    这里我选择的全自动模式，将需求编辑好后发送给大模型，大模型会根据要求自动分析并给出结果：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKUwCLrhROpK8icLibhuqaP6tEcJdUObibnQL7mfQMDteuMlC45q9hYSwjsmYHZkYc4SPeicblO8XQibUQ8N65DhRXJtAfE5P0rJWVo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLqibq151aS4AnNBKaB2gpibwhy8ibxdyibQEYHFFjIHuQ2VhNmX2JlwA5dDMfMDSlwJ74geGQUsiatrohKyMiaHibeuHlr45ic1NRmhdY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

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