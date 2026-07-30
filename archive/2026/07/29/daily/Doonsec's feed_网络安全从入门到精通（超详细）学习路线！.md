---
title: 网络安全从入门到精通（超详细）学习路线！
url: https://mp.weixin.qq.com/s/ZoNQlZBJH9ozT-7UtOf6CQ
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:48:10.504982
---

# 网络安全从入门到精通（超详细）学习路线！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbWEHMerrBZgTgMR21LkshyBVeh4lIlyxPqSF8W34UVBFJc2afc3OIejMTuLMibDicyDQLiad2r0qyfiahUV2icv3wB04oosiaZl3MWlk6IFdJhog/0?wx_fmt=jpeg)

# 网络安全从入门到精通（超详细）学习路线！

编程技术栈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字**

**关注我**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6YnBvoBcYkSnu2s6WY7801C9e955yNEuVO278veTNO4CRiav0sCibofReRXhkPBv3tvBLE5D4jZHTIeia9u2PbV3Q/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

**01**

**一、网络安全学什么**

1、网络安全法

网络并不是狂徒张三的法外之地，在学习网络安全技术之前，首先要学会如何在法律范围之内行事。在2017年6月1日，我国第一部网络安全法《中华人民共和国网络安全法》正式实施，我国网络安全管理迈入法治新阶段。所以，我们学习的第一课就是网络安全的普法课程。

所以，在法律的界限里，先要知道底线在哪里，以前没有网络安全法的时候，有些界限是模糊的，现在我们要严格在网络安全法的范围内活动，不然真的如江湖传言：网络安全，从入门到入狱；Kali学的好，局子进的早；渗透学得好，牢饭吃到饱。

2、黑客守则

听到黑客这个词，肯定觉得和犯罪沾边，但是现在的黑客并不是这样，千万不要觉得黑客是罪犯，其实“黑客”这个词语在刚出来的时候，就像内裤外穿的超人一样，是正义的化身，是一个褒义词。可是近几年，随着一些不讲武德的人占比越来越高，使得这个词语被无情丑化。我们学习网络安全的初心是正义和爱，这个是坚持100年甚至一直不动摇的初心使命，所以我们也要有一些规矩。

3、技术

阶段一：基础部分

Windows部分

基础命令、PowerShell的使用和简单脚本编写

组件：注册表、组策略管理器、任务管理器、事件查看器

另外，可以先学习一下怎么在Windows上搭建虚拟机，学会安装系统，为接下来学习Linux做准备

Linux部分

主要学习如何使用，学习文本编辑、文件、网络、权限、磁盘、用户等相关的命令，要建立一个Linux的基本认知。

这个阶段的误区就是小白很容易一上来就学Kali，连基本的概念都没懂，就去学习使用工具，属于典型的本末倒置。

计算机网络部分

从局域网出发，了解计算机通信的基本网络——以太网

局域网如何通信？

集线器、交换机之间的区别？

MAC地址、IP地址、子网、子网掩码的作用？

随后就要了解广域网、互联网，通过七层和四层模型快速建立起计算机网络的基础概念，各层协议的作用，分别有哪些协议，这些协议在当今的互联网中具体是怎么应用的。

Web基础部分

学习网络安全，就离不开web。Web安全是网络渗透中非常重要的一个组成部分。

掌握HTML+CSS+JS的开发使用

这一部分需要自己动手的会多一些，比如熟悉掌握Javascript、了解Ajax、学习JQuery

数据库基础部分

主要学习一些理论知识，重点掌握库、表、索引概念，学习SQL编写，学会增删改查数据

阶段二：进一步学习基础

Web进阶

学习Apache和Linux的基本知识

动态网页基本原理

CGI/Fast-CGI过渡到ASP/PHP/ASPX/JSP等动态网页技术，了解它们的发展历史，演变过程和基础的工作原理。

Web开发中的基础知识：表单的操作、Session/Cookie、JWT、LocalStorage等等，了解这些基本的术语都是什么意思，做什么用，解决了什么。

PHP编程

选择PHP是因为它更放方便我们研究安全问题。

