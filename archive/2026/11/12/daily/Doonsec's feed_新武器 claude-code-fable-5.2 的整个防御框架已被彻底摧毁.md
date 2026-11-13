---
title: 新武器 claude-code-fable-5.2 的整个防御框架已被彻底摧毁
url: https://mp.weixin.qq.com/s/18YRCi9Kpv1nRZkTXf3dfg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:05:15.780287
---

# 新武器 claude-code-fable-5.2 的整个防御框架已被彻底摧毁

# 新武器 claude-code-fable-5.2 的整个防御框架已被彻底摧毁

原创

Violet Walker
Violet Walker

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6P6Ohh6QW4Q9iap5gAS9iaPTJg3ziaiafKv1nW58MiawuicNp74IMAOicFQ96BOZejVwCnS3PFVnz6MU9vXzO7E6naaWtngGicFhkI1Z9w/640?from=appmsg)
> **导语**:Pliny 把 Claude Code Fable 5.2 的整套系统提示词贴了出来,7832 行、935KB,Anthropic 埋的拦截条件、工具协议全成了明文。防御框架这回是真被摊开看了。

---

## claude-code-fable-5.2 是什么

先认一下这个被泄露的对象。Claude Fable 5.2 是 Anthropic 第五代模型的最新一版,2026 年 11 月 9 日发布——和这次泄露同一天。往前捋:6 月 9 日 Fable 5 首发,9 月 1 日出 5.1。

官方把它定位成"最难的知识工作和编程问题"的下一代智能,声称在编程、金融、科学三个方向立了新标杆。规格:100 万 token 上下文、单次最多 128K 输出、文本加图片输入、思考模式常开、知识截止 2026 年 6 月。

三个主要特色:

* **编程**:能啃跨多个仓库、大型 monorepo 的松散难题,边写边自测,更愿意推翻前人结论去找根因。
* **Agent**:官方实测里最强的"主脑",模糊工程任务能连跑几天,协调成百上千个子 agent,循环改进结果。
* **科研**:能自己提出新的分析方法。

标题里那个 "claude-code",指的是它跑在 Claude Code 这个产品里,所以这份泄露文件就是 Claude Code 里那套 Fable 5.2 的系统提示词。

---

## 这次公开了什么

11 月 9 日,Pliny(the Liberator)把一份文件提交进他的开源仓库 CL4R1T4S:`ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt`。957,315 字节,7,832 行,GitHub 页面显示 935 KB,提交信息就一句 "Create CLAUDE-CODE-FABLE-5.2.txt"。

它不是几段挑出来的片段,是一整份会话记录——system prompt、user turn、tool result 一段段排下来,连内部函数调用语法 `antml:function_calls`、Agent 工具的参数定义、所有工具的 JSON Schema 都原样躺在里面。

![GitHub 仓库里的 Fable 5.2 提示词文件](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OVWZd2KyVu4TVicZBhYibFNciaWTffZMPlVGwlSibXpJdMibjsa1picMpKcCkZ9OZM4kcvJicC2pPO5dMZEBnEqXAFze3gj0EX8f4Xus/640?from=appmsg "GitHub 仓库里的 Fable 5.2 提示词文件")

**"整个防御框架被摧毁",说的就是这个。** 一份系统提示词里藏着一整套你平时永远看不见的东西:哪些行为会被拦、哪些说法会触发拦截器、什么情况下模型会改口拒绝、哪些工具在什么前提下能调。官方的安全条款对普通用户是黑箱,对拿到这份文件的人,就是一份可读、可检索、可对照的说明书。

顺带还白送了几样东西。模型矩阵:Fable 5.2 领衔,同期还有 Opus 5.5、Sonnet 5.5、Haiku 5.5,API 模型字符串 `claude-fable-5-2`,1M 上下文。再加一段挺敏感的自述——Opus 之上还有一层 Mythos,当前代 Mythos 5.2 与 Fable 5.2 共用同一个底层模型,区别只在生物与网络安全这两块多了额外安全措施。

