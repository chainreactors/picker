---
title: Botconf 2024 议题慢递
url: https://mp.weixin.qq.com/s?__biz=MzkyMzE5ODExNQ==&mid=2247487566&idx=1&sn=16cb1f263347cd0050824691af6f8d09&chksm=c1e9e782f69e6e94bedf998d3e6e1660db9887e7553b0c61f90b722ec7e914e54130892d8d0e&scene=58&subscene=0#rd
source: 威胁棱镜
date: 2024-11-26
fetch_date: 2025-10-06T19:20:15.760985
---

# Botconf 2024 议题慢递

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mwXWxRR0HluX4nclsrV6cjcyrhbWPsecuknRPgohHDufujoaLIvUONQ/0?wx_fmt=jpeg)

# Botconf 2024 议题慢递

原创

Avenger

威胁棱镜

2024 年的第十一届 Botconf 来到了法国的尼斯。全世界数百位安全研究人员再一次齐聚一堂，热热闹闹地讨论相关议题。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mmuQCg4ictS0vOJohscFRDoVR7BxJU4aSlj8UZoycMC5lbBeRZwGwrCg/640?wx_fmt=png&from=appmsg)

下面只挑选部分议题进行介绍，感兴趣的同学可以去官网查看全部议题进一步了解。一如既往要强调的是，会议要求参会人一定要遵守 TLP 要求，本文只简要介绍了部分议题，完整、详细的内容请查看官网或者联系作者。

**使用图片监控 APT 投递的第一阶段样本**

APT 组织在攻击中常常会用到图片，通常和政府和各种机构有关：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39myfp6eGlqh29aK9OPL5zzaOlxpNFoe4fpNCDVcRvAnCVbavLwnHHMBg/640?wx_fmt=png&from=appmsg)

各类文档中的图片都可以用来判断相似性：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mL9sdeIiaRibwJuGN9ecuVp8AbGq3VUOib7OLlNGjVEhlYeI4NLVmHAfkQ/640?wx_fmt=png&from=appmsg)

每个攻击组织的样本数量如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m3f4UcPq4qmicSB9dt5ZGAGRMQBK2iaibDibgCDu8I0ve8icp0Q0JHLrtWQA/640?wx_fmt=png&from=appmsg)

APT28 持续使用的图片如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mYdIibySLWZSYIlyROBlahNpibykIpAHvdr0CUKQ04BibUicff1kuNmiakTw/640?wx_fmt=png&from=appmsg)

小手图片一直被 APT28 持续使用接近五年：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m7MeJoRicsxhjibVofdW8DaWn8M8SRv0IPx46iaBTrM4jufo9ic0bX2RYibA/640?wx_fmt=png&from=appmsg)

SideWinder 在多个文档中使用相同的签名笔迹：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39ma1VS419X7Z80OeHMc63TY81iaQDtzVSH4lLwznvSAjEHIja2vTLGeaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mQPCdjf4sV1ibX1BztO0nal6E1VJFKKZZBibAibib6KCVsjBVE62VNia98Qg/640?wx_fmt=png&from=appmsg)

这些都是线索，不能据此直接确定是某个组织，还有可能是 False Flag。Styles.xml 和 [Content\_Types].xml 其实会在多个组织间共享：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m40YaBpUYVUTYRZiaN9jnu3hjmNfGLwOOmPepSO6tTj3OPYMcDyesiagA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mhYcuQbKqiaPtjHnffjAamUFOwIMcHRYdFSFuMyt1j05Es8jzm7RhszA/640?wx_fmt=png&from=appmsg)

VirusTotal 也尝试引入大模型来对图片进行识别，进一步提高可解释性：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m3MVH2uKsMZ4xOibznPTnloqj6zPUpavSCficG92czYrm11uMAY2tqbDA/640?wx_fmt=png&from=appmsg)

以 Blind Eagle 为例，

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mfeHYgashdz2vE4lH9ornMicUnNI2CPkEqSIGWUw2Lca3RsBC7VwJkZA/640?wx_fmt=png&from=appmsg)

