---
title: G.O.S.S.I.P 技术笔记 2025-01-15 薛定谔的寄存器？
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499629&idx=1&sn=2890acf36b4707a5bf91f3c823c4a5db&chksm=c063d1b4f71458a27e12ffc8ec1fe880002d2d92968fadcda511a91279e30d0dacba4fa59f48&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-01-21
fetch_date: 2025-10-06T20:11:04.656800
---

# G.O.S.S.I.P 技术笔记 2025-01-15 薛定谔的寄存器？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Ffzfyzj9icerTSRGjC7u9SyodTdTIqGFSLwzoNpHoCYnSBuib0ojz73RnUib5evs4q7G3IKOJCiczMBg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 技术笔记 2025-01-15 薛定谔的寄存器？

原创

GoSSIP的何同学

安全研究GoSSIP

> 编者按：寒假到啦！今天送上一则来自G.O.S.S.I.P成员何同学（此何同学非彼何同学 没那么丁真）的技术笔记，顺便提醒大家，不能光顾着读论文和抓大放小，也要钻研技术细节，毕竟“The devil is in the details”

---

最近在 macOS（ARM版）上写一些汇编代码时遇到了一个诡异的问题：代码在测试时会随机出错。这里的随机不是指输入随机的情况下遇到某些输入会出错，而是在固定输入的情况下，程序会以一个小概率出错——大约50万次运行才会出现一次，基本无法复现！这种低概率的 Bug 让我一度怀疑：难道是我的代码不小心触发了某种量子效应，让程序在平行宇宙中随机崩溃？又或者是这个代码将能揭示宇宙的本质，因而三体人控制智子在 CPU 中随机引发硬件错误对我进行干扰？为了调试这个 Bug ，我仿佛已经启动了无数个平行宇宙，每次开盒“观测”都不知道这个 Bug 是死是活。

经过一番排查，终于在某次调试中抓到了崩溃的“现行”。Sanitizer（内存检测工具）报告了一个崩溃，原因是程序试图读取0地址的内容。对应的汇编代码如下：

```
10000c278: 90000452    	adrp	x18, 136
10000c27c: 91000252    	add	x18, x18, #0x0
10000c280: a940364c    	ldp	x12, x13, [x18]
10000c284: a9413e4e    	ldp	x14, x15, [x18, #0x10]
```

崩溃发生在第三行代码，问题就出在 `x18` 寄存器上。按理说，经过前两行的操作，`x18` 的值无论如何都不应该是0。这难道就是量子的力量吗

经过一番查阅文档，终于发现了问题的根源：`x18` 寄存器并不是一个普通的寄存器，而是一个Platform Register (PR)。这个寄存器的特殊之处在于，它的用途由系统厂商自行决定。然而，无论是苹果还是安卓的文档，都在字里行间透露出一个强烈的信号：Don’t use/touch this register。而在这个 Bug 中，显然这个寄存器似乎会被某种神秘力量给清空，导致程序随机出错或崩溃。

既然如此，那么我们自然就会发问：为什么 `x18` 会被清空？ 以及 它到底在什么时候被清空？

我们猜测，这可能与上下文切换有关。当程序从内核态切换回用户态时，为了防止敏感信息泄漏，内核可能会清空 `x18` 寄存器的内容。为了验证这个猜想，我们设计了如下实验：

```
// ========== File: check_x18.c =============
#include <stdio.h>

int check_x18();
int main() {
	printf("0x%x\n", check_x18());
	return 0;
}
// ==========================================
// ========== File: check_x18.S =============
.text
.global _check_x18
_check_x18:
	mov x18, #0x2025
	mov x16, #20
	svc #0x80
	mov x0, x18
	ret
// ==========================================
```

该代码中的汇编部分首先将 `0x2025` 立即数放入 `x18` 寄存器中，然后执行系统调用号为 `20` 的系统调用（`getpid`），结束后在把 `x18` 的值作为返回值放入 `x0` 寄存器中返回。如果上下文切换不影响 `x18`，那么函数执行的结果应该是 `0x2025`；反之 `x18` 应该会被清空，结果就会变成0。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Ffzfyzj9icerTSRGjC7u9Syaibib6mL4Y71nKLW8FJH9VOGKrOpfDSqqylrrSRXOc9iaZicZZ0uRepmag/640?wx_fmt=png&from=appmsg)

从实验结果可以看到，上下文切换果然就是导致 `x18` 被清空的“罪魁祸首”！不过 Android 上和 macOS 中对 `x18` 的处理并不一样，关于这个寄存器，很多文章里面专门提到过一些关于它的特定的用途，你可以去问下人工智能助手，它都能帮你总结出来不少。当然，感兴趣的读者也可以进一步自己动手尝试，并欢迎在评论区分享！

最后附上“案发现场”的 Debug 图，给大家还原一下现场情景：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Ffzfyzj9icerTSRGjC7u9SyznZtLkuLibribncZf2MaQWcWibIW1R5ULaE5Wcl35hRibn1VxviaW8It0qw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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