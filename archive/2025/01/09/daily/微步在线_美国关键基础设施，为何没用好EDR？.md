---
title: 美国关键基础设施，为何没用好EDR？
url: https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650182966&idx=1&sn=bb3a511b87619c30ef8ccccbae98a24e&chksm=f4486e8ac33fe79ccaddcc2df6095cb5bad5e9c5eb058129af70ee4394265ff6ec0b7f1044a3&scene=58&subscene=0#rd
source: 微步在线
date: 2025-01-09
fetch_date: 2025-10-06T20:11:24.093870
---

# 美国关键基础设施，为何没用好EDR？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3ia8P3JE20M1dDcUttdjXrUKdK2zYrVVmibcsyribVDO1FZDbQHRnKuQOmQ/0?wx_fmt=jpeg)

# 美国关键基础设施，为何没用好EDR？

原创

ThreatBook

微步在线

![](https://mmbiz.qpic.cn/mmbiz_gif/Yv6ic9zgr5hRYwmkFFVSsK0fQGJBGqwl6iaBoFgqTpPricWCuX7uIb4Rj7eibLo3ibOiaOtqo7vXEnibKhxuInrceOoibg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

前不久，美国网络安全和基础设施安全局 （CISA），对美国关键基础设施行业某组织进行了一次红队演练，以此评估网络安全检测和响应能力。

在前两篇文章中，小编分别介绍了红队的Nday漏洞利用和和针对域控的渗透，详见《[美国顶级红队演练，只用了一个Nday？](https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650182736&idx=1&sn=114de58c87950ec9eac7ccc24b290958&scene=21#wechat_redirect)》、《[美国红队演练，靠什么拿下域控？](https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650182785&idx=1&sn=9ca2c5e535738a6b48dae49bdf05bd0a&scene=21#wechat_redirect)》。

第三篇文章小编将结合攻防双方在办公网的对抗，解读哪些要素应该在EDR的使用过程中应被重点关注，希望能给到大家参考。

**检测免杀样本，先看EDR检出哪些异常行为**

随着免杀成为标配，使用EDR检测恶意文件执行后的特定行为，已经是办公网安全不可替代的手段。

**在本次红队演练中，红队向防守方单位的13名员工投递了钓鱼邮件，邮件网关和杀毒软件均拦截失败，但钓鱼样本被EDR成功检出**。尽管CISA并未披露此次钓鱼样本的细节，但多数情况下防守方需要重点关注以下异常行为：

1. DLL劫持，例如在指定路径创建恶意DLL，利用合法程序加载该DLL；

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3iaOb8tLnibIB1KtI1cicIuWMbJ5iagVRqnmFw9Cicgn7oeHxIDKIkgnfgnWQ/640?wx_fmt=png&from=appmsg)

2. 创建内存Payload，绕过基于磁盘的检测；

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3iacVKZibtzRSXvHNpSb9alCr0R0HEicd6RMdoTN4KfdM5BbA9Zmx6TdGlw/640?wx_fmt=png&from=appmsg)

3. 注册表修改，实现持久化利用。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3iagVrL2ib1J0btb7KicZF2obRibZUEucSpJp79sicJL9qujpDOMNr0nu6Oaw/640?wx_fmt=png&from=appmsg)

这些异常行为的采集与分析，是EDR检出免杀样本的基础与核心能力，需要防守方首先关注。

**内存、横移等高级行为，更需要重点关注**

只关注基础行为是远远不够的。如果忽略了横向移动、内存等高级行为，很可能会漏掉部分入侵活动；即便发现了木马活动的蛛丝马迹，也会因为处处断链而难以溯源。

**此次红队演练中，尽管防守方EDR成功检出了钓鱼样本，但在红队转变策略并攻陷域控后，防守方对于远程创建计划任务这一横向移动行为，并未给予足够的关注。**

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3iaJibO0a6TX4iaZIS9vhSJjicpmvjicicUEJibUtoHDaicPloE2TFRJEGx25r1A/640?wx_fmt=png&from=appmsg)

红队具体入侵过程如下：

1. 红队利用SCCM服务器远程创建计划任务，横移至管理员工作站；
2. 在指定路径下创建恶意DLL，与域内某合法计划任务进行关联；
3. 为规避文件检测，红队将DLL膨胀到100MB以上，超过了上传（如沙箱）的阈值；
4. 利用合法计划任务加载恶意DLL，并通过域前置出网。

由于漏掉了前序横移行为，导致产生断链。如果是防守方视角下，这大概率就是一个合法的DLL加载过程。

值得注意的是，类似容易发生断链的场景还有很多，结合微步OneSEC长期高级威胁对抗经验，需要重点关注的高级行为，包括但不限于以下几种。

**远程服务创建**，攻击者可利用RPC或者Powershell，在远程计算机上创建服务，只关注基础进程行为则无法看到此类行为。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3iab6Sq78XctrX10FawFyXZK2luvjNG2pmN1L1y0qNxzCZvpe3pricO3pA/640?wx_fmt=png&from=appmsg)

图：微步OneSEC检测到远程创建服务

**利用WMI在远程机器上创建进程**，通常也被应用于横向移动。如果只关注普通进程行为，则在目标机器上只能看到wmic.exe执行的动作，看不到背后是谁在调用WMI。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3iaXB1y5cMLOh6OHs9QCoK979vquOicwQmaQwEL1CHhCCsB29BrkewNkLw/640?wx_fmt=png&from=appmsg)

图：OneSEC检测到进程A通过WMI远程创建进程B

**远程线程创建**，将恶意DLL（或Shellcode）注入到一个合法进程中执行，如果只关注基础进程行为，很多时候只能看到被注入进程出现异常，看不到发起注入的进程。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3iabG6mYGnic0lTHBkdmoiae5fTOwH6Dtk2utxAbKF9KxsVOnNHhXOzhvXg/640?wx_fmt=png&from=appmsg)

图：OneSEC检测到异常远程线程创建

**进程挖空**，将一个合法进程的里所有的代码挖空并换成恶意代码。同样，EDR也容易漏掉而发起这个挖空操作的进程。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRAQTqXSaC78I8slR5Hlr3ialQWOgZCzYPiaJdO735hnmbib7Z7Afm2du0HUg1tyCgVscmOktpmfIBzQ/640?wx_fmt=png&from=appmsg)

图：OneSEC检测到某进程在执行挖空

####

**安装率和基于EDR的响应流程也是关键要素**

除了关注EDR自身检测能力之外，尽可能提高EDR安装率，完善基于EDR的运营和应急响应流程，也是提升EDR使用效果的关键要素。但这两方面，此次演练中防守方做得都不够好。

**在安装率方面，防守方部分老旧机器没有安装EDR**，这可能是性能或者兼容性问题所致，红队在这些机器上的访问权限持续到了演练结束。

**在应急响应流程方面，EDR成功检出并自动处置了红队的钓鱼样本，但防守方安全团队并没有查看告警和处置详情。**对于EDR发现的安全事件，正确的做法应当结合原始日志、威胁情报上下文以及其他安全产品的数据，对该事件进行综合研判，这样才能最大化发挥EDR的使用效果。

· END ·

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSA5A4iaspRVClFku4KVwkOUriclTaohLibE2oQKMTrQ8hvSFFHevq88eibd7mstuZbeNLm5U1tPJT3xQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

微步在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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