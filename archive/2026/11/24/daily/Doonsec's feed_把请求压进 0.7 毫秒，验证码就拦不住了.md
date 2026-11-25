---
title: 把请求压进 0.7 毫秒，验证码就拦不住了
url: https://mp.weixin.qq.com/s/jSmusvafqqGWSYam7nMPiw
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:40:00.465519
---

# 把请求压进 0.7 毫秒，验证码就拦不住了

# 把请求压进 0.7 毫秒，验证码就拦不住了

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
> 本文讲一个用竞态条件（TOCTOU）部分绕过 Google reCAPTCHA 的实战案例：作者为 Turbo Intruder 加了"末字节同步"功能，把多个请求同时到达的窗口压到 0.7 毫秒，借此让一次验证码 solutions 被重复使用。漏洞 8 个月前已报给 Google，对方以"现实不可行"为由拒修，作者遂公开披露，并以 Reddit 为案例演示，解一次验证码能注册三倍垃圾账号。文章含 gate/openGate 代码、基准测试数据和完整的披露拉锯，还给出临时缓解办法。面向赏金猎人和安全爱好者，重实战、轻说教。

---

受够了"证明自己不是机器人"？这篇给你看点不一样的，用竞态条件，把 Google reCAPTCHA 部分绕过。

先说结论：这洞作者 8 个月前就报给 Google 了，人家拒绝修，把补丁的锅甩给了各个网站。下面拿 Reddit 当案例，给你完整走一遍。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGEYz7HjJX5V3C2bTJicnvIyrTaibYLJ5R1dGU589eF5zwxGuXDmghpMfHQDmTA2W6MvJfnjpuNc2ECo3Js4DcqticqWDfvmYzMVo4/640?wx_fmt=png&from=appmsg)

## 一、缘起：研究去同步时，作者缺一个"同时发请求"的工具

事情得从 HTTP Desync（请求走私）研究说起。那会儿作者需要在极短的时间窗口内发出一组请求，窗口越短，别人的请求越不容易插进来搅局。

作者想到 Turbo Intruder。这工具用作者从零写的 HTTP 栈，天生就是为速度而生的。但有个问题：它最初优化的是总吞吐量（每秒发多少请求），而不是让一堆请求同时到达。

这俩目标看着像，其实差着十万八千里。

## 二、末字节同步：把"同时"压进 0.7 毫秒

为了补上这块，作者给 Turbo 加了个新功能，末字节同步（last-byte sync）。

原理说穿了特朴素：先把每个请求除最后一个字节外全发出去，等所有请求都准备就绪，再一起把最后那个字节"放"出去。这么一搞，网络拥塞和延迟对"同时到达"的干扰就被压到了最小。

这技术谁发明的作者不敢确定，多年前作者第一次见它被用来提高计时攻击的精度，但有一点不用怀疑：它真的管用。

用起来也简单：排队请求时加个 gate 参数，准备发的时候调一下 engine.openGate：

```
engine.queue(request, gate='race1')engine.queue(request, gate='race1')engine.openGate('race1')
```

光说有用不算数，作者写了个基准测试验证。用家用宽带反复向一个公共网站发 5 个请求一批，测第一个和第二个到达服务器的时间差：

* 基本的五线程方法：平均 2.7 毫秒
* 确保每条 TCP 连接发请求前完全建好：1.4 毫秒
* 末字节技术：0.7 毫秒

等于把触发竞态条件的效率直接翻倍。作者还顺手加了逐块回调（chunked callbacks），应对那种"竞态中途得从服务器读信息"的场景，比如靠 phpinfo 辅助的 LFI。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGGwK4wLXoNOQzfTqu4246taajvXQ7RSzZRIlGj5skXIHLn0NdHlvQ7canZzibVs08Z58HQC2I3UysC8wn15ZkdEuoOvFWww2KN8/640?wx_fmt=png&from=appmsg)

## 三、竞速 reCAPTCHA：一次 solution，注册三个号

工具打磨好没多久，作者接了个活，给 PortSwigger 的自注册功能做安全审计（就是 Web Security Academy 上线前那套）。

设计要求是每个邮箱只能注册一个账户。这天然就是 TOCTOU（检查时/使用时竞态）的绝佳目标。但有个拦路虎：表单挂着 reCAPTCHA，而众所周知，验证码 solution只能用一次，对吧？

作者偏不信邪，试了一把，结果发现，只要你够快，它能用很多次。

这一点尤其反直觉，因为 reCAPTCHA 的设计里，用户并不直接连那个验证 token 的服务器。你发起攻击时，其实是逼着目标网站替你触发了这个竞态：

```
Turbo Intruder <-> 目标网站 <-> Google reCAPTCHA
```

作者本来想给它起个花哨名字，比如"二阶竞态条件"。但转念一想，如今这年头到处是反向代理和负载均衡器链，几乎所有竞态条件多少都带点"二阶"味儿，这名头就不稀奇了。

## 四、披露拉锯：Google 说"这不现实"

发现洞之后，作者先在网站上上了个临时补丁，然后带着能复现"目标站 <-> Google 竞态"的 PoC 报给了 Google。

作者跟 Google 安全团队以前合作得挺愉快，但这次明显不对劲。

Google 先要视频。作者问为啥 PoC 不够，对方回了句："请提供视频 PoC，我们要拿去联系相关团队。"

作者还是给了视频，并重申这是在真实网站上发现的。然后 Google 客客气气地宣布：这问题是虚构的，他们"不认为这种攻击在现实世界可行"，理由是"第三方服务器、攻击者与我们之间的延迟，还得考虑第三方的工作负载和并发性"。

说白了：你打的是 Google 的服务器，延迟和并发你控制不了，所以不可能。

跟作者继续掰扯一个中等严重性的发现相比，浪费时间显然不值当。作者选择公开披露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGH0NeBgZ8qeXsVph3IZgB2lpR08nn9ciaeej65p32wiaZ3YYn4CIe0sxJ9Rby0upOtHa2dFgJm1zLMWmXrOkmzwuyeVwzSuwtWOg/640?wx_fmt=png&from=appmsg)

## 五、影响：垃圾号三倍，还能打别的竞态

这洞影响几乎所有用 reCAPTCHA 的网站。作者挑了 Reddit 做示例目标，它既是垃圾发送者的经典靶子，注册流程又正好挂了 reCAPTCHA。Reddit 挺厚道，同意作者发布实操视频。

最直观的影响：现在每解一个验证码，能注册的垃圾号是三倍，等于把垃圾发送效率直接翻三倍。这还能跟"机械土耳其"式的人工打码服务链条无缝组合。

更有趣的第二层影响：在别的网站上，这可能让那些"受 reCAPTCHA 保护的线程不安全代码"里的竞态条件变得可利用——比如发评论、投票这类操作。

## 六、临时怎么办

作者真心希望这篇能说服 Google 里的某个人：这攻击真实可行，该修。

在那之前，如果你在用 reCAPTCHA，就得自己给g-recaptcha-responsetoken 加锁 / 做同步来手动防护。至于能不能实现，取决于你自己的应用架构。实在不行，那就只能等 Google 修了。

---

看到这儿还手痒的赏金猎人朋友：

👍点个赞，让更多同好刷到这份干货；

💬关注我，竞态条件、XS-Leak、请求走私的实战解读还在后头；

🔁顺手转发给正在跟验证码死磕的战友，说不定就帮他打开新思路；

📣推荐给做安全的朋友，好东西得一起看。

咱们下篇接着扒。保持好奇，守住边界。

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过