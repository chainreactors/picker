---
title: 安卓逆向入门学习-2
url: https://mp.weixin.qq.com/s/QgazVQC661WfnXgrg9jujw
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:51:26.133208
---

# 安卓逆向入门学习-2

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/94kIPh1QgiaC8kFZ5bgCwNjHsk7utYsI8ps5JvvgjVhiaJlIAu4mweH81d0qpoYZU2zlGeZ5C2j3FsCOY612hIBNmQbRyJyWNfia4BngpoVOzY/0?wx_fmt=jpeg)

# 安卓逆向入门学习-2

朝阳
朝阳

Sec朝阳

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 1、JVM、Dalvik、ART

JVM 是 JAVA 虚拟机，运行 JAVA 字节码程序。

Dalvik 是 Google 为 Android 设计的虚拟机，Dalvik 有专属的文件执行格式 dex。

Art （Android Runtime）相当于 Dalvik 的升级版，本质与 Dalvik 无异。

### 2、smali 及其语法

smali 是 Dalvik 的寄存器语言，smali 代码是 dex 反编译而来的。

其实和汇编语言很相似。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaC3LNUFWcUyyZLl5J3eBoeg7pjCWbdbWYeOEbQYpl88E6aLnyBuOHPtAcNNhFnnkpsDL4dibeRoX01R2jnFTGCgH6OmDNCsNuIc/640?wx_fmt=png&from=appmsg)

到手一个程序，要收集硬币，并且完成一键三连，我们点击一键三连会提示让我们充值大会员。

我们这里记住他的关键词，大会员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDboQNzicEGYDicswEXBQC5OOy9G4HHzENvMFNHDePtNfyJSfo2FYnO7ib0C9CG2bqAiaXGjxEgErnCojtc5kPkpS08jxAweHfNLOQ/640?wx_fmt=png&from=appmsg)

看到了关键字了，并且他有两条路径，根据逆向经验，肯定是要把一键三连后面跳转的函数改为当前已经是大会员。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaBSyKpWj4iaFjXdicZjNxfqkaficFUWMRiakng3FiagpAACEC0FGgHmExwRa1SvDIAdGjCGQGEYibswMbLDsiaEQQEjIJIjOH6ZfU5hj8/640?wx_fmt=png&from=appmsg)找到了，其实这里就是一个非常简单的点，就是结果跳转，我可以理解为这里是进行 Patch 的操作。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaAnvVQWDjkkqu6Fqej5vj2M2pVzdQicMc6XuZfslicmMBUlibictdrhpzeqIxfbCC0GMCK1qwOuNWlOAykomEvs5udPoXQX3bU7hB4/640?wx_fmt=png&from=appmsg)

在这里就是 Smali 代码了，我有种看伪代码的感觉。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaD7WWu0rsuiaw3yEuzg9YbB88qzwtG46Vwjr9vFbsSMlDmrPPFH23ibFoYs3zXQqQLBIH1JpweUGNGEykvtMvMGMFbj5eerXVTFY/640?wx_fmt=png&from=appmsg)

在这里能看到方法名，并且要前有对应上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBr7C6Bn2vKxrjA2SZVWibwDgbXmL5UkbJ0EUD0EibgWicybUASnrlNDPwBODm3gO2yVvymjhibkVf6zX13b5HIk9khuAAf1mRrNzU/640?wx_fmt=png&from=appmsg)

都没问题就继续往下走。

