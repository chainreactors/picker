---
title: 【安全圈】AI自动挖洞不是梦，谷歌AI工具OSS-FASZ又发现26个开源漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066127&idx=1&sn=54cc25bc1157b1fcde3352264a6e6737&chksm=f36e7d0fc419f419eba06e5a96d15df8e4c6984457ffe2caa95bdb960aa38174100f2f438f01&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-23
fetch_date: 2025-10-06T19:18:46.027875
---

# 【安全圈】AI自动挖洞不是梦，谷歌AI工具OSS-FASZ又发现26个开源漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgKZbN7RO3qZzvWgQTAPicibNbUribyiaRwECFIibnDPbNuq5mYeT1wovYHW8TufumnbB3nlYoforjTLFA/0?wx_fmt=jpeg)

# 【安全圈】AI自动挖洞不是梦，谷歌AI工具OSS-FASZ又发现26个开源漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

谷歌透露，其基于人工智能的模糊工具OSS-Fuzz 已被用于帮助识别各种开源代码库中的26个漏洞，包括 OpenSSL 加密库中的一个中度漏洞。这一事件代表了自动化漏洞发现的一个里程碑：每个漏洞都是使用AI发现的，利用AI生成和增强的模糊测试目标。

提到的OpenSSL漏洞是CVE-2024-9143（CVSS评分：4.3），一个超出范围的内存写入缺陷，可能导致应用程序崩溃或远程代码执行。这个问题已经在OpenSSL的3.3.3、3.2.4、3.1.8、3.0.16、1.1.1zb和 1.0.2zl版本中得到了解决。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgKZbN7RO3qZzvWgQTAPicibNibCIuDA4rpe9RKsNiasSueNB1LzwqJNHoz6r4YjSlVRSEPHE6cY1Aeibg/640?wx_fmt=jpeg&from=appmsg)

## 破题人类无法发现的漏洞

谷歌在2023年8月增加了利用大型语言模型（LLM）来提高OSS- Fuzz中模糊覆盖率的能力，并表示该漏洞可能在代码库中存在了20年，而且在现有的由人类编写的模糊目标中是无法发现的。此外，他们还指出，使用AI生成模糊测试目标已经提高了272个C/C++项目的代码覆盖率，新增了超过370,000行新代码。

谷歌解释说，这样的漏洞之所以能够长时间未被发现，一个原因是线覆盖率并不能保证函数没有漏洞。代码覆盖率作为一项指标，无法衡量所有可能的代码路径和状态，不同的标志和配置可能会触发不同的行为，从而暴露出不同的漏洞。这些人工智能辅助的漏洞发现也是可能的，因为LLMs被证明擅长模仿开发人员的模糊工作流程，从而允许更多的自动化。正如谷歌之前就提到过，其基于LLM的框架Big Sleep帮助发现SQLite开源数据库引擎中的一个零日漏洞。

## C++代码安全性大幅提升

与此同时，谷歌一直在努力将自己的代码库转换为内存安全语言，如Rust，同时还对现有的C++项目（包括Chrome）中的空间内存安全漏洞（当代码可能访问超出其预定范围的内存时）进行改造。其中包括迁移到安全缓冲区和启用强化的libc ++，后者将边界检查添加到标准的 C ++数据结构中，以消除大量的空间安全缺陷。它进一步指出，纳入这一变化所产生的间接费用很小（即平均0.30%的绩效影响）。

谷歌表示，由开源贡献者最近添加的“hardened libc++”引入了一系列安全检查，旨在捕获生产中的越界访问等漏洞。虽然C++不会完全成为内存安全的语言，但这些改进降低了风险，从而使得软件更加可靠和安全。

具体来说，hardened libc++通过为标准C++数据结构添加边界检查来消除一大类空间安全漏洞。例如，hardened libc++确保对std::vector的每个元素的访问都保持在其分配的边界内，防止尝试读取或写入超出有效内存区域的尝试。同样，hardened libc++在允许访问之前检查std::optional是否为空，防止访问未初始化的内存。这种改进对于提高C++代码的安全性和可靠性具有重要意义。

参考原文：https://thehackernews.com/2024/11/googles-ai-powered-oss-fuzz-tool-finds.html

***END***

阅读推荐

[【安全圈】Ubuntu系统软件中的5个漏洞潜藏了10年才被发现](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066112&idx=1&sn=00fc32fb2126236a289beba3ec9b7b29&chksm=f36e7d00c419f41616a3b529fd231f5c9cb584fc1c962df2286ebe434d3081d23b39cd91ade2&scene=21#wechat_redirect)

[【安全圈】菜鸟黑客们开始抄红队人员的作业？](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066112&idx=2&sn=09bb634b924e35eaff76039d01f35970&chksm=f36e7d00c419f416e741d513ef48b749921a32dfc81493b21049b6c190854ffaefabe6efe559&scene=21#wechat_redirect)

[【安全圈】网络钓鱼警报：通过 DocuSign 冒充政府的攻击激增](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066112&idx=3&sn=dce35e4585bab3391e375bef7d60a394&chksm=f36e7d00c419f416a58fffe5ab88a99af8ab606dac885e999152a64678434bf34b1ca933c490&scene=21#wechat_redirect)

[【安全圈】朝鲜黑客创建经过安全验证的恶意软件攻击macOS系统](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066112&idx=4&sn=5b9242cdb5d2263f743eae03dcbe82d0&chksm=f36e7d00c419f41651171aad9c644ce17a7b061075eb069737ae2c80576eb4d36c322befe171&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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