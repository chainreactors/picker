---
title: 攻击者利用Gemini AI模型实施网络攻击
url: https://mp.weixin.qq.com/s/tgUpCbLfpXR270r3h2AwAA
source: Doonsec's feed
date: 2026-02-13
fetch_date: 2026-02-14T04:05:50.869613
---

# 攻击者利用Gemini AI模型实施网络攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3VqIbANaBWPrjQgUwKTO0ukV7gL6O8FlPlR7Rdxk9yXzNRk5BELnptItUya5vp7UnnyGUpFOA6iclEBibfiaDxqWGd6IT0NclLdo/0?wx_fmt=jpeg)

# 攻击者利用Gemini AI模型实施网络攻击

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3QocfINUZD9sL13x0ibr3bsGALkM2ApzBIas4BicpkHpO3ANValCSGnKyvpZFQ4OgFW6iaU0pzHRbfNrVGbn3HjcgoCN5ibDcsPn0/640?wx_fmt=png&from=appmsg)

攻击者已开始利用Google的Gemini API动态生成C#代码，用于构建多阶段恶意软件，从而规避传统检测方法。Google威胁情报小组(GTIG)在2026年2月的AI威胁追踪报告中详细披露了这一情况，重点介绍了2025年9月首次发现的HONESTCUE框架。

**Part01**

## ****HONESTCUE恶意软件运作机制****

HONESTCUE作为下载器和启动器运行，通过硬编码提示查询Gemini API获取自包含的C#源代码。该代码实现第二阶段功能，例如从Discord等CDN托管的URL下载有效载荷，且不会在磁盘留下痕迹。

![HONESTCUE恶意软件利用GeminiAI](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3iaeQd03DRWJ0YUK34dt5RpBfcRU4FWWRcLickZKR0RYaKa1HSXgXw9ObpveibDlQ23KcWIjx84RDVy5ZicuMWUEnhxOF52FgOZKE/640?wx_fmt=jpeg&from=appmsg)

该恶意软件随后使用合法的.NET CSharpCodeProvider直接在内存中编译和执行接收到的代码，使静态分析和行为检测复杂化。开发者通过单一账户向VirusTotal提交迭代优化的样本，表明这是一个小型团队在进行PoC测试。

**Part02**

## ****Gemini API的滥用过程****

威胁行为者利用Gemini实施攻击的过程分为多个层次：

* **API调用：恶意软件向Gemini发送静态提示，获取可编译的C#代码；**
* **动态编译：CSharpCodeProvider将响应处理为可执行程序集；**
* **载荷投递：第二阶段从攻击者控制的URL（通常通过Discord CDN）获取字节，然后通过Process.Start或反射启动；**
* **无文件持久化：没有二进制文件写入磁盘，破坏终端取证。**

![Clickfix攻击链](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1aFgnqKvYYV9tfWqtffGJAKUKY54pBbp6EtCD8kMTCJGc342SBSAo9ib161X9RGZtmswInOVPbT6VDPZO0cXV9iahQiczA9SnvicA/640?wx_fmt=jpeg&from=appmsg)

**Part03**

## ****攻击者背景与防御建议****

GTIG追踪到朝鲜、伊朗(APT42)和俄罗斯组织滥用Gemini进行网络钓鱼、漏洞研究和C2脚本编写。例如APT31曾伪装成"安全研究员"探测RCE和WAF绕过方法。

Google已通过账户禁用、模型加固和实时分类器进行干预。防御者应监控API异常（高频代码生成查询）、阻止异常的Gemini流量并检查内存中的.NET加载。混合防御策略结合网络遥测和运行时检查正变得至关重要。

**参考来源：**

Google Warns of Hackers Leveraging Gemini AI for All Stages of Cyberattacks

https://cybersecuritynews.com/gemini-ai-model-cyberattacks/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1QWGTwJ4jnO2icEhSqbRNdWd3iaVBKjlfTsWSdDBiayVW1jWahKjlggw6mzYnEo5D6PMvFzRX6fEpVEic5NqQoVDFCWvHlh48OxrA/640?wx_fmt=png&from=appmsg)

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