---
title: 【支付漏洞】金额溢出导致的0元购-网络安全
url: https://mp.weixin.qq.com/s/JAHknlm0Vg6xu_0Be-zd4A
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:28:00.801109
---

# 【支付漏洞】金额溢出导致的0元购-网络安全

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SgRVa0DmgbEunoInXqBEDd6pVvNK9KZyFUK2scjmmvVM1jwEBFNZ6utblZHUjLhoOuAdX7fWUV3KgMcPniafGficiakx4ucR7I3Qk8eH6ufRRs/0?wx_fmt=jpeg)

# 【支付漏洞】金额溢出导致的0元购-网络安全

原创

無名
無名

无名的安全小屋

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SgRVa0DmgbFeSJg8yx47QiccEFuC4G2iaSopuzY20T8FI8vtMeX7CeZNhSOP6ia7JcnRCoLUTicFVqLveEY9KOmu7HVzkFD8IpcQR0IMdvyibORI/640?wx_fmt=png)

**玄域Web/App靶场学习平台**

01

**免责声明**

本次所有操作均在玄域靶场内进行，大家在生活中也务必严格遵守《网络安全法》！

玄域靶场：www.shangsec.com

目前，平台已建成**web**渗透靶场、**安卓App**渗透靶场、**苹果App**渗透靶场、**实战漏洞报告**板块、**面试刷题**板块、**网安学习**板块等等。

除CTF系列关卡环境外，其余所有靶场环境均改编自企业真实漏洞案例！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SgRVa0DmgbETYmq9cibKmghQEHC2PtM8ItUXA5osB1ib6Iq5iaTVqD3EoyiaX1oQ60yN0qYkk1iaDgoGtC7gAYGn1rfzgADoLv2YZ0rarIm3iaGhg/640?wx_fmt=png)

02

**前置知识**

在实际开发中，因为这个业务功能点可能只需要整数，那么开发人员可能就会通过一个整数类型的变量去存储我们的值。

而对于后端开发中最常用的Java也好，还是 Node.js 也好，它们的整型大小都是有范围的。

对于Java来讲int类型的最大值为2147483647，而对于JS来讲，它的最大值是 9007199254740991

下面是代码演示

```
publicclassMain {    publicstaticvoidmain(String[] args){        int maxValue = 2147483647;        int overflowValue = maxValue*2;        System.out.println(overflowValue);     }}
```

可以看到，最后的输出结果确是-2

![](https://mmbiz.qpic.cn/mmbiz_png/SgRVa0DmgbHBPCb1Qf7iaKiaIbntgNXiagqES9I3kpwK0S5qbkYeghmp5OM4a4wm35SpWxOrupNwTDV9iaziblYW2PzFVp33Yc9fOxoDVY6uCpN4/640?wx_fmt=png)

通过上面的代码演示，我们可以知道存在整数溢出这么一个知识点。

但是，它是负数，一般情况下，特别是在这个支付业务中，当你的总金额为负数时，后端肯定会异常处理的，你也是没办法0元或者低价购买这个商品的。

经过进一步尝试，可以发现，目标的单价金额只能修改为比原金额大的一个数。

而优惠券金额只能修改为比原金额小的一个数，甚至是负数，这个逻辑乍一看好像没有任何问题。

毕竟你把单价修改贵了，把优惠券金额修改小了，你付款的时候反而比正常买要更贵了。

这对于厂商来讲是好事，这肯定不是我们想要的一个结果，那么我们怎样结合整数溢出来进行组合利用呢。

03

**实操演示**

**玄域靶场支付漏洞-08环境**

![](https://mmbiz.qpic.cn/mmbiz_png/SgRVa0DmgbFJgfS1oPFkODJSn7SCe2tjQnbyv82BmjQURjrvJvnQKib2XLZQcd0mcrialfoXXHCUkBJSMd4nyiceQ2fLjfGRcxPuP3ib0wnWqso/640?wx_fmt=png)

来到玄域靶场-支付漏洞08环境，选择优惠券后，点击购买后，进行数据包的拦截。

修改数据包如下即可，这样我们就可以结合整数溢出来达到我们想要的一个结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SgRVa0DmgbFKslp97uSnMI9VgtcicwDltY4sJBm8kvhgE5mjnwWqGBjZjjyMuUDibOiaIyuXpahriaN7dSpRaLXvV45XeL5xlOGiaibtWKcUR2zzg/640?wx_fmt=png)

然后放行数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SgRVa0DmgbHGG31NIJSW6RBGp5TDVdiaicCzJWUbYoTNtyYMRC6AIkLYUdj67xhRhhMFBpStOQMYOL6PkAqWan7C91BTI4QevxbEjSSyRUWpM/640?wx_fmt=png)

04

**学习交流qun**

**工具包、资料**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SgRVa0DmgbEicD9hgwJfGtTHuRKJ68icFAxXtm9PIWDggBIIPtHjpzWOW6x9DlruQ0kWyVVv2L317dK2wW68vKIV7doOjOMF12mzibAMkYVuEU/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BZbILNBpkriaqkcb3mVsibPBFZhJmNibp2obghff1gssSjzh2Wz3Rog66ia3IPuopvpLYxeQAP7g2o2icEv5ibZ2Vo4g/0?wx_fmt=png)

无名的安全小屋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BZbILNBpkriaqkcb3mVsibPBFZhJmNibp2obghff1gssSjzh2Wz3Rog66ia3IPuopvpLYxeQAP7g2o2icEv5ibZ2Vo4g/0?wx_fmt=png)

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