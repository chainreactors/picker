---
title: 【漏洞预警】大华智慧园区综合管理平台未授权访问漏洞
url: https://mp.weixin.qq.com/s/ZIlyS54lU2bUWaB3Y_Yo3Q
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:02:50.269691
---

# 【漏洞预警】大华智慧园区综合管理平台未授权访问漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2iarPRAzsofZicmuShVEONKAu31mpTxyg1CqxO8bcbvGIw28fkrySKB6AXqicPSXKnW4DpVrEPoN2KRicbCWnvFrYmqBMtF41zP5Gfa872qmjMU/0?wx_fmt=jpeg)

# 【漏洞预警】大华智慧园区综合管理平台未授权访问漏洞

如棠安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> ❝
>
> **「此公众号所分享的网络安全知识、信息及工具仅供学习和研究使用，不得用于非法活动。此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他！！！」****「如有内容侵权，请联系我们删除处理。谢谢合作！！！」**
>
> ❞

#

# 漏洞介绍

![](https://mmbiz.qpic.cn/mmbiz_png/2iarPRAzsofb9kxCibSldzzo4AlJLIhhgmq2pzTGgYEQOj220R0ibF1fO1Lic76PRGdTE7As0T1E7VBDnTvZt7gnUGJliblibmJicERx0LLuvfia34o/640?wx_fmt=png&from=appmsg)

# 资产测绘

* **「Hunter」**

> ❝
>
> web.body="智慧园区综合管理平台"
>
> ❞❞

# 漏洞复现

**「1、构造数据包」**

**访问/CardSolution/XXXXXXXXXXXXXrol.jsp     回复20260618获取完整POC**

![](https://mmbiz.qpic.cn/mmbiz_png/2iarPRAzsofYnG7n4nE4VLpeBtgFCXz32OMvtgAAFibruCSOter8jYH3gzibHSFjnEvnXmY3DzkibGBYnEh1Aj29kgHKLI006KBaOB2eYO52Xuc/640?wx_fmt=png&from=appmsg)

危害：可远程控制门禁开关，且api接口泄露可利用。

![](https://mmbiz.qpic.cn/mmbiz_png/2iarPRAzsofb6Jib2e97HvXsVA8xGh0Fslt7N8E9ZibV1pE9uMlP4iaicXTacCg6KAtu2Hib8Yx8gibH6tvV8c1lyiaoic50UKhpYyhOR52AFFVgyBEU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/2iarPRAzsofZxWMkpfeicMb84vIGiczumJPHZkT2xWCCrLmmmXwRPbKyxUibUWbuibgic21ZicictJkCZMH27rNFPicuJ35a5WAREZkN683lpzVrBXibM/640?wx_fmt=png&from=appmsg)

#

# 修复方案

> ❝
>
> * 官方已发布安全补丁，建议联系厂商打补丁或升级版本。
> * 引入Web应用防火墙防护，配置接口拦截策略。
>
> ❞

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TD3MkpUYahpeu2xCgI5UbtPl6fXqriaiao04pian96mbv1HuXDKRO3lEa1aU21f32L0rFysqkwpqqocJWbzngReNg/0?wx_fmt=png)

如棠安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TD3MkpUYahpeu2xCgI5UbtPl6fXqriaiao04pian96mbv1HuXDKRO3lEa1aU21f32L0rFysqkwpqqocJWbzngReNg/0?wx_fmt=png)

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