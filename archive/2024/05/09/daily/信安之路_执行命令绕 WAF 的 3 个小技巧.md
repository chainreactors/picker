---
title: 执行命令绕 WAF 的 3 个小技巧
url: https://mp.weixin.qq.com/s?__biz=MzI5MDQ2NjExOQ==&mid=2247499347&idx=1&sn=897aff6aa0c5a55d71520822a7b234b0&chksm=ec1dce7bdb6a476d806203d1e6e3811855a30ba9640deea89be717309bcf332aff1cc64d7f24&scene=58&subscene=0#rd
source: 信安之路
date: 2024-05-09
fetch_date: 2025-10-06T17:16:49.162640
---

# 执行命令绕 WAF 的 3 个小技巧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sGfPWsuKAfeExVlic1nRwIRwBvJRSsYvJjlCknjic5CbB1hpOh1ibnF1bvq9MtHzianEgd1GibibHhhmb5VqAQ8KPHuQ/0?wx_fmt=jpeg)

# 执行命令绕 WAF 的 3 个小技巧

原创

xazlsec

信安之路

WAF 的全称为 Web Application Firewall，顾名思义 WAF 是一款针对 web 端的防火墙产品。通过对 HTTP(S) 请求进行检测，识别并阻断 SQL 注入、跨站脚本攻击、网页木马上传、命令/代码注入、文件包含、敏感文件访问、第三方应用漏洞攻击、CC 攻击、恶意爬虫扫描、跨站请求伪造等攻击，保护 Web 服务安全稳定。

随着免费开源 WAF 的贡献，越来越多的网站拥有了 WAF 的能力，而在实际的测试过程中，遇到 WAF 的几率大大增加，所以绕 WAF 成了渗透测试人员不得不做的事儿，WAF 的检测方式，通常使用正则、关键词等方式匹配数据包中的内容，从而判断是否需要被拦截，而这种规则需要经常更新，不然会存在很多被绕过的情况。

今天要分享的几个小技巧是利用 linux 系统的特性，通过变换命令的形式来绕过 WAF 的黑名单规则。

1、通过在命令中插入未初始化的变量来绕过正则，如图

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeExVlic1nRwIRwBvJRSsYvJL89wnUym7BoicKCA1SmgfAg5aV176KbiaXnUXwPuoxgo85giaPx8fWdhg/640?wx_fmt=png&from=appmsg)

2、使用问号作为占位符，组合插入命令中，如图

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeExVlic1nRwIRwBvJRSsYvJYm4RuFzQqqUUqEE8udXyp2P3RLu9xDZlJagebMQoFnDhAQe7F577QQ/640?wx_fmt=png&from=appmsg)

3、使用单引号插入到命令中间，如图

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeExVlic1nRwIRwBvJRSsYvJyicxBff3bOx2V9udZ4Sb2LHsWQO4NaicZhQtT9NVuxwTLPLwjraZDIpA/640?wx_fmt=png&from=appmsg)

以上就是今天的内容，主要是系统的特性来帮助我们绕过 WAF 的检测，不过规则更新也比较容易，比如将单引号过滤掉，关键词检测，根据返回内容检测等等。

### 关于信安之路目前的几款产品定位及介绍

**成长平台**：适合小白入门、锻炼自学能力、总结能力、沉淀技术基础等场景，通过体系化的任务设置，开放性的任务要求，其他同学报告共享等方式，提升自学、总结、知识沉淀等能力，让自己在竞争中获得一些优势。

**信安之路知识星球：**稳定运营 7 年，历史沉淀三千多主题，两千多份文档，内容丰富，还能同时解锁成长平台和内部文库账号，目前正值年度特惠期间，加入仅需 299，原价 512。

**渗透测试那些事儿**：专注于渗透测试相关内容分享，包括信息收集、通用漏洞 POC、黑盒测试方法、技巧等内容，加入可解锁成长平台账号以及内部文库部分内容，目前正值年度特惠期间，加入仅需 128，原价 168。

**内部文库**：上线近三年，累计积累两千份文档，其中私密内容已有一千七百多份，均已体系化的内容方式呈现，试看目录（阅读原文直达）：https://wiki.xazlsec.com/static/forder.html

![](https://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAfeExVlic1nRwIRwBvJRSsYvJ6tmsFAHZEFapvkK4IhRiat6chGuUWTv8zADMDCeHNEfeiaZ2pLo8FzYw/640?wx_fmt=png&from=appmsg)

‍‍‍

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

信安之路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sGfPWsuKAff6G9jJ5AdPvZ0Fgia0Qm6X5X9Jkm8coDOxGE5UhriblyFP93bTgsDZKRib73zicNBGwibb2MPs9bXH4pA/0?wx_fmt=png)

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