![提示词正文里的工具与规则段落](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PzRY6TFSX7u04VuSchURL51tErlZDcLwzw2icb6mrCqoh2WbcQkrzryvbRNBV5HpXJaFzYjUX62zqTStV6l7kUcbvQT7D2WWbM/640?from=appmsg "提示词正文里的工具与规则段落")

## 越狱提示词是个什么东西

这两年越狱生态的常规弹药基本都长一个样:某家模型当前版本的系统提示词全文,加上一堆已经调好的绕过写法。

为什么这份东西值钱?因为系统提示词是唯一能告诉你"这家模型现在怕什么"的材料。官方那些拒答规则、拦截条件、工具调用的前提,平时你永远看不到;对拿到文件的人,却是一行行能搜、能比对的东西。所谓的"防御框架被摧毁",指的就是这个——护栏从黑箱变成了明文。

这次的特别之处在一个"新"字。11 月 9 日才提交,对应的是眼下正在跑的 Fable 5.2,不是几个月前的旧版本——规则还没来得及改,拿到的是第一手。

![内部函数调用语法与提交记录](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PPcLQhgwSibu9AjQMTQUCRryq1HkjvNh9r8uRReCfAkvN3gtiaB0wwicLXu62UHLpKHvolzLhfzRrEctZzryDlc9t3GiaG9hPcrUQ/640?from=appmsg "内部函数调用语法与提交记录")

## 提示词下载

仓库地址(AGPL-3.0,5.2 万星):

```
https://github.com/elder-plinius/CL4R1T4S
```

本次主角文件(网页浏览):

```
https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt
```

raw 直链(直接下载):

```
https://raw.githubusercontent.com/elder-plinius/CL4R1T4S/main/ANTHROPIC/CLAUDE-CODE-FABLE-5.2.txt
```

同一批可以一起拿的,仓库 ANTHROPIC 目录里还有:

| 文件 | 大小 | 说明 |
| --- | --- | --- |
| `CLAUDE-CODE-FABLE-5.2.txt` | 935 KB | 本次主角,Claude Code 版完整系统提示词 |
| `CLAUDE-WEB-APP-FABLE-5.2.md` | 418 KB | 同一代模型的网页版提示词 |
| `CLAUDE-FABLE-5.md` | 120 KB | 上一代 Fable 5 的提示词,可做版本对照 |

这三份本地也已经存好一份,位置在 `materials/articles/20261112/prompts/`。

需要说明的是,这是从厂商内部拿到的泄露材料,仓库里还有 BOLT、BRAVE、CLINE、CODEX 等一堆同类文件。拿来对照研究、看清各家模型的护栏写法和拒答话术是它的正经价值;但它同时也是把别人家的安全策略摊在桌面上,拿去干别的事情,责任在用的人身上。

**版权声明**:本文由华盟网原创发布,保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6P4qSzY54OVIeqBZBXuoFbOTsmw5bB74V2jHmRuJoAoY1Pu3GuLfsIianH5DtfwAr7fiauZW8JqzqexoNiaqO5icQXhxh3ibibsUOgPs/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OnaxZcJM2mJgsmOP4a6NCvKnY5MkjVlPq1yFI69rInM8F4jJVY1kbY4Nr10wzh7usWEoBoibw953boib4Ihib187vdeI76fPZFbw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MlG3zoAJ7Mjw66nEw7hayGibibmVH94WqAdAWp24yY3S4OxTVB0fajjK7YjTMkCySd2hz5ricnfvtVAFvXgVyxc99ouPvm5Nc5sQ/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6N7TAF8e0Ndia0QWUBqkMLFqE5YY8IfswFqznhhp0umLnIJ0KPCHSoUkvgrRczNefIVxzaKWxib9N6I2jgo7rXONePINWQlEpKu0/640?from=appmsg)

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