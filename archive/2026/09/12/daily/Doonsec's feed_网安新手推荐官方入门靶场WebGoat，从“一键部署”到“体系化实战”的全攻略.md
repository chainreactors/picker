---
title: 网安新手推荐官方入门靶场WebGoat，从“一键部署”到“体系化实战”的全攻略
url: https://mp.weixin.qq.com/s/qRwG55148VY7oOHWfbUoeA
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:53.779036
---

# 网安新手推荐官方入门靶场WebGoat，从“一键部署”到“体系化实战”的全攻略

# 网安新手推荐官方入门靶场WebGoat，从“一键部署”到“体系化实战”的全攻略

沧海讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**在学习Web安全，新手入门渗透测试时，往往绕不开几个经典的练习靶场，除了之前介绍的DVWA和Pikachu，今天在介绍一个“重量级”选手——****WebGoat**。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9Sh2tGHNfLTZgJ8zDroSX72P6rQR1icus85RlcZD55Wzia5Otydg7otuSL6N3uVpr74r7s98IDNdTh2TpicnwMJjPGSuiambNlrlvc/640?wx_fmt=jpeg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=0)

虽然它在国内新手圈的“出圈”程度可能不如前两者，但作为**OWASP官方推出的开源教学靶场**，它的地位绝对不容小觑。

---

一、怎么快速获取和安装

1‌、**Docker 部署（推荐新手）‌：只需一行命令即可启动完整环境。**

* 运行命令：

```
docker run -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
```

* 优点：无需配置 Java 环境，包含 WebGoat 主应用和 WebWolf 配套工具。‌‌‌

**2、Jar 包直接运行‌：适合已有 Java 环境的用户。**

* 先下载最新 jar 包：访问

https://github.com/WebGoat/WebGoat/releases。

* 运行命令：

```
java -jar webgoat-server-xx.x.x.jar --server.port=8080
```

* 需要 JDK 11 或以上版本。‌‌‌

‌3、**源码编译运行‌：适合开发者深入了解内部实现。**

* **克隆仓库：**

```
git clone https://github.com/WebGoat/WebGoat.git
```

* 编译运行：`./mvnw spring-boot:run`‌‌

> ⚠️ 安全提示：
>
>  WebGoat是一个“故意设计得不安全”的应用程序，运行时机器极易受攻击。请务必在本地或隔离环境中运行，切勿将其暴露在公网！未经授权对真实系统进行测试属于违法行为，请始终遵守法律法规。

---

二、三大突出亮点

WebGoat在Web安全学习圈子里使用频率挺高的，基本是新手入门渗透测试时绕不开的一个靶场。它被频繁使用主要有以下几个核心原因：

**1. 官方背景，体系化教学**

作为OWASP官方推出的开源教学靶场，它的课程设计非常体系化、渐进式，非常适合新手用来系统地打牢安全基础。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QKGwg08uOndNl2wNhB0ElPvoyxzK9PoViaIPiaNekcRooUicdvZRGqicQ9jPnqKtVnh2lbYDic8snUdYLuldjibuWF5yQOs5exnRrbI/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

**2. 覆盖全面，建立完整认知**

它内置了30多个训练课程，涵盖了SQL注入、XSS（跨站脚本攻击）、访问控制、认证绕过等常见漏洞类型。一套练下来，能帮你建立起比较完整的漏洞认知体系。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9TMWUSm585EaPErNfjjjicxALYhG4yVoM6mGWVabFV7Tbo73Nib2sv1Eo8d00mW3VL5O2IUpZQpNL0ctvcoauybYrVJvqUicfjX74/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

**3. 上手门槛低，部署灵活**

WebGoat基于Java开发，运行极其方便。你可以直接跑jar包，也可以在本地、虚拟机或云服务器上部署。此外，它还提供在线靶场，让你免搭建直接开练。

---

---

### 三、WebGoat到底“好玩”在哪？

除了上述提到的优势，WebGoat之所以能成为行业标杆，还有几个非常硬核的亮点：

**1、自带“作弊码”的实战靶场**

与其他靶场“只管挖不管埋”不同，WebGoat的每一个子关卡都自带解决方案（Solution）。如果你卡关了，可以直接在顶部菜单查看解题思路，甚至配有WebScarab等代理工具的抓包截图。这种“边打边学”的闭环，能极大降低新手的挫败感。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9Qr15ySOtbBh7ZgISlHvrMDhIIQOgvpibSu3snlGFsuNkXe9G9gORIm7Lm1MDFNkibr73nrHsrCV4DA8Ktg2xk3wrOiayNTrYFtn4/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

2、配套“辅助工具”WebWolf

这是WebGoat的一大特色。WebWolf相当于一个模拟的邮件系统或外部服务器，专门用来接收你在WebGoat中通过漏洞窃取到的Cookie、Token等敏感信息。这种“双端联动”的设计，能让你更直观地理解攻击链的完整过程。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9RvwnEpIkN8SV2CxE8SYicwDfS4WIwAEV5uW4FVuPzIc7cic54hL3PqNiaDJSS1a2ngNqQ9oKwHwm0vFXdib6g6gFYTmdIuxvTPxVA/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

**3、自带计分卡（Report card）**

WebGoat内置了自动评分系统。每当你成功利用一个漏洞，系统会自动打分并解锁下一关。这种类似“打怪升级”的机制，能让枯燥的安全学习变得更有成就感。