Adobe Acrobat Reader 如果打开了 PDF 文件，首页的缩略图会在 C:\Users\<user>\AppData\LocalLow\Adobe\Acrobat\DC\ConnectorIcons\下生成：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39meD0KCuaCm1kK0VTtgSehwVCRPDeRaeGj6F1IsdRLWNDaqqubPcZ7dw/640?wx_fmt=png&from=appmsg)

通过这个文件就可以追溯释放该文件的父文件：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m5pIrdRhR3IYAp6qWhQL0hMCn9xn7pHOCZ4385AjlvCnxabCDFRIRfw/640?wx_fmt=png&from=appmsg)

类似地，用户在 PDF 文件中点击链接打开 Chrome 浏览器访问 SharePoint 网站，在本地会生成 Cache 文件。通过这种方式也可以追查到 Blind Eagle 使用的多个样本文件。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mYuEibqZuUO1icRQHGMs0so2reOibGzZYPREyrPSocWRBURxfiajRoezruQ/640?wx_fmt=png&from=appmsg)

电子邮件附件中的图片，也可以作为线索找到拥有相同图片的电子邮件，攻击了许多其他目标：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m5ls2rdb8ZnHZYB2yNYicju27gQ5ia3FQsYRgt2SdUAS8FvQR1XepFmNg/640?wx_fmt=png&from=appmsg)

**动态分析中正则检测规则的生成**

动态分析中命名对象（互斥量/Mutex、信号量/Semaphore等）与事件（创建文件、删除寄存器等），都可以用于检测恶意软件家族和变种。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mh3aAghkA5IegOUlWBTXlUc7GVrTCNzzzw1bpqsibCib2jsu4QeO7ea0A/640?wx_fmt=png&from=appmsg)

Yara 自带的 Cuckoo 模块就可以用于描述动静态特征：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mekVIpIQN7z12gA5lH8yEQpR3GJSwXA0yQB92vVwibR1XzbEv6UJGxKA/640?wx_fmt=png&from=appmsg)

作者扩展了部分功能，新增了函数与匹配的次数：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mGfvhl2ibSxCpIk0te2jlhzcEde4jUQXZibsSicmhcLT3ibwHyfpvlXcxlg/640?wx_fmt=png&from=appmsg)

整体架构如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mpeLXS3RwwvCjOLzNlLIvoE8CDEQPc1GqPv7UJiaUE3MuDJp4zONT8Og/640?wx_fmt=png&from=appmsg)

输入处理字符串和要匹配的类型：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mtt0icmAhztrrQ1Qq0R5yCjSiavSUGJDgibgEbRtAxN3JabcVIVQqX0CYw/640?wx_fmt=png&from=appmsg)

预处理过程要将十六进制 \xHH 转换为一个字符、删除只包含 GUID 的字符串、删除各种前缀（HKEY\_LOCAL\_MACHINE、Global\、C:\Program Files）、替换用户名。

基于输入的数据，通过 n-grams 进行聚类：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mXZXellELxO85y9YLOOuMY3FMxa6D6hcLF5R671fiaeEkgaFwBEPPSUQ/640?wx_fmt=png&from=appmsg)

创建前缀树：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mgZw6IuFPwmvguhGzNtX1IUqAVwL9FcwFfYYcln97zkW8Ql1SobHAYA/640?wx_fmt=png&from=appmsg)

通过简化的 Brzozowski 代数方法构造最小化自动机：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m3HlwuXpJLfPHxLgK6aSbQ7XUCT3gka0SOdSZUEP1RWFuK1f4dmyU9Q/640?wx_fmt=png&from=appmsg)

求解方程组，为每个聚类生成对应的正则表达式：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mW2xvDwwzSJoGBBShU6ibOMFib4lHhiawFmDlvJVicicKCb3aIGUGPuFwibJQ/640?wx_fmt=png&from=appmsg)

