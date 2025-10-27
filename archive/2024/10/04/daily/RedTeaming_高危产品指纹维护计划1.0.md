---
title: 高危产品指纹维护计划1.0
url: https://mp.weixin.qq.com/s?__biz=MzUyMDgzMDMyMg==&mid=2247484465&idx=1&sn=80feb4c98ed2b33c50b118eea562ceac&chksm=f9e5282cce92a13a8273937e507a5969aad19fd21c774e582e355b116600c241dfe237f455bc&scene=58&subscene=0#rd
source: RedTeaming
date: 2024-10-04
fetch_date: 2025-10-06T18:51:15.560798
---

# 高危产品指纹维护计划1.0

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/D8s0oRfyswl6Uibw7fYZV5GUwNNWFiaEps6u8p472WLKTje5AEMppGGCZuRS03S2YhQVwk5WX3ghI2lmRLicV2FXA/0?wx_fmt=jpeg)

# 高危产品指纹维护计划1.0

原创

XTeam

RedTeaming

大家好，为了更好地识别外部资产中的高优先级产品，进行安全测试以及高危漏洞发现和修复，我们推出了高危产品指纹维护计划 1.0。

一、计划目标

1. 覆盖国内外常见的高优先级产品
2. 高质量的产品指纹
3. 针对性的POC
4. 改造nuclei,让其更智能化

```
简单来说,扫描流程为以下步骤:1. 先使用指定tag指纹集扫描目标2. 根据tag筛选poc进行测试3. 上面的功能nuclei官方已经实现,我的优化点是还支持一个默认规则集的扫描,不论是否识别到指纹,会强制使用用户指定的poc进行扫描.eg:不管有没有识别到组件是不是泛微,都会使用指定的插件id列表进行扫描，比如扫描备份文件,信息泄露等。4. 上传扫描结果
```

代码在:https://github.com/Marshal-EASM/nuclei/tree/wing/dev

```
实际使用飞书文档有更多介绍https://c6k50tuyg6.feishu.cn/wiki/UcN2wSI0qieGdvkN1WZcQzuenQh?from=from_copylink
```

二、参与条件

为了确保计划的有效性和广泛参与性，我们设定了以下参与条件：参与者需要按照指定要求贡献 10 条规则，即可共享全部规则，为了防止规则被滥用，人数达到30人后将不再收取新成员。目前的指纹数量是**118**条。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswl6Uibw7fYZV5GUwNNWFiaEpsSfyvcAGAAlsjcuTgOzMYRJdY6mic6iarS0tsqpqaC5gFXOnqNmJXicWsg/640?wx_fmt=png&from=appmsg)

想加入的同学公众号私聊我即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/D8s0oRfyswl6Uibw7fYZV5GUwNNWFiaEpsTTKJnhAL4GtPNTmvMsccFMsT029sIkec3WfT3kDDIVARsWGAGJM4MQ/640?wx_fmt=png&from=appmsg)

三、后续计划

**指纹规则差不多之后，再开始POC共享计划!**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/D8s0oRfyswn6RH4bWic2xc6qtDPjmey9kwyvRiagHA1lzlAM9uf9aic4K6NJH0JeoXQZ1Hpx7pWJaQibUl4ZulgIEg/0?wx_fmt=png)

RedTeaming

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/D8s0oRfyswn6RH4bWic2xc6qtDPjmey9kwyvRiagHA1lzlAM9uf9aic4K6NJH0JeoXQZ1Hpx7pWJaQibUl4ZulgIEg/0?wx_fmt=png)

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