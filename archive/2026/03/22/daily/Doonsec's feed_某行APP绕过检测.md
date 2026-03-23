---
title: 某行APP绕过检测
url: https://mp.weixin.qq.com/s/1o3Eb7hEYxrM5ZdgeUE-IA
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:21:26.163814
---

# 某行APP绕过检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bblvwHRSX8FHGqB3Z3JBAeHyDgBdibX1lQMpucCNqOUF8SSOYkibtzWm89f40LfhNlobH2WrTXK9k7PEicFiaiamSlz2Fgic2DN3ibfEHF5ZTgiavkI/0?wx_fmt=jpeg)

# 某行APP绕过检测

原创

企鹅王
企鹅王

yunXSecurity

![]()

在小说阅读器中沉浸阅读

最近向NoneVector师傅学习了脱壳和绕检测，来挑战一下金融行业的难度。

先通过MT管理器识别一下他的壳是啥？

![](https://mmbiz.qpic.cn/mmbiz_jpg/bblvwHRSX8HfduqrQgf68ZQVkSxKIIicv09micTVTsfGiaDXp5iaEkuDZdKxGDwZ1YDo9WfpnyAA7liaHmeu2dmcfQicFibdcgKrQV2Zy5VjnUhjGg/640?wx_fmt=jpeg)

看到是梆梆加固企业版，用魔改版frida启动一下看看怎么个事,记着改一下端口，不然很简单就被识别到了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bblvwHRSX8H1BfIejAFlVjPx5Kfo2asQ2upweBpEyyhuVTiazj1VoDzNnBtiabLnriaMQv4xJJJFMxQrWaQAQSCZ2sT93Kpb63zgIaPKYoR5t4/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bblvwHRSX8E1OXJERX4MM6fYZibIsEvlJMB4b2NBRxcR9TrQuCiaNewuTicZnXibCs71tZpR28ULfzyrcZ4ibFjmgyaOIib6NicKlr7mD7BKkrmcJY/640?wx_fmt=png)

直接检测到了，行。

纷争开始！！！！！！

先一步hook dlopen或者android\_dlopen\_ext，看看都加载了哪些栈。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bblvwHRSX8FMTLDzRKibWrLzson61Kt9vHCwVd5oke6ZlprRfOaXPuA1mt3pdb8hA3rxiaXRVUhANwIehsPicZYibiagjYhexexcWdGDqzNLJXsc/640?wx_fmt=png)

看到堆栈死在libmsaoaidsec.so，这个东西直接给他伪实现hook掉。