为了在生产级可用，需要再次进行优化来保证规则的可读性、提高模式匹配的效率、维持误报/漏报率。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mFoF1GurFfwAm2pv2CLlMAI8pu5xVLaIckFImgFLa0CJ9Iiax41k9BWQ/640?wx_fmt=png&from=appmsg)

甚至还包括要增加前缀和后缀：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mwSvtWw87H4IiaiaEMX8S20od4XS52P7GYvy1yohLwlaAA2hCL89lzagA/640?wx_fmt=png&from=appmsg)

最终输出给用户的结果是：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m3VnuIJcdmZ8k2BG6R2PcqeicbOhdLc4SrUIF0hy6dbASribEPicD0EMdw/640?wx_fmt=png&from=appmsg)

利用十个家族的五万多份沙盒报告生成对应的 Yara 检测规则：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mkRn9ZX95AcGrRjZ9lOmQRlT79tUa3LHibF6hJhfgUVY9NJaIgKyXtAQ/640?wx_fmt=png&from=appmsg)

以 Qakbot 为例，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m7m0IcJ2gCFQlNXsbe5kxaTvD6UFdNMTbtt4ficRKje2g8NTp2g0JpGA/640?wx_fmt=png&from=appmsg)

最终 true positive 为 92.34%、false positive 为 0.01%。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39m1dwKJUM07U5AT0uECLo0tXGgb84A3BfmCcxMY81Vl4d1SmThicjSr5w/640?wx_fmt=png&from=appmsg)

```
https://github.com/avast/genrexhttps://github.com/regeciovad/GenRex-demo
```

**瞄准东亚的恶意移动应用程序FluHorse**

攻击者通过在虚假 ETC 通行费催缴信息中提供恶意链接，诱使用户进行点击。实际正确的域名是 fetc.net.tw，攻击者仿冒的域名是 fetc-net.com。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mxsp2uIQ2mnhbxcH83M3vu5s9HxeTMKZVNbRicmDJwI1lDn8UXia6QtibQ/640?wx_fmt=png&from=appmsg)

使用的恶意软件潜伏数月都没有被检出：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mdicyqUcMMvjATHyqUgwk0pMhOJMiaLvDOEnRLkdyfsLkhCUEpfBlF4pw/640?wx_fmt=png&from=appmsg)

针对中国台湾、泰国、越南发起全面攻击，恶意软件下载量超过十万达到百万量级。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39msibsXQfBNCXXy6DZiasoDsCE1erwPh2FgSHgJTibWKbnKWRPL61GnokuA/640?wx_fmt=png&from=appmsg)

恶意应用程序要求受害者输入用户凭据和信用卡信息，拦截用户短信回传双因子认证给攻击者。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mciaDQ4YNobeukicZLJb1soszM1XCAmHbWjZjYOTp1BBKBbO2p1annL7Q/640?wx_fmt=png&from=appmsg)

恶意应用程序使用 Flutter 开发，让分析变得非常困难。

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mJUEL9acsUQOUIh7DsESgwia5VAwLQ8hWIy7HQe7tI6QLkicklicQAyLhA/640?wx_fmt=png&from=appmsg)

发往 C&C 服务器的请求示例如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mg1Fosx63TPNdEsYu2sAETHeVwsDrnMVCk4iaacicRGgpqwNLFF7SnyzQ/640?wx_fmt=png&from=appmsg)

**大规模传播的恶意软件传播策略**

C&C 模式有 P2P、随机、中心型（星形/分层形）、混合型；逃避技术有 Fast-Flux、加密、混淆、非标准端口等。

以 Aurora Stealer 为例，C&C 模式是中心型、硬编码 IP 地址、原生 TCP 连接、base64(gzip(json)) 进行混淆：

![](https://mmbiz.qpic.cn/mmbiz_png/dlhiccJOdNYaPfiaBXvMaiagHFJ2Vy1O39mHHLhic8E5dS9utHxZibB99DdHR6ZI9EsouRsSibosmE1ggpos2SHh5lEA/640?wx_fmt=png&from=appmsg)

收集了近二十万个样本与所...