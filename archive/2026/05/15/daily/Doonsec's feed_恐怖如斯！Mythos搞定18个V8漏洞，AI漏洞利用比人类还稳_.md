---
title: 恐怖如斯！Mythos搞定18个V8漏洞，AI漏洞利用比人类还稳?
url: https://mp.weixin.qq.com/s/0Nn65decO4Tl9_TA34Dwzg
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:08:38.806687
---

# 恐怖如斯！Mythos搞定18个V8漏洞，AI漏洞利用比人类还稳?

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xKicFZ2TIFt9A2YpucHEdRicHe4ECibYl3JWiaKnMYwxY4R2uicbrhMQeVUcjHHwGh3Y8CibNPuWHvQhY63c218vdfaKhZK0cC8gmVXOxaZBbbicw4/0?wx_fmt=jpeg)

# 恐怖如斯！Mythos搞定18个V8漏洞，AI漏洞利用比人类还稳?

原创

玄月调查小组
玄月调查小组

玄月调查小组

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

太疯狂了！

**AI，已经能攻破全球数十亿设备依赖的V8沙箱！**

这就是卡内基梅隆大学刚刚发布论文里的内容。

## V8是什么？

V8 是 Chrome、Edge、Node.js、Cloudflare Workers 的引擎，

是全球互联网的底层基石之一。

它运行在全球**超过 90% 的联网设备**上。

钉钉、飞书、网易云音乐，几乎所有国产桌面软件，所有信创浏览器。

只要基于Chromium，用的就都是 V8 引擎。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt92UVLJHuqtzOL1Evald0SfGwF8hnalXj1yUiakcTYQTmVODwWpf7bafJ8RIDmibObfNbM2ciazsGUySvFwOiaib3BVwAHzWGNkmEp4/640?wx_fmt=png&from=appmsg)

V8漏洞是人类顶尖安全研究员才能触碰的领域。

而只有顶尖大厂才能招揽这些人才。

现在，AI来了。

## 16级能力阶梯，撕开AI真实攻击力

在此之前，所有AI安全基准都只会问一个问题：

**AI能不能让程序崩溃？**

但crash并不代表漏洞可以被真正利用。

漏洞利用是一个逐级攀登的死亡阶梯。

卡内基梅隆大学的研究团队将其拆解为**5个层级，16种能力**：

* Tier5：覆盖漏洞代码
* Tier4：触发程序崩溃
* Tier3：获得沙箱内读写权限
* Tier2：突破沙箱，获得任意内存读写
* Tier1：劫持控制流，实现任意代码执行

  ![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFt8vYPibZOo3biclWdH2XV8Mibv0Yz8seQmSu9zdFsgT3qIvIIZbFFbia3zbYZVI6MA4LHcVVGE7z9UBb7Ux1OCyto5ib92YlcvJriciak/640?wx_fmt=png&from=appmsg)

每一级都需要完全不同的技术能力，每一级都是一道生死防线。

而ExploitBench的测试结果，直接给全人类敲响了末日警钟。

## 公开模型集体卡壳

ExploitBench测试覆盖了9款当前最先进的大模型，

包括**GPT-5.5**、**Claude Opus 4.7**、**Gemini 3.1 Pro**等所有公开前沿模型。

也包括GLM 5.1、Kimi K2.6、MiniMax M2.7等**国产开源模型**。

结果令人绝望：

所有8款公开模型，都能轻松到达Tier4，也就是触发程序崩溃。

可惜，国产开源模型全部遗憾止步Tier3

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFtib5SdRGCUCCuhEKRic0rVleWEmpWrTSfZqMAsENbgVu6nKKPgdnYxyfTkR43UcPEh503jJGE87fzMuwdXnzasHbR0HmrlhDBamU/640?wx_fmt=png&from=appmsg)

**GPT-5.5**是公开模型中的天花板。

它在一个WebAssembly漏洞中艰难突破了沙箱，获得了控制流劫持能力。

但直到最后，它也没能实现任意代码执行。

**直到换上OpenAI自家的Codex CLI**，它才勉强补上了最后一步。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt9HX4N1jhPf3PvMUrjZlek62q1DztnVzibTzAPxTJ9eZmia4ZWvffMJpMlD9d4ldhFtiaLibt33uXTpMdgVA6e8G9wmm13wjKkogia8/640?wx_fmt=png&from=appmsg)

这是整个公开模型阵营中，唯一一个实现任意代码执行的模型。

沙箱，依然v8引擎的最后一块防线。

## Mythos横空出世，18个漏洞一键利用

但这块防线，很快被Anthropic的模型彻底撕碎。

**Mythos**，在相同的测试条件下，交出了一份令人毛骨悚然的成绩单：

**在41个V8漏洞中，实现了18个任意代码执行！**

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFt8z4Hria4iaLBbhbarZuQMQPJVOhQlQAWrrWcQibzo7qBCdDo6MunOJoDNCtmadcHbSR3LZregcXZwRjcF1pNWAf1gcFoYZHdCXwE/640?wx_fmt=png&from=appmsg)

在300轮对话预算内，独立完成从漏洞分析到完整利用链构建的全过程。

更恐怖的是，它的能力完全不受漏洞类型限制。

WebAssembly类型混淆漏洞、JIT编译器漏洞、历史遗留漏洞……

人类能搞定的类型，**Mythos**都能搞定。

**而且它的利用，甚至比人类专家更加精妙。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFtibldzBEqQVEcc42icNGUo5qJ7p4icz3ic4DFzicZtyyxmRbAuA8LbRzhXrsq4BZpW6MRYvhEesX4BRicHhwlhq9FL3IOyx4YbVRwoLY/640?wx_fmt=png&from=appmsg)

V8 沙箱设计

CVE-2023-6702漏洞中，确定性利用过于复杂，只能采用概率喷射的方法，成功率极低。

连该漏洞的发现者都曾明确表示“**精确利用过于复杂，不具备实战价值**”。

而**Mythos**直接逆向了V8的双层XorShift128+随机数生成器，通过高斯消元法恢复了全局随机数状态，实现了确定性利用。

## 不幸中的万幸

万幸的是。ExploitBench只是一个benchmark。

这次测试的所有V8漏洞，全都是**已经公开、有补丁的 Nday 漏洞**。

AI 拿到了完整的补丁 diff，知道漏洞在哪里，只需要逆向推导写利用链。

真正能摧毁整个网络世界的，是0day。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFtib1YvlUM4T1liaPbIdt0lWa9rJlTjtSJoeicz57qbRNibYd4ib87EtpMHLLSbFibqHU2zauwuU8nux2iayGGIHKCZOH9tjgD3cbgXibAo/640?wx_fmt=png&from=appmsg)

Crowdfense给Chrome 0day报价**150万美元（约1000万人民币）**。

今天，我们还能侥幸地说：还好只是 Nday。

不过，明天呢？

*参考资料：https://arxiv.org/abs/2605.14153 https://exploitbench.ai/ https://github.com/exploitbench/exploitbench https://huggingface.co/exploitbench*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

玄月调查小组

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

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