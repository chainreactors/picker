---
title: 赏金猎人私藏，多层编码破WAF盾
url: https://mp.weixin.qq.com/s/qEf04nskxmwuhT6doLC0Ng
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T06:57:50.498761
---

# 赏金猎人私藏，多层编码破WAF盾

# 赏金猎人私藏，多层编码破WAF盾

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

> 【内容描述】
> 本文介绍 Burp Suite 扩展 Hackvertor。它用"标签"做转换，比 Burp 自带解码器强得多——可以多层嵌套编码、在 Repeater 里实时改写请求、用 `throw_eval` 标签绕过 Cloudflare WAF。文章还讲了两个"彩蛋级"功能：用四字母组频率评分自动解 rotN（起因是女儿问 T 恤上的二进制是啥），以及用重合指数自动爆破密钥长度、解重复 XOR 加密。面向赏金猎人和安全爱好者，重技术、轻说教。

---

你大概率没听过这个小工具——Hackvertor。

它是个 Burp Suite 扩展，核心思路就一句话：用标签做转换。听着平平无奇？但你用过就回不去了。Burp 自带的 Decoder 只能一层层手动点，Hackvertor 直接把转换写成"标签嵌套"，想套几层套几层，发送前自动算好。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGG8SFvtfrd04RPUYicQvv3WV3rzpgb5Tu0a28aicobibCvUje6akfDBYW5QCRwUsINyicFrppfKFL9sLYMxxuu6FbBjmibRE2xia1buQ/640?wx_fmt=png&from=appmsg)

这篇不是官方文档，是我边用边写的"实战笔记"。看完你应该能上手，顺便还能懂点编码学和密码学频率分析——别怕，我尽量讲人话。

## 一、标签到底是个啥

Hackvertor 背后的理念很简单：每个标签先把自己的内容转换一遍，再把结果喂给外层的下一个标签。层层套娃，就能轻松实现多层编码。

比如要把字符串编码成 base64，就套个 base64 标签：

```
<@base64_0>test<@/base64_0>
```

想玩花的？先把 "test" 转成十六进制、再整体 base64。那就 hex 包 base64：

```
<@base64_1><@hex_0(” ”)>test<@/hex_0><@/base64_1>
```

注意 hex 标签后面跟了个参数 " "，这是分隔符——它会把每个十六进制串用空格隔开，再传给外层。这种"标签里还能带参"的设计，后面绕过 WAF 时特别好使。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGEzCMpLDG9PJHGydTCcEiapDcYElErT66Rc0GMCB7P2WBLBJAJkSwmTFgo3GgLxkCFlulhQGPtscQn3UuuiaqaeoD92SBv7nibGcs/640?wx_fmt=png&from=appmsg)

## 二、日常怎么用

装好扩展，Burp 里会多出一个叫Hackvertor的标签页。左边输入框、右边输出框，你把要转的文本选中，点一下对应标签，转换结果就出来了。怕手滑没跑？它还有个专门的"转换"按钮可以重跑。

标签按 Encode（编码）、Decode（解码）之类分了类，找起来不费劲。它甚至做了类似 Repeater 的多标签页，等于能同时开好几个独立实例各转各的——审计多个目标时不用反复清空输入框，懂的都懂。

## 三、正经活：用标签绕过 Cloudflare WAF

光转码不够劲，我后来让 Hackvertor 的标签能直接用在 Repeater、Intruder 的真实请求里。用法是：在 Repeater 里右键 → Hackvertor 菜单 → 给选中的文本加标签，请求真正发出去之前，标签会自动执行转换。

代理里也能用，不过默认关着。想开的话去 Burp 主菜单的 Hackvertor → "Allow tags in Proxy" 勾上就行。

上实战。把下面这个 URL 发到 Repeater：

```
hxxps://wafproxy.net/xss/xss.php?x=
```

在等号后面敲入这段 XSS：

```
<img/src/onerror=alert(1)>
```

然后选中其中的 alert(1)，右键 → Hackvertor → XSS → throw\_eval。它会给选中内容裹上标签。点 Go 发送，响应里你看到的是：

```
<img/src/onerror=window.onerror=eval;throw'=alert\x281\x29'>
```

看见没？原本直白的 alert(1) 被改写成 window.onerror=eval;throw'...' 的形式，括号也被 \x28\x29 转义。这种变形经常能绕过规则类 WAF 的特征匹配——Cloudflare 那套正则看到的不复是它认识的 alert(1) 了。

想验证自己发的到底是不是这串？在请求编辑器里右键 → Hackvertor → Copy URL，它会把"标签转完之后"的真实 URL 复制出来。注意别用 Burp 自带的复制 URL，那个复制的是"还带标签"的版本。

> 小提醒：Intruder 里也能用同一套标签，先 Repeater 定义好再发过去即可。配合占位符做多层编码，批量打的时候相当香。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGFjicP0uIv8cgUJ9S541btHsOKVmxZP3Tfl1ibNjggPib17D8x8bHuQDjdZqGstbw9mGIaViaHufib6Noej7ARyV42RuYiatAFD4EDpQ/640?wx_fmt=png&from=appmsg)

看到这儿的朋友，要是觉得这工具能省你几分钟手工活，或者解码思路给你开了点窍——

👍点个赞，让更多白帽同行看到这篇；

💬关注我，后续还有缓存投毒、WAF 绕过、SSTI 之类的实战连载；

🔁顺手转发给还在手工 Base64 套娃的战友，别让他们再点断手；

📣推荐给做安全的朋友，独乐乐不如众乐乐。

咱们下篇接着扒。保持好奇，保持安全。

（Hackvertor 是开源扩展，搜名字就能装。文中所有案例均已合规披露或仅用于教学演示，请勿用于未授权目标。）

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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