需要学习：语法基础，基本的后端请求处理，数据库访问，然后再接触一下常用的ThinkPHP框架

计算机网络进阶

HTTP/HTTPS以及抓包分析

inux上的tcpdump必须掌握，包括常见的参数配置

学习Wireshark分析数据包，用Fiddler抓取分析加密的HTTPS流量。

加解密技术

包括base64编码、对称加密、非对称加密、哈希技术等等。

阶段三：中级技术

Web安全入门

Web安全领域内几大典型的攻击手法：SQL注入、XSS、CSRF、各种注入、SSRF、文件上传漏洞等等，每一个都需要详细学习，一边学习理论，一边动手实践。

这里需要自己在虚拟机中搭建一些包含漏洞的网站，如果在互联网上的网站来攻击是会被请去喝茶的。

网络扫描与注入

学习如何寻找攻击点，获取目标信息

信息包括：目标运行了什么操作系统，开放了哪些端口，运行了哪些服务，后端服务是什么类型，版本信息是什么等等，有哪些漏洞可以利用，只有获取到了这些信息，才能有针对性的制定攻击手段，拿下目标。

需要学习常用的扫描工具以及它们的工作原理。

信息搜集与社会工程学

whois信息用来查询域名信息，shodan、zoomeye、fofa等网络空间搜索引擎检索IP、域名、URL等背后的信息，Google Hacking利用搜索引擎来检索网站内部信息，这些东西都是在网络信息搜集中经常用到的技能。

暴力破解

学习爆破工具hydra、超级弱口令、mimikatz

阶段四：安全防御和检测

WAF技术

需要学习web应用防火墙。掌握WAF工作原理，找到弱点绕过检测，或者加强安全检测和防御能力

需要学习当下主流的WAF软件所采用的架构比如openresty、modsecurity，以及主要的几种检测算法：基于特征的、基于行为的、基于机器学习的等等。

网络协议攻击 & 入侵检测

掌握TCP劫持、DNS劫持、DDoS攻击、DNS隧道、ARP欺骗、ARP泛洪等等传功经典攻击手段的原理

日志技术

系统登录日志（Windows、Linux）、Web服务器日志、数据库日志等

Python编程

学习编程开发，编写爬虫、数据处理、网络扫描工具、漏洞POC等等

浏览器安全

需要重点掌握IE、Chrome两款最主流的浏览器特性，浏览器的沙盒机制是什么，同源策略和跨域技术等等。

阶段五：高级技术

第三方组件漏洞

学习目前互联网服务中实际使用的一些工程组件，比如Java技术栈系列Spring全家桶、SSM、Redis、MySQL、Nginx、Tomcat、Docker等等。

内网渗透

学习在渗透过程中如何转移，在攻下一个点之后，控制更多的节点。这个部分理论少，实战多，需要搭建靶场环境模拟学习

操作系统安全技术 & 提权技术 & 虚拟化技术

阶段六：成熟阶段

CobalStrike & MetaSploit

通过这两个神奇可以对前面学习的信息扫描、漏洞攻击、内网渗透、木马植入、端口反弹等等各种技术进行综合运用，融会贯通。

其他安全技术拓展

到了网络渗透的后期阶段，想成为一个安全高手，绝不只是固步自封在自己擅长的领域，需要多学习网络安全的其他领域，拓展自己的知识面。

比如二进制漏洞攻击、逆向工程、木马技术、内核安全、移动安全、侧信道攻击等等，当然在学习的时候，不用像专业方向的同学那么深入，但需要涉猎了解，丰富自己的知识面，构建全方位的网路安全知识技能栈。

**02**

**二、学习感悟**

其实网络安全的知识都非常有趣，如果你能够认真学习，那么网络安全的很多知识点都会让你沉迷其中，学完之后大喊：好爽......原来电脑如此有趣。当然，学习任何东西刚开始都是不容易的，刚开始都是比较吃力的，特别是许久不怎么学习的同学，心理上是有点排斥，也很难进入学习状态。