```
.method private static final onCreate$lambda-2(Lkotlin/jvm/internal/Ref$IntRef;Lcom/zj/wuaipojie/ui/ChallengeSecond;Landroid/widget/ImageView;Landroid/widget/ImageView;Landroid/widget/ImageView;Landroid/view/View;)Z //这里是方法的参数，是布尔类型。
    .registers 7 //寄存器数量
//这是一个私有的、静态的不可修改的方法。 onCreate$lambda-2 是方法名，后面跟着的是参数。
    .line 33 //代码所在行数。
    iget p0, p0, Lkotlin/jvm/internal/Ref$IntRef;->element:I

    const/4 p5, 0x1

    const/16 v0, 0xa

    if-ge p0, v0, :cond_15

    .line 34
    move-object p0, p1

    check-cast p0, Landroid/content/Context;

    const-string v0, "\u8bf7\u5148\u83b7\u53d610\u4e2a\u786c\u5e01\u54e6"

    check-cast v0, Ljava/lang/CharSequence;

    invoke-static {p0, v0, p5}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p0

    invoke-virtual {p0}, Landroid/widget/Toast;->show()V

    .line 36
    :cond_15
    invoke-virtual {p1}, Lcom/zj/wuaipojie/ui/ChallengeSecond;->isvip()Z

    move-result p0

    if-eqz p0, :cond_43

    .line 37
    check-cast p1, Landroid/content/Context;

    const-string p0, "\u5f53\u524d\u5df2\u7ecf\u662f\u5927\u4f1a\u5458\u4e86\u54e6\uff01"

    check-cast p0, Ljava/lang/CharSequence;

    invoke-static {p1, p0, p5}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p0

    invoke-virtual {p0}, Landroid/widget/Toast;->show()V

    const p0, 0x7f0d0018

    .line 38
    invoke-virtual {p2, p0}, Landroid/widget/ImageView;->setImageResource(I)V

    const p0, 0x7f0d0008

    .line 39
    invoke-virtual {p3, p0}, Landroid/widget/ImageView;->setImageResource(I)V

    const p0, 0x7f0d000a

    .line 40
    invoke-virtual {p4, p0}, Landroid/widget/ImageView;->setImageResource(I)V

    .line 41
    sget-object p0, Lcom/zj/wuaipojie/util/SPUtils;->INSTANCE:Lcom/zj/wuaipojie/util/SPUtils;

    const/4 p2, 0x2

    const-string p3, "level"

    invoke-virtual {p0, p1, p3, p2}, Lcom/zj/wuaipojie/util/SPUtils;->saveInt(Landroid/content/Context;Ljava/lang/String;I)V

    goto :goto_50

    .line 44
    :cond_43
    check-cast p1, Landroid/content/Context;

    const-string p0, "\u8bf7\u5148\u5145\u503c\u5927\u4f1a\u5458\u54e6\uff01"

    check-cast p0, Ljava/lang/CharSequence;

    invoke-static {p1, p0, p5}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p0

    invoke-virtual {p0}, Landroid/widget/Toast;->show()V

    :goto_50
    return p5
.end method
```

我们就把这段代码拿出来，逐行分析一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAe8LDzxialQUPHKC0q7NzxicMm0QKQiaEXRstNaBCdcSTx6nLXu4BNSwaxUwsPBUMOIV9C3DMxKPObt0QHdJiakjKCdZ5GetfbYnM/640?wx_fmt=png&from=appmsg)

分析可以对照表格，当然现在是 2026 年，可以 AI 一把梭哈，但最好还是懂一点原理。

在 smali 中所有操作都必须经过寄存器来进行，本地寄存器用 v 开头数字结尾的符号表示，参数寄存器用 p 开头，在非 static 函数中，p0 代指 this，p1 代表函数的第一个参数，p2 是第二个。其实 p0 可以理解为定位了了。

static 函数中 p0 才对应对一个参数。（JAVA 的 static 方法没有 this 方法）

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDuRWPbYyOI00qJw9nkWQOxU5Zic7orEib3pDTN97hRTdI8EXqgBBg305Dn0iaibpA64WSxIgUaZWntCrCRzroXhAW630HPSklPGfw/640?wx_fmt=png&from=appmsg)

我们直接关注核心点，果然和我们之前的判断如出一辙，这就是进行判定，那其实我们就找到判定是否是大会员的判定点，进行修改，比如说把 if-ge 改为 if-le,或者把 if-xx 的改为直接跳转 goto xxx 即可。

那我们自己找一下判断点即可了啊，就很简单了，逆向好像都是一家的，太相似了。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDeQnDDvlPYfpgoGTN7qYtpGJ1VaAZy5ibDhZZG01P8FLuznhxQnufrXgYCmUr7J1RcPB0ay3AVRYnoH78PXjWlKHz21mM6icTug/640?wx_fmt=png&from=appmsg)

就很典型了，那就是给参数 p5 赋值 1，给 v0 寄存器 复制 16。

然后下面，如果 p0 的值大于等于 v0 则跳转到 cond\_15。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDa2AZxibicrq9M84scLSLIWI9paU4CYO47M9X671FXkWWrsR8wgW3qXNE0KusaGZfB13hHAVLpSu33jMktLQdFiaWyibZ4jVo07MU/640?wx_fmt=png&from=appmsg)

追踪一下 cond\_15,我们翻译一下。

这段翻译成大白话，这里 invoke-vitual 函数就是派个人去问问程序，我们是不是 vip(调用 isvip() 方法)。

