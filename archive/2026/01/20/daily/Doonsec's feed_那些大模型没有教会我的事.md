---
title: 那些大模型没有教会我的事
url: https://mp.weixin.qq.com/s/Ej0kbDENisRUFpKb9_2vew
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:51.337639
---

# 那些大模型没有教会我的事

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LeOoxbgTFQvxs0ia85K7Eqcj4PZe6Z4YpTbGGCG9qLNYVnKV9SRribpldrhBZ7Z5DSCzgNFZ5UUiaRYDFeCkPYpjA/0?wx_fmt=jpeg)

# 那些大模型没有教会我的事

原创

MG
MG

不吃猹的瓜

![]()

在小说阅读器中沉浸阅读

又是一个多月没写公众号了，第一是因为太懒了，第二是因为最近太太太太忙了，有太多的东西需要做了。刚好最近学习了一点有趣但无用的知识，所以分享一下。前情提要，本篇文章水分极高，干货较少，请酌情观看。

#### 背景说明

最近看到了jar-analyzer配合claude skill食用的方法，自然就想到整一整自己的东西。于是研究了一下比较感兴趣的目标，一类是`SharePoint/Exchange`这类大型的`Windows`系统，另一类就是办公软件。纯没事看看，与工作无关，学会了一些大模型没有教会我的东西，可以理解为此篇文章是用于记录构建`skills`过程中遇到的一些问题的。但还是那句话，本文只是笔者一家之言，仅仅代表自己，不代表任何组织观点，有不同看法或者发现错误的朋友欢迎留言交流。

#### SharePoint/Exchange

`SharePoint/Exchange` 这类大型的`Windows`系统，补丁一般都是随着补丁日发布的。所以打补丁的方式也是一样的：

1. https://msrc.microsoft.com/update-guide/ 查看漏洞对应的补丁号
2. https://catalog.update.microsoft.com/Home.aspx 查找对应的补丁号进行下载，`SharePoint`的补丁有两种：一种是`exe`文件，比如：`sts2019-kb5002754-fullfile-x64-glb.exe`；还有一种是`cab`文件，比如：`sts-x-none_ea2ead68dcbc1abd64472f1f3998d1488e30ae94.cab`
3. 获取以上两种补丁内容的方式都是一样的，靠`7zip`解压就好了，不清楚的可以参考Jang的博客

这里以`ToolShell`为例，分析一下它们的补丁，看看是否可以通过`claude skill`跑通整个流程。但在本人实践的过程中，发现修复漏洞的`dll`竟然没有包含在`patch`中。但当打上对应的补丁以后，确实已经完成了修复，这和我五年前看`ProxyShell`时的认知完全不同（这告诉我们，要对自己感兴趣的目标持续追踪！）。

##### 解决问题

发现这个问题后，我全局搜索了`Microsoft.SharePoint.dll`这个文件，发现在`GAC`目录下有一个修复的版本，这时我很自然的怀疑微软官方会下发一些dll，而补丁包的作用只是将下发的dll拷贝至对应的文件夹中。这个论点有个很显而易见的问题，有些环境是不出网的，所以光靠下发明显不靠谱。所以在补丁包里一定含有特定格式的修复文件。启动`processmoniter`安装补丁，发现了几个有趣的事情：

1. `sts2019-kb5002754-fullfile-x64-glb.exe` 会先解压出 `sts-x-none.msp`，然后调用`msiexec`处理解压出的`msp`
2. `msiexec`会在`tmp`目录写入`Microsoft.SharePoint.dll`

继续抽丝剥茧，发现在安装补丁的时候会写入日志，进入日志发现如下记录：

![](https://mmbiz.qpic.cn/mmbiz_png/LeOoxbgTFQvxs0ia85K7Eqcj4PZe6Z4YpFicCCZluHibuJnQmb1GnKwoSqp3qrNyqkEsCbibHaU9d26OtVQNejLZicw/640?wx_fmt=png&from=appmsg)

看来是微软给对应的`dll`进行了重命名，至于为什么我也不知道，有知道的朋友可以留言告诉我！最后就是传统流程，确认了修复逻辑。

![](https://mmbiz.qpic.cn/mmbiz_png/LeOoxbgTFQvxs0ia85K7Eqcj4PZe6Z4YpibC360YmUfEUIuFEKnkernpsUdsX9s3icSicHdRPRgTbzdMQWxFnpLJ1g/640?wx_fmt=png&from=appmsg)

#### 国产办公软件

分析过比较大型二进制目标的朋友们都知道，这种目标的难点在于了解各个模块的作用。无意义的逆向等于\*\*，热衷于逆向的朋友请当我没说。日志就是这类目标很好的切入点，当然看日志的方法有很多。这里简单说一下我用的方法，无非就是动态和静态两种。以我的经验来说，还是动态简单一点，`hook`一下就好。具体就不展开说了，效果如下所示。感兴趣的读者可以自行尝试，遇到问题的话可以留言，这个可以公开，佛系回复。

![](https://mmbiz.qpic.cn/mmbiz_png/LeOoxbgTFQvxs0ia85K7Eqcj4PZe6Z4YpkCoWQPcsVj1BHNiakmGHZXrMXwmYfC4GAlcfnBSr700laKRRarX6NmQ/640?wx_fmt=png&from=appmsg)

#### 总结

回到本文标题那些大模型没有教会我的事，因为以上的两个问题都是我遍寻大模型均无果的问题。这里的大模型不仅包括各类大模型，还包括各类`Agent`。当我给出这两个问题的答案后，大模型马上也将学会这两个问题。陈词滥调不想多说了，希望读者朋友们多用大模型，善用大模型，但也不要忘记独立思考，大胆假设小心求证的人类美德，就酱~！

#### Ref

1. https://www.yuque.com/0cat/wclcea/kfp8bklrdch0hit1
2. https://testbnull.medium.com/a-quick-note-of-ms-sharepoint-net-decompiling-patch-diffing-91238bb35bf3

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LeOoxbgTFQuGziabgfiaGkrPIicYUSzvuDpsrGGdFvXDE1RCv8vATeSOYXVNtqu2MY5yicq1FR2zoVFLWELRYBpx7g/0?wx_fmt=png)

不吃猹的瓜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LeOoxbgTFQuGziabgfiaGkrPIicYUSzvuDpsrGGdFvXDE1RCv8vATeSOYXVNtqu2MY5yicq1FR2zoVFLWELRYBpx7g/0?wx_fmt=png)

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