但是遇到困难，进不去状态的时候不能放弃，因为学习其实就是自己和自己对抗的过程，用专业一点的解释来说，就是人类的大脑里面有个零件叫伏隔核，静不下心来学习就是这个东西在从中作梗，而我们每个人的脑中都有这样的东西。所以，每个人都会面临这样的困难，面对困难我们应该想办法解决。这里给大家一个小方法，对我来说比较有用，可以先欺骗自己，心里想着：就学习几分钟，几分钟之后就可以刷抖音刷番，还可以约上朋友一起喝着啤酒吃着烧烤。但是通常情况下，几分钟之后心就静下来了，就可以继续认真学习了。

其实我学习网络安全尝试过很多种方式，最开始就是自学。在这个过程中碰到的最大的问题就是不知道从何下手，通常情况下在网上找到的学习路线都是不完整或者过时的，而且就算找到了合适的学习路线大纲，找相关知识点的内容也比较麻烦。自学的时候我通常自嘲网络安全其实只需要学两点：这也要学、那也要学。由于内容过于冗杂，所以导致了学习的过程更加艰难。

但是这些问题后来都变成了一些小问题，因为我最终还是放弃了周期长的自学，选择培训。在培训学习期间，老师已经根据当下市场情况和企业用人需求以及我们的基本情况整理了非常完整的学习大纲。上面所说的难以进入学习状态的问题也引刃而解，大家在一个教室里面上课，在浓厚的学习氛围的烘托下，只会越学越带劲。

网络安全入门的时候也非常容易眼高手低，有些相关书籍看完之后觉得非常高大上，知道的理论也非常前沿，但是一旦开始动手操作就开始犯难。在Linux下手动配一个IP地址也不会......要么就是会一些基本操作，系统的网络安全知识框架还是零碎的，未组件的。

后来能够跟着老师学习，能够系统的学习网络安全知识，能够动手操作之后，这些困惑似乎也都不是什么大事了。不管是通过什么方式学习网络安全，不管以前有没有基础，都从头开始学习，一定是没错的。在学习的时候能够把知识更加科学合理的梳理一下，更能够巩固知识。

#网络安全#黑客#web安全#计算机#干货分享#网络安全入门技术#信息安全

**03**

**三、网络安全学习包**

---

如果你也是零基础想转行网络安全，却苦于没系统学习路径、不懂核心攻防技能？光 靠盲目摸索不仅浪费时间，还消磨自己信心。这份 360 智榜样学习中心独家出版《网络攻防知识库》专为转行党量身打造！

#### 01 **内容涵盖**

这份资料专门为零基础转行设计，19 大核心模块从 Linux 系统、Python 基础、HTTP协议等地基知识到 Web 渗透、代码审计、CTF 实战层层递进，攻防结合的讲解方式让新手轻松上手，真实实战案例 + 落地脚本直接对标企业岗位需求，帮你快速搭建转行核心技能体系！

![img](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBbgAzJyfFp29qZsnOiaOPNNfDJ1XzMeLbU5ZU3ZmDnete4nIq8FuAfibqzuLDs9QcuT0t9qqmMHxibz5RwVs5lMCt27IcYF95T9dQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)