move-result p0,这里参数 p0 是存放结果，看返回值是 True 还是 False。

接下来一个 if-eqz 判断，就是如果 p0 这个参数为等于 0，我们跳转到 cond\_43,如果不是继续执行。

那其实我们就应该去看 isvip() 的执行逻辑，看看他判断返回值什么意思，按照这个修改即可。

这里为什么去看 isvip() 内部逻辑是更优选择，因为改了调用处的 if-eqz 虽然快，但是改 isvip() 可以全局生效，一个 App 会有多个地方调用，比如去广告、下载速度、进入 vip 专区。隐藏性也会更好，App 会做逻辑校验，只改一处 if-nez，可能会导致程序不一致，当然这个要看具体逻辑程序，我们先自行分析，再看教程。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaB5S58rppgdzY1Hg94PUgGnbTdfjwCHOWibokxsNjPhwp6iazOe2kFWryCUAygx5o4j1GezBiaZeVRObck9nicctRZ8SKYiaCrK4UKE/640?wx_fmt=png&from=appmsg)

这段我们分析一下，明显能看到一点啊，就是不管我们输入什么，这里的 const/4 v0, 0x0 都是 0 啊，也就是说我们做啥他都不让我们通过。这就是问题所在。其实这里把他改为 const/4 v0,0x1 就好了，本人理解，但是第一次做安卓逆向，不知道会不会出问题，我感觉就是 Patch 一下，然后重新打包校验签名，但有个问题，这个程序就不是原来的程序了，我这里说的有点绕。

但其实这里我们漏掉了一点，就是没有去看是否满足 10 个硬币的逻辑点，我们回去看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAOY6zmfzJtIjfQt37hibraJQJXtPfLtha1rNe9k0cDtPeSqAriaTcUVQVM80WFQrHe8f5TBXHLPnZGHRy5zyaaSf4F0aT1uTccc/640?wx_fmt=png&from=appmsg)其实是在这里，const-string p0 这里，其实是判断我们是否获取了 10 个硬币，这里的 string 就是字符串，我们可以去伪代码里面去找。![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCOWn4Z07PibaDgISjDibG7PFvYjcnrziayblRib3mt1vuUgPWrODXImWrFyLeVxXEsdBGm4xrdkHQCrwMuibkd7ysJT6dz4OFwW6AU/640?wx_fmt=png&from=appmsg)

在这里个位置。其实我们也能看伪代码去理解，就是当我们获取了 10 个硬币后，这是大前提，我们会进入到第二个判断点，是否是大会员，也就是想办法进入到第二个 if 中的逻辑去。

所以这个逻辑就是死的，不修改我们无法通关。

这里 . method 是一个方法的开头，.end method 是一个方法的结束。

那么这里我们就找出了三种修改方案：

修改判断

强制跳转

修改寄存器的值

可以说是最简单的方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAIR4f97vHhvibHzr5lAiaDMFWbFIITUSWlqw3zTHkUT20sV3YWZha7cTfr7pRv57KibkdDwPqPQ8uGYv7Gv8JCwG7FXB3UTmaPTs/640?wx_fmt=png&from=appmsg)

这里把 if-ge 改为 if-le，这里是硬币数量的判定。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCrhe8W14ApF5K7LTHvtTgv2kA2rtggh7SW0G5D2aQHqPsblMOHa9NbK611OfXTCmlxcdAeHxJD18A5iaMCdrzuDhFBPXRrENEk/640?wx_fmt=png&from=appmsg)

然后这里又判断我们是否是 vip 非常简单了，把 if-eqz 改为 if-nez 即可。

或者这里我们注释掉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDpkt59CKKPvmOvDcY4RtibIPDIzQ1nCvSA2zttia7zuP4yGOGlXjibQ7H72kgAnrTxiagyEiaVaczXmNwd84xLsiaPqr1iaBsJjo97KQ/640?wx_fmt=png&from=appmsg)

这是修改判断，注释方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDfSfNyBUY0TWFEpDRNFmm6vV2bVKppnqiartVUsj0ibQMgpGD5tECKR8KkW8icl1HzzuiatZgpyZ4IGAia88PnJiaTHbd8gkgFGqiaoo/640?wx_fmt=png&from=appmsg)

这里改为 0 也一样的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCibQx0cHF1aKVKvM1ibaLC2eco4F6uYhF4Kiclhicibc7lauDpXWfgiaonbshmTPick4CgV3Vp...