#### ![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9SzuY1PYZCKGVfvD5q1SdeHQ2SVx9s5icqPxqBpd5BRtIQicuP4qrfYSoLpK0mQF2eCwH2rXRSojHybLvbWry45CvkrXnnADVMps/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

---

#### 四、WebGoat到底教什么？

WebGoat的关卡设计是其精髓所在，它将复杂的Web安全问题拆解成一个个具体的、可操作的挑战。

**1、OWASP Top 10全覆盖**

WebGoat的课程紧密围绕OWASP Top 10展开，这是Web应用安全领域最权威的十大风险列表。

你可以在这里亲手实践：

* **注入攻击 (Injection):** 从最基础的SQL注入，到更复杂的LDAP注入、OGNL注入，让你理解“数据与代码混淆”的本质。
* 跨站脚本 (XSS): 学习反射型、存储型和DOM型XSS的区别与利用方式，理解为什么用户输入需要被严格过滤和转义。
* **失效的身份认证 (Broken Authentication):** 模拟暴力破解、凭证填充等攻击，学习如何设计安全的登录和会话管理。
* **敏感信息泄露 (Sensitive Data Exposure):** 练习如何从错误的配置、不安全的API响应中挖掘敏感信息。
* **XML外部实体 (XXE):** 理解如何通过恶意构造的XML文件读取服务器本地文件。

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9TRA2dBkdkz4l7Uicv07A5jdzKDRUaqHuZsWpuP6T0zjV4pAj8bSKygI3r9LFCiaZYLRSH4nCHibRXpUTOaia2B6q1kH2NllQIKhs0/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)**

**2、不止于Top 10的进阶挑战**

除了基础漏洞，WebGoat还包含了许多更贴近实战的复杂场景：

* **访问控制漏洞 (Access Control):** 学习如何通过修改URL、参数或请求方法来越权访问其他用户的资源或管理员功能。
* **服务端请求伪造 (SSRF):** 模拟攻击者诱使服务器向内部或外部系统发起请求，从而探测内网或攻击后端服务。
* **不安全的反序列化 (Insecure Deserialization):** 理解如何通过篡改序列化对象，在服务器端执行任意代码。
* **基于逻辑的漏洞:** 一些关卡需要你理解业务流程，通过“非正常”的操作顺序或参数组合来达成攻击目的，非常锻炼思维。

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9SHDYP9picnw3KaJVrbFSzRSDotSictIOSKticd2feNzvDLGzKPibC24YjasPsP9Cg3GatXSqTIw6k6Vp97Bk4IAhBtYlKDXSDYX6A/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)

---

💬 客观存在的“争议点”

当然，任何工具都不是完美的。在安全圈里，关于WebGoat也有一个常见的争议点：

有人觉得它**太“教学化”了**。因为每个关卡都有详细的提示和引导，它跟真实的渗透场景有一定的距离。所以，练完WebGoat后，通常还需要搭配DVWA、Mutillidae这些靶场，或者去真实环境中进行巩固。

因此它更适合作为**入门和打基础的工具**，想要深入，还得靠实战积累。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9TRDOQtxsYb2Rcu1Vxco0WicymiaoibpuoCiayO36FIvB6xnJYOoIa0XcIYYhGnHHsT6tPmu24YqKF0xr5iaqQ1cXQaGawJbY9s9gHE/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)

关于 WebGoat 这种‘自带提示’的靶场，你是觉得‘真香，新手友好’，还是觉得‘太像做题了，没意思’？评论区站队让我看看！👇

---

---

「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

**沧海专属黑客/网络攻防技术资料**

@沧海讲安全：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

**部分技术资料预览**

**01**

***视频教程***

从0到进阶主流攻防技术视频教程（包含红蓝对抗、CTF、HW等技术点）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcYaRKqWc1cxP8sBrX6KZasFTJEVibWmdyoGAuRO4AbzaVjUJ8guoWAzQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcCP8oaOCQm8Cp2qhpCxWiaOjzYrOoA1iac5eSafBicPxSQcpYtchyfVvxA/640?wx_fmt=jpeg&from=appmsg)

**0****2**

***书籍Pdf***

入门必看攻防技术书籍pdf（书面上的技术书籍确实太多了，这些是我精选出来的）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcUumOTUmUznuo7MzKl1JiaEQIeSh4ibkO6jxY68zVZz7iayrwGRtGu2bHw/640?wx_fmt=jpeg&from=appmsg)

**0****3**

*安装包/源码*

主要攻防会涉及到的工具安装包和项目源码（防止你看到这连基础的工具都还没有）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcvsT9h4B1hS9VEPengMcOtNL24949kb4cibKLS9HkIb1k2htW8GYqzMQ/640?wx_fmt=jpeg&from=appmsg)

**0****4**

***面试试题/经验***

网络安全岗位面试经验总结（谁学技术不是为了赚$呢，找个好的岗位很重要）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6Kqcm6J0eAql29R6DIM8bJW4rweVBicM8ibGMOmLNFTpdcQ0gFvefMTOg9dA/640?wx_fmt=jpeg&from=appmsg)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

@沧海讲安全：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kWXbooRKsCUic8In0GE4Hd6nTM7iclEUG0UewS479kicpBqGcfpOAaTibhgwsEsblvqe0EsP95XKBe2E90T9g02cQg/0?wx_fmt=png)

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