![img](https://mmbiz.qpic.cn/sz_mmbiz_gif/sbWEHMerrBZMDDrSNpicXnMXZiaE80AnFOojVbKdwKT8rqvFHFrhHiaH4KytZrZjkQhBO26dPlgarzW6pkGWHXEQyEApxGvMZPDv82AhDHTicibs/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

`《网络安全/黑客技术入门学习大礼包》，可以扫描下方二维码免费领取！`

![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBZXuIpdAx1Tia7thAeMQTLdoCw4520PVib1f8HJAnyibWsCY9yPdY9XX4NhFgqI9uDyEzEs8MkEHwn6CGJStVHdVjxHO6CHNicL5qM/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)

#### **02 知识库价值**

* **深度**

  ： 本知识库超越常规工具手册，深入剖析攻击技术的底层原理与高级防御策略，并对业内挑战巨大的APT攻击链分析、隐蔽信道建立等，提供了**独到的技术视角和实战验证过的对抗方案**。

* **广度**

  ： 面向企业安全建设的核心场景（渗透测试、红蓝对抗、威胁狩猎、应急响应、安全运营），本知识库覆盖了从攻击发起、路径突破、权限维持、横向移动到防御检测、响应处置、溯源反制的全生命周期关键节点，是**应对复杂攻防挑战的实用指南**。

* **实战性**

  ： 知识库内容源于**真实攻防对抗和大型演练实践**，通过详尽的攻击复现案例、防御配置实例、自动化脚本代码来传递核心思路与落地方法。

#### **03 谁需要掌握本知识库**

* 负责企业整体安全策略与建设的 **CISO/安全总监**

* 从事渗透测试、红队行动的 **安全研究员/渗透测试工程师**

* 负责安全监控、威胁分析、应急响应的 **蓝队工程师/SOC分析师**

* 设计开发安全产品、自动化工具的 **安全开发工程师**

* 对网络攻防技术有浓厚兴趣的 **高校信息安全专业师生**

#### **04** **部分核心内容展示**

#### **![在这里插入图片描述](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBZP1ibBia4vG8iboJyVNE2x6ytjVYXeXUJuOW2MjCJ1hmVmcEOfgJxibUGOB7bgCoWgg2H7OCZYrTbdVHJyEotUkNguatQLnrTltico/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)**

360智榜样学习中心独家《网络攻防知识库》采用**由浅入深、攻防结合**的讲述方式，既夯实基础技能，更深入高阶对抗技术。

内容组织紧密结合攻防场景，辅以大量**真实环境复现案例、自动化工具脚本及配置解析**。通过**策略讲解、原理剖析、实战演示**相结合，是你学习过程中好帮手。

**1、网络安全意识**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBYogoA3dHR8vjnpYsuquLxrSfiajiaZLj5bmxpK0YCL2DLeqH0yRORxjBGofMpquqTcI4aLO7SglqK1jytLrqSP1ta8vqDJiaANto/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21)**

**2、Linux操作系统**

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sbWEHMerrBYdSEeBm9sn31XRQOfIfO4WcU6Z5KavcNGYMKQP0qzMzRLMI7JZGy4Gia8BK3rs6wPZZW4cs1wODibTK7Xu8rCKpRBBEO8CddkSg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22)**

**3、WEB架构基础与HTTP协议**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBZpPf3DEbxDbKU1Af7xELzIkxY15efBeJcVmI14JyqgF6SSjCcL7BBVr5nKlKsO4m3cdrDMx2qsCfJTr9j5k6tvb0g2ZwVkHPI/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23)**

**4、Web渗透测试**

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/sbWEHMerrBYGGWhujIh8tS9wIbdXjaNWkJx5vYGzz88nxErD1Od58VOEjOtCic4UHhicH7HF1D4iaK5IBUxJrvjX12BuVbww84CGLJmOdlojicU/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=24)**

**5、渗透测试案例分享**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBakjTeCNSIRSglmOetBoIMjEZYYq1X4gicibYiaFyu08bic3ib08DCILjelvftawJcP8ohOQSuK2T5fa5CHicgnicRcxd5dNLTIJehfPw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=25)**

**6、渗透测试实战技巧**

**![在这里插入图片描述](https://mmbiz.qpic.cn/sz_mmbiz_png/sbWEHMerrBbWVO0GEUFrKSpGm0a3fgRm6dzRHeNQlruhibmetCOPSlJicJDvjb7vCRMJO4lmaialrCicic0NjboKOVr4yLicRc9p1IeDzrgc0JnG0/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=26)**

**7、攻防对战实战**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBZ9MePIGibmM2yfMmqurERefPJaH0B0bKrKdyCs5ZKe2UUdSWgEcuicGlUibDbibuPMXda5DE9lRxFBdm0hnVXdluZP6bkrUtW5Mug/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=27)**

**8、CTF之MISC实战讲解**

**![图片](https://mmbiz.qpic.cn/mmbiz_png/sbWEHMerrBaPLYKAk8PwChNgkXKQ1Le2YDzR9JnCXOFPIoiaTt...