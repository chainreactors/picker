---
title: Betterleaks革新密钥扫描，比Gitleaks更快更准
url: https://mp.weixin.qq.com/s/S9wVPP0li81-i90BmZ4Y8w
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:01:32.908123
---

# Betterleaks革新密钥扫描，比Gitleaks更快更准

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX01rg4TsPSg9RE1ugjW3BrWNOkmLfv5tZT7O349kd9zz1wnKkco5VIKWESjrrK4Xg3UXh8YnsBYyTJtT92MOOA7Xukks6wkMLA/0?wx_fmt=jpeg)

# Betterleaks革新密钥扫描，比Gitleaks更快更准

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2U1TCibbnJqza6APfbmFrgicgNoyOS4Xibib4RicP9FTquicqSjz5j9jyRI433SMn5L63S9v9ibKvHLlicQCGPLIs25V3PKSzHT4FThTQ/640?wx_fmt=jpeg&from=appmsg)

##

**Part01**

## ****工具概述****

密钥扫描已成为工程组织的标准实践，而Gitleaks是该领域应用最广泛的工具之一。该项目作者近日发布了一款名为Betterleaks的新工具，专门用于扫描Git代码库、目录和标准输入流中的凭证泄露，包括API密钥、令牌和密码。

项目负责人Zach Rice约八年前编写了Gitleaks初始代码，现任Aikido Security公司密钥扫描部门主管。

![Betterleaks](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3IGl2XribzYFw5Bej5dMoL56up5MW625luTAqE3EdiaYTT8TDRO9T2j6rHF90wg83OQaJlsYI0AiaS9MOuicicdd9CJCaU6VBldKaA/640?wx_fmt=jpeg&from=appmsg)

实际代码库扫描耗时与Gitleaks对比（来源：Betterleaks GitHub页面）

**Part02**

## ****开发背景****

Rice在项目说明中解释，由于不再完全掌控Gitleaks代码库和名称所有权，促使他启动新项目。Betterleaks设计为Gitleaks的即插即用替代方案，现有命令行参数和配置文件无需修改即可直接沿用。

**Part03**

## ****技术革新****

Betterleaks最显著的技术改进在于候选密钥过滤机制。与多数扫描工具类似，Gitleaks依赖香农熵（Shannon entropy）识别疑似密钥的字符串。Betterleaks则创新性地采用基于字节对编码（BPE）的Token Efficiency技术：

* 该技术通过测量BPE分词器对字符串的压缩效率进行判断
* 自然语言可压缩为较长token，表现出高Token Efficiency值
* 密钥和随机字符串压缩效率低下，产生大量短token和低Token Efficiency值
* 在CredData数据集测试中，Token Efficiency的召回率达98.6%，显著优于熵检测法的70.4%

验证逻辑采用通用表达式语言（CEL）编写，规则制定者可编程控制密钥确认标准。工具默认支持双重和三重编码密钥检测，并通过并行化Git扫描降低耗时。采用纯Go语言构建（无CGO依赖），摆脱对Hyperscan的依赖，实现跨环境无原生库部署。支持扫描归档文件（含嵌套归档），输出格式涵盖JSON、CSV、JUnit、SARIF及自定义模板。

**Part04**

## ****未来规划****

项目路线图包含多项v1版本未实现的功能：

* LLM辅助分类：将匿名化候选密钥传递给本地/远程语言模型获取上下文
* 自动撤销支持：对接提供凭证撤销API的服务商
* 权限映射功能：可视化展示已检出密钥的实际访问权限

**Part05**

## ****AI集成设计****

工具采用基于标志位的输出控制机制，便于AI编程Agent将其作为子进程调用时，能高效解析输出而无需额外token开销。Rice指出，类似Claude Code或Cursor等工具的AI Agent倾向调用具备可控输出的命令行工具，Betterleaks正是为此场景设计。

该工具已在GitHub开源发布。

**参考来源：**

Betterleaks: Open-source secrets scanner

https://www.helpnetsecurity.com/2026/03/19/betterleaks-open-source-secrets-scanner/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hCYIDd7a8icmhzic2aMTw0bics6BfDdhRCQCsKTwXSAB6wXtEwI4OK9jdlFfFFNQJa4JUiapxxu56BjXl4gx3LEXYU1GMRkpiawgA/640?wx_fmt=png&from=appmsg)

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