![](https://mmbiz.qpic.cn/mmbiz_png/bblvwHRSX8H6JfyCQxVnF5JIRzLGhjrYPeh8wC5euSppKEaOfDcqnjYrXekHhuxxLeCxDsEwYnqSqHHlyGQ5AGokdqhhDb3wLpFowhbY3rA/640?wx_fmt=png)

尝试进入成功，但是出现了一个问题app依旧崩溃，明明加载了但是又提示找不到文件，其中应该是被某些东西阻挡，想起刚才MT管理器提示的邦邦加固，查看加载二进制历史。

![](https://mmbiz.qpic.cn/mmbiz_png/bblvwHRSX8F7Z6cYIb042gfRHG4OL7xib1gay8ibA7lPmRvibDRIJOibG4MAossWGvpWCcibvhB1iaun1FvibCQqsZCohzHZ2ASOYGPP45gaM7GETI/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bblvwHRSX8GqwLB6aIlYtNc9114CkkgY2PV0Fcic8HM0ljibywGzSXMUH8fhmV4dZ5umhH8j8OJBmDeA7k8x5nbGs3Zd5w36PyKR44icaGSBHE/640?wx_fmt=png)

经典邦邦libDexHelper.so,在一开始加载，却又什么反应都没，这就很不对劲了。可能是一起开展的检测，导致我们一开始以为用魔改frida绕过了，可能是还没启用。所以邦邦的加固需要和libsaoaidsec.so一起绕。

尝试hook ptrace\_creat用来创建hoo进程。果然直接被干掉，属于一直在监听中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bblvwHRSX8EA73Ev3jTUtxaFAZT06pMOiba98fmLJZ487QGEiazMIIuSzpMnliaNoqzlqbmDlaxhumrfIvHrCzibL46ctTmS7NbDykGGVdJpnoE/640?wx_fmt=png)

我们放弃hooK ptrace\_creat，也有别的办法去hook掉对应的检测比如我们hook clone用来控制线程，这个思路也是根据 “不落”大佬的思路做的方案，通过hook clone规避掉creat的检测来结束线程。

先通过clone获取真实二进制名 与 地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bblvwHRSX8FsToeXksjEOpJUodN0gic5mYgmgKlB2PeNCgiaf1vvk6he9B3Qgfb3yLc7UrQg82fTfcLjgQXzHw7JrarRDb9IH626G5K0fOxnU/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bblvwHRSX8HkSxDDzLVkR0waPncQHGfCp5hko1Dor6iaazYXre2yDY7ILejBhXjrjiaGaibNwUVgK1Xia7f9Hsj44O2xg0Z1YlfqwLia3hTdpoKM/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bblvwHRSX8GY9kN3UEaYlTnu1kqKaliaJLsUhfEtejX9gUOodPXl96zURnQ8KMVzUKylFXQMjst3pAUX9c3Vb21pcS4uIeSDKY3YlbEQHFsI/640?wx_fmt=png)

找到libDexHelper.so创建的线程，通过patch\_func\_nop给线程全部nop掉，成功绕过。进入到APP首页时，卡住不动一到两秒后程序崩溃，结合之前的绕过libmsaoaidsec.so一起启动尝试看是否能完成hook.

![](https://mmbiz.qpic.cn/mmbiz_png/bblvwHRSX8HhyxZoJWQCab0ewMmpiavKWX4icHmicJp0x7ajpAD197Py365ZJjKZSfibbejXCOI9nlmGDkvic0IcHybXHhictWnCAKibjqHVXxBicOo/640?wx_fmt=png)

返回变化了，证明进入了libmsaoaidsec.so，按道理我们的脚本应该也绕过了这个二进制库，因为这个本身网上都有很多案例了，这时候打开jadx看包里面都有哪些lib是可能搭配libmsaoaidsec的，因为加载了这个后才崩溃。

![](https://mmbiz.qpic.cn/mmbiz_png/bblvwHRSX8FoWKicgwwT0KxGGibeatIjtLBzgqZ1FlHjAcBdSx6LvlDWFHJVkR9ZUOd0Es1BQa12ZMialW232Dic5sujLyL8zch6uLQfY8nqhCg/640?wx_fmt=png)

看到这里分析这个libmsaoaidauth.so的名称，因为带了auth应该是对libmsaoaidsec.so这个库进行了校验，返回了某个值用来验证这个库是否被替换了，到这里应该就是最后一步。直接用同样的方法空实现libmsaoaidauth.so.APP正常运行，一次越两个壳结束。

![](https://mmbiz.qpic.cn/mmbiz_png/bblvwHRSX8FP7gYuibGwmIWnmu9f2FJaXxOiayWMk6fKfeVM6q0jN90yCz1uy8ibed5vmYxEQtnHwjspBBVDJEAjHBXiaIfXLpznPq60vsibLLAs/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/300o1nTa8Dyvh7vfBcQYdqNyrFhW1QBzTicmV7A5UaibG1mxs7fOIByCgicsatE8nBREnrVlU5icBMIIia4KBKzA6zw/0?wx_fmt=png)

yunXSecurity

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/300o1nTa8Dyvh7vfBcQYdqNyrFhW1QBzTicmV7A5UaibG1mxs7fOIByCgicsatE8nBREnrVlU5icBMIIia4KBKzA6zw/0?wx_fmt=png)

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