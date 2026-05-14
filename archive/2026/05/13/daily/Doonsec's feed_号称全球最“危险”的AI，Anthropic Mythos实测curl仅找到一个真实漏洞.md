---
title: 号称全球最“危险”的AI，Anthropic Mythos实测curl仅找到一个真实漏洞
url: https://mp.weixin.qq.com/s/LghjpqnG00xbGXwXKbrXIw
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:44:11.706429
---

# 号称全球最“危险”的AI，Anthropic Mythos实测curl仅找到一个真实漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3fdgM4XtVwopfyVDXsWxbWRPibGrGL5rIFX4dPxVFLMYYcfWwt7MJDQchEY8jvdBI8zj77ibtEibyViaRiaWOia7lG7tc8wt3MDyKibE/0?wx_fmt=jpeg)

# 号称全球最“危险”的AI，Anthropic Mythos实测curl仅找到一个真实漏洞

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX38R1qou8FjXgwUNhBTWrZYB70VBVA7ECCn1mKiaACx3GZncTKdicULRdjGsyiaIibI1ke3ibGH65jnv9qP6yQIicVcpn2IlSn0UPM58/640?wx_fmt=png&from=appmsg)

今年四月，Anthropic公司高调发布新型AI模型Mythos，宣称其代码漏洞检测能力"危险地强大"。出于安全考虑，该公司决定暂不向公众开放，仅向少数大型机构提供访问权限，使其能优先修复关键漏洞。

业界对此反应强烈，传闻该模型能在数周内发现数千个0Day漏洞，引发对软件安全现状的质疑。这一话题迅速成为科技圈热点。

curl创始人Daniel Stenberg通过Linux基金会的Alpha Omega项目，间接获得了Mythos对curl代码库的分析报告。结果显示，该模型扫描了17.6万行C代码后，自信地宣称发现五个"已确认安全漏洞"。

Stenberg指出："curl代码量相当于《战争与和平》英文版的1.12倍。AI单方面宣称漏洞'已确认'的说法颇具趣味性。经团队数小时核查，五个问题中仅一个真实漏洞，其余三个是API文档已注明的误报，第四个仅为普通bug。"

**Part01**

## ****实际效果与宣传存在落差****

最终确认的低危漏洞计划在curl 8.21.0版本中修复。Stenberg认为围绕Mythos的炒作更像营销行为："现有证据表明，该模型在发现问题方面并未展现出超越既有工具的特殊优势。"

curl作为全球使用最广泛的数据传输库（部署量超200亿），其代码库经过OSS-Fuzz、Coverity等多轮审计。在Mythos之前，Zeropath等AI工具已发现200-300个缺陷，包括十余个CVE漏洞。Mythos的检测时机较晚，覆盖范围有限。

**Part02**

## ****技术价值在于检测效率****

Mozilla案例显示，Mythos在Firefox中发现270余个漏洞，其价值主要体现在检测速度——缩短了漏洞发现与修复的时间窗口。但Mozilla强调，这些漏洞同样能被顶尖人工审计发现。

Stenberg肯定AI代码分析工具的进步："新一代AI工具在检测源代码安全缺陷方面显著优于传统分析器。"但他指出，至少对curl而言，Mythos尚未展现出实质性突破。

由于Stenberg仅通过第三方报告评估Mythos，其结论存在局限性。虽然该AI在高度审计的curl代码中仅发现一个低危漏洞，但这既不能证实行业炒作，也不应全盘否定技术潜力。当前测试表明，AI漏洞研究具备实用价值，但所谓"革命性能力"的宣称仍显夸大。

Stenberg总结道："任何尚未使用AI工具扫描源代码的项目，都可能通过新一代工具发现大量缺陷。"

**参考来源：**

The world’s most “Dangerous” AI, Anthropic’s Mythos, found only one flaw in curl

https://securityaffairs.com/192029/hacking/the-worlds-most-dangerous-ai-anthropics-mythos-found-only-one-flaw-in-curl.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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